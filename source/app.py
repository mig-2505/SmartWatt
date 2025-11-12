from alertas import alertas_economia
from graficos import (
    preparar_consumo,
    preparar_clima,
    exibir_consumo_diario,
    exibir_correlacao_temperatura,
    exibir_comparacao_dias,
    calcular_correlacao,
    salvar_correlacao,
    salvar_consumo_diario,
    salvar_comparacao_dias
)

# Preparar os dados
consumo = preparar_consumo()
clima = preparar_clima()

# Calcular DataFrames necessários
df_daily = consumo.groupby(consumo['timestamp'].dt.date)['consumption'].sum()
df_compare = calcular_correlacao(consumo, clima)
df_group = consumo.groupby('tipo_dia')['consumption'].mean()

#Menu
while True:
    print("==== MENU ====")
    print("[1] Ver Gráficos")
    print("[2] Ver Alertas")
    print("[3] Salvar Gráficos")
    print("[0] Sair do Programa")
    op = int(input("Digite uma opcao:... "))

    if op == 1:
        print("[1] Gráfico de Consumo Diario de Energia")
        print("[2] Gráfico de Correlação de Temperatura x Consumo de Energia")
        print("[3] Gráficos de Comparação de Dias Úteis x Final de semana")
        print("[4] Todos Gráficos")
        opcao = int(input("Selecione uma opção:... "))
        if opcao == 1:
            exibir_consumo_diario(consumo)
        elif opcao == 2:
            exibir_correlacao_temperatura(consumo, clima)
        elif opcao == 3:
            exibir_comparacao_dias(consumo)
        elif opcao == 4:
            exibir_consumo_diario(consumo)
            exibir_correlacao_temperatura(consumo, clima)
            exibir_comparacao_dias(consumo)
        else:
            print("Opção inválida!")

    elif op == 2:
        print("\nAlertas e sugestões de economia:")
        df_compare = calcular_correlacao(consumo, clima)
        alerta_texto = alertas_economia(df_compare, consumo)
        print(alerta_texto)

    elif op == 3:
        print("[1] Gráfico de Consumo Diario de Energia")
        print("[2] Gráfico de Correlação de Temperatura x Consumo de Energia")
        print("[3] Gráficos de Comparação de Dias Úteis x Final de semana")
        print("[4] Todos Gráficos")
        opcao = int(input("Qual gráfico deseja salvar?:... "))
        if opcao == 1:
            salvar_consumo_diario(df_daily)
        elif opcao == 2:
            salvar_correlacao(df_compare)
        elif opcao == 3:
            salvar_comparacao_dias(df_group)
        elif opcao == 4:
            salvar_consumo_diario(df_daily)
            salvar_correlacao(df_compare)
            salvar_comparacao_dias(df_group)
        else:
            print("Opção inválida!")

    elif op == 0:
        print("Saindo do Programa")
        break

    else:
        print("Opção inválida!")