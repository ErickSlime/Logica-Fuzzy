Aluno: Erick Nicolas Dos Santos

Este projeto implementa um sistema de análise de risco utilizando lógica fuzzy (fuzzy logic). 
O sistema avalia o risco de crédito de um cliente com base em três variáveis de entrada:

Histórico de Crédito
Renda Mensal
Dívida Atual

Utilizando Scikit-fuzzy e Python

Instalado como dependencias: scipy, packaging, networkx, matplotlib

Foram criadas as regras da atividade e exemplos delas sendo usadas no codigo

Definidas os triangulos de forma assimetrica para que consiga lidar mais com as nuances dos valores
e que alguns tenham mais impactos no triangulo, pesquisei e de forma mais realista foi esta a solução

Criação de 17 regras para que o sistema lide com as regras informadas e um pouco mais

Codigo todo comentado explicando cada etapa e função

Processo de desfuzzyficação sendo feito durante o metodo compute() do ControlSystemSimulation,
trazendo o valor de pico do gráfico com processo de desfuzzyficação e transformando tambem em um resultado
entre Baixo, Médio e Alto

Apenas rodar o codigo depois das instalações necessarias e verificar os valores e gráficos criados de 
acordo com o problema

-------------------------------------------------------------------------------------------------------

A classe principal SistemaAnaliseRiscoFuzzy organiza o sistema fuzzy:

Variáveis de Entrada:

historico_credito: Define o histórico de crédito como uma variável fuzzy.
renda_mensal: Define a renda mensal como uma variável fuzzy.
divida_atual: Define a dívida atual como uma variável fuzzy.

Variável de Saída:
risco: Avalia o risco final de crédito com base nas entradas.

Funções de Pertinência: Definidas para cada variável de entrada e saída usando funções triangulares (trimf).

Regras Fuzzy: As regras que determinam a relação entre as variáveis de entrada e o nível de risco.

Simulação: A função avaliar_risco permite a entrada de valores específicos para simulação e cálculo do risco.

Métodos
_definir_funcoes_pertinencia(): Define as funções de pertinência para as variáveis fuzzy.
_definir_regras(): Define as regras fuzzy para avaliar o risco com base nas entradas.
avaliar_risco(historico_credito_val, renda_mensal_val, divida_atual_val): Avalia o risco com base nos valores fornecidos para as 
variáveis de entrada e exibe o gráfico das funções de pertinência da saída.
