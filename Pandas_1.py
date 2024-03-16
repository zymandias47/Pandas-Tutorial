import pandas as pd

s1 = pd.Series([3, 2, 0, 1])
s2 = pd.Series([0, 3, 7, 2])

data = {'Apple': s1, 'Orange': s2}
#print(data)
# Above, we combined the specified series into a DataFrame.

df = pd.DataFrame(data)
print(df)


# We can also provide a list of lists into a DataFrame and assign column headers as 0, 1
df = pd.DataFrame([["Umut", 80], ["Ali", 50], ["Hüseyin", 40], ["Pelda", 100]])
#print(df)
# Alternatively, we can provide column names and indices from outside.
data = [["Umut", 80], ["Ali", 50], ["Hüseyin", 40], ["Pelda", 100]]
df = pd.DataFrame(data, columns=["Name", "Grade"], index=[1, 2, 3, 4])

# If we don't specify the variable names or don't write the column names, we need to be careful about the parameter order.
df = pd.DataFrame(data, columns=["Name", "Grade"], index=[1, 2, 3, 4])
# df = pd.DataFrame(data, [1, 2, 3, 4], ["Name", "Grade"])
# print(df)

# If we create data in a dictionary structure, we don't need to provide column names explicitly.
data_dict = {"Name": ["Umut", "Ali", "Hüseyin", "Pelda"], "Grade": [80, 50, 40, 100]}
# df = pd.DataFrame(data_dict, index=[1, 2, 3, 4])

# Alternatively, a list of dictionaries will yield the same result as above
dict_list = [
    {"Name": "Umut", "Grade": 80},
    {"Name": "Ali", "Grade": 50},
    {"Name": "Hüseyin", "Grade": 40},
    {"Name": "Pelda", "Grade": 100}
]
df = pd.DataFrame(dict_list)
#print(df)


# df = pd.read_csv("USvideos.csv")

# To read an Excel file with extension xlsx, we need to install the xlrd library
df = pd.read_excel("Pandas_Excel.xlsx")
print(df)
# df = pd.read_json("US_category_id.json")
