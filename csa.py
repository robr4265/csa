# %%
import pandas as pd
import altair as alt

# Source: Bajos, N., Ancian, J., Tricou, J., Valendru, A., Pousson, J.-E., & Moreau, C. Child Sexual Abuse in the Roman Catholic Church in France: Prevalence and Comparison With Other Social Spheres. Journal of Interpersonal Violence, 38(7-8), 5452-5470, 2023
# https://journals-sagepub-com.colorado.idm.oclc.org/doi/10.1177/08862605221124263

# %%
# Read Prevalence of CSA by Sphere of Socialization and Sociodemographic Characteristics.
prev_by_sphere = pd.read_csv('prev_csa_by_sphere.csv')
# Note. Data are presented as % [95% CI]. CI = confidence interval; CSA = child sexual abuse.

# Read Prevalence of CSA by Sphere of Socialization and Sociodemographic Characteristics.
char_first_csa = pd.read_csv('char_first_csa.csv')
# Note. Data are presented as %. CSA = child sexual abuse.

# Read Prevalence of CSA by sphere of socialization, sex and sociodemographic characteristics.
prev_by_sex_sphere = pd.read_csv('sup_table_1.csv')
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
print(prev_by_sex_sphere)

# %%
# Percentages of girls and boys reporting CSA sexual violence before the age of 18 years by socialization setting.
# CSA = child sexual abuse.

# Create a bar chart with error bars using Altair
chart = alt.Chart(prev_by_sex_sphere).mark_bar().encode(
    x='Sphere of Socialization',
    y='Total pervalence',
    color='Sex',
    column='Sociodemographic Characteristics'
).properties(
    title='Prevalence of CSA by Sphere of Socialization, Sex, and Sociodemographic Characteristics'
)

# Add error bars
# chart = chart.mark_errorbar(extent='ci').encode(
#     y='Prevalence of CSA:Q'
# )

# Display the chart
# chart.show()