import pyautogui
from datetime import datetime
from helpers.utils import close_tab
from helpers.utils import loading_screen
from helpers.utils import getCnpj
from helpers.utils import getAuto
from helpers.utils import getMonth
from helpers.utils import getYear
from helpers.utils import calculateNumTabPresses
from helpers.utils import open_browser

def access_browser():
    open_browser ('http://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/pgmei.app/Identificacao')


def do_login():
    cnpj = getCnpj ()

    loading_screen ( 'login' )
    pyautogui.typewrite ( cnpj )
    pyautogui.press ( 'tab', presses=3 )
    pyautogui.press ( 'enter' )


def click_emit_guia():
    loading_screen ( 'home' )
    pyautogui.press ( 'tab', presses=2 )
    pyautogui.press ( 'enter' )


def select_year():
    auto = getAuto ()
    year = auto if getYear () else 0

    actual_month = datetime.now ().month
    actual_year = datetime.now ().year

    loading_screen ( 'screen_year' )
    pyautogui.press ( 'tab', presses=6 )
    pyautogui.press ( 'enter' )

    if not auto and year:
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


def click_submit():
    pyautogui.press ( 'tab' )
    pyautogui.press ( 'enter' )


def click_checkbox_month():
    monthConfig = getMonth ()
    actual_month = datetime.now ().month
    auto = getAuto ()

    if not auto & monthConfig:
        actual_month = monthConfig
    else:
        if actual_month == 1:
            actual_month = 12

    loading_screen ( 'component_header_month' )
    pyautogui.press ( 'tab', calculateNumTabPresses ( actual_month ) )
    pyautogui.press ( 'space' )


def click_generate_das():
    pyautogui.press ( 'pgdn' )
    loading_screen ( 'btn_generate_das' )
    generate_das = pyautogui.locateCenterOnScreen ( 'images/btn_generate_das.png', confidence=0.95 )
    pyautogui.click ( generate_das.x, generate_das.y )


def download_pdf():
    loading_screen ( 'component_modal_success', "component_modal_warning" )
    pyautogui.press ( 'tab', presses=6 )
    pyautogui.press ( 'enter' )


def run():
    access_browser ( )
    do_login ()
    click_emit_guia ()
    select_year ()
    click_submit ()
    click_checkbox_month ()
    click_generate_das ()
    download_pdf ()

    close_tab ()
