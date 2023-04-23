import PySimpleGUI as sg


layout = [
    [sg.Button("Gerar DAS")],
    [sg.Button("Emitir Nota Fiscal")],
    [sg.Button("Configurações")],
]

window = sg.Window("MEI Automation", layout, size=(270, 120))


while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Gerar DAS":
        print("Gerando DAS")
    if event == "Emitir Nota Fiscal":
        print("Emitindo Nota Fiscal")
    if event == "Configurações":
        print("Configurando")

window.close()
