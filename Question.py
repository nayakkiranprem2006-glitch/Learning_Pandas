'''--

✅ Day 1: Pandas Basics – 10 Questions

1. Importing Pandas  
➤ Q1: Import the pandas library and print its version.

---

2. Creating Series  
➤ Q2: Create a pandas Series from a list: [10, 20, 30, 40].  
➤ Q3: Create a Series with custom index: data = [100, 200, 300], index = ['a', 'b', 'c'].

---

3. Creating DataFrames  
➤ Q4: Create a DataFrame from this dictionary:  
{'Name': ['Alice', 'Bob'], 'Age': [25, 30]}  
➤ Q5: Create a DataFrame from a list of lists:  
[[1, 2], [3, 4]] with columns ['A', 'B']

---

4. Viewing Data  
➤ Q6: Use head() and tail() to view the first and last 3 rows of this DataFrame:  
python
df = pd.DataFrame({'A': range(1, 11), 'B': range(11, 21)})


---

5. Basic Info & Stats  
➤ Q7: Use info() and describe() on the same DataFrame above.  
➤ Q8: What does df.shape, df.columns, and df.index return?

---

6. Data Selection  
➤ Q9: Select column 'A' from the DataFrame above.  
➤ Q10: Select the value in 2nd row and column 'B'.
'''

'''Let's start practicing question on DAY 1 OF LEARNING PANDAS'''

# ➤ Q1: Import the pandas library and print its version.

'''import pandas as pd
print(pd.__version__)'''

# ➤ Q2: Create a pandas Series from a list: [10, 20, 30, 40, 50].  

'''import pandas as pd
list = [10, 20, 30, 40, 50]
print(type(list))
series = pd.Series(list)
print(series)
print(type(series))'''

# ➤ Q3: Create a Series with custom index: data = [100, 200, 300], index = ['a', 'b', 'c'].
'''import pandas as pd 
data = [100, 200, 300]
indexes = ['a', 'b', 'c']

series = pd.Series(data, index=indexes)
print(series)'''


# ➤ Q4: Create a DataFrame from this dictionary:  
{'Name': ['Alice', 'Bob'], 'Age': [25, 30]}

'''import pandas as pd
dict1 = {
    "Name" : ["Alice", "Bob"],
    "Age" : [25, 30]
} 

df = pd.DataFrame(dict1)
print(df)'''

# ➤ Q5: Create a DataFrame from a list of lists:  
# # [[1, 2], [3, 4]] with columns ['A', 'B']

'''import pandas as pd 
list1 = [[1,2], [3,4]]
indexes = ['A', 'B']
df = pd.DataFrame(list1, columns= indexes)
print(df)'''

# ➤ Q6: Use head() and tail() to view the first and last 3 rows of this DataFrame:  
# python
# df = pd.DataFrame({'A': range(1, 11), 'B': range(11, 21)})
'''import pandas as pd
df = pd.DataFrame({"A" : range(1,11), "B" : range(11,21)})
print(df)

print(df.head(3))
print(df.tail(3))'''

# ➤ Q7: Use info() and describe() on the same DataFrame above.

'''import pandas as pd

df = pd.DataFrame({"A" : range(1,11), "B" : range(11,21)})
df.info()
print(df.describe())'''

# ➤ Q8: What does df.shape, df.columns, and df.index return?

'''import pandas as pd

df = pd.DataFrame({"Name": ["Krishna", "Ankush", "Komal", "Kashish"], "Gender" : ["Male", "Male", "Female", "Female"] })
print(df)
print(df.shape)
print(df.columns)
print(df.index)'''

# ➤ Q9: Select column 'A' from the DataFrame above.  

'''import pandas as pd
df = pd.DataFrame({"Name": ["Krishna", "Ankush", "Komal", "Kashish"], "Gender" : ["Male", "Male", "Female", "Female"] })
print(df.Name)'''

# ➤ Q10: Select the value in 2nd row and column 'B'.

'''import pandas as pd
df = pd.DataFrame({"Name": ["Krishna", "Ankush", "Komal", "Kashish"], "Gender" : ["Male", "Male", "Female", "Female"] })
print(df.iloc[1,1]) #Here df.iloc() will u=locates your code as per index and df.loc() here you need to write column name'''






