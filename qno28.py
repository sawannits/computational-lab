
import pandas as pd
import plotly.express as px

data = {
    "Student": [
        "S1",
        "S2",
        "S3",
        "S4",
        "S5",
        "S6",
        "S7",
        "S8",
        "S9",
        "S10",
    ],
    "Mathematics": [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Student",
    y="Mathematics",
    title="Mathematics Marks Obtained by Students",
    labels={"Student": "Student ID", "Mathematics": "Marks in Mathematics"},
    color="Mathematics",
    color_continuous_scale="Blues",
    text="Mathematics"
)

fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.update_layout(
    xaxis_title="Student",
    yaxis_title="Marks",
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    template="plotly_white"
)
fig.show()
