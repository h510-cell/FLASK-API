import pandas as pd

df = pd.read_csv("gravity.csv")
df.head()

df.drop(['Unnamed: 0'],axis =1,inplace=True)

name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()


final_star_list = []

final_dict ={}
for i in range(0,len(name)):
    final_dict["name"]=name[i]
    final_dict["mass"]=mass[i]
    final_dict["radius"]=radius[i]
    final_dict["distance"]=dist[i]
    final_dict["gravity"]= gravity[i]
    final_star_list.append(final_dict)
    final_dict ={}
print(final_star_list)