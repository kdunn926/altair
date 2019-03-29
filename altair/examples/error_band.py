"""
Error Band Mark
======================================
This example shows how to overlay error bands and mean values using the vega error band mark.
"""
# category: other charts
import altair as alt
from vega_datasets import data

source = data.barley.url

mean_values = alt.Chart(source).mark_point(color='black', filled=True).encode(
    alt.X('month(date):T'),
    alt.Y('mean(temp):Q')
)

error_bands = alt.Chart(source).mark_errorband(extent='stdev').encode(
    alt.X('month(date):T', axis=alt.Axis(title='Month')),
    alt.Y('temp:Q', axis=alt.Axis(title='Temperature [F]'))
)

mean_values + error_bands
