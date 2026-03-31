# Procedimiento de mantenimiento - Geolocalizador-Encuentrame

## Frecuencias

| Intervalo | Actividades |
|-----------|-------------|
| Mensual | Verificacion remota (telemetria), estado de bateria |
| Anual | Inspeccion visual, prueba de activacion, limpieza |
| 5 años | Reemplazo de bateria, overhaul de mecanismo de separacion |
| 10 años | Reemplazo completo (vida util) |

## Mantenimiento anual

### Equipos necesarios
- Multimetro
- Analizador de espectro
- Software de configuracion
- Kit de sellos

### Procedimiento

1. **Inspeccion visual**
   - Carcasa sin golpes ni corrosión
   - Sellos en buen estado
   - Antenas sin daño

2. **Prueba de bateria**
   - Medir voltaje (minimo 3.6V por celda)
   - Capacidad remanente >80%

3. **Prueba de comunicacion**
   - Transmision 406 MHz en modo prueba
   - Verificacion de GPS (fix en <60s)
   - Comunicacion Iridium/LoRaWAN

4. **Prueba de separacion (cada 5 años)**
   - Simulacion electrica del disparo
   - Inspeccion del mecanismo

5. **Registro**
   - Actualizar bitacora de mantenimiento
   - Reportar a plataforma de monitoreo

## Vida util

- Bateria: 5 años
- Mecanismo de separacion: 5 años o 2 activaciones
- Carcasa: 10 años
- Electronica: 10 años
