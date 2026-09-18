# StormSight — SIH 2026 PPT Reference Document (PS77)

> **Team Name:** [YOUR TEAM NAME]
> **Problem Statement:** PS77 (SIH26077)
> **Competition:** Smart India Hackathon 2026
> **Organisation:** Ministry of Earth Sciences / NCMRWF
> **Category:** Disaster Management / AI-ML

---

> ⚠️ **This document is the content bible for the PS77 presentation.**
> It mirrors the format of the CycloneWatch (PS70) PPT reference.
> Every slide has complete content, speaker notes, and visual guidance.
> Adapt numbers to post-implementation state as the project matures.

---

## SLIDE 1 — COVER / TITLE SLIDE

**Slide Title:** STORMSIGHT
**Subtitle:** AI-Driven Hyper-Local Early Warning System for Severe Weather & Flash-Flood Nowcasting

**Bullet Points:**
- PS77 · AI-Driven Hyper-Local Early Warning System for Severe Weather Nowcasting
- Smart India Hackathon 2026
- Organisation: Ministry of Earth Sciences / NCMRWF

**Team Box:**
- Team Name: [YOUR TEAM NAME]
- Institution: [COLLEGE NAME]
- Members: [LIST ALL 6 NAMES]

**Visuals to use:**
- Full dashboard screenshot showing the GIS probability map with hazard overlays
- Atmospheric state panel (IWV, CAPE, CIN, shear gauges)
- XAI explanation panel visible on the right
- SIH 2026 logo (top-right corner as per template)

---

## SLIDE 2 — IDEA TITLE / PROPOSED SOLUTION

**Slide Title:** STORMSIGHT — AI-DRIVEN HYPER-LOCAL SEVERE WEATHER NOWCASTING

### ❖ Proposed Solution

**Detailed Explanation of the Solution:**
- StormSight is an AI-driven, multimodal, spatiotemporal nowcasting system that predicts the formation and evolution of severe weather — specifically tracking the **full hazard cascade** from atmospheric precursors through thunderstorms and cloudbursts to terrain-conditioned flash-flood risk
- The system fuses **INSAT-3D/3DR/3DS satellite imagery** (via MOSDAC), **IMDAA regional atmospheric reanalysis** (via NCMRWF), **MOSDAC Quantitative Precipitation Estimation (QPE)**, and **SRTM Digital Elevation Model** data into a unified spatiotemporal input
- A **physics-guided, multi-task deep learning model** with a shared ConvLSTM/ConvGRU spatiotemporal backbone processes temporal sequences of multimodal observations and simultaneously outputs:
  1. **Thunderstorm probability map** (dense spatial, per grid cell)
  2. **Cloudburst probability map** (dense spatial)
  3. **Flash-flood probability map** (terrain-conditioned)
  4. **Explainable AI attribution** (per-feature contributions + spatial saliency)
- Predictions are made at **multiple lead times: T+1h through T+6h**
- The system operates with **physics-guided feature engineering** — deriving IWV, ΔIWV, CAPE, CIN, vertical wind shear, low-level convergence, CTT, ΔCTT, and moisture flux convergence before the neural network sees the data

**How It Addresses the Problem:**
- PS77 asks for real-time prediction of **localised severe weather formation and evolution** with 2–6 hour lead time — StormSight delivers exactly this as probabilistic hazard maps
- Models the **complete physical hazard chain**: atmospheric precursors → convective initiation → severe thunderstorm → extreme rainfall → terrain response → flash-flood risk
- Provides **hyper-local probability maps**, not broad district-level alerts — each grid cell gets its own probability
- **Explainable AI** answers the critical operational question: "Why is the model warning here, now?" — showing which atmospheric signals are driving the prediction
- India already has operational warning infrastructure (IMD, NCMRWF, flash-flood guidance). StormSight is positioned as an **AI fusion layer** that adds value by combining heterogeneous Indian data sources into one coherent probabilistic forecast
- **Terrain-conditioned flash-flood risk** distinguishes rainfall prediction from actual flood hazard — equal rainfall ≠ equal flood risk because of elevation, slope, and drainage differences

