import PySimpleGUI as sg
from generate_das.generate_das import run as run_generate_das
from iss_fortal.emit_nf import run as run_emit_nf
from pages.config import run as run_config
from pages.clockify_options import run as run_clockify_options

layout = [
    [sg.Button("Gerar DAS")],
    [sg.Button("Emitir Nota Fiscal")],
    [sg.Button("Clockify")],
    [sg.Button("Configurações")],
]

window = sg.Window("AdminBot", layout, size=(225, 150))


def run():
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Gerar DAS":
            run_generate_das()
        if event == "Emitir Nota Fiscal":
            run_emit_nf()
        if event == "Clockify":
            run_clockify_options()
        if event == "Configurações":
            run_config()
            print("Configurando")

    window.close()
