import os
import pandas as pd
import json

df = pd.read_csv("C:\\Files\\INDICADORES DE LEITURAS - COPASA\\DATABASE\\COD_MUNICIPIOS_MG.csv", delimiter=";")

df["COD_MUNICIPIO"] = df["COD_MUNICIPIO"].astype(str)

for filename in os.listdir("C:\\Files\\INDICADORES DE LEITURAS - COPASA\\DATABASE\\MG"):
    if filename.endswith(".json"):
        code = filename[:7]
        if code in df["COD_MUNICIPIO"].values:
            municipio = df[df["COD_MUNICIPIO"] == code]["MUNICIPIO"].values[0]
            os.rename(
                f"C:\\Files\\INDICADORES DE LEITURAS - COPASA\\DATABASE\\MG\\{filename}",
                f"C:\\Files\\INDICADORES DE LEITURAS - COPASA\\DATABASE\\MG\\{municipio}.json"
            )
            print(f"{municipio}")
print("Concluído")