**Innovation and Uniqueness:**
- **Physics-guided ML** — physical meteorological features (CAPE, CIN, IWV, shear) are computed first, then the neural network learns nonlinear relationships among known physical quantities, rather than rediscovering meteorology from raw pixels
- **Multi-task hazard cascade** — a single shared backbone learns common atmospheric representations, with separate heads for each hazard stage, reflecting the physical dependency chain
- **Indian data stack** — built specifically for INSAT-3D/3DR/3DS + IMDAA + MOSDAC QPE, not imported from international models
- **Event-window sampling with hard negatives** — overcomes the rare-event problem by constructing temporal sequences around confirmed events and including "favorable but non-event" cases
- **Operational XAI** — not decorative feature attribution, but actionable explanation: "IWV accumulation: High, CAPE: Very High, CIN: Rapidly decreasing, CTT cooling: Strong → Flash Flood Risk 82%"
- **Multi-lead-time evaluation** — skill is measured separately at T+1h through T+6h with proper severe-weather metrics (POD, FAR, CSI, FSS, Brier Score), not generic accuracy
- **Time-separated validation** — no temporal data leakage; train on 2018–2024, validate on 2025, test on 2026

---

## SLIDE 3 — TECHNICAL APPROACH

**Slide Title:** TECHNICAL APPROACH

### Technologies Used

**Programming Languages & Frameworks:**

| Layer | Technology | Purpose |
|---|---|---|
| ML / AI | Python 3.11, PyTorch 2.x | ConvLSTM/ConvGRU backbone, multi-task training |
| Feature Engineering | NumPy, SciPy, MetPy | Physics-guided atmospheric feature derivation |
| Data Pipeline | xarray, NetCDF4, h5py, rasterio, geopandas | Multi-source geospatial data processing |
| Backend | FastAPI (Python) | REST API, inference endpoints, alert service |
| Database | PostgreSQL + SQLAlchemy async | Event data, predictions, alerts |
| Frontend | React 18 + TypeScript | Interactive GIS dashboard SPA |
| Map Layer | Leaflet.js / MapLibre GL | Probability map overlays, satellite animation |
| State Mgmt | Zustand | Frontend state management |
| XAI | SHAP, captum, custom saliency | Feature attribution + explanation generation |
| Deployment | Docker Compose | Containerised full-stack deployment |

**Data Sources:**

| Source | Data Provided | Resolution | Purpose |
|---|---|---|---|
| ISRO MOSDAC INSAT-3D/3DR/3DS | Multi-spectral satellite imagery (TIR, WV, VIS, SWIR, MIR) | 1–8 km, 15–30 min | Cloud structure, CTT, WV, cloud motion |
| IMDAA Reanalysis (NCMRWF) | Temperature, humidity, wind, geopotential profiles | ~12 km, 6-hourly | CAPE, CIN, shear, convergence, moisture |
| MOSDAC QPE Products | Satellite-derived rainfall estimation | Variable | Quantitative precipitation estimation |
| SRTM DEM | Digital Elevation Model | 30m / 90m | Elevation, slope, basin/drainage |
| IMD Bulletins / Records | Severe weather event catalog | Per-event | Ground truth labelling |

**INSAT-3D Imager Characteristics:**

| Channel | Approximate Resolution | What It Captures |
|---|---|---|
| Visible (VIS) | 1 km | Daytime cloud structure |
| SWIR | 1 km | Ice vs. water cloud differentiation |
| MIR | 4 km | Convective vs. stratus cloud |
| TIR1 (10.3µm) | 4 km | Cloud top temperature — primary storm signal |
| TIR2 (11.5µm) | 4 km | Secondary thermal window |
| Water Vapour (6.8µm) | 8 km | Upper-atmosphere moisture circulation |

---

### System Architecture (Draw as visual diagram on slide)

