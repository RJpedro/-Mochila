from flask import Flask, render_template
from random import randint
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('./index.php')

@app.route("/luis.py")
def solucionaTudo():
	# txtCapacidaden = request.form.get['txtCapacidade']
	# print("CAPACIDADE: ",txtCapacidaden)
	return render_template('./index-resul.php', participantes= participantes[0],candidatos=candidatos,avalia=avalia)

# ROTINA PARA GERAR O AMBIENTE DO PROBLEMA
# GERA O AMBIENTE DO PROBLEMA: UMA MATRIZ DE VALORES ALEATÓRIOS QUE SIMBOLIZAM AS AVALIAÇÕES DE N CANDIDATOS
def gerar_ambiente(n,m,minimo,maximo,minimoPeso,maximoPeso): # N = TOTAL DE NOTAS (COLUNAS), M = TOTAL DE CANDIDATOS (LINHAS), MINIMO/MAXIMO = EXTREMOS DOS VALORES QUE PODEM SER ATRIBUIDOS EM NOTAS, MINIMO/MAXIMOPESO = EXTREMOS QUE PODEM SER ATRIBUIDOS EM PESO
	notaP = np.zeros((m,n), int) # MATRIZ DE NOTAS ALEATÓRIAS SEM PESO
	peso = np.zeros(n, int) # VETOR QUE GERA OS PESOS DE CADA NOTA
	notaComPeso = np.zeros((m,n), int) # MATRIZ DE NOTAS MULTIPLICADAS PELOS PESOS RESPECTIVOS

	# FOR QUE GERA A MATRIZ ALEATÓRIA DE NOTAS SEM PESO
	for i in range(m): 
		for j in range(n):
			notaP[i][j] = randint(minimo, maximo)
	
	# FOR QUE GERA OS PESOS ALEATÓRIOS
	for i in range(n):
		peso[i] = randint(minimoPeso, maximoPeso)

	# FOR QUE GERA A MATRIZ DAS NOTAS MULTIPLICADAS PELOS PESOS
	for i in range(m):
		for j in range(n):
			notaComPeso[i][j] = notaP[i][j]*peso[j]
	
	# RETORNO DA FUNÇÃO SENDO CORRENPONDENTE: [0] = NOTAP (MATRIZ), [1] NOTACOMPESO (MATRIZ), [2] PESO (VETOR)
	return notaP, notaComPeso, peso

# ROTINA PARA GERAR SOLUÇÃO INICIAL
# GERA UMA SOLUÇÃO INICAL DO SISTEMA, NO NOSSO CASO, SELECIONAR CANDIDATOS ALEATÓRIOS
# N = TOTAL DE NOTAS (COLUNAS), M = TOTAL DE CANDIDATOS (LINHAS), C = CAPACIDADE MÁXIMA DE CANDIDATOS QUE SERÃO SELECIONADOS
def solucao_inicial(n,m,c): 
	candidatos = np.zeros(m, int) # VETOR DE QUE CORESPONDE AIS CANDIDATOS SELECIONADOS
	total = 0 # CONTADOR DE COMPARAÇÃO PARA SABER QUANTOS CANDIDATOS FORAM ESCOLHIDOS

	# LAÇO DE REPETIÇÃO QUE SELECIONA CANDIDATOS
	while total<c:
		i = randint(0, n-1)
		if candidatos[i]==0:
			candidatos[i] = 1
			total+=1

	# RETORNO DA FUNÇÃO: VETOR DOS CANDIDATOS ESCOLHIDOS
	return candidatos

# ROTINA PARA CALCULAR A MÉDIA DA SOLUÇÃO INICIAL

