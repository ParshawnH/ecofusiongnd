import pandas as pd
import numpy as np

# Known data points from the chart
data = {
    "Year": [2021, 2025, 2030, 2035],
    "Renewable_Energy_Percentage": [5, 25, 50, 100]
}

# Create initial dataframe
df_known = pd.DataFrame(data)

# Interpolate missing years linearly
df_full = pd.DataFrame({'Year': list(range(2021, 2036))})
df_full = df_full.merge(df_known, on='Year', how='left')
df_full['Renewable_Energy_Percentage'] = df_full['Renewable_Energy_Percentage'].interpolate(method='linear')

import ace_tools as tools; tools.display_dataframe_to_user(name="Interpolated Renewable Energy Data", dataframe=df_full)
