import PySimpleGUI as sg


layout = [
    [sg.Text("Gerar Boleto de Pagamento")],
    [sg.Button("Gerar DAS")],
    [sg.Button("Emitir Nota Fiscal")],
    [sg.Button("Configurações")],
]

janela = sg.Window("DAS Automation", layout, size=(270, 140))


while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == "Gerar DAS":
        print("Gerando DAS")
    if evento == "Emitir Nota Fiscal":
        print("Emitindo Nota Fiscal")
    if evento == "Configurações":
        print("Configurando")

janela.close()
