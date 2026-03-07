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

    soma = 0 
    for n in range(dados_sujos): 
        soma += n 
        media = soma / len(dados_sujos) 
        
        return media
        
def calcular_mediana () :
    pass
def calcular_variancia () :
    pass
def obter_extremos () :
    pass
dados = limpar_dados ( dados_sujos )
print ( f" Dados processados : { dados }")

print("Verificado por: Thiago Miranda")