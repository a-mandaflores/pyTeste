import pytest
from Calculadora import Calculadora
import math

@pytest.fixture
def calculadora():
    return Calculadora()

def test_soma(calculadora):
    assert calculadora.soma(3, 5) == 8
    assert calculadora.soma(-1, 1) == 0
    assert calculadora.soma(0, 0) == 0

def test_subtrai(calculadora):
    assert calculadora.subtrai(10, 5) == 5
    assert calculadora.subtrai(0, 5) == -5
    assert calculadora.subtrai(-5, -5) == 0

def test_multiplica(calculadora):
    assert calculadora.multiplica(4, 5) == 20
    assert calculadora.multiplica(0, 10) == 0
    assert calculadora.multiplica(-3, 3) == -9

def test_divide(calculadora):
    assert calculadora.divide(10, 2) == 5
    with pytest.raises(ValueError, match="Não é possível dividir por zero"):
        calculadora.divide(10, 0)

def test_potencia(calculadora):
    assert calculadora.potencia(2, 3) == 8
    assert calculadora.potencia(5, 0) == 1
    assert calculadora.potencia(0, 5) == 0

def test_modulo(calculadora):
    assert calculadora.modulo(10, 3) == 1
    assert calculadora.modulo(7, 5) == 2
    with pytest.raises(ValueError, match="Não é possível calcular o módulo por zero"):
        calculadora.modulo(10, 0)

def test_raiz_quadrada(calculadora):
    assert calculadora.raiz_quadrada(9) == 3
    assert calculadora.raiz_quadrada(0) == 0
    with pytest.raises(ValueError, match="Não é possível calcular a raiz quadrada de um número negativo"):
        calculadora.raiz_quadrada(-4)

def test_fatorial(calculadora):
    assert calculadora.fatorial(5) == 120
    assert calculadora.fatorial(0) == 1
    with pytest.""raises(ValueError, match="Não é possível calcular o fatorial de um número negativo"):
        calculadora.fatorial(-3)
    with pytest.raises(ValueError, match="O fatorial só é definido para números inteiros"):
        calculadora.fatorial(4.5)

def test_logaritmo(calculadora):
    assert calculadora.logaritmo(math.e) == 1
    assert calculadora.logaritmo(100, 10) == 2
    with pytest.raises(ValueError, match="O logaritmo só é definido para números positivos"):
        calculadora.logaritmo(-1)
    with pytest.raises(ValueError, match="O logaritmo só é definido para números positivos"):
        calculadora.logaritmo(0)
