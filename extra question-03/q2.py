#1.convert series from string to numeric with error handling.
import pandas as pd
s=pd.Series([ '10', '20', 'abc', '30'])
#convert to numeric,invalid parsing will be set as NaN
numeric_s=pd.to_numeric(s, errors='coerce')
print(numeric_s)
pd.to_numeric()
 


#2.convert mixed type series to date time and meet
import pandas as pd
s=pd.Series(['2023-01-01','not a date','2024-05-10'])
dt_s=pd.to_datetime(s,errors='coerce')
valid_dates=dt_s.dropna() 
print(valid_dates)



#3.convert numeric strings with commas to floats.
import pandas as pd
s=pd.Series(['1.000', '2.500', '3.750'])
#remove commas and convert to float
float_s=s.str.replace(',', '').astype(float)#after removing commas, converts string to float type.
print(float_s)

#NOTE:: .str.replace()-> used for string cleaning.remove special charecters before conversion.

#4.convert series to categorical and display categories and codes.
import pandas as pd
s=pd.Series(['apple', 'banana', 'apple', 'orange'])
#convert to categorical.
cat_s=s.astype('category')
#display category codes.
print(cat_s.cat.codes)


#How are category codes assigned in pandas?
#when you convert a series to categorical, pandas assigns integer codes to each unique category based on the order of their appearance in the data.
# The first unique category gets code 0, the second gets code 1, and so on. In the example above, 'apple' is assigned code 0, 'banana' is assigned code 1, and 'orange' is assigned code 2.


#5---convert series to categorical and display categories and codes.
import pandas as pd
s=pd.Series(['apple', 'banana', 'apple', 'orange'])
p=pd.Series(['lion','cat','dog','tiger','monkey','dog','cat'])
#convert to categorical
cat_s=s.astype('category')
print(cat_s)
animal=p.astype('category')
print(animal)
#dispalay category codes
print(cat_s.cat.codes)
print(animal.cat.codes)



#6.create a dataframe and print it.
import pandas as pd
df=pd.DataFrame({'x':[78,85,96,80,86],'y':[84,94,89,83,86],'z':[86,97,96,72,83]});
print(df)


#7.write a pandas program to create a dataframe from a dictionary .
#where values are list of unequal lengths by filling missing values with None.
import pandas as pd
data={
    'A':[1,2,3],
    'B':[4,5],
    'C':[7,8,9,]
}
df=pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))
df=df.where(pd.notnull(df), None)
print(df)


# dictionary cant accept unequal length lists as values because it violates the fundamental principle of a dictionary, which is to have a unique key for each value.
# When you try to create a dictionary with unequal length lists, it will raise a ValueError because the dictionary cannot determine how to align the keys with the values.
# Each key must correspond to exactly one value, and if the lists have different lengths, it creates ambiguity in how to assign values to keys.


#8.write a pandas program to create a dataframe from a list of dictionaries.
#and then transpose it,ensuring that data types remain consistent.
import pandas as pd
data=[
    {'Name':'Alice','Age':30,'City':'New York'},
    {'Name':'Bob','Age':25,'City':'Los Angeles'},
    {'Name':'Charlie','Age':35,'City':'Chicago'}
]
df=pd.DataFrame(data)
print("Original DataFrame:")
print(df)
transposed_df=df.transpose()
print("\nTransposed DataFrame:")



#9.write a pandas program to split the following dataframes into group based on school code.Also check the type of the groupby object.
import pandas as pd
pd.set_option('display.max_columns', None)
#pd.set-option('display.max_rows', None)
student_data=pd.DataFrame({
    'school_code':['s001','s002','s001','s003','s002','s004'],
    'class':['V','V','VI','VI','V','VI'],
    'name':['Alisa','Bobby','Cathrine','Alberto','Beverly','Brandon'],
    'date_of_birth':['2009-04-01','2008-05-12','2007-06-23','2006-07-14','2005-08-25','2006-09-05'],
    'age':[12,13,14,15,16,15],
    'height':[150,160,158,165,155,162],
    'adderess':['street 1','street 2','street 3','street 1','street 2','street 4'],
    'index':['s1','s2','s3','s4','s5','s6']
})
print("Original DataFrame:")
print(student_data)
print('\nsplit the said data on school_code:')
result=student_data.groupby('school_code')
print(result)
for name, group in result:
    print(f"\nGroup:")
    print(name)
    print(group)
print("\ntype of the object:")
print(type(result))


#10.write a pandas program to split a dataset to group by two columns and count by each row.
import pandas as pd
#simple sales dataset
data = {
    'customer_id': [101, 102, 101, 103, 102, 101],
    'salesman_id': [1, 2, 1, 3, 2, 2],
    'amount': [500, 300, 200, 400, 150, 250]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Group by customer_id and salesman_id and count rows
result = df.groupby(['customer_id', 'salesman_id']).size().reset_index(name='count')
#Group → Count rows → Convert to table(INTO A PROPERDATAFRAME)
print("\nGrouped Count:")
print(result)




# 11.write a pandas program tojoin the two given dataframes along rows and assign all data.
import pandas as pd

student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})

student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})

print("Original DataFrames:")
print(student_data1)
print("-------------------------------------")
print(student_data2)
print("\nJoin the said two dataframes along rows:")
result_data = pd.concat([student_data1, student_data2])
print(result_data)



# 12.Write a Pandas program to merge two DataFrames on a single column id.
import pandas as pd
# Create two sample DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Selena', 'Annabel', 'Caeso']
})
df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Age': [25, 30, 22]
})
# Merge the two DataFrames on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='right')
# Output the result
print(merged_df)



# 13.Write a Pandas program to select the rows where the score is missing,i.e. is NaN
import pandas as pd
import numpy as np
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("Rows where score is missing:")
print(df[df['score'].isnull()])


#Pandas prefers np.nan because it is designed for numerical operations
#  and works efficiently with arrays and calculations.


# 14.Write a Pandas program to draw a basic line plot with Pandas and Matplotlib.
import pandas as pd
import matplotlib.pyplot as plt
# Create a sample DataFrame
df = pd.DataFrame({
    'Year': [2017, 2018, 2019, 2020, 2021],
    'Sales': [200, 250, 300, 350, 400]
})
# Plot the 'Year' against 'Sales' using a line plot
plt.plot(df['Year'], df['Sales'])
# Add labels and a title
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Yearly Sales Trend')
# Display the plot
plt.show()


#Created a sample DataFrame with 'Year' and 'Sales' columns.
#Used plt.plot() to plot 'Year' vs 'Sales'.
##Added axis labels and a title to the plot using plt.xlabel(), plt.ylabel(), and plt.title().
#Displayed the plot using plt.show().


# 15.Write a Pandas program to plot multiple line plots 
# in one figure with Pandas.
import pandas as pd
import matplotlib.pyplot as plt
# Create a sample DataFrame
df = pd.DataFrame({
    'Year': [2017, 2018, 2019, 2020, 2021],
    'Product_A': [200, 250, 300, 350, 400],
    'Product_B': [150, 200, 250, 300, 350]
})
# Plot multiple lines for Product A and Product B
plt.plot(df['Year'], df['Product_A'], label='Product A', marker='o')#CIRCLE
plt.plot(df['Year'], df['Product_B'], label='Product B', marker='s')#SQUARE 
# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales of Product A and B Over Time')
# Add a legend
plt.legend()
# Display the plot
plt.show()
#plt.legend() is used to display a key (legend) on the graph that explains
#  what each line, color, or marker represents.


