import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

from preparar_dados import preparar_consumo, preparar_clima

# Preparar os dados
consumo = preparar_consumo()
clima = preparar_clima()

# Dia atual
dia = date.today().isoformat()

# Consumo diário total
def exibir_consumo_diario(consumo):
    df_daily = consumo.groupby(consumo['timestamp'].dt.date)['consumption'].sum()
    plt.figure(figsize=(10, 5))
    plt.plot(df_daily, linewidth=2)
    plt.title("Consumo Diário de Energia (kWh)")
    plt.xlabel("Data")
    plt.ylabel("Energia Consumida (kWh)")
    plt.grid(True)
    plt.show()
    return df_daily

# Calcular correlação
def calcular_correlacao(consumo, clima):
    df_daily = consumo.groupby(consumo['timestamp'].dt.date)['consumption'].sum()
    df_temp = clima.groupby(clima['timestamp'].dt.date)['air_temperature'].mean()
    df_compare = pd.concat([df_daily, df_temp], axis=1, keys=['consumo_kwh', 'temperatura_media']).dropna()
    return df_compare

# Correlação com temperatura
def exibir_correlacao_temperatura(consumo, clima):
    df_compare = calcular_correlacao(consumo, clima)
    plt.figure(figsize=(8, 5))
    plt.scatter(df_compare['temperatura_media'], df_compare['consumo_kwh'], alpha=0.6)
    plt.title("Correlação: Temperatura x Consumo de Energia")
    plt.xlabel("Temperatura Média (°C)")
    plt.ylabel("Consumo (kWh)")
    plt.grid(True)
    plt.show()
    corr = df_compare.corr().iloc[0,1]
    print(f"Correlação entre temperatura e consumo: {corr:.2f}")
    return df_compare

# Comparação dias úteis vs finais de semana
def exibir_comparacao_dias(consumo):
    df_group = consumo.groupby('tipo_dia')['consumption'].mean()
    df_group.plot(kind='bar', color=['#FFB300', '#2E8B57'], figsize=(6, 4))
    plt.title("Média de Consumo: Dia Útil vs Final de Semana")
    plt.ylabel("Energia Média (kWh)")
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.show()
    return df_group

# Função para salvar gráfico de consumo diário
def salvar_consumo_diario(df_daily, caminho=f'../media/Consumo Diario/grafico_consumo_diario_{dia}.png'):
    plt.figure(figsize=(10,5))
    plt.plot(df_daily, linewidth=2)
    plt.title("Consumo Diário de Energia (kWh)")
    plt.xlabel("Data")
    plt.ylabel("Energia Consumida (kWh)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(caminho)
    plt.close()  # fecha a figura para não exibir

# Função para salvar gráfico de correlação temperatura x consumo
def salvar_correlacao(df_compare, caminho=f'../media/Correlação de Temperatura x Consumo/grafico_correlacao_{dia}.png'):
    plt.figure(figsize=(8,5))
    plt.scatter(df_compare['temperatura_media'], df_compare['consumo_kwh'], alpha=0.6)
    plt.title("Correlação: Temperatura x Consumo de Energia")
    plt.xlabel("Temperatura Média (°C)")
    plt.ylabel("Consumo (kWh)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(caminho)
    plt.close()

# Função para salvar gráfico de dias úteis x finais de semana
def salvar_comparacao_dias(df_group, caminho=f'../media/Comparação de Dias Úteis x Final de semana/grafico_dias_{dia}.png'):
    plt.figure(figsize=(6,4))
    df_group.plot(kind='bar', color=['#FFB300', '#2E8B57'])
    plt.title("Média de Consumo: Dia Útil vs Final de Semana")
    plt.ylabel("Energia Média (kWh)")
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig(caminho)
    plt.close()
