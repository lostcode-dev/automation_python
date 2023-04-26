import PySimpleGUI as sg
from generate_das.generate_das import run as run_generate_das
from emit_nf.emit_nf import run as run_emit_nf


layout = [
    [sg.Button("Gerar DAS")],
    [sg.Button("Emitir Nota Fiscal")],
    [sg.Button("Configurações")],
]

window = sg.Window("MEI Automation", layout, size=(270, 120))

def run():
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Gerar DAS":
            run_generate_das()
        if event == "Emitir Nota Fiscal":
            run_emit_nf()
        if event == "Configurações":
            print("Configurando")

    window.close()