```
┌──────────────────────────────────────────────────────────────────────────┐
│                  DATA ACQUISITION LAYER                                  │
│  MOSDAC INSAT-3D/3DR/3DS  ·  IMDAA Reanalysis (NCMRWF)                │
│  MOSDAC QPE Products  ·  SRTM DEM  ·  IMD Event Records                │
└────────────────────────┬─────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────────────────────┐
│                  DATA PIPELINE LAYER                                     │
│  download_insat.py · download_imdaa.py · download_qpe.py                │
│  compute_features.py · align_grid.py · label_events.py                  │
│  Output: Unified grid tensors [C, H, W] per timestep                    │
│  Physics-guided features: IWV, ΔIWV, CAPE, CIN, shear, ΔCTT, etc.      │
└────────────────────────┬─────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────────────────────┐
│         AI/ML LAYER — Multi-Task Spatiotemporal Model                    │
│                                                                          │
│  Input: [B, T=6, C=21+, H, W] — 6 timesteps × multimodal channels      │
│  → Per-frame CNN encoder (shared weights)                                │
│  → ConvLSTM/ConvGRU temporal processing                                  │
│  → Shared spatiotemporal representation                                  │
│                                                                          │
│  ┌────────────────┐ ┌────────────────┐ ┌────────────────┐               │
│  │ Thunderstorm   │ │ Cloudburst     │ │ Flash-Flood    │               │
│  │ Probability    │ │ Probability    │ │ Probability    │               │
│  │ Head           │ │ Head           │ │ Head           │               │
│  │ [B,1,H,W]     │ │ [B,1,H,W]     │ │ [B,1,H,W]     │               │
│  └────────────────┘ └────────────────┘ └────────────────┘               │
│                                              ↑                           │
│                                     Terrain conditioning                 │
│                                     (DEM + slope + drainage)             │
│                                                                          │
│  Explainable AI: SHAP attributions + spatial saliency maps               │
└────────────────────────┬─────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────────────────────┐
│                  BACKEND LAYER (FastAPI + PostgreSQL)                     │
│  /api/nowcast · /api/predict · /api/explain · /api/alerts                │
│  Event database · Prediction history · Alert dispatch                    │
└────────────────────────┬─────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────────────────────┐
│          FRONTEND LAYER (React + Leaflet/MapLibre GIS Dashboard)         │
│                                                                          │
│  HazardMap: Probability overlay on interactive map                       │
│  AtmosphericPanel: IWV, CAPE, CIN, shear, CTT gauge displays            │
│  TimelineSlider: Lead-time selector (T+1h → T+6h)                       │
│  XAIPanel: "Why is the model warning?" — feature contributions           │
│  AlertFeed: Real-time alert stream                                       │
│  SatelliteView: Live INSAT animation                                     │
└──────────────────────────────────────────────────────────────────────────┘
```

**Methodology — Key Design Decisions:**

1. **Physics-Guided ML:** Derive CAPE, CIN, IWV, shear, ΔCTT first → feed known physical quantities to the neural network → scientifically defensible + explainable
2. **Multi-Task Learning:** Shared backbone learns atmospheric representation; separate heads predict each hazard stage → reflects the physical cascade
3. **Event-Window Sampling:** Temporal sequences around confirmed events + hard negatives → overcomes the rare-event (~0.5%) problem
4. **Terrain Conditioning:** Flash-flood head receives DEM/slope/drainage as additional input → equal rainfall ≠ equal flood risk
5. **Time-Separated Validation:** Train 2018–2024, Val 2025, Test 2026 → no temporal leakage

---

## SLIDE 4 — FEASIBILITY AND VIABILITY

**Slide Title:** FEASIBILITY AND VIABILITY

### Technical Feasibility

- ✅ All primary data sources (MOSDAC, IMDAA, SRTM DEM) are **free and publicly accessible** via government portals
- ✅ INSAT-3D/3DR/3DS data available through MOSDAC with standard registration
- ✅ IMDAA reanalysis provides the atmospheric state variables needed for CAPE/CIN/shear derivation
- ✅ MOSDAC already provides QPE products suitable for validation
- ✅ SRTM DEM is freely available at 30m resolution — global coverage
- ✅ ConvLSTM / ConvGRU architectures are proven for spatiotemporal weather prediction (DGMR, MetNet-3)
- ✅ PyTorch, FastAPI, React — mature, production-grade open-source stack
- ✅ Physics-guided feature engineering uses established meteorological formulations
- ✅ Multi-task learning is well-established in weather prediction literature

