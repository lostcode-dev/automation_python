import pyautogui
from helpers.utils import close_tab
from helpers.utils import loading_screen
from helpers.utils import get_cpf
from helpers.utils import open_browser
from helpers.utils import get_pwd
from helpers.utils import get_client_cnpj


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
    pyautogui.press('tab', presses=15)
    pyautogui.press('enter')


def emit_nf_data():
    pyautogui.sleep(0.5)
    pyautogui.press('tab', presses=15)
    pyautogui.press('right')
    pyautogui.press('pgdn') #Corrigir erro na página caso barra de rolagem não esteja no final
    pyautogui.press('tab')
    cnpj_client = get_client_cnpj()
    pyautogui.typewrite(cnpj_client)
    pyautogui.sleep(0.5)
    pyautogui.press('down')
    pyautogui.sleep(1)
    pyautogui.press('tab')


def click_service_screen():
    pyautogui.sleep(2)
    service_layout = pyautogui.locateOnScreen('images/service_screen.png', confidence=0.9)
    service_layout_center = pyautogui.center(service_layout)
    pyautogui.click(service_layout_center.x, service_layout_center.y)


def service_data():
    pyautogui.press('tab', presses=3)
    pyautogui.press('down')


    # exit()


def run():
    access_browser_nf()
    do_login_nf()
    click_emit_nf()
    emit_nf_data()
    click_service_screen()
    service_data()
    print('Rodando Script')

    # close_tab()