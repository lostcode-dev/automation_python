import PySimpleGUI as sg
import datetime

current_year = datetime.datetime.now().year
previous_year = current_year - 1

layout = [
    [sg.Text("Dados Pessoais")],
    [sg.Text("CNPJ:"), sg.Input(key="-CNPJ-", size=(14, 1))],
    [sg.Text("Gerar DAS")],
    [sg.Text("Mês:"), sg.Combo(['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'], key="-MONTH-")],
    [sg.Text("Ano:"), sg.Combo([str(current_year), str(previous_year)], default_value=str(current_year), key="-YEAR-")],
    [sg.Checkbox('Auto', default=False)],
    [sg.Button("Salvar")],
]

window = sg.Window("Configurações", layout, size=(250, 215))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "-CNPJ-":
        cnpj_number = "-CNPJ-"
    elif event == "-YEAR-":
        selected_year = int(values["-YEAR-"])
    elif event == "Auto":
        if values["Auto"]:
            window["-MONTH-"].update('')
            window["-YEAR-"].update('')
        else:
            window["-MONTH-"].update('Janeiro')
            window["-YEAR-"].update(current_year)
    elif event == "Salvar":
        print("Configurando")

window.close()