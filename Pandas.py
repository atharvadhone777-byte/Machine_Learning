#csv = comma seperated values
import pandas as pd
print(pd.__version__)   #2.3.3 current version of pandas

#✅SERIES - Pandas 1-D labeled array that can hold any datatype
data=[100,101,102] #Pyhton list #64 bit integers
s=pd.Series(data)  #Makes an indexed series 0 1 2
s=pd.Series(data,index=["a","b","c"],name="My_series")   #Jitne elements utne index khudse dene padenge for diff indexing
#name prints as Name:My_series, dtype:object

print(s.loc["a"])   #Prints value at index a #'loc' means located at
s.loc["c"]=200      #Edits value at that index
print(s.iloc[0])    #indexing chahe dusri ho but integer indexing ke hisab se ye batayga 
print(s[s>100])     #gives rows of values greater than 100

score={"D1":21,"D2":23,"D3":32} #Python Dictionary
s1=pd.Series(score)             #Keys hi indexing ka kaam krenge if dictionary pass ki toh

#✅Dataframes - A tabular data structure with rows and columns
data1={"col1":["d11","d12","d13"],
    "col2":["d21","d22","d23"]
}
df=pd.DataFrame(data1)  #A table forms #Khud se har baar indexing dene ki jarurat nhi 0 1 2 .. already hoti hai
print(df.iloc[0])  #Gives row of index '0'

#Add a new column
df["col3"]=["d31","d32","d33"]
#Add a new row
new_row=pd.DataFrame([{"col1":"d41","col2":"d42","col3":"d43"}])
df=pd.concat([df,new_row])  #New row in concatinated
#[ ] dena imp as jo object pd.concat mein pass karoge wo iterable hona chahiye like list or tuple

#✅Importing
d1=pd.read_csv("data.csv",index_col="col1")   #index_col ne col1 ko as index set kr diya hai instead of default indexes
d2=pd.read_json("data.json")  #Gets value of json file
d3=pd.read_excel("data.xlsx") #excel
d4=pd.read_csv("data.txt",sep=" ")  #Text file jisme data space se seperated hai use , ki tarah treat karega

#✅Selection
print(d2["col1","col2"].to_string())   #to_string =  #Selection by column
print(d2.iloc[0,["col1","col2"]])        #In row indexed 0 we want only col1 and col2 #Selection by row
print(d2.iloc[0:4])           #Gives rows indexed from 0 to 3 excluding 4
print(d2.iloc[0:4:2])         #Gives every second row after selected row
print(d2.iloc[0:4,0:3])       #Gives rows from 0 to 3 and columns from 0 to 2 besides index column

#✅Filtering - Keeping the rows that match a condition
v1=df[(df["col1"]>=101) | (df["col2"]=="d11")]  #Gives rows which have specific value of column satisfying given condition
#| or logical operator is used to apply two conditions () | () dont use 'or' as in python

#✅Aggregate - Reduces a set of values into a single summary value. Used to summarize and analyze data. Often used with the groupby() function
df.max(numeric_only=True)   #It only works on numeric data so numeric_only selects only numeric data wale all columns
df.min(numeric_only=True)
df.mean(numeric_only=True)
df.sum(numeric_only=True)
df.count(numeric_only=True) #counts number of non-NaN(non-null) values in each columns
df["col1"].max(numeric_only=True)   #Only one column is selected
df["col2"].value_counts()   #Column mein har ek word and uski frequency in that column dega
df["col2"].value_counts(ascending=True) #It given in increasing order than default decreasing order

#✅Grouping
g=df.groupby("col2")    #Things are grouped by col2 
print(g["col1"].count()) #col2 becomes index and each col2's group's frequency will be printed of col1 
#Ex: Jab col2 ki value A hai to A kitni baar us column mein occur hua ye dega

#✅Data cleaning - process of removing/fixing incomplete, incorrect or irrelevant data. ~75% work in pandas is data cleaning
# 1. Drop irrelevant columns 
df=df.drop(columns=["col2","col3"])   #Drops the col2 & col3 from dataframe df
df=df.dropna(subset=["col3"])         #Drops rows which have any NaN value

# 2. Handle missing data
df=df.fillna({"col2":"None"})         #Replaces NaN in that column with "None" word
df['col1'] = df['col1'].fillna(df['col1'].median()) # Fill missing data with median not by mean as decimal values aa sakti hai

# 3 Fix inconsistent values
df["col1"]=df["col1"].replace({"d11":"c11","d12":"c12"})    #All occurences of col1's d11 & d12 will be replaced by c11 & c12

# 4 standardize text
df["col3"]=df["col3"].str.upper()   #Converts to upper case
df["col3"]=df["col3"].str.lower()   #Converts to lower case

# 5 Fix data types
df["col2"]=df["col2"].astype(float) #Typecasts the dataype of col2 as float

# 6 Removes Duplicate values
df=df.drop_duplicates() #Drops duplicate rows

# 7 Number of null values
df.isnull().sum()

# 8 Number of duplicate rows
df.duplicated().sum()

#✅Extra Methods
d1.head()   #Shows first 5 rows
d1.tail()   #Shows last 5 rows
d1.head(3)  #Shows first 3 rows
d1.tail(3)  #Shows last 3 rows
d1.sample(5)    #Gives any 5 random rows as sample
d1.shape    #Gives no. of rows and columns in dataframe
d1.info()   #Gives detailed summary of dataframe
d1.describe()   # Summary Statistics of the Numerical Columns
d1.describe(include="all") # Statistical Summary of whole dataset including non-numerical columns
d1["col1"] = d1["col1"].astype('object')    # Converting the DataType
d1.nunique() # Number of unique values in each column
