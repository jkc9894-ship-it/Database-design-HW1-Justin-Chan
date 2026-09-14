import pandas as pd

#local filename
filepath = "data.csv"
df = pd.read_csv(filepath, na_values = ".")

#Part 1
#printing first 2 rows

print(df.head(2))

#Part 2
#printing first row 

print(df.iloc[0])

#Part 3
#printing rows 10-19

print(df.iloc[10:20])

#Part 4 
#printing column names 

print(df.columns)

#Part 5
#printing first 10 values of Leading Cause. 

print(df["Leading Cause"].head(10))

#Part 6
#printing first 10 rows of 3 columns

print(df[["Leading Cause", "Sex", "Deaths"]].head(10))

#Part 7 
#how many deaths were recorded in 2021
year_2021 = df[df["Year"] == 2021]
print(year_2021["Deaths"].sum())

#how many deaths were recorded for each sex
df["Sex"] = df["Sex"].replace({"F": "Female", "M": "Male"})
print(df.groupby("Sex")["Deaths"].sum())

#how many deaths were recorded for each sex in 2021?
year_2011 = df[df["Year"] == 2011]
print(year_2011.groupby("Sex")["Deaths"].sum())

