def glc_para_pda(variaveis, terminais, regras, simbolo_inicial):
    pda = {
        "estados": {"q"},
        "alfabeto_entrada": terminais,
        "alfabeto_pilha": variaveis.union(terminais),
        "transicoes": [],
        "estado_inicial": "q",
        "simbolo_inicial_pilha": simbolo_inicial,
        "estados_finais": {"q"}
    }

    # Para cada regra A → α
    for A, alpha in regras:
        # Se a produção é ε
        if alpha == "ε":
            producao = []
        else:
            # Converte "a S b" para ['b', 'S', 'a']
            producao = list(reversed(alpha.split()))
        pda["transicoes"].append({
            "de": ("q", "", A),
            "para": ("q", producao)
        })

    # Para cada terminal a, adicionar transição de consumo
    for a in terminais:
        pda["transicoes"].append({
            "de": ("q", a, a),
            "para": ("q", [])
        })

    return pda


# Exemplo: GLC para L = { aⁿ bⁿ | n ≥ 0 }
glc = {
    "variaveis": {"S"},
    "terminais": {"a", "b"},
    "regras": [
        ("S", "a S b"),
        ("S", "ε")
    ],
    "simbolo_inicial": "S"
}

# Executar conversão
pda = glc_para_pda(**glc)

# Imprimir transições do PDA
print("PDA Gerado:")
for t in pda["transicoes"]:
    print(t)
