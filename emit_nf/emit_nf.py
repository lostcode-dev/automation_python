import pyautogui
from helpers.utils import close_tab
from helpers.utils import loading_screen
from helpers.utils import get_cpf
from helpers.utils import getAuto
from helpers.utils import open_browser


def access_browser_nf():
    open_browser('https://iss.fortaleza.ce.gov.br/grpfor/login.seam')


def do_login_nf():
    cpf = get_cpf()
    loading_screen('login_nf')
    pyautogui.press('tab', presses=2)
    pyautogui.typewrite(cpf)


def run():
    access_browser_nf()
    do_login_nf()
    print('Rodando Script')