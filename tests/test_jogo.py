import pytest
import pygame.display
import pygame.font
import pygame_gui
import pygame_gui.elements

from classes.jogo import JogoCobrinha
from unittest.mock import mock_open

# ---------- Testes do Jogo (com mocks) ----------
"""
O monkeypatch é uma fixture integrada ao pytest, que é automaticamente injetada quando você a coloca como argumento da função de teste

"""
@pytest.fixture
def jogo(monkeypatch):
    # Mocks para evitar criação real de tela e UI
    monkeypatch.setattr(pygame.display, "set_mode", lambda *a, **kw: None)
    monkeypatch.setattr(pygame.font, "SysFont", lambda *a, **kw: lambda text, antialias, color: None)
    monkeypatch.setattr(pygame_gui, "UIManager", lambda *a, **kw: lambda *args, **kwargs: None)
    monkeypatch.setattr(pygame_gui.elements, "UIButton", lambda *a, **kw: None)
    monkeypatch.setattr(pygame_gui.elements, "UITextEntryLine", lambda *a, **kw: None)
    return JogoCobrinha()

def test_pontuacao_inicial_zero(jogo):
    assert jogo.pontuacao == 0

def test_reiniciar_reseta_pontuacao(jogo):
    jogo.pontuacao = 10
    jogo.reiniciar()
    assert jogo.pontuacao == 0

def test_salvar_pontuacao(monkeypatch, jogo):
    jogo.pontuacao = 8
    jogo.nome_jogador = "Alice"

    m = mock_open()
    monkeypatch.setattr("builtins.open", m)

    jogo.salvar_pontuacao()
    m().write.assert_called_once_with("Alice - 8 pontos\n")

def test_obter_melhores_pontuacoes(monkeypatch, jogo):
    conteudo = "Ana - 10 pontos\nBob - 25 pontos\nClara - 15 pontos\n"
    m = mock_open(read_data=conteudo)
    monkeypatch.setattr("builtins.open", m)

    top = jogo.obter_melhores_pontuacoes()
    assert top == [("Bob", 25), ("Clara", 15), ("Ana", 10)]
