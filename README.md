# Geolocalizador-Encuéntrame


[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)


Dispositivo autónomo de localización post-impacto / pérdida, adaptable a distintos escenarios como infraestructura especial. Se activa ante una emergencia, puede separarse del objeto al que está acoplado y transmite coordenadas exactas desde el minuto 1, con autonomía extendida.

## ¿Qué es?

Es una plataforma de localización de emergencia diseñada para ser adaptable a diferentes ámbitos: aeronáutico, marítimo, terrestre y personal. Dependiendo de la configuración, puede instalarse en aeronaves, embarcaciones, vehículos de alto valor, contenedores, infraestructura crítica, o portarse como dispositivo personal.

Ante una situación crítica (accidente inminente, hundimiento, pérdida, emergencia), se activa autónomamente, se separa (si corresponde) y comienza a transmitir su posición exacta vía satélite y radiofrecuencia.

A diferencia de los localizadores tradicionales (ELT, EPIRB, PLB), Geolocalizador-Encuéntrame puede eyectarse antes del impacto, flota, y transmite durante semanas, no horas.

## Principio de operación

1. **Detección** — Sensores (aceleración, presión, vibración, temperatura) monitorean continuamente. Algoritmos de IA detectan condiciones anormales según el escenario.
2. **Activación** — Se activa automáticamente (por detección de impacto, hundimiento, pérdida de señal) o manualmente.
3. **Separación** — Si está acoplado a un objeto, se libera mediante mecanismo pirotécnico o neumático (según modelo).
4. **Flotación / estabilización** — Se despliega sistema de flotación y se estabiliza para máxima visibilidad (en versiones marítimas y aeronáuticas).
5. **Transmisión** — Envía coordenadas GPS de alta precisión vía múltiples canales.
6. **Rescate** — Los equipos de búsqueda reciben posición exacta desde el primer minuto.

## Escenarios de uso

### Aeronáutico
- Aviones comerciales, helicópteros, avionetas.
- Se instala en estabilizador, cono de cola o raíz de ala.
- Se eyecta ante impacto inminente (300–1000 m AGL).

### Marítimo
- Barcos, contenedores, boyas, equipos de pesca.
- Flota indefinidamente, transmite posición aunque la embarcación se hunda.
- Resistente a presión y corrosión marina.

### Terrestre
- Infraestructura crítica, vehículos de alto valor, equipos en zonas remotas.
- Se activa por robo, vuelco o pérdida de señal.
- Diseño adaptable a postes, torres, casetas de monitoreo.

### Personal
- Dispositivo de emergencia para montañismo, expediciones, navegación.
- Versión liviana con activación manual y alerta satelital.
- Integrable a sistemas de seguridad de instalaciones especiales.

## Ventajas frente a sistemas existentes

| Caracteristica | Geolocalizador-Encuéntrame | ELT / EPIRB / PLB tradicionales |
|----------------|----------------------------|--------------------------------|
| Activación | Pre-evento (IA) o manual | Post-evento (impacto >5G o manual) |
| Separación | Sí, antes del impacto/hundimiento | No |
| Flotación | Sí | Algunos modelos |
| Transmisión | GPS + 406 MHz + AIS + Iridium | 406 MHz + 121.5 MHz |
| Autonomia | >30 días | 24–72 horas |
| Precision | 2.5 cm (RTK) | 3–20 km (triangulación) |

## Componentes tecnicos (plataforma base)

### 1. Unidad de detección y control
- Microcontrolador de ultra bajo consumo.
- Sensores: acelerómetro (XYZ), presión, temperatura, humedad, micrófono (vibraciones).
- Algoritmo de IA entrenable por escenario.

### 2. Mecanismo de separación
- Carga pirotécnica controlada o sistema electromecánico.
- Activación automática o remota.
- Seguro antiactivación accidental.

### 3. Cápsula de supervivencia
- Material compuesto de alta resistencia.
- Flotadores hinchables con estabilización (según modelo).
- Protección IP68 (sumergible hasta 100 m).
- Reflector radar y baliza IR.

### 4. Sistema de comunicaciones
- GPS de alta precisión (RTK, corrección diferencial).
- Transmisor 406 MHz COSPAS-SARSAT (5W ERP).
- Transmisor 121.5 MHz para homing final.
- AIS 161.975 MHz para detección marítima.
- Iridium SBD / Globalstar para respaldo satelital.
- LoRaWAN / Sigfox para aplicaciones terrestres.

### 5. Alimentación
- Baterías de litio de alta densidad.
- Autonomía: >30 días en transmisión continua.
- Modo de ultra bajo consumo (años) en espera.
- Activación por separación o por evento.

## Configuraciones disponibles

