from IPython.display import HTML, display

dashboard_header = """
<div style="text-align:center; margin-bottom:20px;">
  <h1 style="
    font-size: 2.5em;
    font-weight: bold;
    background: linear-gradient(to right, #16a34a, #2563eb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  ">
    EcoFusion GND
  </h1>
  <p style="font-size: 1.2em; color: #4b5563; max-width: 600px; margin: 0 auto;">
    Uniting data and dollars for Grenada's clean-energy roadmap
  </p>
</div>
"""

display(HTML(dashboard_header))
