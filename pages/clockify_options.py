import PySimpleGUI as sg
from clockify.import_time_tracking import run as run_import_time_tracking
from clockify.generate_report import run as run_generate_report

def run():
    layout = [
        [sg.Button("Importar Time Tracking")],
        [sg.Button("Gerar Relatório")],
    ]

    window = sg.Window("Clockify", layout, size=(230, 95))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Importar Time Tracking":
            run_import_time_tracking()
        if event == "Gerar Relatório":
            run_generate_report()

    window.close()

