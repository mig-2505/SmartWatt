from preparar_dados import preparar_consumo, preparar_clima

# Preparar os dados
consumo = preparar_consumo()
clima = preparar_clima()

# Alertas e estimativa de economia
def alertas_economia(df_compare, consumo):
    mensagens = []

    # Consumo fora do horário útil
    fora_horario = consumo[(consumo['hora'] < 8) | (consumo['hora'] > 18)]
    consumo_fora = fora_horario['consumption'].sum()
    mensagens.append(f"Consumo fora do horário útil: {consumo_fora:.2f} kWh")
    mensagens.append("Solução: desligar sistemas não essenciais fora do expediente.")

    # Dias quentes
    temp_critica = 28
    dias_quentes = df_compare[df_compare['temperatura_media'] > temp_critica]
    if not dias_quentes.empty:
        mensagens.append("Dias com temperatura crítica (>28°C) — sugerir ajuste de climatização:")
        mensagens.append(dias_quentes.to_string())

    # Finais de semana
    df_group = consumo.groupby('tipo_dia')['consumption'].mean()
    if df_group['Final de Semana'] > df_group['Dia Útil']:
        mensagens.append("Alerta: consumo elevado nos finais de semana — sugerir desligamento automático.")

    # Economia potencial
    economia_potencial = consumo_fora * 0.10
    mensagens.append(f"Economia potencial com ajustes automáticos: {economia_potencial:.2f} kWh")

    # Retorna tudo como uma única string
    return "\n".join(mensagens)
