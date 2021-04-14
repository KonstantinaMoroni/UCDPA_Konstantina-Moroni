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
#I will create a new dictionary (dict_countries) with the unique country names (from S_Korea) and continent where they belong and will then convert it to a dataframe
unique_country_names=S_Korea["nation"].unique()
print(unique_country_names)
print(S_Korea["nation"].nunique()) #how many unique countries do I have
print(type(unique_country_names)) #numpy array
dict_countries={"nation":unique_country_names,"Continent":["ASIA","N.AMERICA","ASIA","ASIA","EUROPE/ASIA (Russia)","ASIA","EUROPE","ASIA","ASIA","ASIA","ASIA","N.AMERICA","EUROPE","ASIA","ASIA","EUROPE","EUROPE","ASIA","ASIA","AFRICA","ASIA","ASIA","OCEANIA","EUROPE","OCEANIA","N/S AMERICA","EUROPE","EUROPE","EUROPE","EUROPE","EUROPE","ASIA","EUROPE","S.AMERICA","EUROPE","S.AMERICA","ASIA","EUROPE","ASIA","ASIA","EUROPE","EUROPE","EUROPE","EUROPE","EUROPE","EUROPE","ASIA","EUROPE","ASIA","EUROPE","EUROPE","AFRICA","ASIA","ASIA","ASIA","OCEANIA","ASIA","ASIA","STATELESS","ASIA"]}
print(dict_countries)
df_countries=pd.DataFrame(dict_countries) #new dataframe with country names and continents
print(df_countries)
df_countries["nation"]=df_countries["nation"].replace(["Austrailia"],"Australia") #spotted typo in Australia ("Austrailia") so I will fix it
print(df_countries.iloc[22])
print(df_countries) #fixed
new_S_Korea=S_Korea.merge(df_countries,on="nation",how="inner")
print(new_S_Korea.shape) #to see new dataframe's shape, we see that we have same no of rows and columns so all ok
print(new_S_Korea.isna().sum())
new_S_Korea=new_S_Korea.round({"Growth %":2,"Share %":2}) #rounding new_s_korea growth and share (cleaning new dataframe)
new_S_Korea.set_index("date",inplace=True) #cleaning new dataframe,setting index
new_S_Korea.sort_values(["date","visitor"],ascending=(True,False),inplace=True)
new_S_Korea.rename(columns = str.lower ,inplace = True)
print(new_S_Korea)
#I will find out total No of visitors per nation Jan 2019-April 2020
s=new_S_Korea.groupby("nation")["visitor"].sum()
print(s)
print(s.sort_values(ascending=False))
s_frame=pd.DataFrame([s])
print(s_frame)
s_frame_transposed=s_frame.T
print(s_frame_transposed.sort_values("visitor")) #so now we see the strongest markets from Jan 2019 to May 2020
#I will find out total No of visitors per month
y=new_S_Korea.groupby("date")["visitor"].sum()
y_frame=pd.DataFrame([y])
y_frame_transposed=y_frame.T
print(y_frame_transposed.sort_values("visitor")) #to see the months with the most visitors
print(new_S_Korea[["age0-20","age21-30","age31-40","age41-50","age51-60","age61"]].apply(np.sum,axis=0))
#China is the country with the most visitors, so we will investigate Chinese visitor's characteristics
df_china=new_S_Korea.loc[new_S_Korea.nation=="China"] #new dataframe for China,to see which age group S Korea tourists are from (21-30)
df_china.sort_values("date")
print(df_china) #even though I am sorting by date, three dates 2019-10,2019-11,2019-12 are not getting place in the right order
print(df_china[["age0-20","age21-30","age31-40","age41-50","age51-60","age61"]].apply(np.sum,axis=0))
#we saw what age group most tourists from china come from (i.e. 21-30)
for index,row in df_china.iterrows(): #to see which month the 21-30 yrs olds from china visit S.Korea
    print(index,row["age21-30"])