### Scientific Feasibility

- International research (DGMR / Nature 2021, MetNet-3 / Google 2023) demonstrates deep learning's effectiveness for precipitation nowcasting
- CAPE/CIN derived from vertical profiles is standard meteorological practice
- CTT cooling rate is a well-documented precursor signal for convective initiation
- Terrain-conditioned flood risk modeling is established in hydrology
- Multi-task prediction of related hazards has shown benefits in weather research

### Operational Feasibility

- Designed to **complement, not replace** existing IMD/NCMRWF operational systems
- Positioned as an **AI fusion layer** feeding into the existing advisory chain
- Output format (probability maps + explanations + alerts) compatible with operational workflows
- Can run inference on standard server hardware — no GPU required at inference time

---

### Challenges and Mitigations

| Challenge | Mitigation |
|---|---|
| Data access — MOSDAC/IMDAA may require registration | Build pipeline with open/research substitutes; keep interfaces compatible |
| Sparse extreme events (~0.5% occurrence) | Event-window sampling + hard negatives + class-balanced focal loss |
| Temporal autocorrelation → data leakage risk | Time-separated validation (train 2018–2024, val 2025, test 2026) |
| Multiple spatial resolutions (1km–12km) | Unified grid alignment pipeline with validated interpolation |
| Missing data across sources | Robust missing-data handling + fallback to available channels |
| False alarm fatigue | POD+FAR+CSI evaluated jointly; calibration analysis |
| Spatial displacement errors | FSS metric with neighborhood verification |
| Label scarcity for cloudbursts | Use IMD bulletins + news reports + satellite-verified events |

---

## SLIDE 5 — IMPACT AND BENEFITS

**Slide Title:** IMPACT AND BENEFITS

### Potential Impact on Target Audience

**Primary: NCMRWF / IMD / National Weather Services**
- AI fusion layer that combines heterogeneous Indian observation data into a single probabilistic forecast
- Hyper-local probability maps complement existing district-level warnings
- Explainable AI enables meteorologists to understand and trust the AI predictions
- 2–6 hour lead time fills the critical gap for convective-scale nowcasting
- Automated monitoring never fatigues — watches every satellite frame continuously

**Secondary: State Disaster Management Authorities (SDMAs) / NDRF**
- Flash-flood probability maps — terrain-conditioned, not generic rainfall alerts
- Pre-positioned disaster response based on hazard-specific predictions (thunderstorm vs. cloudburst vs. flash flood)
- Risk timeline showing hazard evolution helps allocate resources progressively

**Tertiary: Vulnerable Communities**
- Flash floods kill more people in India annually than cyclones
- Hyper-local warnings for mountain valleys, urban catchments, and river basins
- Extra 2–6 hours of lead time for evacuation in flash-flood-prone regions
- Farmers, fishermen, construction workers — weather-exposed populations get actionable warnings

---

### Benefits — Social, Economic, Environmental

**Social Impact:**
- Flash floods caused **~1,600 deaths** in India in 2023 alone — many preventable with better lead time
- Mountain regions (Uttarakhand, Himachal, J&K, Northeast) face repeated devastating cloudbursts
- **Kedarnath 2013** — over 5,000 deaths from a single cloudburst/flash-flood event — hyper-local warning could have saved thousands
- Explainable warnings reduce "alert fatigue" — people trust warnings they can understand
- Calibrated probabilities enable **proportional response** — not every yellow alert requires full evacuation

**Economic Impact:**
- Flash floods cause **₹5,000–15,000 crore** in annual infrastructure damage in India
- Agricultural crop loss from severe convective storms is estimated at **₹10,000+ crore** annually
- Pre-emptive evacuation cost ratio: **1:7** (₹1 on prevention saves ₹7 in post-disaster relief)
- System uses free public data sources — near-zero operational data cost

