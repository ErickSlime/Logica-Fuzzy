from LogicaFuzzyBanco import SistemaAnaliseRiscoFuzzy

# Criar uma instância do sistema fuzzy
sistema_risco = SistemaAnaliseRiscoFuzzy()

# Avaliar o risco com entradas sendo historico Alto e divida atual Baixa
risco_calculado = sistema_risco.avaliar_risco(historico_credito_val=9, renda_mensal_val=0, divida_atual_val=2)
classificacao_risco = sistema_risco.classificar_risco(risco_calculado)

print(f"-----------------------------------------------")
print(f"Situação 1: Historico Alto e divida atual Baixa")
print(f"Risco avaliado: {risco_calculado:.2f}")
print(f"Classificação de risco: {classificacao_risco}")
print(f"-----------------------------------------------")

# Avaliar o risco com entradas sendo historico Baixo e divida atual Alta
risco_calculado = sistema_risco.avaliar_risco(historico_credito_val=2, renda_mensal_val=0, divida_atual_val=8)
classificacao_risco = sistema_risco.classificar_risco(risco_calculado)

print(f"Situação 2: Historico Baixo e divida atual Alta")
print(f"Risco avaliado: {risco_calculado:.2f}")
print(f"Classificação de risco: {classificacao_risco}")
print(f"-----------------------------------------------")

# Avaliar o risco com entradas sendo historico Bom e renda mensal Média divida atual Moderada
risco_calculado = sistema_risco.avaliar_risco(historico_credito_val=7, renda_mensal_val=5, divida_atual_val=5)
classificacao_risco = sistema_risco.classificar_risco(risco_calculado)

print(f"Situação 3: Historico Bom e renda mensal Média divida atual Moderada")
print(f"Risco avaliado: {risco_calculado:.2f}")
print(f"Classificação de risco: {classificacao_risco}")
print(f"-----------------------------------------------")

# Avaliar o risco com entradas sendo historico Regular divida atual Moderada
risco_calculado = sistema_risco.avaliar_risco(historico_credito_val=5, renda_mensal_val=0, divida_atual_val=5)
classificacao_risco = sistema_risco.classificar_risco(risco_calculado)

print(f"Situação 4: Historico Regular divida atual Moderada")
print(f"Risco avaliado: {risco_calculado:.2f}")
print(f"Classificação de risco: {classificacao_risco}")
print(f"-----------------------------------------------")