#Reusable code
def df_orig(path):
 df1.drop_dulicates(inplace=True) #dropping duplicates
 df1.fillna("Unknown",inplace=True) #replacing Nas with "Unknown"
 df1.rename(columns=str.lower,inplace=True) #changing column names to lower case
 df.set_index(df1.iloc[:,1]) #setting the first column of the dataframe as index
#Visualisation
#1
fig,ax=plt.subplots(figsize=(8,8))
sns.lineplot(data=new_S_Korea,x="date",y="visitor") #to see how S Koreas visitors developed over the years
plt.title("S_Korea:No of visitors")
plt.xticks(rotation=90)
plt.show()
#2
fig,ax=plt.subplots(figsize=(10,10))
sns.barplot(data=new_S_Korea,y="continent",x="visitor") #to see which continent most visitors come from
plt.title("S_Korea:Origin of visitors")
plt.show()
#3
fig,ax=plt.subplots(figsize=(10,10))
sns.lineplot(data=df_china,x="date",y="visitor") #to see how china's visitors developed over the years
plt.xticks(rotation=90)
plt.title("China:Visitors")
plt.show()
#4 to see how the different age groups of S.Korea's visitors developed over the years
new_S_Korea_ages=new_S_Korea[["age0-20","age21-30","age31-40","age41-50","age51-60","age61"]].sort_values("date")
print(new_S_Korea_ages.head())
fig,ax=plt.subplots(figsize=(10,10))
sns.lineplot(data=new_S_Korea_ages,x="date",y="age0-20",label="age0-20yrs")
sns.lineplot(data=new_S_Korea_ages,x="date",y="age21-30",label="age21-30yrs")
sns.lineplot(data=new_S_Korea_ages,x="date",y="age31-40",label="age31-40yrs")
sns.lineplot(data=new_S_Korea_ages,x="date",y="age41-50",label="age41-50yrs")
sns.lineplot(data=new_S_Korea_ages,x="date",y="age51-60",label="age51-60yrs")
sns.lineplot(data=new_S_Korea_ages,x="date",y="age61",label="age61yrs")
plt.title("S_Korea visitors:age trends")
plt.ylabel("age_group")
plt.xticks(rotation=90)
plt.show()
#5 to see how S.Korean tourism growth has developed over the years
fig,ax=plt.subplots(figsize=(10,10))
sns.lineplot(data=new_S_Korea,x="date",y="growth %")
plt.title("S_Korea visitors (tourism) :Growth")
plt.xticks(rotation=90)
plt.show()
#6 visualise the top 4 countries for S.Korea's tourism/data taken from s_frame_transposed that was created earlier and was showing No of visitors per nation. From this, I keep only the No of visitors for the top 4 countries and I create a dataframe which I will use to create the barplot
top_countries=s_frame_transposed.loc[["China","Japan","Taiwan","USA"]]
print(top_countries)
sns.barplot(data=top_countries,x=top_countries.index,y="visitor")
plt.title("S_Korea visitors: Top 4 Countries")
plt.show()
#7 S.Korea's biggest "client" ie China - visualise relationship between the number of visitors coming from China yo S.Korea and China's share in the S.Korean tourism market
sns.scatterplot(data=df_china,x="visitor",y="share %")
plt.title("S_Korea case: China's visitor/share% relationship")
plt.show()
#Interactive visualisation from a dataframe(i.e df_china showing info for visitors from china
from bokeh.plotting import ColumnDataSource, figure
from bokeh.io import output_file,show
from bokeh.models import HoverTool
from bokeh.models import CategoricalColorMapper
from bokeh.models import Range1d
from bokeh.models import NumeralTickFormatter
source=ColumnDataSource(df_china)
plot=figure(x_axis_label="No of visitors", y_axis_label="Share %",tools="hover",title="S_Korea visitors from China:Visitors/Share %")
plot.circle(x="visitor",y="share %",source=source,size=10,fill_color="grey",alpha=0.1,line_color=None,hover_fill_color="red",hover_alpha=0.5,hover_line_color="white")
hover=HoverTool(tooltips=[("Date","@date")])
plot.xaxis[0].formatter = NumeralTickFormatter(format='000,000')
plot.add_tools(hover)
output_file("S_Korea_interactive.html")
show(plot)