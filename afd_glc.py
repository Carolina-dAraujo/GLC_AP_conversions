def afd_para_glc(estados, alfabeto, transicoes, estado_inicial, finais):
    regras = []
    variaveis = set()
    
    for (estado_atual, simbolo), estado_destino in transicoes.items():
        variaveis.add(f"A_{estado_atual}")
        variaveis.add(f"A_{estado_destino}")
        regras.append((f"A_{estado_atual}", f"{simbolo} A_{estado_destino}"))
    
    for final in finais:
        regras.append((f"A_{final}", "ε"))
    
    return {
        "variaveis": sorted(variaveis),
        "terminais": alfabeto,
        "regras": regras,
        "simbolo_inicial": f"A_{estado_inicial}"
    }

# Exemplo:
afd = {
    "estados": {"q0", "q1"},
    "alfabeto": {"a", "b"},
    "transicoes": {
        ("q0", "a"): "q1",
        ("q1", "b"): "q0"
    },
    "estado_inicial": "q0",
    "finais": {"q0"}
}

glc = afd_para_glc(**afd)
print("GLC Gerada:")
print(glc)
