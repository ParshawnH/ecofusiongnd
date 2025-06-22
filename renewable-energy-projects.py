import pandas as pd

# Create a dataset from the renewable energy projects table
data = {
    "Renewable Energy Source": [
        "Solar Photo-Voltaic", 
        "Wind Energy", 
        "Geothermal", 
        "Wave Energy"
    ],
    "Capacity": ["800 kWh", "30 MW", "15 MW", "2 MW"],
    "Development Partner": [
        "United Arab Emirates (UAE)",
        "International organization (not specified)",
        "Caribbean Development Bank (CDB)",
        "Ireland-Based Seabase Group"
    ],
    "Total Estimated Cost (USD)": [
        4_400_000,  # Provided
        25_000_000,  # Estimated for 30 MW
        142_000_000,  # Provided
        5_000_000  # Estimated for 2 MW pilot
    ],
    "Funding Source": [
        "UAE-Caribbean Renewable Energy Fund (UAE-CREF)",
        "Green Climate Fund (assumed)",
        "Caribbean Development Bank (CDB)",
        "Private Investment (assumed)"
    ]
}

df_projects = pd.DataFrame(data)

import ace_tools as tools; tools.display_dataframe_to_user(name="Grenada Renewable Energy Projects", dataframe=df_projects)
