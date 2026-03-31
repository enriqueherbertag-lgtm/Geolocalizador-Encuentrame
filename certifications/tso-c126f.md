# Plan de certificacion TSO-C126f

## Alcance

Certificacion del sistema Geolocalizador-Encuentrame conforme a TSO-C126f (Emergency Locator Transmitters) y EASA ETSO-C126.

## Entidad certificadora

- FAA: TSO autorizacion
- EASA: ETSO autorizacion
- Laboratorio de pruebas: NTS (National Technical Systems) o similar

## Fases del proceso

### Fase 1: Revision de diseño (4 meses)

| Actividad | Documentos requeridos |
|-----------|----------------------|
| Analisis funcional | Diagrama de bloques, especificacion funcional |
| Analisis de riesgos | FMEA, FTA, analisis de seguridad |
| Diseño hardware | Esquematicos, layout PCB, lista de materiales |
| Diseño software | Arquitectura, diagramas de flujo, algoritmos |
| Calificacion ambiental | Plan de pruebas DO-160G |

### Fase 2: Pruebas ambientales DO-160G (3 meses)

| Prueba | Condiciones |
|--------|-------------|
| Temperatura y altitud | –40°C a +85°C, 50,000 ft |
| Vibracion | Categoria S (helicopteros) y U (aeronaves fijas) |
| Humedad | 95% RH, 10 días |
| Choque | 50 G, 11 ms |
| Nieve/hielo | Simulacion de condiciones extremas |
| Resistencia a fluidos | Combustible, aceite, fluidos hidraulicos |

### Fase 3: Pruebas de TSO (2 meses)

| Prueba | Criterio |
|--------|----------|
| Precision GPS | <2.5 cm (RTK) |
| Potencia de transmision | 5W ERP ±1 dB |
| Frecuencia 406 MHz | ±1 kHz |
| Sensibilidad de activacion | Ajustable por escenario |
| Autonomia de bateria | >30 dias en transmision |
| Flotacion | 30 dias sin perdida de señal |

### Fase 4: STC por tipo de aeronave (6 meses por tipo)

- Seleccion de aeronave base (B737-800)
- Ingenieria de instalacion
- Pruebas en tierra y vuelo
- Documentacion final

## Entregables

- TSO Authorization Letter (FAA)
- ETSO Authorization (EASA)
- Reportes de pruebas DO-160G
- Manual de instalacion y mantenimiento
- STC para cada tipo de aeronave

## Cronograma estimado

| Actividad | Meses |
|-----------|-------|
| Revision de diseño | 1-4 |
| Pruebas DO-160G | 5-7 |
| Pruebas TSO | 8-9 |
| STC primer tipo | 10-15 |
| Produccion | 16+ |

## Presupuesto

| Concepto | USD |
|----------|-----|
| Tasas FAA/EASA | 25,000 |
| Pruebas NTS | 60,000 |
| Ingenieria STC | 80,000 |
| Documentacion | 15,000 |
| **Total** | **180,000** |
