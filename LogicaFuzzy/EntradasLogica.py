from LogicaFuzzyBanco import SistemaAnaliseRiscoFuzzy

# Criar uma instância do sistema fuzzy
sistema_risco = SistemaAnaliseRiscoFuzzy()

# Avaliar o risco com entradas de exemplo
risco_calculado = sistema_risco.avaliar_risco(historico_credito_val=9, renda_mensal_val=10, divida_atual_val=1)

print(f"Risco avaliado: {risco_calculado:.2f}")