import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # Layout da tela
        self.layout = [
            [sg.Text('Nome'), sg.Input(key='nome')],
            [sg.Text('Idade'), sg.Input(key='idade')],
            [sg.Text("Quais provedores de email são aceitos?")],
            [sg.Checkbox("Gmail", key="Gmail"),sg.Checkbox('Outlook', key="Outlook"),sg.Checkbox('Yahoo', key="Yahoo")],
            [sg.Button('Enviar')],
            [sg.Output(size=(30,20))]
            [sg.Slider()]
        ]

        # Janela
        self.janela = sg.Window("Dados do usuário", self.layout)

    def Iniciar(self):
        # Extração de dados da tela
        event, self.values = self.janela.read()  # Ler evento e valores da janela


        nome = self.values['nome']
        nome = self.values['idade']
        nome = self.values['Gmail']
        nome = self.values['Outlook']
        nome = self.values['Yahoo']

        if event == sg.WINDOW_CLOSED or event == 'Enviar':
            print(self.values)  # Exibe os valores inseridos
        self.janela.close()  # Fecha a janela

# Criando a instância e rodando a tela
if __name__ == '__main__':  # Garanta que a classe será executada ao rodar o script
    tela = TelaPython()
    tela.Iniciar()
