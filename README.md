# EcoFusion GND Renewable Energy

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)



**Live Demo:** [https://ecofusion-gnd-renewableenergy.lovable.app/](https://ecofusion-gnd-renewableenergy.lovable.app/)

## 🚀 Overview

**EcoFusion GND** is an interactive dashboard and data-analysis toolkit that helps Grenada’s planners balance dollars and clean-energy capacity. From budgeting grid upgrades and storage to optimizing solar, wind, and wave installations, EcoFusion GND turns inputs into recommended unit allocations and gap analyses.

## 🔑 Key Features

- **Budget Configuration**  
  Reserve portions of your total budget for grid upgrades and energy storage.

- **Estimator Tab**  
  • Input your Total Budget ($), Installation Cost Allocation (%), Storage (% of Daily Energy), and Storage Cost ($/kWh)  
  • Specify unit costs, outputs, OPEX, and maintenance for Solar, Wind, and Wave technologies  
  • “Calculate Allocation” computes how many units of each tech you can afford based on cost-effectiveness.

- **Targets**  
  Set renewable-generation and EV-adoption goals over a multi-year horizon.

- **Renewable Progress Tracker**  
  Visualize historical vs. forecasted renewable capacity and budget spending.

- **Implementation Plan**  
  Geo-map proposed installations, view charger or plant locations over Grenada’s outline.

- **AI Plant Locator**  
  Recommend optimal sites for new renewables using machine-learning suitability scores.

---
## 🛠️ Tech Stack

- **Frontend:** React + TypeScript  
- **Styling/UI:** Chakra UI, Recharts, Leaflet.js  
- **Backend Forecasting:** Python (Holt-Winters / Exponential Smoothing) exposed via Netlify Functions  
- **Data:** World Bank API for energy indicators, custom CSVs for cost/OPEX parameters  
- **Deployment:** Vercel (frontend) & Netlify Functions (data API)
- **Data Analysis,Forecasting and Calculations :** Python


```sh
# Step 1: Clone the repository using the project's Git URL.
git clone <YOUR_GIT_URL>

# Step 2: Navigate to the project directory.
cd <YOUR_PROJECT_NAME>

# Step 3: Install the necessary dependencies.
npm i

# Step 4: Start the development server with auto-reloading and an instant preview.
npm run dev
```
## Code Conversion Note
All original analysis notebooks and scripts were authored in Python.
The front-end application—including map rendering, interactive UI, and final UI components—was generated and fine-tuned by Lovable from those Python prototypes.

