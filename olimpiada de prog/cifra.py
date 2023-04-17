#um programa que codifique uma palavra.
#essa codificação deve seguir algumas regras chatas.
"""
Ler a palavra e usar um 'for' para percorre-la, concatenando as letras numa nva str a partir de certas regras.
Para cada letra, devo checar se:
    É uma vogal: se sim, apenas concateno.
    Se não:
        concateno a consoante.
        concateno a vogal mais proxima dela (a letra) no alfabeto original
        (se houver um empate de proximidade de vogais, a mais proxima do inicio ganha).
        concateno a proxima consoante."""

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z']
vogais = ['a','e','i','o','u']
palavra = input()
nova_palavra = ''
for c in palavra:
    if c in vogais:
        nova_palavra += c
    else:
        nova_palavra +=c
        marca = int()
        for l in alfabeto:
            if l == c:
                marca = alfabeto.index(l)
                dir_temp = int()
                esq_temp = int()
                for vogal in alfabeto:
                    if alfabeto.index(vogal) > marca and vogal in vogais:
                        dir_temp = vogal
                        break
                
                alfa_reverso = list(reversed(alfabeto))
                for vogal in alfa_reverso:
                    if alfa_reverso.index(vogal) > marca and vogal in vogais:
                        esq_temp = vogal
                        break
                print((esq_temp,dir_temp))
                ind_dir = alfabeto.index(l) - alfabeto.index(dir_temp)
                ind_esq = alfabeto.index(l) - alfabeto.index(esq_temp)
                print((ind_esq,ind_dir))

                if abs(ind_dir)<abs(ind_esq):
                    nov
            
                for consoante in alfabeto:
                    if alfabeto.index(consoante) > marca and consoante not in vogais:
                        nova_palavra += consoante
                        break
        print(marca)


print(alfa_reverso,'\n',alfabeto,'\n',vogais)
print(nova_palavra)