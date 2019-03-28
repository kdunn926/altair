"""
Error Bars showing Confidence Interval
======================================
This example shows how to show error bars using confidence intervals. The confidence intervals are computed internally in vega by a non-parametric `bootstrap of the mean <https://github.com/vega/vega-statistics/blob/master/src/bootstrapCI.js>`_.
"""
# category: other charts
import altair as alt
from vega_datasets import data

source = data.barley.url

mean_values = alt.Chart(source).mark_point(color='black', filled=True).encode(
    alt.X('mean(yield):Q'),
    alt.Y('variety:O')
)

error_bars = alt.Chart(source).mark_errorbar(extent='stdev').encode(
    alt.X(
        'yield:Q',
        scale=alt.Scale(zero=False)
    ),
    alt.Y('variety:O')
)

mean_value + error_bars
