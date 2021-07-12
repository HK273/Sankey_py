# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 21:07:50 2021

@author: Hector Kurtyanek
"""

# may need to run pip install plotly from the command line

from plotly.offline import plot  # To render this in Spyder use this
import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=30,
        thickness=50,
        line=dict(color="LightBlue", width=1.0),
        label=["CDU", "ED", "GU", "Medicine", "Midwifery", "Not Recorded", "Section 136", "UCC", "Ward",
                "Emergency 60 Mins.", "Not Recorded", "Urgent Inpatient (24 Hrs.)", "Routine Inpatient (2 Days)",
                "Admission MHA", "Back to GP", "BDAS", "CMHT", "Discharged Home", "Discharged to PRUE/QE", "Drug & Alcohol Services",
                "HTT", "IAPT", "Informal Admission", "Not Recorded", "Other", "Remain in PRUE/QE"
                ],

        color="DarkBlue"
    ),
    link=dict(
        source=[0, 0,  0,  1,   1,  1,  2, 3,  3,  4,  5,  5,  5,  6, 6,  7,  7,  7,  8,  8,  8,  8,  9,
                9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  10, 10, 10, 11, 12, 12, 12, 12, 12, 12, 12,  12,  12],
        target=[9, 10, 11, 9,   10, 11, 9, 10, 11, 11, 9,  10, 11, 9, 11, 9,  10, 11, 9,  10, 11, 12, 13,
                14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 20, 22, 25, 25, 16, 17, 18, 19, 21, 22, 23,  24,  25],
        value=[2, 1,  1,  188, 5,  2,  1, 1,  2,  1,  12, 9,  4,  5, 1,  4,  1,  1,  1,  2,  1,  59, 19,
               37, 1,  24, 9,  1,  5, 1,  18, 10, 4,  4,  17, 1,  4,  1,  1,  13, 1,  6,  29, 1,   6,   14]
    ))])

fig.update_layout(
    title_text="Patient Flow MHLT Week Beginning 5th Feb 2021", font_size=20)
plot(fig, auto_open=True)