**Environmental Impact:**
- Climate change increasing frequency and intensity of severe convective events in India
- Western Ghats, Himalayan foothills seeing unprecedented cloudburst frequency
- Automated monitoring scales to increasing event frequency without proportional human analyst increase

---

## SLIDE 6 — RESEARCH AND REFERENCES

**Slide Title:** RESEARCH AND REFERENCES

### Primary Data Sources

1. **ISRO MOSDAC / INSAT-3D/3DR/3DS** — Meteorological and Oceanographic Satellite Data Archival Centre
   Space Applications Centre, ISRO. Multi-spectral meteorological satellite imagery.
   URL: https://www.mosdac.gov.in

2. **IMDAA Regional Reanalysis** — Indian Monsoon Data Assimilation and Analysis
   NCMRWF/IMD/UK Met Office collaboration. ~12 km resolution atmospheric reanalysis.
   Indira et al. (2021). *J. Climate*, 34(12).
   URL: https://journals.ametsoc.org/view/journals/clim/34/12/JCLI-D-20-0412.1.xml

3. **MOSDAC QPE Products** — Satellite-derived rainfall estimation
   URL: https://www.mosdac.gov.in/doi/155/

4. **SRTM DEM** — Shuttle Radar Topography Mission
   NASA/USGS. 30m digital elevation data.
   URL: https://earthexplorer.usgs.gov

5. **IMD Annual Report 2025** — India Meteorological Department
   URL: https://metnet.imd.gov.in/docs/imdnews/ANNUAL_REPORT2025English.pdf

### Scientific Literature

6. **Ravuri, S., et al. (2021).** "Skilful precipitation nowcasting using deep generative models of radar." *Nature*, 597, 672–677. (DGMR)
   URL: https://www.nature.com/articles/s41586-021-03854-z

7. **Andrychowicz, M., et al. (2023).** "MetNet-3: A state-of-the-art neural weather model." Google Research.
   URL: https://research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/

8. **National Flash Flood Guidance System, India**
   URL: https://hydro.imd.gov.in/national/

9. **Cloudburst threshold research.** MAUSAM / IMD.
   URL: https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/view/5084

10. **Flash-flood guidance evaluation, MAUSAM / IMD.**
    URL: https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/view/7366

11. **MOSDAC INSAT-3DS Operational Products**
    URL: https://mosdac.gov.in/docs/INSAT-3DS_Operational_Products_V1.pdf

---

## OPTIONAL SLIDE 7 — THE PROBLEM IN DEPTH

**Slide Title:** THE PROBLEM — THE HAZARD CASCADE

**Key Points:**
- PS77 is NOT simply a rainfall prediction problem
- It asks for prediction of the full **hazard cascade**: atmospheric precursors → convective initiation → severe thunderstorm → cloudburst → terrain-conditioned flash-flood risk
- The critical technical challenge: **predicting WHERE severe weather will develop 2–6 hours ahead** from multimodal observations
- India already has operational systems (IMD nowcasting, National Flash Flood Guidance). The research question is: **"Can AI improve spatial precision, probabilistic quality, lead time, and explainability?"**

**The Hazard Cascade (draw as visual):**

```
09:20  Moisture accumulation ↑           ← Atmospheric precursors
09:50  CAPE ↑ / CIN ↓                    ← Instability building
10:20  Rapid CTT cooling detected        ← Convective initiation
10:40  Severe convection probability: 78% ← Thunderstorm
11:10  Extreme rainfall probability: 71%  ← Cloudburst risk
11:40  Flash-flood probability: 64%       ← Terrain + drainage response
```

**Why this is technically difficult:**
- Severe weather is a **rare event** (~0.5% of observations)
- High CAPE alone ≠ disaster — many favorable setups produce nothing
- The signal is **nonlinear, spatial, temporal, and multimodal**
- Cloud Top Temperature (CTT) cooling rate is inherently temporal — sequence matters more than single snapshots
- Equal rainfall ≠ equal flood risk — terrain, slope, drainage all matter

