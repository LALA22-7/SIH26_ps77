# StormSight — AI-Driven Hyper-Local Severe Weather & Flash-Flood Nowcasting

**Smart India Hackathon 2026 Submission · PS77 (SIH26077)**  
*AI-driven hyper-local early warning system for severe weather nowcasting — fusing Indian satellite, atmospheric reanalysis, precipitation, and terrain data to predict severe thunderstorms, cloudbursts, and flash-flood risk with 2–6 hour lead time.*

> **Organisation:** Ministry of Earth Sciences / NCMRWF  
> **Category:** Software · **Theme:** Disaster Management

---

## 🎯 One-Line Positioning

> **An explainable AI fusion layer for hyper-local 2–6 hour severe-weather and flash-flood risk prediction using Indian satellite, atmospheric, precipitation, and terrain data.**

---

## 🌩️ What Is StormSight?

StormSight is a multimodal, spatiotemporal, probabilistic nowcasting system that predicts the **formation and evolution of localised severe weather** — specifically the progression from atmospheric precursors → severe thunderstorms → cloudbursts → flash-flood risk.

Unlike generic rainfall classifiers, StormSight models the **full hazard cascade**:

```
Atmospheric State (Moisture + Instability + Lift)
        ↓
Convective Initiation
        ↓
Severe Thunderstorm
        ↓
Cloudburst / Extreme Rainfall
        ↓
Terrain + Drainage Response
        ↓
Flash-Flood Risk
        ↓
Hyper-Local Warning + Explanation
```

### Why This Matters

India already has world-class operational weather infrastructure (IMD, NCMRWF, radar networks, flash-flood guidance). StormSight is **not** a replacement — it is an **AI fusion layer** that adds value by:

- Combining heterogeneous signals (satellite evolution + thermodynamics + rainfall + terrain) into **one coherent probabilistic forecast**
- Providing **hyper-local** probability maps, not district-level broad alerts
- Offering **Explainable AI** — answering "why is the model warning here, now?"
- Targeting the critical **2–6 hour lead time** gap for severe convective weather

---

## 📂 Repository Structure

