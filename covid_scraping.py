#%%
import pandas as pd
import requests
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
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
#tolgo l'ultima riga (ultime due)
decessi = decessi.iloc[:-2,:]
#converto la colonna in float
decessi["DECESSI"] = decessi["DECESSI"].astype(float)
data = decessi.iloc[:,1]
dec = decessi.iloc[:,2]
fig = plt.figure( dpi=300)
fig, ax = plt.subplots(1)
fig.autofmt_xdate()


#titoli
fig.suptitle(None)
ax.set_title("Decessi")
ax.set_ylabel("Numero decessi")
ax.set_xlabel("Data")

#creo un intervallo equamente spaziato per la data
#in questo modo non include il punto finale
# space = np.arange(0,len(decessi),round(len(decessi)/6))
ix_ticks = np.linspace(0, len(decessi), num=9, endpoint=True, dtype="int")
plt.xticks(ticks=list(data.index.intersection(ix_ticks)))
#ticker per data
# ax.xaxis_date
# ticker.MaxNLocator(n=4)
#plot
ax.plot(data,dec,color='r')
#salvataggio
plt.savefig("decessi.pdf", dpi=600)
# ax.scatter(Y,X)
# fig.show()





# %%
