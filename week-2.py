print("Hello, World!")

previous_balance = 1379
transaction = 200
current_balance = previous_balance - transaction

print(f'Your previous balance was £{previous_balance} \n'
      f'You have withdrawn £{transaction} \n'
      f'So your new balance is £{current_balance}'
  )
# %%

fruit = ["apple", "banana", "cherry", "durian", "elderberry"]

list(range(0, 5))

fruit[1]  ##output: 'banana'because python indexes from 0

fruit[-2] ##output: 'durian' because negative indexing starts from the end of the list
fruit[:2] ##output: ['apple', 'banana'] because it returns the first two elements of the list
fruit[3:5] ##output: ['durian', 'elderberry'] because it returns elements from index 3 to 4
fruit[1:4] ##output: ['banana', 'cherry', 'durian'] because it returns elements from index 1 to 3


# %%

print("This is new cell")

fruit.append("fig") ##here we used the append to add a new fruit to the list

print(fruit) 

#%%

take = fruit.pop()
print(fruit) 
print(take)

#%%
import pandas as pd

#%%

df = pd.DataFrame(
    data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fred'],
    'Age': [20, 21, 19, 22, 20, 32],
    'Grade': ['A', 'B', 'A', 'A', 'C', 'B'],
    'Score': [88, 75, 90, 95, 65, 70],
    'Enrolled': pd.to_datetime(
        ['2025-09-01', '2025-09-01', '2025-09-15', '2025-09-01', '2025-09-20', '2025-09-20']
    )
}
)

# %%

df.head()  

#%%

df.head(2)
# %%

df.tail(2)

# %%

df["Age"]

#%%
df["Age", "Grade"]
# %%
df[["Age", "Grade"]]
# %%
df.Age
# %%
df.loc[1] 
# %%
df.loc[1:3]
# %%
df.loc[1:3, "Age"]
# %%
df.loc[1:3, ["Age", "Grade"]]
# %%
df.tail(3)

# %%
df.loc[3:5, ["Student", "Enrolled"]]
# %%
df[["Student", "Enrolled"]].tail(3)
# %%
df[[True, False, True, False, False, True]]# %%

# %%
df.Age == 20
# %%
df[df.Age == 20]
# %%
df[df.Age < 30]
# %%
(df.age == 20) & (df.Grade == "A")
# %%
df[(df.Age == 20) & (df.Grade == "A")]
# %%
df.loc[df["Age"] > 21, "Student"]
# %%
df[df.Age > 21].loc[:, ["Student"]]
# %%
df.Score >= 70
df.Score <= 85
(df.Score >= 70) & (df.Score <= 85)
# %%
df[(df.Score >= 70) & (df.Score <= 85)]
# %%
df.loc[
    (df.Score >= 70) & (df.Score <= 85),
    ["Grade"] 
]
# %%
df.Enrolled > "2025-09-15"
# %%
df.sort_values(by = 'Grade')


# %%
df.sort_values(by = 'Enrolled')
# %%
df.sort_values(by = 'Score')

# %%
df.sort_values(by = ['Grade', 'Age'] , ascending = [True, False])
# %%

new_data = pd.DataFrame(
    data = {
    'Student': ['Gautham'],
    'Age': [23],
    'Grade': ['A'],
    'Score': pd.NA, # NA means "Not Available". This value is missing.
    'Enrolled': pd.to_datetime(['2025-09-30'])
}
)


# %%

pd.concat([df, new_data],) 
# %%
pd.concat([df, new_data], ignore_index = True)
# %%
df = pd.concat([df, new_data], ignore_index = True)
# %%
df

# %%
df.count()
# %%

df['FavouriteFood'] = [
  'Chips',
  'Curry',
  'Chicken',
  'Cabbage',
  'Cheese',
  'Carrot',
  'Cauliflower']

print(df)
# %%
df['ScoreAsProportion'] = df.Score/100

print(df)
# %%
df.assign(AgeInMonths = df.Age*12)
# %%
df.assign(AgeInMonths = df.Age*12).sort_values(by = 'AgeInMonths')
# %%
(df
  .assign(AgeInMonths = df.Age*12)
  .sort_values(by = 'AgeInMonths')
)
# %%
flights = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/nycflights13/flights.csv")

# %%
flights.dtypes
# %%
