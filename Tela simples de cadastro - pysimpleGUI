import PySimpleGUI as sg

# Layout da janela
layout3 = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('OK')]
]

# Criando a janela
janela = sg.Window('Tela de login', layout3)

# Loop de eventos
while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'OK':  # O nome do botão é 'OK', então o evento será 'OK'
        if valores['usuario'] == 'jhonatan' and valores['senha'] == '123456':
            print("Seja bem-vindo")
        else:
            print("Usuário ou senha incorretos")

janela.close()
