import random

class Forca:
    def __init__(self):
        self.palavras = ["python", "java", "ruby", "swift", "go"]
        self.palavra_secreta = self.selecionar_palavra_secreta()
        self.erros = []
        self.acertos = ["_"] * len(self.palavra_secreta)
        self.vidas = 6

    def selecionar_palavra_secreta(self):
        return random.choice(self.palavras)

    def imprimir_estado_do_jogo(self):
        print(" ".join(self.acertos))
        print("Erros:", ", ".join(self.erros))
        print(f"Você tem {self.vidas} vidas restantes.")

    def adivinhar_letra(self, letra):
        if len(letra)!= 1:
            print("Você deve adivinhar uma letra única!")
            return

        if letra in self.erros or letra in self.acertos:
            print("Você já adivinhou essa letra!")
            return

        if letra in self.palavra_secreta:
            print("Correto!")
            for i in range(len(self.palavra_secreta)):
                if self.palavra_secreta[i] == letra:
                    self.acertos[i] = letra
        else:
            print("Incorreto!")
            self.erros.append(letra)
            self.vidas -= 1

    def adivinhar_palavra(self, palavra):
        if palavra == self.palavra_secreta:
            print("Parabéns, você ganhou!")
            return True
        else:
            print(f"Incorreto! A palavra secreta não é {palavra}.")
            self.vidas -= 1
            return False

    def jogar(self):
        while self.vidas > 0:
            self.imprimir_estado_do_jogo()
            escolha = input("Você deseja adivinhar uma letra ou a palavra inteira? (L/P): ")
            if escolha.upper() == "L":
                letra = input("Adivinhe uma letra: ")
                self.adivinhar_letra(letra)
            elif escolha.upper() == "P":
                palavra = input("Adivinhe a palavra inteira: ")
                if self.adivinhar_palavra(palavra):
                    break
            else:
                print("Escolha inválida!")

            if "_" not in self.acertos:
                print("Parabéns, você ganhou!")
                break

        print(f"Jogo terminado! A palavra secreta era {self.palavra_secreta}.")

if __name__ == "__main__":
    jogo = Forca()
    jogo.jogar()