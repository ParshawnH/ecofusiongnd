import ipywidgets as widgets
from IPython.display import display, clear_output
import matplotlib.pyplot as plt
import pandas as pd

# Renewable energy targets (mock data)
renewable_targets_data = {
    year: target for year, target in [
        (2021, 5.00), (2022, 10.00), (2023, 15.00), (2024, 20.00), (2025, 25.00),
        (2026, 30.00), (2027, 35.00), (2028, 40.00), (2029, 45.00), (2030, 50.00),
        (2031, 60.00), (2032, 70.00), (2033, 80.00), (2034, 90.00), (2035, 100.00)
    ]
}

# Widgets
year_input = widgets.BoundedIntText(value=2024, min=2021, max=2035, description="Year:")
nonrenewable_input = widgets.FloatText(value=0, description="Non-Renewable (MWh):")
renewable_input = widgets.FloatText(value=0, description="Renewable (MWh):")
generate_button = widgets.Button(description="Generate Report", button_style='success')
output_area = widgets.Output()

def generate_report(button):
    with output_area:
        clear_output()
        year = year_input.value
        non_renewable = nonrenewable_input.value
        renewable = renewable_input.value
        total = non_renewable + renewable
        actual_pct = (renewable / total) * 100 if total > 0 else 0
        target_pct = renewable_targets_data.get(year, 0)
        gap_pct = target_pct - actual_pct

        print(f"📅 Year: {year}")
        print(f"🔋 Actual Renewable Share: {actual_pct:.2f}%")
        print(f"🎯 Target Renewable Share: {target_pct:.2f}%")
        print(f"📉 Gap: {gap_pct:.2f}% {'below' if gap_pct > 0 else 'above'} target")

        # Chart
        data = pd.DataFrame([{
            "Year": str(year),
            "Actual": actual_pct,
            "Target": target_pct
        }])
        ax = data.plot(kind='bar', x='Year', y=['Actual', 'Target'], color=['#22c55e', '#0369a1'])
        ax.set_ylabel("Percentage (%)")
        ax.set_title("Renewable Energy Share vs Target")
        ax.legend(["Actual Renewable Share", "Target Renewable Share"])
        ax.set_ylim(0, 110)
        plt.grid(axis='y', linestyle='--', alpha=0.4)
        plt.tight_layout()
        plt.show()

        # Interpretation
        print("\n📈 Analysis Interpretation:")
        if gap_pct > 0:
            required_mwh = (gap_pct / 100) * total
            print(f"⚠️ Shortfall of {gap_pct:.2f}% compared to the {year} target.")
            print(f"➡️ Consider adding approximately {required_mwh:.2f} MWh of renewable energy to meet the goal.")
        else:
            print(f"✅ You are {abs(gap_pct):.2f}% ahead of the {year} target.")
            print(f"👏 Continue with current implementation strategy.")

generate_button.on_click(generate_report)

display(widgets.VBox([
    widgets.HTML("<h2>📊 Renewable Progress Tracker</h2>"),
    widgets.HBox([year_input, nonrenewable_input, renewable_input]),
    generate_button,
    output_area
]))
