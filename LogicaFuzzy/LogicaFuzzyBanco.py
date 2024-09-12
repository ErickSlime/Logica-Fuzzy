import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# numpy é usado para criar intervalos de valores e definir o universo de variáveis fuzzy.
# fuzz é usado para acessar funções de pertinência, como trimf, que define funções de pertinência triangular.
# ctrl é usado para acessar classes e funções para criar variáveis de entrada e saída (Antecedent e Consequent),
# definir regras (Rule), e construir e simular o sistema de controle (ControlSystem e ControlSystemSimulation).

class SistemaAnaliseRiscoFuzzy:
    def __init__(self):
        # Variáveis de entrada
        self.historico_credito = ctrl.Antecedent(np.arange(0, 11, 1), 'historico_credito')
        self.renda_mensal = ctrl.Antecedent(np.arange(0, 11, 1), 'renda_mensal')
        self.divida_atual = ctrl.Antecedent(np.arange(0, 11, 1), 'divida_atual')
        # np.arrange cria arrays de valores de 0 a 10, usados para definir o universo das variáveis fuzzy.
        # ctrl.Antecedent Cria uma variável de entrada fuzzy (antecedente) com um intervalo de valores (universe) e um nome.
        
        # Variável de saída
        self.risco = ctrl.Consequent(np.arange(0, 11, 1), 'risco')
        # ctrl.Consequent Cria uma variável de saída fuzzy (consequente) com um intervalo de valores (universe) e um nome.
        
        # Definindo as funções de pertinência
        self._definir_funcoes_pertinencia()
        
        # Definindo as regras
        self._definir_regras()
        
        # Criando o sistema de controle
        # ctrl.ControlSystem Cria um sistema de controle fuzzy a partir de uma lista de regras.
        self.sistema_ctrl = ctrl.ControlSystem(self.regras)
        # ctrl.ControlSystemSimulation Simula o sistema de controle fuzzy criado.
        self.simulador = ctrl.ControlSystemSimulation(self.sistema_ctrl)

    def _definir_funcoes_pertinencia(self):
        # Histórico de crédito
        self.historico_credito['excelente'] = fuzz.trimf(self.historico_credito.universe, [7, 9, 10])
        self.historico_credito['bom'] = fuzz.trimf(self.historico_credito.universe, [5, 7, 9])
        self.historico_credito['regular'] = fuzz.trimf(self.historico_credito.universe, [3, 5, 7])
        self.historico_credito['ruim'] = fuzz.trimf(self.historico_credito.universe, [0, 3, 5])

        # fuzz.trimf Cria uma função de pertinência triangular. Recebe um array de valores x
        #  e três parâmetros a, b, c que definem os pontos da função triangular.
        
        # Renda mensal
        self.renda_mensal['alta'] = fuzz.trimf(self.renda_mensal.universe, [7, 9, 10])
        self.renda_mensal['media'] = fuzz.trimf(self.renda_mensal.universe, [4, 6, 8])
        self.renda_mensal['baixa'] = fuzz.trimf(self.renda_mensal.universe, [0, 3, 5])
        
        # Dívida atual
        self.divida_atual['baixa'] = fuzz.trimf(self.divida_atual.universe, [0, 2, 4])
        self.divida_atual['moderada'] = fuzz.trimf(self.divida_atual.universe, [3, 5, 7])
        self.divida_atual['alta'] = fuzz.trimf(self.divida_atual.universe, [6, 8, 10])
        
        # Risco
        self.risco['baixo'] = fuzz.trimf(self.risco.universe, [0, 2, 4])
        self.risco['medio'] = fuzz.trimf(self.risco.universe, [3, 5, 7])
        self.risco['alto'] = fuzz.trimf(self.risco.universe, [6, 8, 10])

        #self.historico_credito.view()
        #plt.show()

        #self.renda_mensal.view()
        #plt.show()

    def _definir_regras(self):
    # Se o histórico de crédito do cliente é "Excelente" e a dívida atual é "Baixa", então o risco é classificado como "Baixo"
        rule1 = ctrl.Rule(self.historico_credito['excelente'] & self.divida_atual['baixa'], self.risco['baixo'])
    
    # Se o histórico de crédito do cliente é "Ruim" e a dívida atual é "Alta", então o risco é classificado como "Alto"
        rule2 = ctrl.Rule(self.historico_credito['ruim'] & self.divida_atual['alta'], self.risco['alto'])

    # Se o histórico de crédito do cliente é "Bom", a renda mensal é "Média" e a dívida atual é "Moderada", então o risco é classificado como "Médio"    
        rule3 = ctrl.Rule(self.historico_credito['bom'] & self.renda_mensal['media'] & self.divida_atual['moderada'], self.risco['medio'])
    
    # Se o histórico de crédito é excelente e a renda é alta, mesmo com dívida moderada, o risco é baixo
        rule4 = ctrl.Rule(self.historico_credito['excelente'] & self.renda_mensal['alta'] & self.divida_atual['moderada'], self.risco['baixo'])
    
    # Se o histórico de crédito é excelente e a dívida é alta, o risco é moderado
        rule5 = ctrl.Rule(self.historico_credito['excelente'] & self.divida_atual['alta'], self.risco['medio'])
    
    # Se o histórico de crédito é bom e a renda é alta, com dívida baixa, o risco é baixo
        rule6 = ctrl.Rule(self.historico_credito['bom'] & self.renda_mensal['alta'] & self.divida_atual['baixa'], self.risco['baixo'])
    
    # Se o histórico de crédito é bom e a dívida é alta, o risco é alto
        rule7 = ctrl.Rule(self.historico_credito['bom'] & self.divida_atual['alta'], self.risco['alto'])
    
    # Se o histórico de crédito é regular e a dívida é moderada, o risco é moderado
        rule8 = ctrl.Rule(self.historico_credito['regular'] & self.divida_atual['moderada'], self.risco['medio'])
    
    # Se o histórico de crédito é regular e a dívida é alta, o risco é alto
        rule9 = ctrl.Rule(self.historico_credito['regular'] & self.divida_atual['alta'], self.risco['alto'])
    
    # Se o histórico de crédito é ruim e a renda é baixa, com dívida moderada, o risco é alto
        rule10 = ctrl.Rule(self.historico_credito['ruim'] & self.renda_mensal['baixa'] & self.divida_atual['moderada'], self.risco['alto'])
    
    # Se o histórico de crédito é ruim e a dívida é baixa, o risco é moderado
        rule11 = ctrl.Rule(self.historico_credito['ruim'] & self.divida_atual['baixa'], self.risco['medio'])
    
    # Se o histórico de crédito é regular, a renda é alta, e a dívida é baixa, o risco é baixo
        rule12 = ctrl.Rule(self.historico_credito['regular'] & self.renda_mensal['alta'] & self.divida_atual['baixa'], self.risco['baixo'])
    
    # Se o histórico de crédito é bom, a renda é baixa, e a dívida é moderada, o risco é moderado
        rule13 = ctrl.Rule(self.historico_credito['bom'] & self.renda_mensal['baixa'] & self.divida_atual['moderada'], self.risco['medio'])

    # Atribuir as regras
        self.regras = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13]


    def avaliar_risco(self, historico_credito_val, renda_mensal_val, divida_atual_val):
        self.simulador.input['historico_credito'] = historico_credito_val
        self.simulador.input['renda_mensal'] = renda_mensal_val
        self.simulador.input['divida_atual'] = divida_atual_val
        self.simulador.compute()
        return self.simulador.output['risco']