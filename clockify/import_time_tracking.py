import pyautogui
from helpers.utils import open_browser
from helpers.utils import loading_screen
from helpers.utils import get_email
from helpers.utils import get_clockify_pwd


#ABIR SITE DO CLOCKIFY
def access_browser_clockify():
    open_browser('https://clockify.me/')


#FAZER LOGIN
def do_login_clockify():
    pyautogui.sleep(1)
    pyautogui.press('tab', presses=4)
    pyautogui.press('enter')
    loading_screen('clockify_login')
    button_location = pyautogui.locateOnScreen('images/login_google_clockify.png', confidence=0.80)
    button_location_center = pyautogui.center(button_location)
    if button_location_center:
        pyautogui.sleep(2)
        pyautogui.click(button_location_center.x, button_location_center.y)
        pyautogui.sleep(1.5)
        loading_screen('another_google_account_clockify')
        button_another_account = pyautogui.locateOnScreen('images/another_google_account_clockify.png', confidence=0.80)
        button_another_account_center = pyautogui.center(button_another_account)
        pyautogui.click(button_another_account_center.x, button_another_account_center.y)
        pyautogui.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.keyUp('ctrl')
        email = get_email()
        pyautogui.typewrite(email)
        pyautogui.press('enter')
        pyautogui.sleep(2)
        pwd = get_clockify_pwd()
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.keyUp('ctrl')
        pyautogui.typewrite(pwd)
        pyautogui.press('enter')



#LER EXCEL

#IMPORTAR CADA LINHA UTILIZANDO A LÓGICA DOS TABS

#1: DESCRIPTION

#2: PROJECT

#3: TAGS

#4: START TIME

#5: END TIME

#6 DATE

#7: CLICK ADD

def run():
    access_browser_clockify()
    do_login_clockify()
