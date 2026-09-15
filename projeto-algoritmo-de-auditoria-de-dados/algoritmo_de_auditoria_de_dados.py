# -*- coding: utf-8 -*-
"""
Sistema de Auditoria de Recursos Corporativos
Autor: Carlos Eduardo

Objetivo:
Percorrer a estrutura de departamentos da empresa (Matriz e Filial SP),
somar os gastos de cada setor e calcular o total geral, apontando
qual unidade e qual departamento mais pesam no orçamento.
"""

empresa = {
    "Matriz": {
        "TI": {
            "Infraestrutura": 120000,
            "Desenvolvimento": 95000,
        },
        "RH": {
            "Recrutamento": 60000,
            "Treinamento": 35000,
        },
        "Marketing": {
            "Digital": 55000,
            "Eventos": 40000,
        },
    },
    "Filial SP": {
        "Vendas": 75000,
        "Logistica": 90000,
    },
}

total_geral = 0
maior_departamento_nome = ""
maior_departamento_valor = 0

print("=" * 55)
print("     RELATÓRIO DE AUDITORIA DE RECURSOS CORPORATIVOS")
print("=" * 55)

# Laço externo: percorre cada unidade (Matriz, Filial SP)
for unidade in empresa:
    print(f"\nUnidade: {unidade}")
    total_unidade = 0

    # Laço interno: percorre os departamentos/subitens de cada unidade
    for departamento in empresa[unidade]:
        conteudo = empresa[unidade][departamento]

        # Se o conteúdo for um número, é um gasto direto (ex: Filial SP)
        if isinstance(conteudo, (int, float)):
            valor = conteudo
            print(f"  {departamento}: R$ {valor:,.2f}")
            total_unidade = total_unidade + valor

            if valor > maior_departamento_valor:
                maior_departamento_valor = valor
                maior_departamento_nome = f"{departamento} ({unidade})"

        # Se for um dicionário, precisa somar os subitens (ex: TI, RH, Marketing)
        else:
            subtotal = 0
            for item in conteudo:
                subtotal = subtotal + conteudo[item]

            print(f"  {departamento}: R$ {subtotal:,.2f}")
            total_unidade = total_unidade + subtotal

            if subtotal > maior_departamento_valor:
                maior_departamento_valor = subtotal
                maior_departamento_nome = f"{departamento} ({unidade})"

    print(f"  Subtotal da unidade: R$ {total_unidade:,.2f}")
    total_geral = total_geral + total_unidade

print("\n" + "=" * 55)
print("                  RESUMO GERAL")
print("=" * 55)
print(f"Total geral da empresa       : R$ {total_geral:,.2f}")
print(f"Departamento com maior gasto : {maior_departamento_nome} "
      f"(R$ {maior_departamento_valor:,.2f})")

# Classificação final do orçamento total
if total_geral > 400000:
    print("Situação geral: orçamento ELEVADO, requer atenção.")
elif total_geral > 200000:
    print("Situação geral: orçamento moderado.")
else:
    print("Situação geral: orçamento dentro do esperado.")
