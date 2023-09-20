import json
from collections import defaultdict

def carregar_questionario():
    try:
        with open("questionario.json", "r") as arquivo_json:
            questionario = json.load(arquivo_json)
        return questionario
    except FileNotFoundError:
        print("O arquivo questionario.json não foi encontrado.")
        return []
def receber_respostas(questionario):
    respostas = defaultdict(lambda: defaultdict(int))  # Usamos defaultdict para rastrear a quantidade numérica de respostas
    for pergunta in questionario:
        print(pergunta["pergunta"])
        for i, opcao in enumerate(pergunta["opcoes"]):
            print(f"{i + 1}: {opcao}")
        resposta = input("Escolha a opção correspondente (1, 2, 3, etc.), ou digite 'cancelar' para sair: ")
        if resposta.lower() == 'cancelar':
            return None 
        respostas[pergunta["pergunta"]][pergunta["opcoes"][int(resposta) - 1]] += 1
    return respostas

def exibir_relatorio(respostas):
    if not respostas:
        print("Questionário cancelado.")
    else:
        print("Respostas:")
        for pergunta, opcoes in respostas.items():
            print(pergunta + ":")
            for opcao, quantidade in opcoes.items():
                print(f"{opcao} respondido {quantidade} vezes")

def salvar_respostas(questionario, respostas):
    with open("respostas.json", "a") as arquivo_json:
        data = {"questionario": questionario, "respostas": respostas}
        json.dump(data, arquivo_json)
        arquivo_json.write("\n")  

while True:
    print("\nMenu:")
    print("1. Iniciar novo questionário")
    print("2. Visualizar relatório de questionário existente")
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1/2/3): ")

    if opcao == '1':
        questionario = carregar_questionario()
        if questionario:
            respostas = receber_respostas(questionario)
            if respostas:
                salvar_respostas(questionario, respostas)
                exibir_relatorio(respostas)
    elif opcao == '2':
        try:
            with open("respostas.json", "r") as arquivo_json:
                linhas = arquivo_json.readlines()
                todas_respostas = defaultdict(lambda: defaultdict(int))
                for linha in linhas:
                    data = json.loads(linha)
                    for pergunta, opcoes in data["respostas"].items():
                        for opcao, quantidade in opcoes.items():
                            todas_respostas[pergunta][opcao] += quantidade
                print("\nRelatório Final:")
                exibir_relatorio(todas_respostas)
        except FileNotFoundError:
            print("Nenhum questionário existente.")
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1/2/3).")