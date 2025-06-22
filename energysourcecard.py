import ipywidgets as widgets
from IPython.display import display

def create_energy_source_card(source_key, source_data, on_update_callback):
    def get_title(key):
        return {
            "solar_farm": "Solar Panels",
            "wind_farm": "Wind Station",
            "wave_energy": "Wave Station"
        }.get(key, key.replace("_", " ").title())

    def on_field_change(field):
        def handler(change):
            try:
                val = float(change['new']) if field != 'overrideQty' else int(change['new'])
            except ValueError:
                val = 0
            on_update_callback(source_key, field, val)
        return handler

    unit_cost_input = widgets.FloatText(value=source_data["unitCost"], description="Unit Cost ($)", style={"description_width": "initial"})
    production_rate_input = widgets.FloatText(value=source_data["productionRate"], description="Output (MW)", style={"description_width": "initial"})
    daily_opex_input = widgets.FloatText(value=source_data["dailyOpex"], description="Daily OPEX ($)", style={"description_width": "initial"})
    annual_maint_input = widgets.FloatText(value=source_data["annualMaint"], description="Annual Maint. ($)", style={"description_width": "initial"})
    override_qty_input = widgets.IntText(value=source_data["overrideQty"] or 0, description="Quantity", style={"description_width": "initial"})

    unit_cost_input.observe(on_field_change('unitCost'), names='value')
    production_rate_input.observe(on_field_change('productionRate'), names='value')
    daily_opex_input.observe(on_field_change('dailyOpex'), names='value')
    annual_maint_input.observe(on_field_change('annualMaint'), names='value')
    override_qty_input.observe(on_field_change('overrideQty'), names='value')

    card = widgets.VBox([
        widgets.HTML(f"<h4 style='margin: 0;'>{get_title(source_key)}</h4>"),
        widgets.HBox([unit_cost_input, production_rate_input]),
        widgets.HBox([daily_opex_input, annual_maint_input]),
        override_qty_input,
        widgets.HTML("<span style='font-size: 0.8em; color: gray;'>Enter the exact number of units to allocate</span>")
    ])

    card.layout = widgets.Layout(border='1px solid #ccc', padding='12px', margin='10px 0', border_radius='8px')
    return card

def example_update(source_key, field, value):
    print(f"🔧 Updated {source_key} → {field} = {value}")

solar_data = {
    "unitCost": 150000,
    "productionRate": 32,
    "dailyOpex": 1000,
    "annualMaint": 5000,
    "overrideQty": None
}

solar_card = create_energy_source_card("solar_farm", solar_data, example_update)
display(solar_card)
