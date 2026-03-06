import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Neha", "Vishal", "Rohan", "Sneha", "Karan", "Pooja", "Arjun"],
    "Score": [85, 72, 40, 90, 82, 65, 55, 30, 78, 92],
    "Passed": [True, True, False, True, True, True, True, False, True, True],
    "Category": ["A", "B", "C", "A", "A", "B", "C", "C", "B", "A"]
}

df = pd.DataFrame(data)

head = df.head()        
print(head)

tail = df.tail()
print(tail)

info = df.info()
print(info)

describe = df.describe()
print(describe)

# Select a single column and store it in a variable.
names=df["Name"]
print(names)

# Select multiple columns and store them in a new DataFrame.
names_score=df[["Name","Score"]]
print(names_score)

# Filter rows based on a numerical condition.
score_above_80=df[df["Score"]>80]
print(score_above_80)

