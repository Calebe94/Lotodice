import unittest
from src.lotodice.jogo import Jogo
from src.lotodice.mega import MegaSena
from src.lotodice.quina import Quina

class TestJogo(unittest.TestCase):

    def test_gerar_jogo(self):
        jogo = Jogo(60, [])
        jogo_gerado = jogo.gerar_jogo()
        self.assertEqual(len(jogo_gerado), 6)

    def test_verificar_premio(self):
        jogo = Jogo(60, [4, 11, 46, 48, 52])
        jogos = [[4, 11, 46, 48, 52, 53], [1, 2, 3, 4, 5, 6]]
        resultado_esperado = ["GANHAMOOOOOO CARALHOOOOOW!!!", ""]
        self.assertEqual(jogo.verificar_premio(jogos), resultado_esperado)

    def test_carregar_jogos(self):
        jogo = Jogo(60, [])
        jogos = jogo.carregar_jogos("jogos/jogos-dezembro-23.csv")
        self.assertEqual(len(jogos), 10)


class TestMegaSena(unittest.TestCase):

    def test_verifica_tipo_premio(self):
        mega = MegaSena([])
        self.assertEqual(mega.verifica_tipo_premio(6), "GANHAMOOOOOO CARALHOOOOOW!!!")


class TestQuina(unittest.TestCase):

    def test_verifica_tipo_premio(self):
        quina = Quina([])
        self.assertEqual(quina.verifica_tipo_premio(5), "GANHAMOOOOOO CARALHOOOOOW!!!")


if __name__ == '__main__':
    unittest.main()