---

## OPTIONAL SLIDE 8 — DASHBOARD CONCEPT

**Slide Title:** THE PLATFORM — HYPER-LOCAL NOWCASTING DASHBOARD

**Dashboard Layout (draw as visual):**

```
┌─────────────────────────────────────────────────────┐
│ STORMSIGHT — SEVERE WEATHER NOWCAST                  │
├───────────────────────┬─────────────────────────────┤
│                       │                             │
│   GIS HAZARD MAP      │     ATMOSPHERIC STATE       │
│   Probability         │     IWV ↑   CAPE ↑          │
│   overlays            │     CIN ↓   SHEAR ↑         │
│   (Leaflet/MapLibre)  │     CTT ↓                   │
│                       │                             │
│   🔴 Flash Flood 64%  │   HAZARD PROBABILITIES      │
│   🟠 Cloudburst  71%  │   Thunderstorm   78%        │
│   🟡 Thunderstorm 78% │   Cloudburst     71%        │
│                       │   Flash Flood    64%        │
├───────────────────────┴─────────────────────────────┤
│ TIMELINE SLIDER                                      │
│ T+1h   T+2h   T+3h   T+4h   T+5h   T+6h           │
├─────────────────────────────────────────────────────┤
│ WHY THE MODEL IS WARNING (XAI)                       │
│ Rapid CTT cooling + moisture accumulation + slope    │
│ + increasing QPE → SHAP attributions visible         │
├─────────────────────────────────────────────────────┤
│ ALERTS / LOCATION SEARCH / API STATUS                │
└─────────────────────────────────────────────────────┘
```

The UI should help a user answer **three questions immediately:**
1. **Where is the hazard?** → Probability map
2. **How likely is it?** → Per-hazard probabilities at selected lead time
3. **Why is the system warning me?** → XAI panel with feature contributions

---

## OPTIONAL SLIDE 9 — MODELING PROGRESSION & ABLATION

**Slide Title:** FROM BASELINES TO FULL HAZARD CASCADE MODEL

**Ablation Study Table (show on slide):**

| Model | Satellite | Thermodynamics | QPE | DEM | Output |
|---|---|---|---|---|---|
| **M1** Persistence | No | No | Yes | No | Rainfall extrapolation baseline |
| **M2** XGBoost | Yes | Yes | Yes | No | Engineered-feature baseline |
| **M3** ConvLSTM | Yes | Yes | Yes | No | Spatiotemporal risk maps |
| **M4** Temporal U-Net | Yes | Yes | Yes | Yes | Dense probability maps |
| **M5** Multi-Task | Yes | Yes | Yes | Yes | Full hazard cascade |

**Key research questions answered by each step:**
- M1 → How much can you get without AI?
- M2 → How much do physics-guided features help?
- M3 → Does spatiotemporal learning add value?
- M4 → Does terrain conditioning improve flash-flood prediction?
- M5 → Does multi-task learning outperform independent models?

---

## OPTIONAL SLIDE 10 — TEAM SLIDE

**Slide Title:** OUR TEAM

| Name | Role | Contribution |
|---|---|---|
| [Member 1] | ML Engineer | ConvLSTM backbone, multi-task heads, training pipeline |
| [Member 2] | Data Engineer | MOSDAC/IMDAA download pipeline, grid alignment, feature computation |
| [Member 3] | Backend Developer | FastAPI, PostgreSQL, inference API, alert service |
| [Member 4] | Frontend Developer | React GIS dashboard, hazard maps, timeline, XAI panel |
| [Member 5] | Research / XAI | Physics-guided features, SHAP/saliency, evaluation metrics |
| [Member 6] | DevOps / PM | Docker, deployment, documentation, event labelling |

**Mentor:** [FACULTY NAME], [DESIGNATION], [INSTITUTION]

---

---

# APPENDIX A — KEY NUMBERS TO MEMORISE (BACKSTAGE REFERENCE)

