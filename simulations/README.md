# Simulaciones - Geolocalizador-Encuentrame

Este directorio contiene los archivos de simulacion utilizados para validar el comportamiento del sistema.

## Impact Simulation

Simulacion de impactos y eyeccion utilizando:

- **Software:** ANSYS Explicit Dynamics / LS-DYNA
- **Modelo:** Carcasa, mecanismo de eyeccion, estructura de montaje
- **Condiciones:** Impacto a 50 m/s, angulos 0-90 grados
- **Resultados:** Deformacion, tensiones, integridad de la capsula

## Trajectory Analysis

Analisis de trayectoria post-eyeccion:

- **Software:** MATLAB / Python con modelos aerodinamicos
- **Variables:** Altitud de eyeccion (300-1000 m AGL), velocidad de la aeronave, viento
- **Resultados:** Area de dispersion, tiempo al agua/tierra

## Communication Coverage

Simulacion de cobertura de comunicaciones:

- **Software:** STK (Systems Tool Kit)
- **Satelites:** COSPAS-SARSAT, Iridium, AIS
- **Resultados:** Tiempo hasta primera fijacion, tasa de exito de transmision

Los archivos de simulacion se encuentran disponibles bajo solicitud debido a su tamano.
