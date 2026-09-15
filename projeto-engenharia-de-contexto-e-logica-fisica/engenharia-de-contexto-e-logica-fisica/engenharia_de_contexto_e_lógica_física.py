# -*- coding: utf-8 -*-
"""
Projeto: Monitoramento de Microclima Urbano
Bairros: Mooca, Tatuape, Guaianases
Autor: Carlos Eduardo Azevedo Alves
"""

estacoes_monitoramento = {
    "Mooca": [
        {"periodo": "Manha", "temperatura": 19, "umidade": 78, "particulas": 40},
        {"periodo": "Tarde", "temperatura": 31, "umidade": 35, "particulas": 70},
    ],
    "Tatuape": [
        {"periodo": "Manha", "temperatura": 19, "umidade": 76, "particulas": 36},
        {"periodo": "Tarde", "temperatura": 30, "umidade": 36, "particulas": 66},
    ],
    "Guaianases": [
        {"periodo": "Manha", "temperatura": 18, "umidade": 82, "particulas": 33},
        {"periodo": "Tarde", "temperatura": 29, "umidade": 38, "particulas": 56},
    ],
}


def classificar_qualidade_ar(particulas):
    """Classifica a qualidade do ar com base na contagem de particulas (indice proprio)."""
    if particulas < 35:
        return "🟢 Otima"
    elif particulas < 55:
        return "🟡 Aceitavel"
    elif particulas < 75:
        return "🟠 Alerta"
    else:
        return "🔴 Critica"


def calcular_indice_bem_estar(temperatura, umidade, particulas):
    """
    Indice de Bem-Estar Urbano (IBU), de 0 a 10.
    - temperatura ideal considerada 20 graus, cada grau de diferenca reduz 0.4 ponto
    - umidade ideal considerada 55%, cada 1% de diferenca reduz 0.1 ponto
    - particulas reduzem 0.06 ponto por unidade
    """
    perda_temperatura = abs(temperatura - 20) * 0.4
    perda_umidade = abs(umidade - 55) * 0.1
    perda_particulas = particulas * 0.06

    indice = 10 - (perda_temperatura + perda_umidade + perda_particulas)

    if indice < 0:
        indice = 0

    return round(indice, 1)


def gerar_relatorio_microclima():
    print("=" * 55)
    print(" RELATORIO DE MICROCLIMA - ZONA LESTE")
    print(" Bairros: Mooca | Tatuape | Guaianases")
    print("=" * 55)

    for bairro, medicoes in estacoes_monitoramento.items():
        print(f"\n📍 BAIRRO: {bairro}")
        print("-" * 45)

        for medicao in medicoes:
            periodo = medicao["periodo"]
            temperatura = medicao["temperatura"]
            umidade = medicao["umidade"]
            particulas = medicao["particulas"]

            qualidade = classificar_qualidade_ar(particulas)
            indice_bem_estar = calcular_indice_bem_estar(temperatura, umidade, particulas)

            print(f"\n  ⏰ {periodo}")
            print(f"    • Temperatura : {temperatura}C")
            print(f"    • Umidade     : {umidade}%")
            print(f"    • Particulas  : {particulas} ({qualidade})")
            print(f"    ⭐ Indice de Bem-Estar: {indice_bem_estar} / 10")

    print("\n" + "=" * 55)
    print(" Fim do relatorio.")
    print("=" * 55)


gerar_relatorio_microclima()


# ==========================================
# Parte 2: Simulador de Rota entre Bairros
# ==========================================

def simular_rota_entrega():
    print("\n\n" + "=" * 55)
    print(" SIMULADOR DE ROTA: MOOCA -> TATUAPE -> GUAIANASES")
    print("=" * 55)

    trajeto = ["Mooca", "Av. Radial Leste", "Tatuape", "Linha do Trem", "Guaianases"]
    condicoes = ["livre", "transito_intenso", "livre", "atraso_trem", "chegada"]

    etapa_atual = 0
    combustivel = 12
    pedagio_pago = False
    finalizado = False

    while combustivel > 0 and not finalizado:
        local = trajeto[etapa_atual]
        condicao = condicoes[etapa_atual]

        print(f"\n📍 Em: {local} | Condicao: {condicao} | Combustivel: {combustivel}")

        if condicao == "chegada":
            print("  ✅ Entrega concluida em Guaianases!")
            finalizado = True

        elif condicao == "livre":
            print("  ➤ Caminho livre, seguindo viagem.")
            etapa_atual += 1
            combustivel -= 2

        elif condicao == "transito_intenso":
            if pedagio_pago:
                print("  ➤ Pedagio ja pago, seguindo pela via expressa.")
                etapa_atual += 1
            else:
                print("  ➤ Transito parado, pagando pedagio para via alternativa.")
                pedagio_pago = True
                etapa_atual += 1
            combustivel -= 3

        elif condicao == "atraso_trem":
            print("  ➤ Cruzamento com a linha do trem atrasado, aguardando.")
            combustivel -= 4
            etapa_atual += 1

    print("\n" + "-" * 45)
    if combustivel <= 0 and not finalizado:
        print("  ❌ Sem combustivel suficiente para concluir a rota.")
    print("-" * 45)


simular_rota_entrega()
