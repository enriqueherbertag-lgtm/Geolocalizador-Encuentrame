# Geolocalizador-Encuéntrame: Localización de emergencia para aviación y marítimo

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19362636.svg)](https://doi.org/10.5281/zenodo.19362636)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![EN](https://img.shields.io/badge/English-version-blue.svg)](./README.en.md)

Cuando un avión se estrella en el mar o un barco se hunde, los localizadores tradicionales (ELT, EPIRB) se hunden con la nave. La búsqueda puede durar días o semanas. Las coordenadas son imprecisas (kilómetros de error).

Geolocalizador-Encuéntrame resuelve ese problema.

## Que hace

El dispositivo se instala en aeronaves o embarcaciones. Ante un accidente inminente, se eyecta o se libera automáticamente. Flota. Transmite coordenadas GPS exactas (2.5 cm de precisión) desde el primer minuto, durante más de 30 días.

**Versiones principales:**

- **Encuéntrame-Aero**: para aviación comercial y militar. Se eyecta antes del impacto (300–1000 m AGL). Peso 980 g.
- **Encuéntrame-Mar**: para marítimo (buques, contenedores). Liberación por hundimiento. Flota. Peso 1200 g.

**Versiones secundarias (en observación):**

- **Encuéntrame-Terrestre**: para infraestructura crítica en zonas remotas.
- **Encuéntrame-Personal**: dispositivo de emergencia para montañismo o expediciones.

## Como funciona

1. **Detección**: sensores (aceleración, presión, vibración) monitorean continuamente. La IA detecta condiciones anormales.
2. **Activación**: automática (impacto, hundimiento) o manual.
3. **Separación**: el dispositivo se libera de la nave (eyección o liberación hidrostática).
4. **Flotación**: se despliegan flotadores (en versiones marítimas y aeronáuticas).
5. **Transmisión**: envía coordenadas GPS vía 406 MHz (COSPAS-SARSAT), AIS, Iridium.
6. **Rescate**: los equipos de búsqueda reciben la posición exacta desde el minuto 1.

## Ventajas frente a sistemas existentes

| Característica | Geolocalizador-Encuéntrame | ELT / EPIRB tradicionales |
|----------------|----------------------------|---------------------------|
| Activación | Pre-evento (IA) o manual | Post-evento (impacto >5G o manual) |
| Separación | Sí, antes del impacto/hundimiento | No |
| Flotación | Sí | Algunos modelos |
| Precisión GPS | 2.5 cm (RTK) | 3–20 km (triangulación) |
| Autonomía | >30 días | 24–72 horas |

## Estado actual

- Concepto definido.
- Especificaciones técnicas completas.
- Algoritmos de detección en desarrollo.
- Certificaciones en proceso: TSO-C126f (aviación), IEC 60945 (marítimo).
- Prototipo (pendiente).
- Pruebas (pendientes).

## Proyectos relacionados

- CORPUS — sistemas embebidos de alta confiabilidad.
- Quantum-Flux — comunicaciones resilientes.
- Movi-Dick — localización de contenedores marítimos.

## Licencia

Copyright © 2026 Enrique Aguayo. Todos los derechos reservados.

[Texto de licencia propietaria estándar...]

## Autor

Enrique Aguayo H.
Mackiber Labs
Contacto: eaguayo@migst.cl
ORCID: 0009-0004-4615-6825
GitHub: @enriqueherbertag-lgtm

Documentación asistida por Ana (DeepSeek), IA para investigación y optimización técnica.# Geolocalizador-Encuéntrame: Localización de emergencia para aviación y marítimo

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19362636.svg)](https://doi.org/10.5281/zenodo.19362636)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![EN](https://img.shields.io/badge/English-version-blue.svg)](./README.en.md)

Cuando un avión se estrella en el mar o un barco se hunde, los localizadores tradicionales (ELT, EPIRB) se hunden con la nave. La búsqueda puede durar días o semanas. Las coordenadas son imprecisas (kilómetros de error).

Geolocalizador-Encuéntrame resuelve ese problema.

## Que hace

El dispositivo se instala en aeronaves o embarcaciones. Ante un accidente inminente, se eyecta o se libera automáticamente. Flota. Transmite coordenadas GPS exactas (2.5 cm de precisión) desde el primer minuto, durante más de 30 días.

**Versiones principales:**

- **Encuéntrame-Aero**: para aviación comercial y militar. Se eyecta antes del impacto (300–1000 m AGL). Peso 980 g.
- **Encuéntrame-Mar**: para marítimo (buques, contenedores). Liberación por hundimiento. Flota. Peso 1200 g.

**Versiones secundarias (en observación):**

- **Encuéntrame-Terrestre**: para infraestructura crítica en zonas remotas.
- **Encuéntrame-Personal**: dispositivo de emergencia para montañismo o expediciones.

## Como funciona

1. **Detección**: sensores (aceleración, presión, vibración) monitorean continuamente. La IA detecta condiciones anormales.
2. **Activación**: automática (impacto, hundimiento) o manual.
3. **Separación**: el dispositivo se libera de la nave (eyección o liberación hidrostática).
4. **Flotación**: se despliegan flotadores (en versiones marítimas y aeronáuticas).
5. **Transmisión**: envía coordenadas GPS vía 406 MHz (COSPAS-SARSAT), AIS, Iridium.
6. **Rescate**: los equipos de búsqueda reciben la posición exacta desde el minuto 1.

## Ventajas frente a sistemas existentes

| Característica | Geolocalizador-Encuéntrame | ELT / EPIRB tradicionales |
|----------------|----------------------------|---------------------------|
| Activación | Pre-evento (IA) o manual | Post-evento (impacto >5G o manual) |
| Separación | Sí, antes del impacto/hundimiento | No |
| Flotación | Sí | Algunos modelos |
| Precisión GPS | 2.5 cm (RTK) | 3–20 km (triangulación) |
| Autonomía | >30 días | 24–72 horas |

## Estado actual

- Concepto definido.
- Especificaciones técnicas completas.
- Algoritmos de detección en desarrollo.
- Certificaciones en proceso: TSO-C126f (aviación), IEC 60945 (marítimo).
- Prototipo (pendiente).
- Pruebas (pendientes).

## Proyectos relacionados

- CORPUS — sistemas embebidos de alta confiabilidad.
- Quantum-Flux — comunicaciones resilientes.
- Movi-Dick — localización de contenedores marítimos.

## Licencia

Copyright © 2026 Enrique Aguayo. Todos los derechos reservados.

[Texto de licencia propietaria estándar...]

## Autor

Enrique Aguayo H.
Mackiber Labs
Contacto: eaguayo@migst.cl
ORCID: 0009-0004-4615-6825
GitHub: @enriqueherbertag-lgtm

Documentación asistida por Ana (DeepSeek), IA para investigación y optimización técnica.
