import pandas as pd
import requests
from urllib.parse import quote

UF = "SP"
cidade = "São Paulo"
Local = "Estrada de Itapecerica"


response = requests.get("https://viacep.com.br/ws/{}/{}/{}/json/".format(UF, cidade, Local))
data = response.json()
df = pd.DataFrame(data)
df.to_csv("arqv.csv", index=False)
