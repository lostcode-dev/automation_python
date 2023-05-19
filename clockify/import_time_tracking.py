import pyautogui
from helpers.utils import open_browser
from helpers.utils import loading_screen
import pandas as pd
from helpers.utils import fill_login_clockify



#ABIR SITE DO CLOCKIFY
def access_browser_clockify():
    open_browser('https://clockify.me/')


#FAZER LOGIN
def do_login_clockify():
    pyautogui.sleep(2)
    pyautogui.press('tab', presses=4)
    pyautogui.press('enter')
    loading_screen('clockify_login')
    button_location = pyautogui.locateOnScreen('images/login_google_clockify.png', confidence=0.80)
    if button_location:
        pyautogui.sleep(2)
        button_location_center = pyautogui.center(button_location)
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
        fill_login_clockify()


def fill_description(description): # Necessário inserir tratamento de erro (demora do site após login) e verificar se está em timer(n) ou manual(m)
    pyautogui.sleep(0.8)
    pyautogui.typewrite(description)


def fill_project(project):
    pyautogui.sleep(0.5)
    click_project = pyautogui.locateOnScreen('images/clockify_project.png', confidence=0.80)
    click_project_center = pyautogui.center(click_project)
    pyautogui.click(click_project_center.x, click_project_center.y)
    pyautogui.sleep(0.5)
    pyautogui.typewrite(project)
    pyautogui.sleep(1)
    pyautogui.press('enter')


def fill_tag(tag):
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.typewrite(tag)
    pyautogui.sleep(0.5)
    tag_click = pyautogui.locateOnScreen('images/clockify_select_tag.png', confidence=0.75)
    tag_click_center = pyautogui.center(tag_click)
    pyautogui.click(tag_click_center.x, tag_click_center.y)


def fill_start_time(start_time):
    pyautogui.sleep(0.5)
    pyautogui.press('tab', presses=2)
    pyautogui.typewrite(start_time)


def fill_end_time(end_time):
    pyautogui.press('tab')
    pyautogui.typewrite(end_time)


def fill_date(day):
    pyautogui.press('tab', presses=3)
    pyautogui.typewrite(day.strftime('%d/%m/%Y'))


def click_bt_add():
    bt_add = pyautogui.locateOnScreen('images/clockify_add.png', confidence=0.80)
    pyautogui.click(bt_add)


#LER EXCEL
def fill_clockify_data():
    loading_screen('clockify_work_page')
    data_table = pd.read_excel('clockify/clockify_database.xlsx')
    day = data_table['DIA']
    description = data_table['DESCRIÇÃO']
    project = data_table['PROJETO']
    tag = data_table['TAGS']
    start_time = data_table['HORA INICIO']
    start_time = pd.to_datetime(start_time, format='%H:%M:%S').dt.strftime('%H%M')
    end_time = data_table['HORA FIM']
    end_time = pd.to_datetime(end_time, format='%H:%M:%S').dt.strftime('%H%M')

# IMPORTAR CADA LINHA UTILIZANDO A LÓGICA DOS TABS
    for d, desc, proj, t, start, end in zip(day, description, project, tag, start_time, end_time):
        fill_description(desc)
        fill_project(proj)
        fill_tag(t)
        fill_start_time(start)
        fill_end_time(end)
        fill_date(d)
        click_bt_add()


def run():
    access_browser_clockify()
    do_login_clockify()
    fill_clockify_data()
