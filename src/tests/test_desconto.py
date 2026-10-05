import pytest

from tech.ecommerce.desconto import calcular_desconto


@pytest.mark.parametrize(
    "valor_compra, tipo_cliente, esperado",
    [
        (0, "COMUM", 0),
        (0, "VIP", 0),
        (50, "COMUM", 0),
        (50, "VIP", 2.50),
        (99.99, "COMUM", 0),
        (99.99, "VIP", 5),
        (100, "COMUM", 10),
        (100, "VIP", 15),
        (100.01, "COMUM", 10),
        (100.01, "VIP", 15),
        (300, "COMUM", 30),
        (300, "VIP", 45),
        (499.99, "COMUM", 50),
        (499.99, "VIP", 75),
        (500, "COMUM", 100),
        (500, "VIP", 125),
        (500.01, "COMUM", 100),
        (500.01, "VIP", 125),
        (300, "vip", 45),
        (300, "Vip", 45),
        (300, "vIp", 45),
        (300, "comum", 30),
        (799.96, "VIP", 199.99),
        (800, "VIP", 200),
        (800.04, "VIP", 200),
        (999.95, "COMUM", 199.99),
        (1000, "COMUM", 200),
        (1000.05, "COMUM", 200),
        (2000, "COMUM", 200),
        (2000, "VIP", 200),
        (123.45, "COMUM", 12.35),
    ],
)
def test_calcular_desconto(valor_compra, tipo_cliente, esperado):
    resultado = calcular_desconto(valor_compra, tipo_cliente)

    assert resultado == pytest.approx(esperado)
    
@pytest.mark.parametrize(
    "valor_compra",
    ["300", None, True, False, [], {}],
)
def test_rejeitar_tipo_invalido_de_valor(valor_compra):
    with pytest.raises(TypeError):
        calcular_desconto(valor_compra, "COMUM")


@pytest.mark.parametrize(
    "valor_compra",
    [-1, -100, float("nan"), float("inf"), float("-inf")],
)
def test_rejeitar_valor_invalido(valor_compra):
    with pytest.raises(ValueError):
        calcular_desconto(valor_compra, "VIP")


@pytest.mark.parametrize(
    "tipo_cliente",
    [None, 123, True, [], {}],
)
def test_rejeitar_tipo_invalido_de_cliente(tipo_cliente):
    with pytest.raises(TypeError):
        calcular_desconto(300, tipo_cliente)


@pytest.mark.parametrize(
    "tipo_cliente",
    ["", "   ", "PREMIUM"],
)
def test_rejeitar_categoria_invalida(tipo_cliente):
    with pytest.raises(ValueError):
        calcular_desconto(300, tipo_cliente)    