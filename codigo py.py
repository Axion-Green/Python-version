
#antes disso é necessário uma estrutura que ative o leitor de composição do ar e receba o output dele, fornecendo o índice de poluição do ar
#a media deve se encontrar em uma escala de 1 a 10 sendo 1 o ar mais limpo e 10 o ar mais poluido
#a escala funciona classificando os valores de 1 a 3.33 o ar pouco poluído, de 3.33 a 6.66 o ar com poluição média, e entre 6.66 a 10 o ar muito poluído

import matplotlib.pyplot as plt

dados = []
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ags', 'Set', 'Out', 'Nov', 'Dez']
count = 0
opcao = 0

def exibir_menu():
    print('_______________')
    print('- AXION GREEN -')
    print('_______________')
    print('\nAQUI ESTA NOSSO CODIGO EM VERSÃO PITHON')
    print('\nUTILIZAMOS FERRAMENTAS VISTAS EM AULA')
    print('\nEscolha uma opção:')
    print('(1) Inserir dados')
    print('(2) Ver gráfico')

def plotar_grafico():
    #gera o grafico no final do codigo
    plt.plot(dados, color='darkcyan', label='Leituras de cada mês')
    plt.title('Qualidade do ar - Anual')
    plt.xlabel('Meses')
    plt.ylabel('Valor')
    plt.xticks(range(12), meses)
    plt.yticks(range(10))
    plt.legend()
    plt.show()

exibir_menu()

while opcao != 2:
    opcao = int(input('Opção: '))
    if opcao == 1:
        for i in range(12):
            mes = meses[i]
            ar = int(input(f'{mes}:\\nMédia mensal da qualidade do ar fornecida pelo sensor: '))

            if 1 <= ar < 3:
                ar = 3
                led = 'VERDE'
                buzzer = 'Notone'
            elif 3 <= ar < 6:
                ar = 6
                led = 'AMARELO'
                buzzer = 'Notone'
            elif 6 <= ar <= 10:
                ar = 9
                led = 'VERMELHO'
                buzzer = 'Tone'
            else:
                print("Digite um número entre 1 e 10")
                continue

            dados.append(ar)
            count += 1

            if count == 12:
                break
    elif opcao == 2:
        print('\\nGráfico:')
        plotar_grafico()
    else:
        print('Opção inválida. Por favor, escolha novamente.')
        
#A partir daqui é necessária uma estrutura que seja capaz de ativar os diferentes LEDs da protoboard, seguindo a escala de índice de poluição
