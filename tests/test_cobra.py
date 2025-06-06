import pytest
from classes.cobra import Cobra


# ---------- Testes da Cobra ----------

@pytest.fixture
def cobra():
    return Cobra(100, 100, 20)

def test_mover_cobra(cobra):
    cobra.direcao = (1, 0)
    cobra.mover()
    assert cobra.corpo[0] == (120, 100)

def test_crescer_cobra(cobra):
    cobra.crescer()
    assert len(cobra.corpo) == 2

def test_colisao_com_parede(cobra):
    cobra.corpo[0] = (820, 100)
    assert cobra.colidiu_com_parede(800, 800)

def test_colisao_com_si_mesma():
    c = Cobra(100, 100, 20)
    c.corpo = [(100, 100), (120, 100), (140, 100), (120, 100), (100, 100), (80, 100)]
    assert c.colidiu_com_si_mesma()
