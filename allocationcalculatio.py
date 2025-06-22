import ipywidgets as widgets
from IPython.display import display, clear_output
import pprint

# Define sample energy sources
energy_sources = {
    "solar": {
        "unitCost": 150000,
        "productionRate": 32,
        "dailyOpex": 1000,
        "annualMaint": 5000,
        "overrideQty": None
    },
    "wind": {
        "unitCost": 180000,
        "productionRate": 28,
        "dailyOpex": 900,
        "annualMaint": 4800,
        "overrideQty": None
    },
    "wave": {
        "unitCost": 220000,
        "productionRate": 24,
        "dailyOpex": 800,
        "annualMaint": 4600,
        "overrideQty": None
    }
}

# Allocation calculation function
def calculate_allocation(budget: float, energy_sources: dict,
                         storage_target_mwh: float, grid_allocation_pct: float = 0.1):
    results = {
        "quantities": {},
        "allocated_costs": {},
        "daily_opex_total": 0,
        "annual_maint_total": 0,
        "daily_energy_mwh": 0,
        "storage_target_mwh": storage_target_mwh,
        "storage_cost": 0,
        "grid_allocation": 0,
        "remaining_budget": 0
    }

    results["grid_allocation"] = budget * grid_allocation_pct
    results["storage_cost"] = storage_target_mwh * 5000  # $5000/MWh assumed

    budget_remaining = budget - results["grid_allocation"] - results["storage_cost"]

    total_unit_costs = sum(es["unitCost"] for es in energy_sources.values())
    for source_name, source_data in energy_sources.items():
        share = source_data["unitCost"] / total_unit_costs
        allocated = budget_remaining * share
        quantity = int(allocated / source_data["unitCost"])

        results["quantities"][source_name] = quantity
        results["allocated_costs"][source_name] = quantity * source_data["unitCost"]
        results["daily_opex_total"] += quantity * source_data["dailyOpex"]
        results["annual_maint_total"] += quantity * source_data["annualMaint"]
        results["daily_energy_mwh"] += quantity * source_data["productionRate"]

    total_allocated = sum(results["allocated_costs"].values())
    results["remaining_budget"] = budget - (
        results["grid_allocation"] + results["storage_cost"] + total_allocated
    )

    return results

# Define the callback function
def on_calculate_clicked(_):
    clear_output(wait=True)
    print("📊 Calculate button clicked!")

    # Run the real allocation logic
    total_budget = 5000000  # Example: $5 million budget
    storage_target = 180  # Example: 180 MWh target
    results = calculate_allocation(total_budget, energy_sources, storage_target)

    # Display results
    display(button)
    print("\n🔍 Allocation Results:")
    pprint.pprint(results)

# Create the styled button
button = widgets.Button(
    description="Calculate Allocation",
    tooltip="Click to calculate budget allocation",
    icon="line-chart",
    layout=widgets.Layout(width="auto", padding="12px"),
    style=dict(button_color="linear-gradient(to right, #16a34a, #2563eb)", text_color='white')
)

# Attach the click handler
button.on_click(on_calculate_clicked)

# Display the button
display(button)
