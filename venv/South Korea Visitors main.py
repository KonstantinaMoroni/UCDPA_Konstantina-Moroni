import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
S_Korea=pd.read_csv(r"C:\Users\konstantina\Downloads\South Korea Visitors.csv")
print(S_Korea.head()) #to first 5 rows in the dataframe
print(S_Korea.shape) #to see number of rows and columns
print(S_Korea.info()) #to see data types that columns contain
print(S_Korea.isna().sum()) #to check missing values, none found
S_Korea.drop_duplicates(inplace=True) #to drop rows that are completely identical
print(S_Korea.shape) #no duplicates found/dropped
S_Korea.sort_values(["date","visitor"],ascending=(False,False),inplace=True)
S_Korea.rename(columns={"growth":"Growth %","share":"Share %"},inplace=True)
unique_country_names=S_Korea["nation"].unique()
print(unique_country_names)
print(S_Korea["nation"].nunique()) #how many unique countries do I have
print(type(unique_country_names)) #numpy array
dict_countries={"nation":unique_country_names,"Continent":["ASIA","N.AMERICA","ASIA","ASIA","EUROPE/ASIA (Russia)","ASIA","EUROPE","ASIA","ASIA","ASIA","ASIA","N.AMERICA","EUROPE","ASIA","ASIA","EUROPE","EUROPE","ASIA","ASIA","AFRICA","ASIA","ASIA","OCEANIA","EUROPE","OCEANIA","N/S AMERICA","EUROPE","EUROPE","EUROPE","EUROPE","EUROPE","ASIA","EUROPE","S.AMERICA","EUROPE","S.AMERICA","ASIA","EUROPE","ASIA","ASIA","EUROPE","EUROPE","EUROPE","EUROPE","EUROPE","EUROPE","ASIA","EUROPE","ASIA","EUROPE","EUROPE","AFRICA","ASIA","ASIA","ASIA","OCEANIA","ASIA","ASIA","STATELESS","ASIA"]}
print(dict_countries)
df_countries=pd.DataFrame(dict_countries)
print(df_countries)
df_countries["nation"]=df_countries["nation"].replace(["Austrailia"],"Australia") #spotted typo in Australia ("Austrailia") so I will fix it
print(df_countries.iloc[22])
print(df_countries) #fixed
new_S_Korea=S_Korea.merge(df_countries,on="nation",how="inner")
print(new_S_Korea.shape) #to see new dataframes shape, we see that we have same no of rows and columns so all ok
new_S_Korea=new_S_Korea.round({"Growth %":2,"Share %":2}) #rounding new_s_korea growth and share (cleaning new dataframe)
new_S_Korea.set_index("date",inplace=True) #cleaning dew dataframe,setting index
new_S_Korea.sort_values(["date","visitor"],ascending=(True,False),inplace=True)
print(new_S_Korea)
s=new_S_Korea.groupby("nation")["visitor"].sum()
print(s)
print(s.sort_values(ascending=False))
s_frame=pd.DataFrame([s])
print(s_frame)
s_frame_transposed=s_frame.T #df showing total No of visitors per nation Jan 2019-April 2020
print(s_frame_transposed.sort_values("visitor")) #so now we see the strongest markets from Jan 2019 to May 2020
new_S_Korea.rename(columns = str.lower ,inplace = True)
y=new_S_Korea.groupby("date")["visitor"].sum()
y_frame=pd.DataFrame([y])
y_frame_transposed=y_frame.T #df showing total No of visitors per month
print(y_frame_transposed.sort_values("visitor")) #to see the months with the most visitors
print(new_S_Korea[["age0-20","age21-30","age31-40","age41-50","age51-60","age61"]].apply(np.sum,axis=0))
df_china=new_S_Korea.loc[new_S_Korea.nation=="China"] #to see which age group S Korea tourists are from (21-30)
print(df_china.head())
print(df_china[["age0-20","age21-30","age31-40","age41-50","age51-60","age61"]].apply(np.sum,axis=0))
#we saw what age group most tourists from china come from (21-30)
for index,row in df_china.iterrows(): #to see which month the 21-30 yrs olds from china visit S.Korea
    print(index,row["age21-30"])
#Reusable code
def df_orig(path):
 df1.drop_dulicates(inplace=True) #dropping duplicated
 df1.fillna("Unknown",inplace=True) #replacing Nas with "Unknown"
 df1.rename(columns=str.lower,inplace=True) #changing column names to lower case
 df.set_index(df1.iloc[:,1]) #setting the first column of the dataframe as index