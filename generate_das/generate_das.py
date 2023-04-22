import pyautogui
from datetime import datetime
from helpers.utils import close_tab
from helpers.utils import loading_screen
from helpers.utils import getCnpj
from helpers.utils import getAuto
from helpers.utils import getMonth
from helpers.utils import getYear
from helpers.utils import calculateNumTabPresses
from helpers.utils import open_receita_website


cnpj = getCnpj()
auto = getAuto()
month = auto if getMonth() else 0
year = auto if getYear() else 0
actual_month = datetime.now().month
actual_year = datetime.now().year

# ACESSAR NAVEGADOR
open_receita_website()
loading_screen('login')
pyautogui.typewrite(cnpj)

# LOGIN
pyautogui.press('tab', presses=3)
pyautogui.press('enter')

# CLICK EMITIR GUIA
loading_screen('home')
pyautogui.press('tab', presses=2)
pyautogui.press('enter')

# CLICK SELECT ANO
loading_screen('screen_year')
pyautogui.press('tab', presses=6)
pyautogui.press('enter')

# CLICK YEAR VALUE
if not auto & year:
    actual_year = year
else:
    if actual_month == 1:
        actual_year = actual_year - 1

pyautogui.sleep(0.3)
positionYear = {
    2022: pyautogui.locateCenterOnScreen('images/2022.png', confidence=0.95),
    2023: pyautogui.locateCenterOnScreen('images/2023.png', confidence=0.95),
    2024: pyautogui.locateCenterOnScreen('images/2024.png', confidence=0.95),
    2025: pyautogui.locateCenterOnScreen('images/2025.png', confidence=0.95),
    2026: pyautogui.locateCenterOnScreen('images/2026.png', confidence=0.95),
}

pyautogui.click(positionYear[actual_year].x, positionYear[actual_year].y)
pyautogui.sleep(1)

# CLICK SUBMIT
pyautogui.press('tab')
pyautogui.press('enter')

# CLICK CHECKBOX MONTH
loading_screen('component_header_month')

# Calculando o número de pressionamentos de tecla TAB necessários
num_tab_presses = calculateNumTabPresses(actual_month)

# Pressionando a tecla TAB o número de vezes necessário
pyautogui.press('tab', num_tab_presses)

# Clicando no checkbox do mês anterior
pyautogui.press('space')

# CLICK GENERATE DAS
pyautogui.press('pgdn')
loading_screen('btn_generate_das')
generate_das = pyautogui.locateCenterOnScreen('images/btn_generate_das.png', confidence=0.95)
pyautogui.click(generate_das.x, generate_das.y)

# BAIXAR PDF
loading_screen('component_modal_success', "component_modal_warning")
pyautogui.press('tab', presses=6)
pyautogui.press('enter')
close_tab()
