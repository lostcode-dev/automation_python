import PySimpleGUI as sg
import datetime
import configparser

current_year = datetime.datetime.now().year
previous_year = current_year - 1

layout = [
    [sg.Text("Dados Pessoais")],
    [sg.Text("CNPJ:"), sg.Input(size=(14, 1), key="-CNPJ-", enable_events=True)],
    [sg.Text("Gerar DAS")],
    [sg.Text("Mês:"), sg.Combo(['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'], key="-MONTH-", enable_events=True)],
    [sg.Text("Ano:"), sg.Combo([str(current_year), str(previous_year)], default_value=str(current_year), size=(4), key="-YEAR-")],
    [sg.Checkbox('Auto', default=False, key="-AUTO-", enable_events=True)],
    [sg.Button("Salvar")],
]

window = sg.Window("Configurações", layout, size=(250, 215))

config = configparser.ConfigParser()
config.read('../env.txt')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-CNPJ-":
        print(values["-CNPJ-"])
        if len(values["-CNPJ-"]) > 14:
            values["-CNPJ-"] = values["-CNPJ-"][:14]
            window["-CNPJ-"].update(value=values["-CNPJ-"])
            sg.popup('A entrada deve ter exatamente 14 caracteres.')
    if event == "-YEAR-":
        print("-YEAR-")
    if event == "-AUTO-":
        if values["-AUTO-"]:
            print('Clicado')
            window["-MONTH-"].update('')
            window["-YEAR-"].update('')
            window["-MONTH-"].update(disabled=True)
            window["-YEAR-"].update(disabled=True)
        else:
            window["-MONTH-"].update(disabled=False)
            window["-YEAR-"].update(disabled=False)
    if event == "Salvar":
        print("Configurando")
        config.set('ENV', 'CNPJ', values['-CNPJ-'])
        # config.set('MONTH=', 'MONTH', values['-MONTH-'])
        config.set('ENV', 'YEAR', values['-YEAR-'])
        # config.set('SEÇÃO', 'AUTO', values['-AUTO-'])
        with open('../env.txt', 'w') as configfile:
            config.write(configfile)

window.close()