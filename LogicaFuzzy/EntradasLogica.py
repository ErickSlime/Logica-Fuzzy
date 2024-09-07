from LogicaFuzzyBanco import SistemaAnaliseRiscoFuzzy

# Criar uma instância do sistema fuzzy
sistema_risco = SistemaAnaliseRiscoFuzzy()

# Avaliar o risco com entradas de exemplo
risco_calculado = sistema_risco.avaliar_risco(historico_credito_val=6, renda_mensal_val=7, divida_atual_val=5)

print(f"Risco avaliado: {risco_calculado:.2f}")