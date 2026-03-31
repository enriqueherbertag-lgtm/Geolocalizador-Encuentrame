#!/usr/bin/env python3
"""
Geolocalizador-Encuentrame - Cloud Dashboard
Sistema de monitoreo y alertas para dispositivos desplegados
"""

import json
import sqlite3
import threading
import time
from datetime import datetime
from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Configuracion
DB_PATH = '/var/lib/geolocalizador/data.db'
ALERT_WEBHOOK = 'https://hooks.slack.com/services/...'
SATELLITE_API = 'https://api.iridium.com/v1/messages'

class DeviceMonitor:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.init_db()
        self.devices = {}  # device_id -> {status, last_location, battery}
        self.running = True
        
    def init_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS devices (
                id TEXT PRIMARY KEY,
                name TEXT,
                scenario TEXT,
                status TEXT,
                last_lat REAL,
                last_lon REAL,
                last_seen TEXT,
                battery REAL,
                firmware_version TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_id TEXT,
                timestamp TEXT,
                alert_type TEXT,
                lat REAL,
                lon REAL,
                resolved INTEGER DEFAULT 0
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS telemetry (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_id TEXT,
                timestamp TEXT,
                lat REAL,
                lon REAL,
                battery REAL,
                status TEXT
            )
        ''')
        self.conn.commit()
    
    def process_iridium_message(self, message):
        """Procesa mensaje recibido via Iridium SBD"""
        try:
            data = json.loads(message)
            device_id = data.get('device_id')
            lat = data.get('lat')
            lon = data.get('lon')
            battery = data.get('battery')
            alert = data.get('alert', False)
            timestamp = datetime.now().isoformat()
            
            # Actualizar telemetria
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO telemetry (device_id, timestamp, lat, lon, battery, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (device_id, timestamp, lat, lon, battery, 'active'))
            
            # Actualizar ultima ubicacion del dispositivo
            cursor.execute('''
                UPDATE devices SET last_lat = ?, last_lon = ?, last_seen = ?, battery = ?, status = ?
                WHERE id = ?
            ''', (lat, lon, timestamp, battery, 'active', device_id))
            
            # Si es alerta, crear registro y notificar
            if alert:
                cursor.execute('''
                    INSERT INTO alerts (device_id, timestamp, alert_type, lat, lon)
                    VALUES (?, ?, ?, ?, ?)
                ''', (device_id, timestamp, 'activation', lat, lon))
                self.send_alert_notification(device_id, lat, lon, timestamp)
            
            self.conn.commit()
            
        except Exception as e:
            print(f"Error processing message: {e}")
    
    def send_alert_notification(self, device_id, lat, lon, timestamp):
        """Envia notificacion de alerta via webhook"""
        # Obtener informacion del dispositivo
        cursor = self.conn.cursor()
        cursor.execute('SELECT name, scenario FROM devices WHERE id = ?', (device_id,))
        row = cursor.fetchone()
        device_name = row[0] if row else device_id
        scenario = row[1] if row else 'unknown'
        
        # Construir mensaje
        alert_data = {
            'text': f'ALERTA: {device_name} activado',
            'blocks': [
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f'*Dispositivo:* {device_name}\n*Escenario:* {scenario}\n*Ubicacion:* {lat:.6f}, {lon:.6f}\n*Hora:* {timestamp}'
                    }
                },
                {
                    'type': 'actions',
                    'elements': [
                        {
                            'type': 'button',
                            'text': {'type': 'plain_text', 'text': 'Ver en mapa'},
                            'url': f'https://maps.google.com/?q={lat},{lon}'
                        }
                    ]
                }
            ]
        }
        
        try:
            requests.post(ALERT_WEBHOOK, json=alert_data, timeout=5)
        except Exception as e:
            print(f"Alert notification failed: {e}")
    
    def get_device_status(self, device_id):
        """Retorna estado actual del dispositivo"""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT name, scenario, status, last_lat, last_lon, last_seen, battery, firmware_version
            FROM devices WHERE id = ?
        ''', (device_id,))
        row = cursor.fetchone()
        
        if row:
            return {
                'id': device_id,
                'name': row[0],
                'scenario': row[1],
                'status': row[2],
                'location': {'lat': row[3], 'lon': row[4]},
                'last_seen': row[5],
                'battery': row[6],
                'firmware': row[7]
            }
        return None
    
    def register_device(self, device_id, name, scenario, firmware):
        """Registra un nuevo dispositivo en la base de datos"""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO devices (id, name, scenario, status, firmware_version)
            VALUES (?, ?, ?, ?, ?)
        ''', (device_id, name, scenario, 'registered', firmware))
        self.conn.commit()

# Inicializar monitor
monitor = DeviceMonitor()

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/devices')
def api_devices():
    cursor = monitor.conn.cursor()
    cursor.execute('SELECT id, name, scenario, status, last_lat, last_lon, last_seen, battery FROM devices')
    rows = cursor.fetchall()
    devices = []
    for row in rows:
        devices.append({
            'id': row[0],
            'name': row[1],
            'scenario': row[2],
            'status': row[3],
            'location': {'lat': row[4], 'lon': row[5]} if row[4] else None,
            'last_seen': row[6],
            'battery': row[7]
        })
    return jsonify(devices)

@app.route('/api/alerts')
def api_alerts():
    cursor = monitor.conn.cursor()
    cursor.execute('''
        SELECT a.id, a.device_id, d.name, a.timestamp, a.alert_type, a.lat, a.lon, a.resolved
        FROM alerts a
        LEFT JOIN devices d ON a.device_id = d.id
        ORDER BY a.timestamp DESC LIMIT 50
    ''')
    rows = cursor.fetchall()
    alerts = []
    for row in rows:
        alerts.append({
            'id': row[0],
            'device_id': row[1],
            'device_name': row[2],
            'timestamp': row[3],
            'type': row[4],
            'location': {'lat': row[5], 'lon': row[6]},
            'resolved': bool(row[7])
        })
    return jsonify(alerts)

@app.route('/api/telemetry/<device_id>')
def api_telemetry(device_id):
    cursor = monitor.conn.cursor()
    cursor.execute('''
        SELECT timestamp, lat, lon, battery FROM telemetry
        WHERE device_id = ? ORDER BY timestamp DESC LIMIT 100
    ''', (device_id,))
    rows = cursor.fetchall()
    telemetry = []
    for row in rows:
        telemetry.append({
            'timestamp': row[0],
            'location': {'lat': row[1], 'lon': row[2]},
            'battery': row[3]
        })
    return jsonify(telemetry)

@app.route('/api/webhook/iridium', methods=['POST'])
def iridium_webhook():
    """Endpoint para recibir mensajes Iridium"""
    data = request.json
    if data:
        monitor.process_iridium_message(json.dumps(data))
        return jsonify({'status': 'ok'}), 200
    return jsonify({'status': 'error'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
