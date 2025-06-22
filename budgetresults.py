from IPython.display import display, HTML
import matplotlib.pyplot as plt
import ipywidgets as widgets

# Sample data structure
results = {
    "quantities": {
        "solar": 10,
        "wind": 8,
        "wave": 4
    },
    "allocated_costs": {
        "solar": 1500000,
        "wind": 1200000,
        "wave": 950000
    },
    "daily_opex_total": 50000,
    "annual_maint_total": 200000,
    "daily_energy_mwh": 320,
    "storage_target_mwh": 180,
    "storage_cost": 800000,
    "grid_allocation": 650000,
    "remaining_budget": 300000
}

# Format functions
def format_currency(amount):
    return "${:,.0f}".format(amount)

def format_number(amount, decimals=2):
    return f"{amount:,.{decimals}f}"

def get_source_title(key):
    return key.replace('_', ' ').title()

# Compute totals
total_allocated = sum(results["allocated_costs"].values()) + results["storage_cost"] + results["grid_allocation"]
budget_used_pct = total_allocated / (total_allocated + results["remaining_budget"]) * 100

# 1. Summary Cards
summary_html = f"""
<h3>⚡ Energy Summary</h3>
<div style="display:flex; gap:20px; flex-wrap:wrap;">
    <div style="flex:1; background:#22c55e; color:white; padding:16px; border-radius:10px;">
        <p>Daily Energy</p>
        <h2>{format_number(results['daily_energy_mwh'])} MWh</h2>
    </div>
    <div style="flex:1; background:#3b82f6; color:white; padding:16px; border-radius:10px;">
        <p>Storage Required</p>
        <h2>{results['storage_target_mwh']} MWh</h2>
    </div>
    <div style="flex:1; background:#8b5cf6; color:white; padding:16px; border-radius:10px;">
        <p>Daily OPEX</p>
        <h2>{format_currency(results['daily_opex_total'])}</h2>
    </div>
    <div style="flex:1; background:#f97316; color:white; padding:16px; border-radius:10px;">
        <p>Annual Maintenance</p>
        <h2>{format_currency(results['annual_maint_total'])}</h2>
    </div>
</div>
"""

# 2. Budget Allocation Breakdown
allocation_html = f"""
<h3>💰 Budget Allocation</h3>
<p><b>Budget Utilization:</b> {budget_used_pct:.1f}%</p>
<progress value="{budget_used_pct}" max="100" style="width:100%; height:20px;"></progress>
<p style="font-size:13px;">Used: {format_currency(total_allocated)} | Remaining: {format_currency(results['remaining_budget'])}</p>
"""

# 3. Energy Source Breakdown
source_html = "<h4>🔋 Energy Sources</h4><ul>"
for k, v in results["quantities"].items():
    source_html += f"<li><b>{get_source_title(k)}</b>: {v} units – {format_currency(results['allocated_costs'][k])}</li>"
source_html += "</ul>"

# 4. Storage + Grid Allocation
storage_html = f"""
<h4>💾 Storage Allocation</h4>
<p><b>Renewable Energy Storage:</b> {results['storage_target_mwh']} MWh</p>
<p>Cost: {format_currency(results['storage_cost'])}</p>
<h4>🔌 Installation Cost Allocation</h4>
<p><b>Grid Upgrade:</b> {format_currency(results['grid_allocation'])}</p>
"""

# 5. Display all
display(HTML(summary_html))
display(HTML(allocation_html))
display(HTML(source_html))
display(HTML(storage_html))
