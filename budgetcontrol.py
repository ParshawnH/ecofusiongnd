import ipywidgets as widgets
from IPython.display import display

def create_main_budget_controls(
    budget_val=1_000_000,
    grid_pct_val=5,
    storage_pct_val=10,
    storage_unit_cost_val=100,
    on_change_callback=None
):
    budget = widgets.FloatText(value=budget_val, description="Total Budget ($)", style={'description_width': 'initial'})
    grid_percent = widgets.FloatSlider(value=grid_pct_val, min=0, max=100, step=0.1, description="Grid Allocation (%)", style={'description_width': 'initial'})
    storage_percent = widgets.FloatSlider(value=storage_pct_val, min=0, max=100, step=0.1, description="Storage (% Energy)", style={'description_width': 'initial'})
    storage_unit_cost = widgets.FloatText(value=storage_unit_cost_val, description="Storage Cost ($/kWh)", style={'description_width': 'initial'})

    def notify_change(change):
        if on_change_callback:
            on_change_callback({
                "budget": budget.value,
                "gridPercent": grid_percent.value,
                "storagePercent": storage_percent.value,
                "storageUnitCost": storage_unit_cost.value
            })

    for widget in [budget, grid_percent, storage_percent, storage_unit_cost]:
        widget.observe(notify_change, names='value')

    card = widgets.VBox([
        widgets.HTML("<h3>🧮 Budget Configuration</h3>"),
        widgets.HBox([budget]),
        widgets.HBox([grid_percent, storage_percent]),
        widgets.HBox([storage_unit_cost])
    ])

    return {
        "widget": card,
        "budget": budget,
        "gridPercent": grid_percent,
        "storagePercent": storage_percent,
        "storageUnitCost": storage_unit_cost
    }

# Example usage
controls = create_main_budget_controls()
display(controls["widget"])
