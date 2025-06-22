import ipywidgets as widgets
from IPython.display import display, clear_output
import pprint

# Initial energy source data
energy_sources = {
    "solar_farm": {
        "unitCost": 5000,
        "productionRate": 0.5,
        "dailyOpex": 20,
        "annualMaint": 980,
        "overrideQty": 0
    },
    "wind_farm": {
        "unitCost": 30000,
        "productionRate": 2.5,
        "dailyOpex": 50,
        "annualMaint": 3500,
        "overrideQty": 0
    },
    "wave_energy": {
        "unitCost": 10000000,
        "productionRate": 2,
        "dailyOpex": 1000,
        "annualMaint": 12000,
        "overrideQty": 0
    }
}

# Global variables
calculation_result = None
error_output = widgets.Output()

# Budget Controls
budget_input = widgets.IntText(value=1_000_000, description="Budget ($)")
storage_pct_input = widgets.IntSlider(value=10, min=0, max=100, description="Storage %")
grid_pct_input = widgets.IntSlider(value=5, min=0, max=100, description="Grid %")
storage_unit_cost_input = widgets.IntText(value=100, description="Storage Unit Cost ($/MWh)")

def create_energy_card(source_key, source_data, update_callback):
    def on_change(field):
        def handler(change):
            source_data[field] = change["new"]
            update_callback()
        return handler

    unit_cost = widgets.FloatText(value=source_data["unitCost"], description="Unit Cost")
    output = widgets.FloatText(value=source_data["productionRate"], description="Output (MW)")
    opex = widgets.FloatText(value=source_data["dailyOpex"], description="Daily OPEX")
    maint = widgets.FloatText(value=source_data["annualMaint"], description="Annual Maint.")
    qty = widgets.IntText(value=source_data["overrideQty"], description="Quantity")

    unit_cost.observe(on_change("unitCost"), names="value")
    output.observe(on_change("productionRate"), names="value")
    opex.observe(on_change("dailyOpex"), names="value")
    maint.observe(on_change("annualMaint"), names="value")
    qty.observe(on_change("overrideQty"), names="value")

    return widgets.VBox([
        widgets.HTML(f"<h4>{source_key.replace('_', ' ').title()}</h4>"),
        unit_cost, output, opex, maint, qty
    ])

def allocate_budget_with_storage(
    budget, unitCosts, productionRates, dailyOpex, annualMaint,
    storageUnitCost, priorities, overrideQty, storagePct, gridPct
):
    result = {
        "quantities": {},
        "allocated_costs": {},
        "daily_opex_total": 0,
        "annual_maint_total": 0,
        "daily_energy_mwh": 0,
        "storage_target_mwh": 0,
        "storage_cost": 0,
        "grid_allocation": 0,
        "remaining_budget": 0
    }

    result["grid_allocation"] = budget * (gridPct / 100)
    result["storage_target_mwh"] = (budget * (storagePct / 100)) / storageUnitCost
    result["storage_cost"] = result["storage_target_mwh"] * storageUnitCost

    available_budget = budget - result["grid_allocation"] - result["storage_cost"]

    total_costs = sum(unitCosts.values())
    for key in unitCosts:
        alloc_budget = available_budget * (unitCosts[key] / total_costs)
        qty = overrideQty.get(key) or int(alloc_budget / unitCosts[key])
        result["quantities"][key] = qty
        result["allocated_costs"][key] = qty * unitCosts[key]
        result["daily_opex_total"] += qty * dailyOpex[key]
        result["annual_maint_total"] += qty * annualMaint[key]
        result["daily_energy_mwh"] += qty * productionRates[key]

    used = sum(result["allocated_costs"].values()) + result["grid_allocation"] + result["storage_cost"]
    result["remaining_budget"] = budget - used
    return result

def calculate():
    try:
        error_output.clear_output()
        unitCosts = {k: v["unitCost"] for k, v in energy_sources.items()}
        productionRates = {k: v["productionRate"] for k, v in energy_sources.items()}
        dailyOpex = {k: v["dailyOpex"] for k, v in energy_sources.items()}
        annualMaint = {k: v["annualMaint"] for k, v in energy_sources.items()}
        overrideQty = {k: v["overrideQty"] for k, v in energy_sources.items()}
        priorities = {k: 1 for k in energy_sources}

        result = allocate_budget_with_storage(
            budget_input.value,
            unitCosts,
            productionRates,
            dailyOpex,
            annualMaint,
            storage_unit_cost_input.value,
            priorities,
            overrideQty,
            storage_pct_input.value,
            grid_pct_input.value
        )

        clear_output(wait=True)
        display(main_ui)
        with error_output:
            print("✅ Allocation Result:")
            pprint.pprint(result)

    except Exception as e:
        error_output.clear_output()
        with error_output:
            print("❌ Error:", str(e))

def update_ui():
    pass  # fields are reactive; no state needs syncing here

# UI Elements
energy_cards = [create_energy_card(k, v, update_ui) for k, v in energy_sources.items()]
calculate_button = widgets.Button(description="Calculate Allocation", button_style="success")
calculate_button.on_click(lambda _: calculate())

main_ui = widgets.VBox([
    widgets.HTML("<h2>📊 EcoFusion Estimator</h2>"),
    budget_input,
    widgets.HBox([storage_pct_input, grid_pct_input, storage_unit_cost_input]),
    widgets.HTML("<h3>⚙️ Configure Energy Sources</h3>"),
    widgets.HBox(energy_cards),
    calculate_button,
    error_output
])

display(main_ui)
