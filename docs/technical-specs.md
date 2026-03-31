# Especificaciones tecnicas - Geolocalizador-Encuentrame

## Hardware

### Dimensiones y peso
- Carcasa: 120 × 120 × 60 mm (version estandar)
- Peso base: 450 g
- Peso configuraciones:
  - Aero: 980 g
  - Mar: 1200 g
  - Terrestre: 500 g
  - Personal: 200 g

### Materiales
- Carcasa: Aluminio 6061-T6 anodizado o composite fibra de carbono
- Proteccion: IP68 (sumergible hasta 100 m)
- Resistencia a impactos: 50 G (MIL-STD-810H)

### Ambiente
- Temperatura operativa: –40°C a +85°C
- Humedad: 0–100% condensante
- Corrosion: Resistente a niebla salina (ASTM B117)

## Sensores

| Sensor | Tipo | Rango | Precision |
|--------|------|-------|-----------|
| Acelerometro | MEMS 3-ejes | ±16 g | 0.1 mg |
| Presion | Barometro | 300–1100 hPa | ±1 hPa |
| Temperatura | Termistor | –40 a +125°C | ±0.5°C |
| Humedad | Capacitivo | 0–100% RH | ±3% |
| Vibracion | PZT | 0–5 kHz | 0.1 Hz |

## GPS

- Receptor: u-blox ZED-F9P (RTK)
- Precision: 2.5 cm (RTK) / 1.5 m (estandar)
- Canales: 184
- Sensibilidad: –167 dBm
- Actualizacion: 10 Hz

## Comunicaciones

| Sistema | Frecuencia | Potencia | Alcance |
|---------|------------|----------|---------|
| COSPAS-SARSAT | 406.037 MHz | 5W ERP | Global |
| Homing | 121.5 MHz / 243.0 MHz | 50 mW | 10 km |
| AIS | 161.975 MHz | 2W | 20 km |
| Iridium SBD | L-band | 1.6W | Global |
| LoRaWAN | 868/915 MHz | 100 mW | 5–15 km |
| Bluetooth | 2.4 GHz | 10 mW | 50 m |

## Alimentacion

- Bateria: LiFePO4 / Li-ion de alta densidad
- Capacidad: 10 Wh (version personal) a 100 Wh (version maritima)
- Autonomia en transmision: >30 días
- Autonomia en espera: >5 años
- Activacion: Separacion, evento, manual

## Mecanismo de separacion

- Tipo: Pirotecnico o neumatico
- Activacion: Señal electrica 24V DC
- Tiempo de eyeccion: <50 ms
- Velocidad de separacion: 10 m/s
- Seguridad: Doble seguro (mecanico + electronico)

## Interfaces

- ARINC 429 (aviacion)
- CAN Bus (automotriz, maritimo)
- RS-485 (industrial)
- Bluetooth 5.0 (configuracion)
- USB-C (programacion)
