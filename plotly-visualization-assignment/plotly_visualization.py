import plotly.express as px
import pandas as pd

data={
    "epoch":[1,2,3,4,5,6,7,8,9,10],
    "loss":[0.8,0.6,0.5,0.4,0.3,0.2,0.1,0.15,0.12,0.1]
}
df=pd.DataFrame(data)

fig=px.line(
    df,
    x="epoch",
    y="loss",
    title="Training Loss Over Epochs"
)

fig.add_annotation(
    x=7,
    y=0.1,
    text="Loss stabilizes ",
    arrowhead=2,
    arrowsize=1,    
    arrowwidth=2,
    showarrow=True

)
fig.show()
