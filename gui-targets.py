import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, HTML

# Data
data = [
    {"Year": 2024, "Target": 20.00, "Forecast": 1.02},
    {"Year": 2025, "Target": 25.00, "Forecast": 1.17},
    {"Year": 2026, "Target": 30.00, "Forecast": 1.32},
    {"Year": 2027, "Target": 35.00, "Forecast": 1.47},
    {"Year": 2028, "Target": 40.00, "Forecast": 1.62},
    {"Year": 2029, "Target": 45.00, "Forecast": 1.77},
    {"Year": 2030, "Target": 50.00, "Forecast": 1.92},
    {"Year": 2031, "Target": 60.00, "Forecast": 2.07},
    {"Year": 2032, "Target": 70.00, "Forecast": 2.22},
    {"Year": 2033, "Target": 80.00, "Forecast": 2.37},
    {"Year": 2034, "Target": 90.00, "Forecast": 2.52},
    {"Year": 2035, "Target": 100.00, "Forecast": 2.67},
]
df = pd.DataFrame(data)
df["Gap"] = df["Target"] - df["Forecast"]
df["Status"] = df["Gap"].apply(lambda g: "Below Target" if g > 0 else "Above Target")

# Display Table
styled_table = df.style.applymap(
    lambda v: "color: red;" if isinstance(v, float) and v > 0 else "color: green;",
    subset=["Gap"]
).format({
    "Target": "{:.2f}%",
    "Forecast": "{:.2f}%",
    "Gap": "{:.2f}%"
})
display(HTML("<h3>📋 Grenada Renewable Energy Targets (2024–2035)</h3>"))
display(styled_table)

# Chart
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
plt.plot(df["Year"], df["Target"], label="Target", linewidth=2, marker='o', color="#0369a1")
plt.plot(df["Year"], df["Forecast"], label="Forecast", linewidth=2, marker='o', color="#16a34a")
plt.plot(df["Year"], df["Gap"], label="Gap", linestyle='--', marker='o', color="#ef4444")
plt.title("Grenada Renewable Energy Targets vs Forecast", fontsize=14)
plt.ylabel("Renewable Share (%)")
plt.xlabel("Year")
plt.ylim(0, 110)
plt.legend()
plt.tight_layout()
plt.show()

# Explanation
explanation_html = """
<div style="margin-top: 24px; padding: 16px; background: #ebf8ff; border-radius: 6px; font-size: 0.95em;">
  <p><strong>About This Data:</strong></p>
  <p>This table displays Grenada's renewable energy targets from 2024 to 2035, showing the targeted renewable energy share, forecasted share based on historical trends, and the gap between them.</p>
  <p style="margin-top: 8px;">A <span style="color: red;">positive gap</span> indicates forecasted renewable energy is below target, requiring additional intervention. A <span style="color: green;">negative gap</span> means the target is exceeded.</p>
  <p style="margin-top: 8px;">The chart highlights how current progress significantly lags behind national goals, underscoring the urgency of accelerated implementation.</p>
</div>
"""
display(HTML(explanation_html))
