import pyautogui
import platform
import os


def close_tab():
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    # pyautogui.press('enter')


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
        if count == 4:
            break



def getCnpj():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        cnpjInFile = [i for i in content if "cnpj =" in i]
        return cnpjInFile[0][7:-1]


def getAuto():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        autoInFile = [i for i in content if "auto =" in i][0]
        itsTrue = autoInFile[7:-1].lower() == "true"

        if itsTrue:
            return True
        else:
            return False


def getMonth():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        monthInFile = [i for i in content if "month =" in i][0]
        containsData = monthInFile[8:-1]  != ''

        if containsData and int(monthInFile[8:-1]) > 0:
            return int(monthInFile[8:-1])
        else:
            return 0


def getYear():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        yearInFile = [i for i in content if "year =" in i][0]
        containsData = yearInFile[7:-1]  != ''

        if containsData and int(yearInFile[7:-1]) > 0:
            return int(yearInFile[7:-1])
        else:
            return 0


def calculateNumTabPresses(month):
    num_presses = 7 + (2*month)
    return num_presses


def open_browser(link):
    if platform.system() == 'Windows':
        os.system('start chrome {}'.format(link))
    elif platform.system() == 'Linux':
        os.system('google-chrome {}'.format(link))
    elif platform.system() == 'Darwin':
        os.system('open -a /Applications/Google\\ Chrome.app {}'.format(link))


def get_cpf():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        cpfInFile = [i for i in content if "cpf =" in i]
        return cpfInFile[0][6:-1]


def get_pwd():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        pwdInFile = [i for i in content if "pwd =" in i]
        return pwdInFile[0][6:-1]


def get_client_cnpj():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        client_cnpj_in_file = [i for i in content if "client_cnpj =" in i]
        return client_cnpj_in_file[0][14:-1]


def get_payment():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        payment_in_file = [i for i in content if "payment =" in i]
        payment_value = payment_in_file[0][10:-1]

        return str(payment_value)


def get_email():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        email_in_file = [i for i in content if "email =" in i]
        return email_in_file[0][8:-1]


def get_clockify_pwd():
    with open("env.txt", "r") as configFile:
        content = configFile.readlines()
        clockify_pwd_in_file = [i for i in content if "clockify_pwd =" in i]
        return clockify_pwd_in_file[0][15:-1]
