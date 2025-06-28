import json

pilotos = []
melhores_voltas = []
positions = []
resultados = []

with open("Corrida_RR-1.json", "r") as dado_json:
    dados = json.load(dado_json)

position = int(0)

nome_corrida = dados["EventName"]
for i in dados["Result"]:
    # criação de variavel posição(menor tempo de prova + maior numero de voltas):
        # print(f"piloto: {driver} Melhor volta: {melhor_volta} Posição: {position}")
        # print(position)
        # print(piloto["position"])
    position += 1
    # resto das variaveis(já tem no json)
    piloto = i["DriverName"]
    melhor_volta = i["BestLap"]
    num_volta = i["NumLaps"]
    # print("piloto:", piloto, "Melhor volta:", melhor_volta, "Posição:", position)
    resultado = {"posicao": position, "piloto": piloto, "melhor_volta": melhor_volta, "voltas": num_volta}
    pilotos.append(piloto)
    melhores_voltas.append(melhor_volta)
    positions.append(position)
    resultados.append(resultado)
    dados_uso = {
        "EventName": nome_corrida,
        "Results": resultados,
    }
    with open("Dados_Achatados.json", "w") as f:
        json.dump(dados_uso, f, indent=4)
# print(pilotos)
# print(melhores_voltas)
# print(positions)
# print(resultados)
# dados_relevantes = {
    # "EventName": event_name,
    # "Results": pilotos_filtrados,
# }
print("Processo Finalizado")