```
SIH26_ps77/
├── backend/                    # FastAPI server, PostgreSQL, inference endpoints
│   ├── app/
│   │   ├── api/                # Route handlers: /predict, /nowcast, /alerts, /explain
│   │   ├── core/               # Config, settings, constants
│   │   ├── db/                 # SQLAlchemy async engine & session management
│   │   ├── models/             # DB ORM models (events, predictions, alerts)
│   │   ├── schemas/            # Pydantic request/response schemas
│   │   └── services/           # nowcast_service.py, xai_service.py, alert_service.py
│   ├── scripts/                # seed_db.py, precompute_events.py
│   ├── tests/                  # Pytest test suite
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── README.md
│
├── ml/                         # PyTorch ML pipeline
│   ├── src/
│   │   ├── models/
│   │   │   ├── backbone.py     # Shared spatiotemporal encoder (ConvLSTM/ConvGRU)
│   │   │   ├── heads.py        # Multi-task heads (thunderstorm, cloudburst, flash-flood)
│   │   │   ├── unet.py         # U-Net / Temporal U-Net for dense probability maps
│   │   │   └── fusion.py       # Multimodal feature fusion module
│   │   ├── dataset.py          # Event-window dataset with hard negatives
│   │   ├── train.py            # Multi-task training loop
│   │   ├── evaluate.py         # POD, FAR, CSI, FSS, Brier Score evaluation
│   │   ├── features.py         # Physics-guided feature engineering
│   │   └── xai.py              # SHAP, saliency maps, attention attribution
│   ├── baselines/
│   │   ├── persistence.py      # Baseline 1: Persistence / advection
│   │   └── gradient_boost.py   # Baseline 2: XGBoost with engineered features
│   ├── inference.py            # Public predict() API for backend integration
│   ├── checkpoints/            # Trained model weights
│   │   └── .gitkeep
│   ├── configs/
│   │   ├── model_config.json   # Architecture hyperparameters
│   │   └── training_config.json
│   ├── notebooks/              # Exploratory analysis & ablation studies
│   └── README.md
│
├── data/                       # Data pipeline & processed datasets
│   ├── raw/                    # Downloaded satellite/reanalysis files (gitignored)
│   ├── interim/                # Intermediate processing outputs (gitignored)
│   ├── processed/              # Final training-ready tensors
│   │   └── .gitkeep
│   ├── ground_truth/           # Labelled severe weather events
│   │   ├── events_catalog.csv  # Master event catalog with metadata
│   │   └── .gitkeep
│   ├── dem/                    # Digital elevation, slope, basin layers
│   │   └── .gitkeep
│   ├── event_manifest.csv      # Event-window training manifest
│   └── README.md
│
├── scripts/                    # Data acquisition & processing pipeline
│   ├── download_insat.py       # INSAT-3D/3DR/3DS data from MOSDAC
│   ├── download_imdaa.py       # IMDAA reanalysis download
│   ├── download_qpe.py         # QPE / rainfall estimation data
│   ├── download_dem.py         # SRTM / DEM / terrain data
│   ├── compute_features.py     # Derive IWV, CAPE, CIN, shear, ΔCTT, convergence
│   ├── align_grid.py           # Spatiotemporal alignment to unified grid
│   ├── label_events.py         # Event-window extraction + labelling
│   ├── build_hard_negatives.py # Construct hard-negative samples
│   └── requirements.txt
│
├── frontend/                   # React + TypeScript GIS dashboard
│   ├── src/
│   │   ├── App.tsx             # Root layout
│   │   ├── components/
│   │   │   ├── Dashboard/
│   │   │   │   ├── HazardMap.tsx       # Leaflet/MapLibre probability map overlay
│   │   │   │   ├── AtmosphericPanel.tsx # IWV, CAPE, CIN, shear, CTT gauges
│   │   │   │   ├── TimelineSlider.tsx  # Lead-time selector (T+1h → T+6h)
│   │   │   │   ├── XAIPanel.tsx        # Explainability: feature contributions
│   │   │   │   ├── AlertFeed.tsx       # Real-time alert stream
│   │   │   │   └── SatelliteView.tsx   # Live INSAT animation viewer
│   │   │   └── shared/
│   │   ├── store/              # Zustand state management
│   │   ├── data/               # Region configs, event metadata
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   └── README.md
│
├── docs/                       # Technical documentation
│   ├── SIH26_PS77_PPT_REFERENCE.md  # PPT content bible (this repo's equivalent)
│   ├── architecture.md         # System architecture deep-dive
│   ├── data_sources.md         # All data sources, formats, access
│   ├── feature_engineering.md  # Derived atmospheric features explained
│   ├── evaluation_metrics.md   # POD, FAR, CSI, FSS, Brier Score definitions
│   ├── xai_guide.md            # Explainability approach & techniques
│   ├── hazard_cascade.md       # The thunderstorm → cloudburst → flash-flood chain
│   ├── ablation_study.md       # Model comparison & feature contribution
│   └── api_contract.md         # Full API schema documentation
│
├── PROJECT_EXPLAINER.md        # Non-technical full project explainer
└── README.md                   # This file
```

---

## 🚀 Local Development Setup

> **Prerequisites:** Python 3.11+, Node.js 18+, Git

### Step 1 — Clone the repo

```bash
git clone https://github.com/LALA22-7/SIH26_ps77.git
cd SIH26_ps77
```

### Step 2 — Backend Setup (FastAPI)

```bash
cd backend

# Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Configure environment:**
```bash
cp .env.example .env
```

```env
DATABASE_URL=sqlite+aiosqlite:///./stormsight.db
CORS_ORIGINS=http://localhost:5173
DEBUG=true
ML_FORCE_STUB=true
```

**Start the server:**
```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### Step 3 — Frontend Setup (React Dashboard)

