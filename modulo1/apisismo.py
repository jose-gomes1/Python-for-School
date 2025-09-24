import requests
from datetime import datetime

urlPrincipal_template = "https://api.ipma.pt/open-data/observation/seismic/{area}.json"

try:
    choose = input("Gostaria de acessar os Açores (1) ou a Madeira e Continente (2)? ")
    if choose == "1":
        choose = 3
    elif choose == "2":
        choose = 7
    else:
        print("Opção inválida! Digite apenas 1 ou 2.")
        exit()
    
    urlPrincipal = urlPrincipal_template.format(area=choose)
    resposta = requests.get(urlPrincipal)
    resposta.raise_for_status()
    dados_sismos = resposta.json()

    eventos = dados_sismos.get("data", [])

    if eventos:
        for evento in eventos[:10]:
            # Pega a data original
            data_iso = evento.get("time", None)
            if data_iso:
                try:
                    data_formatada = datetime.fromisoformat(data_iso).strftime("%d/%m/%Y %H:%M:%S")
                except ValueError:
                    data_formatada = data_iso  # se falhar, mostra como veio
            else:
                data_formatada = "N/A"

            print(
                f"Sismo de magnitude {evento.get("magnitud", "N/A")} "
                f"na data {data_formatada} "
                f"com latitude de {evento.get("lat", "N/A")}, longitude {evento.get("lon", "N/A")} "
                f"e profundidade de {evento.get("depth", "N/A")} km "
                f"em {evento.get("obsRegion", "N/A")}"
            )
    else:
        print("Nenhum sismo encontrado.")

except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a API: {e}")
