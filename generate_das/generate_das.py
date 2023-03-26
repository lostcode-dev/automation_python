import pyautogui
from datetime import datetime
import os


def close_tab():
    pyautogui.keyDown ( 'ctrl' )
    pyautogui.press ( 'w' )
    pyautogui.keyUp ( 'ctrl' )


def loading_screen(screen, image_error=""):
    loading = pyautogui.locateOnScreen ( f'images/{screen}.png', confidence=0.8 )
    while loading is None:
        pyautogui.sleep ( 0.5 )
        loading = pyautogui.locateOnScreen ( f'images/{screen}.png', confidence=0.8 )
        error = False
        if image_error:
            error = pyautogui.locateOnScreen ( f'images/{image_error}.png', confidence=0.8 )
        if error:
            close_tab ()
            exit ()


def getCnpj():
    with open ( "config", "r" ) as configFile:
        content = configFile.readlines ()
        cnpjInFile = [i for i in content if "CNPJ=" in i]
        return cnpjInFile[0][5:-1]


def getAuto():
    with open ( "config", "r" ) as configFile:
        content = configFile.readlines ()
        autoInFile = [i for i in content if "AUTO=" in i]
        if autoInFile[0][5:-1].lower () == "true":
            return True
        else:
            return False


def getMonth():
    with open ( "config", "r" ) as configFile:
        content = configFile.readlines ()
        monthInFile = [i for i in content if "MONTH=" in i]
        if int ( monthInFile[0][6:-1] ) > 0:
            return int ( monthInFile[0][6:-1] )
        else:
            return 0


def getYear():
    with open ( "config", "r" ) as configFile:
        content = configFile.readlines ()
        yearInFile = [i for i in content if "YEAR=" in i]
        if int ( yearInFile[0][5:-1] ) > 0:
            return int ( yearInFile[0][5:-1] )
        else:
            return 0


cnpj = getCnpj ()
auto = getAuto ()
month = auto if getMonth () else 0
year = auto if getYear () else 0
actual_month = datetime.now ().month
actual_year = datetime.now ().year

# ACESSAR NAVEGADOR
os.system (
    'google-chrome http://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/pgmei.app/Identificacao' )
loading_screen ( 'login' )
pyautogui.typewrite ( cnpj )

# LOGIN
continue_btn = pyautogui.locateCenterOnScreen ( 'images/btn_continue.png' )
pyautogui.moveTo ( continue_btn.x, continue_btn.y, duration=0.2 )
pyautogui.click ( continue_btn.x, continue_btn.y )

# CLICK EMITIR GUIA
loading_screen ( 'home' )
link_emit_guia = pyautogui.locateCenterOnScreen ( 'images/link_emit_guia.png', confidence=0.8 )
pyautogui.click ( link_emit_guia.x, link_emit_guia.y )

# CLICK SELECT ANO
loading_screen ( 'screen_year' )
pyautogui.press ( 'tab', presses=6 )
pyautogui.press ( 'enter' )

# CLICK YEAR VALUE
if not auto & year:
    actual_year = year
else:
    if actual_month == 1:
        actual_year = actual_year - 1

pyautogui.sleep ( 0.3 )
positionYear = {
    2022: pyautogui.locateCenterOnScreen ( 'images/2022.png', confidence=0.95 ),
    2023: pyautogui.locateCenterOnScreen ( 'images/2023.png', confidence=0.95 ),
    2024: pyautogui.locateCenterOnScreen ( 'images/2024.png', confidence=0.95 ),
    2025: pyautogui.locateCenterOnScreen ( 'images/2025.png', confidence=0.95 ),
    2026: pyautogui.locateCenterOnScreen ( 'images/2026.png', confidence=0.95 ),
}

pyautogui.click ( positionYear[actual_year].x, positionYear[actual_year].y )
pyautogui.sleep ( 1 )

# CLICK SUBMIT
pyautogui.press ( 'tab' )
pyautogui.press ( 'enter' )

# CLICK CHECKBOX MONTH
loading_screen ( 'component_header_month' )
positionMonth = {
    1: pyautogui.locateOnScreen ( 'images/jan.png', confidence=0.95 ),
    2: pyautogui.locateOnScreen ( 'images/fev.png', confidence=0.95 ),
    3: pyautogui.locateOnScreen ( 'images/mar.png', confidence=0.95 ),
    4: pyautogui.locateOnScreen ( 'images/abr.png', confidence=0.95 ),
    5: pyautogui.locateOnScreen ( 'images/mai.png', confidence=0.95 ),
    6: pyautogui.locateOnScreen ( 'images/jun.png', confidence=0.95 ),
    7: pyautogui.locateOnScreen ( 'images/jul.png', confidence=0.95 ),
    8: pyautogui.locateOnScreen ( 'images/ago.png', confidence=0.95 ),
    9: pyautogui.locateOnScreen ( 'images/set.png', confidence=0.95 ),
    10: pyautogui.locateOnScreen ( 'images/out.png', confidence=0.95 ),
    11: pyautogui.locateOnScreen ( 'images/nov.png', confidence=0.95 ),
    12: pyautogui.locateOnScreen ( 'images/dez.png', confidence=0.95 ),
}

month_pay = actual_month

if not auto & month:
    month_pay = month
else:
    month_pay = actual_month == 1 if 12 else actual_month - 1

pyautogui.click ( positionMonth[month_pay].left + 10, positionMonth[month_pay].top + 10 )

# CLICK GENERATE DAS
generate_das = pyautogui.locateCenterOnScreen ( 'images/btn_generate_das.png' )
pyautogui.click ( generate_das.x, generate_das.y )

# BAIXAR PDF
loading_screen ( 'component_modal_success', "component_modal_warning" )
download_pdf = pyautogui.locateCenterOnScreen ( 'images/btn_download_pdf.png' )
pyautogui.click ( download_pdf.x, download_pdf.y )
close_tab ()
