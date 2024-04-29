# %%
import pandas as pd
import altair as alt

# Source: Bajos, N., Ancian, J., Tricou, J., Valendru, A., Pousson, J.-E., & Moreau, C. Child Sexual Abuse in the Roman Catholic Church in France: Prevalence and Comparison With Other Social Spheres. Journal of Interpersonal Violence, 38(7-8), 5452-5470, 2023
# https://journals-sagepub-com.colorado.idm.oclc.org/doi/10.1177/08862605221124263

# %%

# Read Prevalence of CSA by Sphere of Socialization and Sociodemographic Characteristics.
char_first_csa = pd.read_csv('first_abuse.csv')
# Note. Data are presented as %. CSA = child sexual abuse.

# Read Prevalence of CSA by sphere of socialization, sex and sociodemographic characteristics.
prev_by_sphere = pd.read_csv('prevalence.csv')
# Note. Data are presented as % [95% CI]. CI = confidence interval; CSA = child sexual abuse.
# Sample sizes:
# Any: Women (n=14,694) Men (n=13,332)
# Family: Women (n=14,167) Men (n=13,324)
# Catholic Church: Women (n=7234) Men (n=7125)
# Public School: Women (n=12,183) Men (n=11,055)  

# %%
print(prev_by_sphere)

# %%
print(char_first_csa)

# %%
# Make the prevelence interactive chart
dropdown = alt.binding_select(options=prev_by_sphere["characteristics"].unique(), name="Explore Characteristics of Prevalence: ")

selection = alt.selection(type='single', fields=['characteristics'], bind=dropdown, value=[{'characteristics': 'Total prevalence'}])

chart = alt.Chart(prev_by_sphere).mark_bar().encode(
    x=alt.X('sphere', title='Sphere of Socialization'),
    y=alt.Y('mean', title='Prevalence of CSA (%)'),
    xOffset='sex',
    color=alt.Color('sex', scale=alt.Scale(scheme='category20')),
).add_selection(selection).properties(
    title='Prevalence of CSA and Sociodemographic Characteristics',
    width='container'
)

prev_chart = chart.transform_filter(selection)

prev_chart

# %%
# Make the first csa interactive chart
dropdown = alt.binding_select(options=char_first_csa["characteristics"].unique(), name="Explore Characteristics of First CSA: ")

selection = alt.selection(type='single', fields=['characteristics'], bind=dropdown, value=[{'characteristics': '0–9 age of first abuse'}])

chart = alt.Chart(char_first_csa).mark_bar().encode(
    x=alt.X('sphere', title='Sphere of Socialization'),
    y=alt.Y('value', title='First CSA (%)'),
).add_selection(selection).properties(
    title='Characteristics of First CSA',
    width='container'
)

first_csa_chart = chart.transform_filter(selection)

first_csa_chart

# %%
two_charts_template = """
<!DOCTYPE html>
<html>
<head>
  <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/vega@5"></script>
  <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/vega-lite@5.17.0"></script>
  <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
</head>
<body>

<div id="vis1"></div>
<div id="vis2"></div>

<script type="text/javascript">
  vegaEmbed('#vis1', {spec1}).catch(console.error);
  vegaEmbed('#vis2', {spec2}).catch(console.error);
</script>
</body>
</html>
"""

with open('charts.html', 'w') as f:
    f.write(two_charts_template.format(
        vega_version=alt.VEGA_VERSION,
        vegalite_version=alt.VEGALITE_VERSION,
        vegaembed_version=alt.VEGAEMBED_VERSION,
        spec1=prev_chart.to_json(indent=None),
        spec2=first_csa_chart.to_json(indent=None),
    ))
# %%
