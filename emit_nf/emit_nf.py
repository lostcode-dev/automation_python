import pyautogui
from helpers.utils import close_tab
from helpers.utils import loading_screen
from helpers.utils import get_cpf
from helpers.utils import open_browser
from helpers.utils import get_pwd


def access_browser_nf():
    open_browser('https://iss.fortaleza.ce.gov.br/grpfor/login.seam')


def do_login_nf():
    cpf = get_cpf()
    pwd = get_pwd()
    loading_screen('login_nf')
    pyautogui.press('tab', presses=2)
    pyautogui.typewrite(cpf)
    pyautogui.press('tab')
    pyautogui.typewrite(pwd)
    pyautogui.press('tab')
    #Verificar captcha (procurar outra forma melhor depois):
    captcha = pyautogui.prompt(text='Digite os caracteres da captcha:', title='Captcha', default='')
    captcha_uppercase = captcha.upper()
    pyautogui.write(captcha_uppercase)
    pyautogui.press('enter')
    #Em caso de erro de qualquer dado inserido:
    # loading_screen('invalid_data_nf')
    # warning = pyautogui.locateOnScreen('images/invalid_data_nf.png', confidence=0.95)
    # if warning:
    #     pass


def click_emit_nf():
    # Verificar erro de carregamento infinito no inicio da tela click gerar NF
    pyautogui.sleep(1)
    pyautogui.press('F5')
    pyautogui.sleep(1)


def run():
    access_browser_nf()
    do_login_nf()
    click_emit_nf()
    print('Rodando Script')

    # close_tab()