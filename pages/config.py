import PySimpleGUI as sg
import datetime
import configparser
from helpers.utils import getCnpj
from helpers.utils import getYear
from helpers.utils import get_cpf
from helpers.utils import get_pwd
from helpers.utils import get_client_cnpj
from babel.numbers import format_currency


months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
          'Novembro', 'Dezembro']

def default_month():
    with open("env.txt", "r") as configfile:
        lines = configfile.readlines()
        monthInFile = [i for i in lines if "month =" in i][0]
        month_num = int(monthInFile.split('=')[1].strip())
        return months[month_num - 1]


def select_year():
    current_year = datetime.datetime.now().year
    previous_year = current_year - 1
    return [str(current_year), str(previous_year)]


def returnMonth(month=None):
    if month is None:
        return months
    elif month in months:
        return str(months.index(month) + 1)
    else:
        return ""


def saved_payment():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        payment_in_file = [i for i in content if "payment =" in i]
        saved_value = payment_in_file[0][13:-1]
        saved_value = saved_value.replace(".", "")
        print(saved_value)
        return str(saved_value)


def run():
    layout_tab_generate_das = [
                [sg.Text ( "Mês:" ), sg.Combo ( returnMonth (), default_value=default_month(), size=(14, 1), key="-MONTH-", enable_events=True )],
                [sg.Text ( "Ano:" ), sg.Combo ( select_year (), default_value=getYear(), size=(6, 1), key="-YEAR-" )],
                [sg.Checkbox ( 'Auto', default=False, key="-AUTO-", enable_events=True)],
            ]

    layout_tab_emit_nf = [
        [sg.Text ( "Password:" ), sg.Input ( size=(8, 1), default_text=get_pwd() ,key="-PASSWORD-", enable_events=True, expand_x=True )],
        [sg.Text ( "CNPJ:" ), sg.Input ( size=(8, 1), default_text=get_client_cnpj(), key='-CLIENT_CNPJ-', enable_events=True, expand_x=True )],
        [sg.Text("Serviço R$:"), sg.Input(size=(8,1), default_text=saved_payment(), key="-PAYMENT-", enable_events=True, expand_x=True)],
    ]

    layout = [
        [sg.Text ( "Dados Pessoais" )],
        [sg.Text ( "CNPJ:" ), sg.Input ( size=(14, 1), default_text=getCnpj(), key="-CNPJ-", enable_events=True, expand_x=True )],
        [sg.Text("CPF:"), sg.Input(size=(8, 1), default_text=get_cpf(), key="-CPF-", enable_events=True, expand_x=True)],
        [sg.TabGroup ([[
            sg.Tab ( 'Gerar DAS', layout_tab_generate_das),
            sg.Tab ( 'Emitir NF',  layout_tab_emit_nf)
        ]], expand_x=True)],

        [sg.Button ( "Salvar", key="-SAVE-")],
    ]

    window = sg.Window ( "Configurações", layout, size=(250, 230) )

    config = configparser.ConfigParser ()
    config.read ( 'env.txt' )

    while True:
        event, values = window.read ()
        if event == sg.WIN_CLOSED:
            break
        if event == "-CNPJ-":
            if len(values["-CNPJ-"]) == 14:
                window['-SAVE-'].update(disabled=False)
            if len(values["-CNPJ-"]) < 14:
                window['-SAVE-'].update(disabled=True)
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
            config.set('ENV', 'CPF', values["-CPF-"])
            config.set('ENV', 'PWD', values["-PASSWORD-"])
            config.set('ENV', 'CLIENT_CNPJ', values['-CLIENT_CNPJ-'])
            pay = format_currency(float(values["-PAYMENT-"].replace(',', '.')), 'BRL', locale='pt_BR')
            config.set('ENV', "PAYMENT", str(pay))
            with open ( 'env.txt', 'w' ) as configfile:
                config.write ( configfile )
            break


    window.close ()
