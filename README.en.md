[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19362636.svg)](https://doi.org/10.5281/zenodo.19362636)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![ES](https://img.shields.io/badge/Spanish-version-green.svg)](./README.md)

# Geolocalizador-Encuéntrame: Emergency location for aviation and maritime

**Designed so that no plane ever gets lost again.**

Aircraft like MH370 disappear without a trace. When a plane crashes into the sea or a ship sinks, traditional locators (ELT, EPIRB) go down with the vessel. The search can take days or weeks. Coordinates are inaccurate (kilometers of error).

Geolocalizador-Encuéntrame solves this problem.

## What it does

The device is installed on aircraft or vessels. In the event of an imminent accident, it ejects or releases automatically. It floats. It transmits exact GPS coordinates (2.5 cm accuracy) from the first minute, for more than 30 days.

**Main versions:**

- **Encuéntrame-Aero**: for commercial and military aviation. Ejects before impact (300–1000 m AGL). Weight 980 g.
- **Encuéntrame-Mar**: for maritime (ships, containers). Releases upon sinking. Floats. Weight 1200 g.

**Secondary versions (under observation):**

- **Encuéntrame-Terrestre**: for critical infrastructure in remote areas.
- **Encuéntrame-Personal**: emergency device for mountaineering or expeditions.

## How it works

1. **Detection**: sensors (acceleration, pressure, vibration) monitor continuously. AI detects abnormal conditions.
2. **Activation**: automatic (impact, sinking) or manual.
3. **Separation**: the device releases from the vessel (ejection or hydrostatic release).
4. **Floating**: flotation devices deploy (in maritime and aeronautical versions).
5. **Transmission**: sends GPS coordinates via 406 MHz (COSPAS-SARSAT), AIS, Iridium.
6. **Rescue**: search teams receive exact position from minute one.

## Advantages over existing systems

| Feature | Geolocalizador-Encuéntrame | Traditional ELT / EPIRB |
|---------|----------------------------|-------------------------|
| Activation | Pre-event (AI) or manual | Post-event (>5G impact or manual) |
| Separation | Yes, before impact/sinking | No |
| Floating | Yes | Some models |
| GPS accuracy | 2.5 cm (RTK) | 3–20 km (triangulation) |
| Battery life | >30 days | 24–72 hours |

## Current status

- Concept defined.
- Complete technical specifications.
- Detection algorithms in development.
- Certifications in process: TSO-C126f (aviation), IEC 60945 (maritime).
- Prototype (pending).
- Testing (pending).

## Related projects

- CORPUS — embedded high-reliability systems.
- Quantum-Flux — resilient communications.
- Movi-Dick — maritime container localization.

## License

Copyright © 2026 Enrique Aguayo. All rights reserved.

[Standard proprietary license text...]

## Author

Enrique Aguayo H.
Mackiber Labs
Contact: eaguayo@migst.cl
ORCID: 0009-0004-4615-6825
GitHub: @enriqueherbertag-lgtm

Documentation assisted by Ana (DeepSeek), AI for research and technical optimization.
