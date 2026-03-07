# Projeto Colaborativo - Ciencia de Dados
dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]

def limpar_dados(lista):
    dados_limpos = []
    
    for item in lista:
        if isinstance(item, (int, float)):
            dados_limpos.append(item)
            
    return dados_limpos

resultado = limpar_dados(dados_sujos)
print(resultado)
def calcular_media () :
    pass
def calcular_mediana () :
    pass
def calcular_variancia () :
    pass
def obter_extremos(dados):
    menor = dados[0]
    maior = dados[0]

    for numero in dados:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero

    return menor, maior

dados = limpar_dados(dados_sujos)

menor, maior = obter_extremos(dados)

print(f"Dados processados: {dados}")
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")


dados = limpar_dados ( dados_sujos )
print ( f" Dados processados : { dados }")

print("Verificado por: Guilherme Rocco")

print("Verificado por: Guilherme Rocco")