| Modelo | Aplicacion | Peso | Separacion | Comunicacion | Caracteristica clave |
|--------|------------|------|------------|--------------|----------------------|
| Encuentrame-Aero | Aviacion comercial y militar | 980 g | Si (eyeccion) | 406 MHz + AIS + Iridium | Integrable a bus de datos ARINC 429 |
| Encuentrame-Mar | Maritimo (buques, plataformas, contenedores) | 1200 g | Si (liberacion) | 406 MHz + AIS + Iridium | Resistencia a presion y corrosion prolongada |
| Encuentrame-Terrestre | Infraestructura critica, vehiculos de alto valor, zonas remotas | 500 g | Opcional | 406 MHz + LoRaWAN + Iridium | Diseno adaptable a postes, torres, casetas de monitoreo |
| Encuentrame-Personal | Infraestructura de seguridad para personal en entornos remotos | 200 g | No (activacion manual) | 406 MHz + Bluetooth + Iridium | Integrable a sistemas de seguridad de instalaciones especiales |

## Diseno como infraestructura especial adaptable

Geolocalizador-Encuentrame no es un dispositivo aislado, sino una **plataforma de localización diseñada para integrarse como infraestructura especial** en entornos críticos:

- **Infraestructura energética:** Torres de transmisión, subestaciones, parques eólicos y solares remotos.
- **Infraestructura de transporte:** Puentes, túneles, estaciones de ferrocarril en zonas aisladas.
- **Infraestructura de defensa:** Instalaciones militares, puestos de vigilancia fronteriza.
- **Infraestructura de telecomunicaciones:** Torres de comunicacion, estaciones base en zonas de dificil acceso.
- **Infraestructura de monitoreo ambiental:** Estaciones hidrometeorologicas, sensores remotos, boyas oceanograficas.

En todos estos casos, el dispositivo se integra como parte de la infraestructura fija, con alimentacion redundante, comunicacion satelital de respaldo y capacidad de activacion autonoma ante eventos de perdida o destruccion parcial de la instalacion.

**Ventaja:** Una misma plataforma hardware, con configuraciones especificas por escenario, permite estandarizar la localizacion de emergencia en distintos tipos de infraestructura critica, reduciendo costos de implementacion y mantenimiento.

## Especificaciones clave (plataforma base)

| Parametro | Valor |
|-----------|-------|
| Dimensiones | 120 × 120 × 60 mm (version estandar) |
| Peso base | 450 g (sin opcionales) |
| Temperatura operativa | –40°C a +85°C |
| Resistencia al impacto | 50 G |
| Profundidad operativa | 100 m (IP68) |
| Precision GPS | 2.5 cm (RTK) / 1.5 m (estandar) |
| Autonomia en transmision | >30 días |
| Autonomia en espera | >5 años |
| Interfaces | ARINC 429, CAN Bus, RS-485, Bluetooth, USB-C |

## Instalacion segun escenario

- **Aeronaves:** Montaje en estructura fija, conexion al bus de datos.
- **Embarcaciones:** Soporte con liberacion hidrostatica.
- **Infraestructura terrestre:** Acople a estructuras existentes (postes, torres, casetas) con alimentacion redundante.
- **Personal:** Clip o correa de transporte, integracion a sistemas de seguridad.

## Certificaciones en proceso

- TSO-C126f / EASA ETSO-C126 (aviacion)
- IEC 60945 (maritimo)
- IP68 (sumergibilidad)
- MIL-STD-810H (ambiental)

## Estado actual

✅ Concepto definido  
✅ Arquitectura tecnica  
✅ Algoritmos de deteccion en desarrollo  
🔲 Prototipo funcional  
🔲 Pruebas de separacion y flotacion  
🔲 Certificaciones por ambito  
🔲 Produccion

## Proximos pasos

1. Desarrollo de prototipo funcional.
2. Pruebas en laboratorio y campo por escenario.
3. Obtencion de certificaciones.
4. Pilotaje en cada ambito.
5. Produccion y distribucion.

## Proyectos relacionados

- **CORPUS** — sistemas embebidos de alta confiabilidad
- **Evo-2** — analisis de datos con IA
- **Movi-Dick** — localizacion de contenedores maritimos
- **Generador Horizontal de Oleaje** — sistemas de alimentacion para dispositivos remotos

## Licencia

Apache 2.0 con restriccion de uso comercial.

## Autor

**Enrique Aguayo H.**  
Mackiber Labs  
Contacto: eaguayo@migst.cl  
ORCID: 0009-0004-4615-6825  
GitHub: [@enriqueherbertag-lgtm](https://github.com/enriqueherbertag-lgtm)

Documentacion asistida por **Ana (DeepSeek)** , IA para investigacion y optimizacion tecnica.
