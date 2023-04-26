import PySimpleGUI as sg
import datetime
import configparser

def select_year():
    current_year = datetime.datetime.now().year
    previous_year = current_year - 1
    return [str(current_year), str(previous_year)]


def returnMonth(month=None):
    months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    if month is None:
        return months
    elif month in months:
        return str(months.index(month) + 1)
    else:
        return ""

def run():
    layout_tab_generate_das = [
                [sg.Text ( "Mês:" ), sg.Combo ( returnMonth (),  size=(14, 1), key="-MONTH-", enable_events=True )],
                [sg.Text ( "Ano:" ), sg.Combo ( select_year (), size=(6, 1), key="-YEAR-" )],
                [sg.Checkbox ( 'Auto', default=False, key="-AUTO-", enable_events=True)],
            ]

    layout_tab_emit_nf = [
        [sg.Text ( "CPF:" ), sg.Input ( size=(8, 1), key="-CPF-", enable_events=True, expand_x=True )],
        [sg.Text ( "Password:" ), sg.Input ( size=(8, 1), key="-PASSWORD-", enable_events=True, expand_x=True )],
        [sg.Text ( "CNPJ:" ), sg.Input ( size=(8, 1), key="-CNPJ_CLIENTE-", enable_events=True, expand_x=True )],

    ]

    layout = [
        [sg.Text ( "Dados Pessoais" )],
        [sg.Text ( "CNPJ:" ), sg.Input ( size=(14, 1), key="-CNPJ-", enable_events=True, expand_x=True )],
        [sg.TabGroup ([[
            sg.Tab ( 'Gerar DAS', layout_tab_generate_das),
            sg.Tab ( 'Emitir NF',  layout_tab_emit_nf)
        ]], expand_x=True)],

        [sg.Button ( "Salvar", key="-SAVE-", disabled=True )],
    ]

    window = sg.Window ( "Configurações", layout, size=(250, 215) )

    config = configparser.ConfigParser ()
    config.read ( 'env.txt' )

    while True:
        event, values = window.read ()
        if event == sg.WIN_CLOSED:
            break
        if event == "-CNPJ-":
            if len ( values["-CNPJ-"] ) == 14:
                window["-SAVE-"].update ( disabled=False )
            if len ( values["-CNPJ-"] ) > 14:
                values["-CNPJ-"] = values["-CNPJ-"][:14]
                window["-CNPJ-"].update ( value=values["-CNPJ-"] )
                sg.popup ( 'CNPJ só pode ter no máximo 14 caracteres' )
        if event == "-AUTO-":
            if values["-AUTO-"]:
                window["-MONTH-"].update ( '' )
                window["-YEAR-"].update ( '' )
            window["-MONTH-"].update ( disabled=values["-AUTO-"] )
            window["-YEAR-"].update ( disabled=values["-AUTO-"] )
        if event == "-SAVE-":
            config.set ( 'ENV', 'CNPJ', values['-CNPJ-'] )
            config.set ( 'ENV', 'MONTH', returnMonth ( values['-MONTH-'] ) )
            config.set ( 'ENV', 'YEAR', values['-YEAR-'] )
            config.set ( 'ENV', 'AUTO', str ( values['-AUTO-'] ) )
            with open ( 'env.txt', 'w' ) as configfile:
                config.write ( configfile )
            break
    window.close ()