# GERA UM VALOR NUMÉRICO QUE REPRESENTA A MÉDIA PONDERADA
# N = TOTAL DE NOTAS (COLUNAS), M = TOTAL DE CANDIDATOS (LINHAS), 
# NOTACOMPESO = SEGUNDA MATRIZ GERADA PELA FUNÇÃO GERAR_AMBIENTE [1], 
# PESOS = PESO DA NOTAS - TERCEIRO RETORNO DA FUNÇÃO GERAR_AMBIENTE [2], 
# CANDIDATOS: VETOR QUE INDICA QUAIS CANDIDATOS FORAM SELECIONADOS - RETORNO DA FUNÇÃO SOLUÇÃO_INICIAL
def avalia(n, m, notaComPeso, pesos, candidatos): 
	notas = np.zeros(m, int) # VETOR QUE ARMAZENA A SOMA DAS NOTAS COM PESOS
	medias = np.zeros(m, int) # VETOR QUE ARMAZENA AS MÉDIAS DAS NOTAS
	somaPesos = 0 # VARIÁVEL QUE ARMAZENA O VALOR DA SOMA DOS PESOS

	#FOR QUE FAZ AS SOMAS DAS NOTAS COM PESOS DOS CANDIDATOS SELECIONADOS
	for i in range(m):
		for j in range(n):
			if candidatos[i]==1:
				notas[i] += notaComPeso[i][j]
			j+=1
		i+=1

	#FOR QUE FAZ A SOMA DOS PESOS
	for i in range(n):
		somaPesos+=pesos[i]

	# FOR QUE FAZ A MÉDIA PONDERADA : MEDIA = (N1*P1) + (N2*P2) + ... + (Nn*Pn)/ SOMA DOS PESOS
	for i in range (n):
		medias[i]+=notas[i]//somaPesos

	return medias

# PROGRAMA PRINCIPAL

# VARIAVEIS DE LIMITAÇÃO DAS COLUNAS E LINHAS
N = 5 # TOTAL DE NOTAS (COLUNAS)
M = 5 # TOTAL DE CANDIDATOS (LINHAS)

#VARIAVEIS DE LIMITAÇÃO DE VALORES DE VETORES E MATRIZES
MINP = 1 # MINIMO DE PESO DE UMA NOTA
MAXP = 5 # MAXIMO DE PESO DE UMA NOTA
MIN = 0 # MINIMO DE VALOR QUE UMA NOTA PODE TER
MAX = 5 # MAXIMO DE VALOR QUE UMA NOTA PODE TER

#VARIAVEL DE LIMITAÇÃO DE FILTRO
CAPACIDADE = 2 # QUANTIDADE DE CANDIDATOS QUE SERÃO SELECIONADOS

# USAR A FUNÇÃO GERAR_AMBIENTE E MOSTRÁ-LA AO USUÁRIO
participantes=gerar_ambiente(N,M,MIN,MAX,MINP,MAXP) # N = TOTAL DE NOTAS, M = TOTAL DE COLUNAS, MIN/MAX = EXTREMOS DE VALOR DE NOTA, MINP/MAXP = EXTREMOS DE VALOR DE PESO
print("Ambiente:\n", participantes[0]) #PRINT FUNÇÃO GERAR_AMBIENTE, PARTICIPANTES[0] = NOTAS SEM PESO (MATRIZ)

# USAR A FUNÇÃO SOLUCAO_INICIAL E MOSTRÁ-LA AO USUÁRIO
candidatos=solucao_inicial(N,M,CAPACIDADE) # N = TOTAL DE NOTAS, M = TOTAL DE COLUNAS, CAPACIDADE = MAXIMO QUE IRÁ SER SELECIONADO
print("\nCandidatos escolhidos:", candidatos) # PRINT FUNÇÃO SOLUCAO_INICIAL, CANDIDATOS = CANDIDATOS SELECIONATOS (VETOR)

# USAR A FUNÇÃO AVALIA E MOSTRÁ-LA AI USUÁRIO
avalia=avalia(N,M,participantes[1],participantes[2],candidatos) # N = TOTAL DE NOTAS, M =TOTAL DE CANDIDATOS, PARTICIPANTES[1] = NOTAS COM PESO, PARTICIPANTES [2] = PESO DAS NOTAS
print("\nMédias das notas dos escolhidos:", avalia) # PRINT FUNÇÃO AVALIA, AVALIA = MÉDIA PONDERADA DAS NOTAS (MATRIZ)

if __name__ == "__main__":
	app.run()