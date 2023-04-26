import pyautogui
import platform
import os


def close_tab():
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')


def loading_screen(screen: object, image_error: object = "") -> object:
    loading = pyautogui.locateOnScreen(f'images/{screen}.png', confidence=0.8)
    count = 0;
    while loading is None:
        pyautogui.sleep(0.5)
        loading = pyautogui.locateOnScreen(f'images/{screen}.png', confidence=0.8)
        error = False
        count += 1
        if image_error:
            error = pyautogui.locateOnScreen(f'images/{image_error}.png', confidence=0.8)
        if error:
            close_tab()
            exit()
        if count == 10:
            break



def getCnpj():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        cnpjInFile = [i for i in content if "CNPJ=" in i]
        return cnpjInFile[0][5:-1]


def getAuto():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        autoInFile = [i for i in content if "AUTO=" in i]
        if autoInFile[0][5:-1].lower() == "true":
            return True
        else:
            return False


def getMonth():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        monthInFile = [i for i in content if "MONTH=" in i]
        if int(monthInFile[0][6:-1]) > 0:
            return int(monthInFile[0][6:-1])
        else:
            return 0


def getYear():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        yearInFile = [i for i in content if "YEAR=" in i]
        if int(yearInFile[0][5:-1]) > 0:
            return int(yearInFile[0][5:-1])
        else:
            return 0


def calculateNumTabPresses(month):
    month_pay = 12 if month == 1 else month - 1
    num_presses = 7 + (2*month_pay)
    return num_presses


def open_receita_website():
    if platform.system() == 'Windows':
        os.system('start chrome {}'.format('http://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/pgmei.app/Identificacao'))
    elif platform.system() == 'Linux':
        os.system('google-chrome {}'.format('http://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/pgmei.app/Identificacao'))
    elif platform.system() == 'Darwin':
        os.system('open -a /Applications/Google\ Chrome.app {}'.format('http://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/pgmei.app/Identificacao'))
