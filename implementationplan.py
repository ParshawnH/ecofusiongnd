from IPython.display import display, HTML

implementation_plan_html = """
<div style="border:1px solid #ddd; padding:24px; border-radius:6px; background:#fff; box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
  <h2 style="font-size: 1.5em; font-weight: bold; margin-bottom: 20px;">Implementation Plan</h2>

  <section style="margin-bottom: 32px;">
    <h3 style="font-size: 1.25em; font-weight: 600; margin-bottom: 12px;">Short-Term (1–2 Years)</h3>
    <ul style="padding-left: 20px;">
      <li><strong>Workforce Upskilling:</strong> Partner with UWI St. George's to offer certificate courses in structural and electrical engineering for renewable-tech installation & maintenance.</li>
      <li><strong>Infrastructure Grants:</strong> Secure funding to deploy initial charging stations and mini-grids.</li>
      <li><strong>Streamline Permitting:</strong> Fast-track environmental and building permits for small-scale solar, wind, and wave projects.</li>
      <li><strong>Rooftop Solar Rebates:</strong> Offer point-of-sale rebates for residential and commercial PV panel installations.</li>
    </ul>
  </section>

  <section style="margin-bottom: 32px;">
    <h3 style="font-size: 1.25em; font-weight: 600; margin-bottom: 12px;">Mid-Term (3–5 Years)</h3>
    <ul style="padding-left: 20px;">
      <li><strong>Technical Vocational Scholarships:</strong> Fund scholarships for youth at vocational schools in electrical trades and renewable-system design.</li>
      <li><strong>Microgrid Pilots:</strong> Install community microgrids in Carriacou and Petite Martinique with local O&M training.</li>
      <li><strong>Public-Private Partnerships:</strong> Joint ventures with private developers for utility-scale wind and wave farms, sharing investment risk.</li>
      <li><strong>SCADA Deployment:</strong> Roll out Supervisory Control & Data Acquisition on major plants for real-time performance monitoring.</li>
      <li><strong>Green Finance Window:</strong> Partner with local banks to offer low-interest loans backed by a government guarantee fund for clean-energy projects.</li>
    </ul>
  </section>

  <section>
    <h3 style="font-size: 1.25em; font-weight: 600; margin-bottom: 12px;">Long-Term (6–10 Years)</h3>
    <ul style="padding-left: 20px;">
      <li><strong>Local Manufacturing Hub:</strong> Attract an assembly plant for solar modules & EV chargers to reduce import costs and create jobs.</li>
      <li><strong>Sovereign Green Bonds:</strong> Issue long-term bonds to finance large-scale storage projects and grid modernization.</li>
    </ul>
  </section>
</div>
"""

display(HTML(implementation_plan_html))
