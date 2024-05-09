"""
    Gerador de senhas
    Um programa de interface gráfica que deve ser capaz de:
    [ ] Armazenar o site/sofware para o qual a senha será gerada
    [ ] Armazenar o usuário/e-mail
    [ ] Possibilitar a configuração do tamanho da senha
    [ ] BONUS - Tocar música de fundo ao iniciar o programa
"""

import random
import PySimpleGUI as sg #para gerar a interface grafica do programa
import os # para lidar com cliação de arquivo


class PassGen:
    def _init_(self):
        sg.theme('Black')

    def Iniciar(self):
        pass

    def salvar_senha(self):
        pass

gen = PassGen() #instanciei a class
gen.Iniciar()
