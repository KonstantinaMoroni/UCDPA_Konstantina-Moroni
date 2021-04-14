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
print(type(unique_country_names))
print(S_Korea["nation"].nunique())
dict_countries={"nation":['Vietnam','USA','China', 'Indonesia', 'Russia', 'Phillipines', 'Germany',
 'Myanmar', 'Overseas Korean', 'Mongolia', 'Cambodia', 'Canada', 'Netherland',
 'Japan', 'Thailand', 'UK', 'France', 'India', 'Sri Lanka', 'Africa others',
 'Taiwan', 'Malaysia', 'Austrailia', 'Ukraine', 'New Zealand', 'America others',
 'Poland', 'Romania', 'Greece', 'Europe others', 'Austria', 'Pakistan',
 'Belgium', 'Mexico', 'Italy', 'Brazil', 'Singapore', 'Bulgaria', 'Asia others',
 'Hong Kong', 'Norway', 'Sweden', 'Finland', 'Swiss', 'Spain', 'Denmark',
 'Turkey', 'Portugal', '*GCC', 'Croatia', 'Ireland', 'South Africa', 'Israel',
 'Kazakhstan', 'Iran', 'Oceania others', 'Bangladesh', 'Uzbekistan',
 'Stateless', 'Macao'],"Continent":["ASIA","N.AMERICA","ASIA","ASIA","EUROPE","ASIA","EUROPE","ASIA","ASIA","ASIA","AFRICA","N.AMERICA","EUROPE","ASIA","ASIA","EUROPE","EUROPE","ASIA","ASIA","AFRICA","ASIA","OCEANIA","EUROPE","OCEANIA","N/S AMERICA","EUROPE","EUROPE","EUROPE","EUROPE","EUROPE","EUROPE","ASIA","EUROPE","S.AMERICA","EUROPE","S.AMERICA","ASIA","EUROPE","ASIA","ASIA","EUROPE","EUROPE","EUROPE","EUROPE","EUROPE","EUROPE","ASIA","EUROPE","ASIA","EUROPE","EUROPE","AFRICA","ASIA","ASIA","ASIA","OCEANIA","ASIA","ASIA","STATELESS","ASIA"]}
df_countries=pd.DataFrame(dict_countries)
