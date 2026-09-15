# New York City Leading Causes of Death HW1


## Why I Chose This Dataset
I chose this dataset because although it is quite morbid, I find it interesting to see which combination of leading cause and other factors
lead to the most deaths in NYC. 
What made the dataset unique to work with aswell is that each row is not tied to one death. Instead, each row is a summary of one combination of 
year, cause, sex, and race group, with a death count attached.
The structure of the dataset also covers all the required criteria such as having more than 100 
rows, 5 columns, and multiple categorical columns. 

---

## Three Data Questions

# Question 1: How many deaths were recorded in 2021

#year_2021 = df[df["Year"] == 2021]
#print(year_2021["Deaths"].sum())
#output: 63560

Why the data structure supports this question:

This works because every row records the year it belongs to in its own column,
alongside a corresponding death count for that specific group. The set keeps only the 
rows where the Year equals 2021, isolates that year, and adds up the deaths column across
those rows. It is also important to sum the deaths column rather than count the rows, because 
each row is a summary of a group rather than a singular death.


# Question 2: How many deaths were recorded for each sex
#df["Sex"] = df["Sex"].replace({"F": "Female", "M": "Male"})
#print(df.groupby("Sex")["Deaths"].sum())
#output: Female    422602.0.  Male      420457.0

Why the data structure supports this question:

This works because Sex is a categorical column that assigns every row to a group,
and the deaths column stores the size of that group. The dataset also originally labeled 
the same category two different ways (F and Female / M and Male), so I standardized those 
labels first, otherwise the totals would have been split across duplicate groups.

# Question 3: How many deaths were recorded for each sex in 2021?
#year_2011 = df[df["Year"] == 2011]
#print(year_2011.groupby("Sex")["Deaths"].sum())
#output: Female    27075.0.      Male      25651.0

Why the data structure supports this question:

This works because Year and Sex are stored on the same row as the death count, so
the data can be narrowed by one column and then summarized by another. I filtered
the 2021 first, then grouped the remaining rows by sex, which combines both conditions.



# What the Data Cannot Answer

The data wouldn't be able to help me answer the question "how old were people when they died of X cause". The dataset 
does not have an "age" column, and the "age adjusted death rate" is something completely different. This is also because
the data is grouped, as in each row does not convey individual deaths, but rather a group of people who died from the 
same leading cause. Even if there was an average age of death for the leading cause, I don't think that data really 
answers the original question well. 