| Number | Context |
|---|---|
| **2–6 hours** | Lead time target for severe weather nowcasting |
| **~0.5%** | Severe events as fraction of all observations (rare-event problem) |
| **1,600** | Approximate deaths from flash floods in India in 2023 |
| **5,000+** | Deaths in Kedarnath cloudburst/flash-flood disaster (2013) |
| **₹5,000–15,000 crore** | Annual infrastructure damage from flash floods in India |
| **1:7** | Cost ratio: pre-emptive evacuation vs. post-disaster relief |
| **T+1h to T+6h** | Lead times at which model is evaluated |
| **POD, FAR, CSI** | Primary evaluation metrics (not plain accuracy) |
| **FSS** | Spatial verification metric (displacement tolerance) |
| **Brier Score** | Probabilistic forecast quality metric |
| **3** | Number of hazard types: thunderstorm, cloudburst, flash flood |
| **Hard negatives** | High-CAPE/no-event cases critical for reducing false alarms |
| **IMDAA** | Indian Monsoon Data Assimilation and Analysis (regional reanalysis) |
| **CTT** | Cloud Top Temperature — key precursor signal |
| **ΔCTT** | CTT cooling rate — temporal evolution of convective growth |
| **IWV** | Integrated Water Vapor — atmospheric moisture column |
| **CAPE** | Convective Available Potential Energy |
| **CIN** | Convective Inhibition |

---

# APPENDIX B — ANTICIPATED JUDGE Q&A

**Q: How is this different from what IMD / NCMRWF already does?**
> India already has world-class operational weather infrastructure. StormSight is an **AI fusion layer** that complements the existing ecosystem. We combine INSAT satellite evolution, IMDAA thermodynamics, QPE rainfall, and terrain into one coherent probabilistic forecast with hyper-local spatial resolution and explainable AI — something no single existing system provides in a unified manner.

**Q: Why is this better than existing flash-flood guidance?**
> The National Flash Flood Guidance System uses hydrological models and rainfall thresholds. StormSight adds **upstream prediction** — forecasting severe weather formation 2–6 hours before the rainfall occurs, using satellite temporal evolution and atmospheric precursor signals. We predict the cause, not just react to the consequence.

**Q: How do you handle the rare-event problem?**
> Three strategies: (1) **Event-window sampling** — construct temporal sequences centered on confirmed severe events. (2) **Hard negatives** — include cases where CAPE was high and moisture was favorable but no severe event occurred. (3) **Focal loss with positive weighting** — the loss function heavily penalises missed events. This teaches the model that "high CAPE alone ≠ disaster."

**Q: What makes the physics-guided approach better than end-to-end deep learning?**
> End-to-end models must rediscover basic meteorology from raw pixels. Physics-guided ML gives the network known physical quantities (CAPE, CIN, IWV, shear, ΔCTT) as inputs. This is scientifically defensible, more data-efficient, and much easier to explain — the XAI panel can show "CAPE contributed 30% to this prediction" because the model explicitly receives CAPE.

**Q: How do you evaluate a rare-event prediction system?**
> Plain accuracy is meaningless — a model saying "no event" 99.5% of the time gets 99.5% accuracy. We use **POD** (did we catch events?), **FAR** (how many false alarms?), **CSI** (overall overlap), **FSS** (spatial tolerance), and **Brier Score** (probabilistic quality). Evaluated separately at each lead time from T+1h to T+6h, because skill degrades with lead time.

**Q: What is the difference between cloudburst probability and flash-flood probability?**
> Cloudburst is an atmospheric phenomenon — extreme rainfall intensity (typically >100mm/hour). Flash-flood is a hydrological consequence that depends on terrain: elevation, slope, basin shape, drainage density. Equal rainfall in a mountain valley vs. a flat plain produces very different flood risk. The flash-flood head is terrain-conditioned using DEM/slope/drainage data.

**Q: Can this work in real time?**
> Yes. INSAT-3D data is available from MOSDAC approximately every 15–30 minutes. The inference model processes a new observation in milliseconds on CPU. The pipeline is: new INSAT frame → feature extraction → model inference → probability maps → alert dispatch, all automated.

