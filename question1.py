import pandas as  pd

data={
    "Name":["Ajay","Bhuvan","Vishal","Manas","Rohit","Suresh","Karan","Rahul"],
    "Score":[83,72,29,95,67,88,75,92],
    "Passed":[True,True,False,True,True,True,True,True],
    "Category":["A","B","F","A+","C","A","B","A+"]
}

df=pd.DataFrame(data)


# Selects a single column and prints it
print(df["Name"])

#Selects multiple column and stores them in a Dataframe
multiple_df=df[["Name","Passed"]]
print(multiple_df)

#Use iloc to retrieve the first three items
print(df.iloc[0:3])

# Use loc after setting meaningful labels for index
df.index=["Student1","Student2","Student3","Student4","Student5","Student6","Student7","Student8"]
print(df.loc["Student1":"Student8"])

# Filter rows where score>85
print(df[df["Score"]>85])

# Filter rows where score>85 and passed is True
print(df[(df["Score"]>85) & (df["Passed"]==True)])

# Sort filtered result in descending order of score 
res=df.sort_values("Score",ascending=False)
print(res)