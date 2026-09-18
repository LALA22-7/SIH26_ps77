# StormSight: Complete Project Explainer

*Written for judges, evaluators, non-technical stakeholders, and anyone who wants to deeply understand what StormSight is, why it exists, how it works, and where it is going. Read this first.*

---

## How to Read This Document

This file is structured like a book. You do not need to be a data scientist to follow it.

**Chapters:**
1. [The Problem](#chapter-1-the-problem)
2. [The Data](#chapter-2-the-data)
3. [The AI Model](#chapter-3-the-ai-model)
4. [The Dashboard](#chapter-4-the-dashboard)
5. [What Makes This Different](#chapter-5-what-makes-this-different)
6. [Limitations](#chapter-6-limitations)
7. [Glossary](#chapter-7-glossary)

---

## Chapter 1: The Problem

### Severe Weather Kills More Indians Than Cyclones

While tropical cyclones dominate disaster headlines, **localised severe weather events** — thunderstorms, cloudbursts, and flash floods — kill far more people annually in India. In 2023 alone, flash floods caused approximately **1,600 deaths** across India. The 2013 Kedarnath disaster, triggered by a cloudburst, killed over **5,000 people** in a single event.

### Why These Events Are Hard to Predict

Unlike cyclones that form over days and track predictably, severe thunderstorms and cloudbursts can develop **explosively in 1–3 hours**. They are driven by a complex chain of atmospheric conditions:

1. **Moisture accumulates** in the atmosphere (high Integrated Water Vapor)
2. **Instability builds** (high CAPE — energy for updrafts; weakening CIN — the "cap" holding convection back)
3. **A trigger occurs** (wind convergence, terrain lift, frontal boundary)
4. **Explosive convection develops** — cloud tops shoot upward (visible as rapid Cloud Top Temperature cooling)
5. **Extreme rainfall occurs** — sometimes exceeding 100mm/hour (cloudburst threshold)
6. **Terrain responds** — depending on slope, elevation, and drainage, the same rainfall can produce very different flood risk

### What India Already Has

India is **not** starting from zero. The India Meteorological Department (IMD) and the National Centre for Medium Range Weather Forecasting (NCMRWF) operate sophisticated observation networks, numerical weather prediction models, radar-based nowcasting, and a National Flash Flood Guidance System.

### What's Missing: The AI Fusion Gap

No single existing system combines **all** of these heterogeneous signals — satellite temporal evolution, atmospheric thermodynamics, precipitation estimation, and terrain — into one coherent, hyper-local, probabilistic, explainable forecast at the 2–6 hour lead time.

**That is what StormSight builds.**

---

## Chapter 2: The Data

StormSight fuses four types of Indian Earth observation and model data:

### Satellite Imagery (INSAT-3D/3DR/3DS via MOSDAC)
India's own meteorological satellites provide multi-spectral imagery every 15–30 minutes. The thermal infrared channels show cloud top temperatures — a rapidly cooling cloud top means a storm is growing explosively. The water vapor channel shows moisture circulation patterns.

### Atmospheric Reanalysis (IMDAA)
IMDAA is an Indian regional atmospheric reanalysis developed by NCMRWF. It provides a consistent historical description of temperature, humidity, wind, and pressure at multiple atmospheric levels. From these profiles, we derive the critical meteorological quantities: CAPE, CIN, wind shear, and moisture convergence.

### Precipitation (QPE from MOSDAC)
Satellite-derived rainfall estimation tells us what precipitation is actually occurring — both for real-time monitoring and for validating whether the model's predicted rainfall risk matched reality.

### Terrain (SRTM Digital Elevation Model)
A 30-meter resolution map of elevation, slope, and drainage characteristics. This is what makes the difference between "heavy rain" and "flash flood" — the terrain determines how water flows and where it concentrates.

---

## Chapter 3: The AI Model

### Physics-Guided, Not Black-Box

StormSight does **not** throw raw satellite pixels into a neural network and hope it discovers meteorology. Instead, we first compute physically meaningful atmospheric features — CAPE, CIN, IWV, wind shear, CTT cooling rate, convergence — using established meteorological formulations. Then the neural network learns the complex, nonlinear relationships among these known quantities.

This makes the model:
- **Scientifically defensible** — grounded in atmospheric physics
- **More data-efficient** — doesn't need to learn basic physics from scratch
- **Explainable** — we can show which physical features drove each prediction

### Multi-Task Hazard Cascade

Instead of three independent models, StormSight uses a **shared spatiotemporal backbone** (ConvLSTM) that processes temporal sequences of multimodal observations. The backbone learns common atmospheric representations. Three separate prediction heads then output:

1. **Thunderstorm probability** — spatial map of severe thunderstorm risk
2. **Cloudburst probability** — spatial map of extreme rainfall risk
3. **Flash-flood probability** — spatial map of flood risk, conditioned on terrain

This architecture directly reflects the physical hazard chain: the three hazards are causally related, so learning them together helps the model.

### Handling Rare Events

Severe weather is rare (~0.5% of observations). A naïve model could achieve 99.5% "accuracy" by always predicting "nothing." We overcome this with:
- **Event-window sampling** — extracting temporal sequences around confirmed events
- **Hard negatives** — including cases where conditions looked favorable but nothing happened
- **Focal loss** — making the model pay a heavy penalty for missing actual events

---

## Chapter 4: The Dashboard

The dashboard answers three questions immediately:

1. **Where is the hazard?** → Interactive GIS map with probability overlays
2. **How likely is it?** → Per-hazard probability at the selected lead time (T+1h to T+6h)
3. **Why is the system warning me?** → XAI panel showing feature contributions

The atmospheric state panel shows current readings of IWV, CAPE, CIN, wind shear, and CTT — so a meteorologist can see the raw signals alongside the AI prediction.

---

## Chapter 5: What Makes This Different

| What We Are | What We Are NOT |
|---|---|
| An AI fusion layer for existing Indian weather infrastructure | A replacement for IMD or NCMRWF |
| A multi-hazard, hyper-local probabilistic forecast | A generic rainfall classifier |
| Physics-guided ML with explainability | A black-box "AI weather app" |
| Terrain-conditioned flash-flood risk | Treating cloudburst probability = flood probability |
| Evaluated with POD/FAR/CSI/FSS at multiple lead times | Evaluated with plain "accuracy" |

---

## Chapter 6: Limitations

- **Labels are the hardest part** — confirmed cloudburst and flash-flood events are sparse and inconsistently documented
- **IMDAA is historical** — reanalysis is not real-time observation; the production system needs a clear data source distinction
- **Spatial resolution** — INSAT water vapor channel is 8 km; truly hyper-local (sub-kilometer) prediction requires additional data sources
- **We cannot predict a cloudburst with certainty** — probabilistic forecasts are inherently uncertain; calibration helps but uncertainty remains
- **Data access** — some MOSDAC products may require registration and specific usage conditions

---

## Chapter 7: Glossary

| Term | Meaning |
|---|---|
| **CAPE** | Convective Available Potential Energy — energy available for thunderstorm updrafts |
| **CIN** | Convective Inhibition — the "cap" suppressing convection |
| **IWV** | Integrated Water Vapor — total moisture in the atmospheric column |
| **CTT** | Cloud Top Temperature — colder tops = higher/stronger convection |
| **ΔCTT** | CTT cooling rate — how fast cloud tops are ascending |
| **QPE** | Quantitative Precipitation Estimation — satellite-derived rainfall |
| **DEM** | Digital Elevation Model — terrain height map |
| **Cloudburst** | Extreme rainfall event (typically >100mm/hour over a small area) |
| **ConvLSTM** | Convolutional Long Short-Term Memory — neural network for spatiotemporal data |
| **POD** | Probability of Detection — fraction of events correctly predicted |
| **FAR** | False Alarm Ratio — fraction of predictions that were false alarms |
| **CSI** | Critical Success Index — overall quality of event detection |
| **FSS** | Fractions Skill Score — spatial verification with displacement tolerance |
| **IMDAA** | Indian Monsoon Data Assimilation and Analysis — regional atmospheric reanalysis |
| **MOSDAC** | Meteorological and Oceanographic Satellite Data Archival Centre (ISRO) |
| **NCMRWF** | National Centre for Medium Range Weather Forecasting |

---

## Document Map — Where to Read Next

| Topic | Document |
|---|---|
| Repository structure and setup | [README.md](README.md) |
| PPT content reference | [docs/SIH26_PS77_PPT_REFERENCE.md](docs/SIH26_PS77_PPT_REFERENCE.md) |
| System architecture | [docs/architecture.md](docs/architecture.md) |
| Data sources | [docs/data_sources.md](docs/data_sources.md) |
| ML pipeline | [ml/README.md](ml/README.md) |
| Backend API | [backend/README.md](backend/README.md) |
| Frontend guide | [frontend/README.md](frontend/README.md) |

---

*Built for Smart India Hackathon 2026 · PS77 (SIH26077) · Ministry of Earth Sciences / NCMRWF*