```bash
cd frontend
npm install
npm run dev
```

Dashboard at: `http://localhost:5173`

### Step 4 — (Optional) ML Training

```bash
cd ml
python -m src.train --config configs/training_config.json
```

---

## 🧠 Architecture Overview

```
                         LIVE / HISTORICAL DATA
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
           INSAT               IMDAA                 QPE
        3D/3DR/3DS           Reanalysis          Rainfall
             │                    │                    │
             ▼                    ▼                    ▼
       WV / TIR / CTT      CAPE / CIN / Shear      Rainfall fields
       IWV / cloud motion  Convergence / profiles
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  ▼
                         DATA ALIGNMENT / GRID
                              (align_grid.py)
                                  │
                                  ▼
                       SPATIOTEMPORAL MODEL
                         (Shared Backbone)
                                  │
             ┌────────────────────┼────────────────────┐
             ▼                    ▼                    ▼
      Thunderstorm           Cloudburst          Flash-Flood
      Probability            Probability          Probability
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  ▼
                       TERRAIN / BASIN CONDITIONING
                            (DEM + Slope)
                                  │
                                  ▼
                           RISK MAP ENGINE
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
                GIS Dashboard    XAI      Alerts / API
```

---

## 📊 Modeling Progression (Baselines → Final)

| Model | Satellite | Thermodynamics | QPE | DEM | Output |
|---|---|---|---|---|---|
| **M1** — Persistence/Advection | No | No | Yes | No | Rainfall extrapolation baseline |
| **M2** — XGBoost | Yes | Yes | Yes | No | Engineered-feature baseline |
| **M3** — ConvLSTM/ConvGRU | Yes | Yes | Yes | No | Spatiotemporal risk maps |
| **M4** — Temporal U-Net | Yes | Yes | Yes | Yes | Dense probability maps |
| **M5** — Multi-Task Backbone | Yes | Yes | Yes | Yes | Full hazard cascade |

---

## 🔬 Evaluation Metrics

| Metric | Purpose |
|---|---|
| **POD** (Probability of Detection) | Did we catch observed events? |
| **FAR** (False Alarm Ratio) | How many warnings were false? |
| **CSI** (Critical Success Index) | Overall event overlap quality |
| **FSS** (Fractions Skill Score) | Spatial displacement tolerance |
| **Brier Score** | Probabilistic forecast quality |
| **Calibration** | Does 70% risk → ~70% occurrence? |

Evaluated at lead times: **T+1h, T+2h, T+3h, T+4h, T+5h, T+6h**

---

## 📡 Data Sources

| Source | Data | Resolution | Purpose |
|---|---|---|---|
| ISRO MOSDAC INSAT-3D/3DR/3DS | Multi-spectral satellite imagery | 1–8 km, 15–30 min | Cloud structure, CTT, WV, cloud motion |
| IMDAA Reanalysis (NCMRWF) | Atmospheric state variables | ~12 km, 6-hourly | CAPE, CIN, shear, humidity, temperature profiles |
| MOSDAC QPE Products | Satellite-derived rainfall | Variable | Quantitative precipitation estimation |
| SRTM DEM | Digital elevation model | 30m / 90m | Elevation, slope, basin/drainage characteristics |
| IMD Bulletins | Severe weather event records | Per-event | Ground truth event labelling |

---

## 🏗️ Key Technical Decisions

### Why Multi-Task Learning?
A shared encoder learns common atmospheric representations. Separate heads predict thunderstorm, cloudburst, and flash-flood probability. This reflects the physical hazard chain and produces a more coherent forecast than three independent models.

### Why Physics-Guided ML?
Instead of raw-pixel deep learning, we derive physically meaningful features (IWV, CAPE, CIN, vertical shear, ΔCTT, convergence) first. The neural network learns nonlinear relationships among known meteorological quantities — scientifically defensible and easier to explain.