**Q: How do you prevent data leakage?**
> Weather data is highly autocorrelated in time. Random splitting adjacent timesteps across train/test produces inflated metrics. We use **time-separated validation**: train on 2018–2024, validate on 2025, test on 2026. Optionally, **event-separated** validation ensures entire storm systems stay in one split.

**Q: What about false alarms?**
> The system is calibrated: a 70% probability should materialize ~70% of the time over many cases. We explicitly evaluate FAR alongside POD. Hard-negative training reduces the model's tendency to over-predict. The probability map format gives users nuanced information (yellow vs. orange vs. red) rather than binary yes/no alerts.

---

# APPENDIX C — DESIGN NOTES FOR PPT CREATION

- **Color Scheme:** Dark navy/charcoal background + amber/orange for thunderstorm, deep red for flash-flood, electric blue for atmospheric state. Match the dashboard aesthetic.
- **Font:** IBM Plex Sans or Inter (Google Fonts) for clean, technical look.
- **Slide 3 architecture:** Draw as a 5-layer vertical diagram with tech logos (ISRO/MOSDAC, Python, PyTorch, FastAPI, React, Leaflet).
- **Slide 5 impact numbers:** Large bold callout numbers (e.g., "5,000+ lives" in 80pt, "2–6 hours" in 80pt, "3 hazards" in 80pt).
- **Hazard cascade diagram:** Draw the timeline evolution (09:20 → 11:40) as a descending chain with increasing color intensity.
- **XAI explanation:** Show a mock-up with actual feature contribution bars: "CAPE: ████ 30%, CTT cooling: ████ 25%, IWV: ███ 20%".
- **Ablation table:** Highlight rows M1→M5 with checkmarks showing progressive feature inclusion.
- **Max 5 bullet points per slide** — use speaker notes for detail.
- **Avoid:** Stock photos, plain white backgrounds, walls of text, generic "AI weather app" language.
- **Key visual:** Show a side-by-side: "Generic Rainfall Map" vs. "StormSight Hazard Cascade" — demonstrating the depth difference.

---

# APPENDIX D — STRONGEST DIFFERENTIATION FROM PS70 (CYCLONEWATCH)

| Aspect | PS70 — CycloneWatch | PS77 — StormSight |
|---|---|---|
| **Hazard** | Tropical cyclones (large, 100+ km) | Severe thunderstorms, cloudbursts, flash floods (localised, <50 km) |
| **Scale** | Synoptic (ocean basin) | Mesoscale / hyper-local |
| **Lead time** | T+12h, T+24h, T+48h | T+1h to T+6h (nowcasting) |
| **Primary data** | GridSat-B1, INSAT-3DR, ERA5, Copernicus Marine | INSAT-3D/3DR/3DS, IMDAA, QPE, DEM |
| **Key signal** | Cloud morphology classification (Dvorak) | Atmospheric precursors (CAPE, CIN, IWV, CTT cooling rate) |
| **Output** | Cyclone pattern label + track + intensity | Multi-hazard probability maps at each lead time |
| **Terrain** | Coastal distance only | Full DEM/slope/drainage conditioning for flash-flood risk |
| **XAI** | Structural pattern explanation | Per-feature meteorological attribution |
| **Evaluation** | Classification accuracy + MAE | POD, FAR, CSI, FSS, Brier Score |
| **Event type** | Rare (5–10 cyclones/year in NIO) | Less rare but still sparse (~0.5% of observations) |
| **Organisation** | IMD | NCMRWF |

**Shared team expertise / knowledge transfer:**
- MOSDAC data access and processing pipeline
- ConvLSTM/ConvGRU spatiotemporal architectures
- FastAPI + React + Leaflet full-stack pattern
- Docker deployment pattern
- SIH presentation experience

---

*End of SIH 2026 PPT Reference Document (PS77) — StormSight*

*Source: PS77 research brief, PS70 PPT reference (format template),
SIH 2026 problem statement portal.*
