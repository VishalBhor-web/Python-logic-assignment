import plotly.express as  px
import pandas as pd

df=pd.read_csv("iris.csv")
# print(df)

#Eda steps: step 1.Understand the dataset
print(df.columns)
print(df.describe())

#step 2:Inspect the data quality
print(df.info())

#step 3:Study distribution
fig=px.histogram(
   df,
   x="petal_length" ,
   nbins=30,
   title="Distribution over petal length"
)
fig.show()

#step 4 :Detect the outliers
fig1=px.box(
    df,
    y="petal_length",
    title=" "
)
fig1.show()

#step 5:Analyze relationship between variables
corr=df[["petal_length","petal_width"]].corr(numeric_only=True)
fig2=px.imshow(
    corr,
    text_auto=True,
    title="Correlation between Petal lenngth and Petal width"
)
fig2.show()


# step 6:Generate insights:Based on all 5 steps ,we analyze the figures and generate meaningful insights.
# From the first figure we  understand petal length from range 1.4-1.5 are maximum having count of 26
