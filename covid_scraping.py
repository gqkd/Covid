#%%
import pandas as pd
import requests
import matplotlib.pyplot as plt

url = "https://www.epicentro.iss.it/coronavirus/open-data/covid_19-iss.xlsx"

res = requests.get(url)
with open("covid.xlsx",'wb') as output:
    output.write(res.content)
    
casi_prelievo_diagnosi = pd.read_excel("covid.xlsx", sheet_name="casi_prelievo_diagnosi")
casi_inizio_sintomi = pd.read_excel("covid.xlsx", sheet_name="casi_inizio_sintomi")
casi_inizio_sintomi_sint = pd.read_excel("covid.xlsx", sheet_name="casi_inizio_sintomi_sint")
casi_regioni = pd.read_excel("covid.xlsx", sheet_name="casi_regioni")
casi_provincie = pd.read_excel("covid.xlsx", sheet_name="casi_provincie")
ricoveri = pd.read_excel("covid.xlsx", sheet_name="ricoveri")
decessi = pd.read_excel("covid.xlsx", sheet_name="decessi")
sesso_eta = pd.read_excel("covid.xlsx", sheet_name="sesso_eta")
stato_clinico = pd.read_excel("covid.xlsx", sheet_name="stato_clinico")


#%% grafico decessi
#rimpiazzo i <5 
decessi = decessi.replace('<5','5')
#tolgo l'ultima riga
decessi = decessi.iloc[:-1,:]
#converto la colonna in float
decessi["DECESSI"] = decessi["DECESSI"].astype(float)
Y = decessi.iloc[:,1]
X = decessi.iloc[:,2]
fig = plt.figure(figsize=(3.15,3.15), dpi=50)
ax = plt.subplots()
ax.plot(X)
# ax.scatter(Y,X)
# fig.show()





# %%
