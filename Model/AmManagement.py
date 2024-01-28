from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException,TimeoutException
import time
from utils import Utils as u

def am_management(data):
    print(f"Start Am Account managment")
    # Go to the target website
    browser = u.open_and_refresh_page("http://newcrm.liptispharma.com:88/liptis/crm/index.php")
    # ________________________________Login page_____________________________________
    browser.find_element('name', 'uname').send_keys("admin")
    browser.find_element('name', 'upass').send_keys("S_Admin2023")
    browser.find_element('name', 'atype').send_keys('admin')
    browser.find_element('name', 'page').send_keys('Message')
    browser.find_element(By.CLASS_NAME, 'button').click()

    not_found_ids_list =[]
    # unpack each element in data
    for i , record in enumerate(data,1):
        unpack_data = list(zip(record))
        am_id,am_name,am_brick = unpack_data[:][0],unpack_data[:][1],unpack_data[:][2]
        # print(f"id: {am_id}, name: {am_name}, brick: {am_brick}")
        try:
            # Open link in a new tab
            browser.execute_script(f"window.open('', '_blank');")
            print(f">>>> Navigating to account:\nid: {am_id}, name: {am_name}, brick: {am_brick}<<<<<\n")
            id = u.navigate_to_am(browser,am_id)
            if id:
                not_found_ids_list.append(am_id)
            browser.switch_to.window(browser.window_handles[-1])
        except IndexError:
            print("Index Error")
        
        if ((i % 10 == 0) | (data[-1] == record)):
            for window_handle in browser.window_handles:
                browser.switch_to.window(window_handle)
                if browser.current_url != 'about:blank':
                    try:
                        clinic = browser.find_element(By.XPATH, '//*[@id="rightlist"]/table/tbody/tr[4]')
                    except Exception as _:
                        # not_found_ids_list.append(am_id)
                        continue
                    clinic.click()

            # u.waitforclinic(browser)

            # prompt user to contiue    
            user_input = input(f"{i} links opened. Do you want to continue? (y/n): ").lower()
            # if user input wasn't 'y' so exit all the opened tab except blank one and go to the deactivation process
            if user_input != 'y':
                # confirm closing
                user_input2 = input(f"Are you sure you want to close? (y/n): ").lower()
                if user_input2 == 'y':
                    # break the for parent for loop and go to the deactivation
                    break
            # if the user write y to continue >> close all opened tabs except blank one
            for window_handle in browser.window_handles:
                browser.switch_to.window(window_handle)
                if browser.current_url != 'about:blank':
                    browser.close()
    print(f"Not found Ids are:\n{not_found_ids_list}")
