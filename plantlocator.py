import folium
from folium.plugins import MarkerCluster
from IPython.display import display, clear_output
import ipywidgets as widgets

# AI Recommended Site Data
recommended_sites = [
    {"id": "r1", "score": 0.92, "lat": 12.1165, "lng": -61.6790, "type": "Solar", "capacity": 20.5, "isOffshore": False},
    {"id": "r2", "score": 0.87, "lat": 12.0851, "lng": -61.7152, "type": "Wind", "capacity": 15.2, "isOffshore": False},
    {"id": "r3", "score": 0.84, "lat": 12.1554, "lng": -61.6694, "type": "Solar", "capacity": 18.7, "isOffshore": False},
    {"id": "r5", "score": 0.91, "lat": 12.2098, "lng": -61.6543, "type": "Wind", "capacity": 22.1, "isOffshore": False},
    {"id": "r6", "score": 0.81, "lat": 12.0123, "lng": -61.7345, "type": "Solar", "capacity": 17.8, "isOffshore": False},
    {"id": "r8", "score": 0.89, "lat": 12.0678, "lng": -61.7891, "type": "Wind", "capacity": 19.6, "isOffshore": False},
    {"id": "r9", "score": 0.82, "lat": 12.1876, "lng": -61.6932, "type": "Solar", "capacity": 16.9, "isOffshore": False},
    {"id": "r11", "score": 0.86, "lat": 12.1243, "lng": -61.6312, "type": "Solar", "capacity": 21.3, "isOffshore": False},
    {"id": "r13", "score": 0.88, "lat": 12.0435, "lng": -61.7712, "type": "Wave", "capacity": 12.8, "isOffshore": True},
    {"id": "r14", "score": 0.83, "lat": 12.1789, "lng": -61.8023, "type": "Wave", "capacity": 10.5, "isOffshore": True},
    {"id": "r15", "score": 0.90, "lat": 12.1325, "lng": -61.6523, "type": "Wind", "capacity": 17.3, "isOffshore": False},
    {"id": "r16", "score": 0.85, "lat": 12.1987, "lng": -61.6832, "type": "Solar", "capacity": 19.2, "isOffshore": False},
    {"id": "r17", "score": 0.93, "lat": 12.0765, "lng": -61.8287, "type": "Wave", "capacity": 11.9, "isOffshore": True}
]


plant_types = ['All'] + sorted({site['type'] for site in recommended_sites})
filter_dropdown = widgets.Dropdown(options=plant_types, description='Filter:')


def render_map(filter_type='All'):
    m = folium.Map(location=[12.1165, -61.7190], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(m)

    filtered_sites = [s for s in recommended_sites if filter_type == 'All' or s['type'] == filter_type]

    for site in filtered_sites:
        popup = (
            f"<b>{site['type']} Plant {'(Offshore)' if site['isOffshore'] else ''}</b><br>"
            f"Score: {site['score'] * 100:.1f}%<br>"
            f"Capacity: {site['capacity']} MW<br>"
            f"Location: {site['lat']:.4f}, {site['lng']:.4f}"
        )
        color = {
            "Solar": "orange",
            "Wind": "blue",
            "Wave": "cadetblue"
        }.get(site["type"], "gray")

        folium.Marker(
            location=[site['lat'], site['lng']],
            popup=popup,
            icon=folium.Icon(color=color, icon="info-sign")
        ).add_to(marker_cluster)

    return m

# Callback when dropdown is changed
def update_map(change):
    clear_output(wait=True)
    display(filter_dropdown)
    display(render_map(change.new))

filter_dropdown.observe(update_map, names='value')

# Initial display
display(filter_dropdown)
display(render_map())
