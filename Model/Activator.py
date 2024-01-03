from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from utils import Utils as u

def Activate(id):
    print(f"{f'Start Activating ID {id}':*^40}")
    # Go to the target website
    browser = u.open_and_refresh_page("http://newcrm.liptispharma.com:88/liptis/crm/index.php")
    # ________________________________Login page_____________________________________
    browser.find_element('name', 'uname').send_keys("admin")
    browser.find_element('name', 'upass').send_keys("S_Admin2023")
    browser.find_element('name', 'atype').send_keys('admin')
    browser.find_element('name', 'page').send_keys('Message')
    browser.find_element(By.CLASS_NAME, 'button').click()

    # navigate to IDs
    browser.get(
        "http://newcrm.liptispharma.com:88/liptis/crm/clinic.php?lang=")

    id_box = browser.find_element(
        By.XPATH, '//*[@id="right"]/table[1]/tbody/tr[2]/td/form/table/tbody/tr[1]/td[2]/input')
    id_box.send_keys(id)

    search_btn = browser.find_element(
        By.XPATH, '//*[@id="right"]/table[1]/tbody/tr[2]/td/form/table/tbody/tr[5]/td/img')
    search_btn.click()
    errors = [NoSuchElementException, ElementNotInteractableException]
    clinic = WebDriverWait(driver=browser, timeout=10, ignored_exceptions=errors).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="rightlist"]/table/tbody/tr[4]')))
    clinic.click()