### Why Event-Window Sampling?
Severe weather is rare (~0.5% of observations). We construct temporal sequences around confirmed events and include **hard-negative** cases (high CAPE + no event) to prevent the model from just predicting "no event" always.

---

## 🔮 Research Questions

| # | Question |
|---|---|
| **RQ1** | Does satellite temporal evolution improve prediction over atmospheric variables alone? |
| **RQ2** | Does CTT cooling rate improve convective initiation detection? |
| **RQ3** | Does combining CAPE/CIN with moisture and wind-shear reduce false alarms? |
| **RQ4** | Does terrain conditioning improve flash-flood risk over rainfall-only models? |
| **RQ5** | Does multimodal fusion outperform single-source models? |
| **RQ6** | Does multi-task learning outperform three independent hazard models? |
| **RQ7** | How much predictive skill is retained at 2, 4, and 6 hour lead times? |

---

## ⚠️ Key Technical Risks & Mitigations

| Risk | Mitigation |
|---|---|
| **Data access** — operational datasets may need registration | Build pipeline with open/research data substitutes; keep interfaces compatible |
| **Sparse extreme events** | Event-window sampling + hard negatives + class-balanced objectives |
| **Data leakage** — temporal autocorrelation | Time-separated validation (e.g., train 2018–2024, val 2025, test 2026) |
| **False alarms** — over-warning loses trust | Evaluate POD+FAR+CSI together; calibration analysis |
| **Spatial mismatch** | FSS metric + displacement error visualisation |

---

## 📖 Documentation Map

| Topic | Document |
|---|---|
| Non-technical project explainer | [PROJECT_EXPLAINER.md](PROJECT_EXPLAINER.md) |
| PPT content reference | [docs/SIH26_PS77_PPT_REFERENCE.md](docs/SIH26_PS77_PPT_REFERENCE.md) |
| System architecture | [docs/architecture.md](docs/architecture.md) |
| Data sources guide | [docs/data_sources.md](docs/data_sources.md) |
| Feature engineering | [docs/feature_engineering.md](docs/feature_engineering.md) |
| Evaluation metrics | [docs/evaluation_metrics.md](docs/evaluation_metrics.md) |
| Explainability guide | [docs/xai_guide.md](docs/xai_guide.md) |
| Hazard cascade model | [docs/hazard_cascade.md](docs/hazard_cascade.md) |
| API contract | [docs/api_contract.md](docs/api_contract.md) |
| Backend setup | [backend/README.md](backend/README.md) |
| ML pipeline | [ml/README.md](ml/README.md) |
| Frontend guide | [frontend/README.md](frontend/README.md) |

---

## 🤝 Contributing

This is a team project for SIH 2026. Each team member should:

1. **Clone** the repo and set up the local environment (Steps 1–3 above)
2. **Create a feature branch** for your work: `git checkout -b feature/your-feature`
3. **Commit with clear messages**: `git commit -m "feat(ml): add ConvLSTM backbone"`
4. **Push and open a PR**: `git push origin feature/your-feature`

### Branch Naming Convention
- `feature/` — new features
- `fix/` — bug fixes
- `data/` — data pipeline changes
- `docs/` — documentation updates

### Team Role Assignments

| Role | Responsibilities | Key Directories |
|---|---|---|
| **ML Engineer** | Model architecture, training, evaluation | `ml/` |
| **Data Engineer** | Data download, processing, alignment pipeline | `scripts/`, `data/` |
| **Backend Developer** | API endpoints, database, inference integration | `backend/` |
| **Frontend Developer** | GIS dashboard, maps, XAI panels | `frontend/` |
| **Research / XAI** | Feature engineering, explainability, evaluation | `ml/src/xai.py`, `docs/` |
| **DevOps / PM** | Docker, deployment, documentation, coordination | `docs/`, root configs |

---

*Built for Smart India Hackathon 2026 · PS77 · Ministry of Earth Sciences / NCMRWF*
