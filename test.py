
palavra_secreta = "python"

letras_erradas = []

letras_certas = ["_"] * len(palavra_secreta)

vidas = 6

print("Bem-vindo ao Jogo da Forca!")
print("Você tem", vidas, "vidas.")

while vidas > 0:
    print(" ".join(letras_certas))
    print("Letras erradas:", ", ".join(letras_erradas))
    letra = input("Digite uma letra: ")

    if len(letra) != 1:
        print("Você deve digitar apenas uma letra!")
        continue

    if letra in letras_erradas or letra in letras_certas:
        print("Você já digitou essa letra!")
        continue

    if letra in palavra_secreta:
        print("Você acertou!")
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_certas[i] = letra
    else:
        print("Você errou!")
        letras_erradas.append(letra)
        vidas -= 1

    if "_" not in letras_certas:
        print("Parabéns, você ganhou!")
        break

print("Game over! A palavra secreta era", palavra_secreta)