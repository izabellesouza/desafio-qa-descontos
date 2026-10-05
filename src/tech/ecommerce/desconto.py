import math


def calcular_desconto(valor_compra, tipo_cliente):
    if isinstance(valor_compra, bool) or not isinstance(
        valor_compra, (int, float)
    ):
        raise TypeError("O valor da compra deve ser numérico.")

    if not math.isfinite(valor_compra) or valor_compra < 0:
        raise ValueError("O valor deve ser finito e não negativo.")

    if not isinstance(tipo_cliente, str):
        raise TypeError("O tipo de cliente deve ser texto.")

    tipo_cliente = tipo_cliente.upper()

    if tipo_cliente not in ("COMUM", "VIP"):
        raise ValueError("O cliente deve ser COMUM ou VIP.")

    if valor_compra >= 500:
        percentual = 0.20
    elif valor_compra >= 100:
        percentual = 0.10
    else:
        percentual = 0

    if tipo_cliente == "VIP":
        percentual += 0.05

    return round(min(valor_compra * percentual, 200), 2)