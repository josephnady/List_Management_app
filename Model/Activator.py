from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time
from utils import Utils as u

def Activate_Pool_Phase1(ActivationID,lin,terr):
    # variables
    LineInputvar = str(lin).strip()
    TerrInputvar = str(terr).strip()
    print(
        f"\nyour inputs are: \nLine: {LineInputvar}\nTerritory: {TerrInputvar}\n")
    # ______________________Process Started________________________________________
    # InOrder to calculate the process duraion.
    start_time1 = time.time()

    # This Function create list from droplist to exclude the first blank option
    def itemlist(x):
        xSelector = Select(x)
        all_x = xSelector.options
        x_list = []
        for x in all_x:
            if x.text == "":
                continue
            x_list.append(x.text)
        # print(f"{len(x_list)}\n{x_list}")

    print(">>>>>>>>>>>><><><<<<<<<<<<<\nWELCOME   TO   JOSEPH   BOT\nDeveloped By Dr. Joseph Nady\n>>>>>>>>>>>><><><<<<<<<<<<<")
    print("\n1-Phase one -> Activation from list managment settings report\n")

    # ________________________________Login page_____________________________________
    # Go to the target website
    browser = u.open_refresh_without_close(
        "http://newcrm.liptispharma.com:88/liptis/crm/index.php")
    # browser.get("http://newcrm.liptispharma.com:88/liptis/crm/index.php")
    time.sleep(.5)
    browser.find_element('name', 'uname').send_keys("admin")
    # write the password
    browser.find_element('name', 'upass').send_keys("S_Admin2023")
    # choose the department
    browser.find_element('name', 'atype').send_keys('admin')
    # choose the page
    browser.find_element('name', 'page').send_keys('Message')
    time.sleep(.5)
    # click on login button
    browser.find_element(By.CLASS_NAME, 'button').click()
    # ____________________________________let's Go _____________________________________
    browser.get(
        "http://newcrm.liptispharma.com:88/liptis/crm/setting_list_management_search.php?lang=")
    teamdrp = browser.find_element(
        By.XPATH, '/html/body/table/tbody/tr[4]/th/center/fieldset/form/table/tbody/tr[1]/td[2]/select')
    territorydrp = browser.find_element(By.ID, 'tdivlist')
    # Account Type
    pharmacy_Chk_bx = browser.find_element(
        By.XPATH, '/html/body/table/tbody/tr[4]/th/center/fieldset/form/table/tbody/tr[3]/td[2]/div/table/tbody/tr/td[2]/input')
    am_Chk_bx = browser.find_element(
        By.XPATH, '/html/body/table/tbody/tr[4]/th/center/fieldset/form/table/tbody/tr[3]/td[2]/div/table/tbody/tr/td[3]/input')
    # Active
    status = browser.find_element(
        By.XPATH, '/html/body/table/tbody/tr[4]/th/center/fieldset/form/table/tbody/tr[5]/td[2]/select')
    # search button
    search_btn = browser.find_element(
        By.XPATH, '/html/body/table/tbody/tr[4]/th/center/fieldset/form/table/tbody/tr[6]/th/input')
    # \\\\\\\\\\\\\\\\selecting the line and terr and search/////////////
    teamdrp.click()
    itemlist(teamdrp)
    teamdrp.send_keys(LineInputvar)
    teamdrp.click()
    time.sleep(1)
    territorydrp.click()
    itemlist(territorydrp)
    territorydrp.send_keys(TerrInputvar)
    time.sleep(.5)
    pharmacy_Chk_bx.click()
    am_Chk_bx.click()
    status.send_keys("All")
    time.sleep(.5)
    print(LineInputvar, TerrInputvar)
    search_btn.click()
    # speak(f"Process started")

    # هنا هيقري كل الصفوف اللي في الجدول اللي جواه الليسته الخاصة بالمندوب
    clinic_teams_table_rows = browser.find_elements(
        By.XPATH, '/html/body/table/tbody/tr[4]/th/form/table/tbody/tr[3]/td/table/tbody/tr')
    
    trNo = 2
    CrmIdList = []
    print("\nStay Calm While reading the CRM data........\n")
    for tr in clinic_teams_table_rows:
        trNo += 1
        checkbox = browser.find_element(
            By.XPATH, f'/html/body/table/tbody/tr[4]/th/form/table/tbody/tr[3]/td/table/tbody/tr[{str(trNo)}]/td[1]/input')
        DrId = browser.find_element(
            By.XPATH, f'/html/body/table/tbody/tr[4]/th/form/table/tbody/tr[3]/td/table/tbody/tr[{str(trNo)}]/td[3]')
        CrmIdList.append(DrId.text)
        if trNo >= len(clinic_teams_table_rows):
            break

    print(f"length of \"ALL\" list are {len(CrmIdList)}")

    Not_Exist_list = []
    for id in ActivationID:
        if id in CrmIdList:
            # print(f" {id} exist and its index is {CrmIdList.index(id)}.")
            rowindex = int(CrmIdList.index(id))
            rownumber = rowindex + 3
            checkbox = browser.find_element(
                By.XPATH, f'/html/body/table/tbody/tr[4]/th/form/table/tbody/tr[3]/td/table/tbody/tr[{str(rownumber)}]/td[1]/input')
            checkbox.click()
            # browser.find_element(By.XPATH, "/html/body").click()
        else:
            # print(f"the id {id} is not found")
            Not_Exist_list.append(id)
    '''
    Start Activation from setting clinic for
    the Ids that need to be actived but not
    exist is the all list pool of the employee
    '''
    print(
    f'''
    IDs that not found in Ids pool
    and will be actived are '{len(Not_Exist_list)}'
    {Not_Exist_list}
    ''')
    
    print("2-Phase 2 Activation from clinic settings")
    
    # ______________________Process Finished_______________________________________
    # Calculate the process time
    print(f"{'  Activation has been finished  ':*^60}")
    print("Process Duration is:\n\n")
    print("-------- %s seconds --------" %
          round((time.time() - start_time1), 2))
    print("\n\n")
    # Save the report
    u.save_report(ActivationID,TerrInputvar,1)
    return Not_Exist_list

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


def Activate_listmanagment(ActivationID,lin,terr):
    # variables
    LineInputvar = str(lin).strip()
    TerrInputvar = str(terr).strip()
    print(
        f"\nyour inputs are: \nLine: {LineInputvar}\nTerritory: {TerrInputvar}\n")
    # ______________________Process Started________________________________________
    # InOrder to calculate the process duraion.
    start_time1 = time.time()

    # This Function create list from droplist to exclude the first blank option
    def itemlist(x):
        xSelector = Select(x)
        all_x = xSelector.options
        x_list = []
        for x in all_x:
            if x.text == "":
                continue
            x_list.append(x.text)
        # print(f"{len(x_list)}\n{x_list}")

    print(">>>>>>>>>>>><><><<<<<<<<<<<\nWELCOME   TO   JOSEPH   BOT\nDeveloped By Dr. Joseph Nady\n>>>>>>>>>>>><><><<<<<<<<<<<")
    print("\n1-Phase one -> Activation from list managment settings report\n")

    # ________________________________Login page_____________________________________
    # Go to the target website
    browser = u.open_refresh_without_close(
        "http://newcrm.liptispharma.com:88/liptis/crm/index.php")
    # browser.get("http://newcrm.liptispharma.com:88/liptis/crm/index.php")
    time.sleep(.5)
    browser.find_element('name', 'uname').send_keys("admin")
    # write the password
    browser.find_element('name', 'upass').send_keys("S_Admin2023")
    # choose the department
    browser.find_element('name', 'atype').send_keys('admin')
    # choose the page
    browser.find_element('name', 'page').send_keys('Message')
    time.sleep(.5)
    # click on login button
    browser.find_element(By.CLASS_NAME, 'button').click()
    # ____________________________________let's Go _____________________________________
    browser.get(
        "http://newcrm.liptispharma.com:88/liptis/crm/setting_list_management_search.php?lang=")
    teamdrp = browser.find_element(
        By.XPATH, '/html/body/table/tbody/tr[4]/th/center/fieldset/form/table/tbody/tr[1]/td[2]/select')
    territorydrp = browser.find_element(By.ID, 'tdivlist')
    # Account Type
    pharmacy_Chk_bx = browser.find_element(
        By.XPATH, '/html/body/table/tbody/tr[4]/th/center/fieldset/form/table/tbody/tr[3]/td[2]/div/table/tbody/tr/td[2]/input')
    am_Chk_bx = browser.find_element(
        By.XPATH, '/html/body/table/tbody/tr[4]/th/center/fieldset/form/table/tbody/tr[3]/td[2]/div/table/tbody/tr/td[3]/input')
    # Active
    status = browser.find_element(
        By.XPATH, '/html/body/table/tbody/tr[4]/th/center/fieldset/form/table/tbody/tr[5]/td[2]/select')
    # search button
    search_btn = browser.find_element(
        By.XPATH, '/html/body/table/tbody/tr[4]/th/center/fieldset/form/table/tbody/tr[6]/th/input')
    # \\\\\\\\\\\\\\\\selecting the line and terr and search/////////////
    teamdrp.click()
    itemlist(teamdrp)
    teamdrp.send_keys(LineInputvar)
    teamdrp.click()
    time.sleep(1)
    territorydrp.click()
    itemlist(territorydrp)
    territorydrp.send_keys(TerrInputvar)
    time.sleep(.5)
    pharmacy_Chk_bx.click()
    am_Chk_bx.click()
    status.send_keys("All")
    time.sleep(.5)
    print(LineInputvar, TerrInputvar)
    search_btn.click()
    # speak(f"Process started")

    # هنا هيقري كل الصفوف اللي في الجدول اللي جواه الليسته الخاصة بالمندوب
    clinic_teams_table_rows = browser.find_elements(
        By.XPATH, '/html/body/table/tbody/tr[4]/th/form/table/tbody/tr[3]/td/table/tbody/tr')
    
    trNo = 2
    CrmIdList = []
    print("\nStay Calm While reading the CRM data........\n")
    for tr in clinic_teams_table_rows:
        trNo += 1
        checkbox = browser.find_element(
            By.XPATH, f'/html/body/table/tbody/tr[4]/th/form/table/tbody/tr[3]/td/table/tbody/tr[{str(trNo)}]/td[1]/input')
        DrId = browser.find_element(
            By.XPATH, f'/html/body/table/tbody/tr[4]/th/form/table/tbody/tr[3]/td/table/tbody/tr[{str(trNo)}]/td[3]')
        CrmIdList.append(DrId.text)
        if trNo >= len(clinic_teams_table_rows):
            break

    print(f"length of \"ALL\" list are {len(CrmIdList)}")

    Not_Exist_list = []
    for id in ActivationID:
        if id in CrmIdList:
            # print(f" {id} exist and its index is {CrmIdList.index(id)}.")
            rowindex = int(CrmIdList.index(id))
            rownumber = rowindex + 3
            checkbox = browser.find_element(
                By.XPATH, f'/html/body/table/tbody/tr[4]/th/form/table/tbody/tr[3]/td/table/tbody/tr[{str(rownumber)}]/td[1]/input')
            checkbox.click()
            # browser.find_element(By.XPATH, "/html/body").click()
        else:
            # print(f"the id {id} is not found")
            Not_Exist_list.append(id)
    '''
    Start Activation from setting clinic for
    the Ids that need to be actived but not
    exist is the all list pool of the employee
    '''
    print(
    f'''
    IDs that not found in Ids pool
    and will be actived are '{len(Not_Exist_list)}'
    {Not_Exist_list}
    ''')
    
    from Controller.mainfiles import  main_Activate_sync
    print("2-Phase 2 Activation from clinic settings")

    main_Activate_sync(Not_Exist_list)

    # ______________________Process Finished_______________________________________
    # Calculate the process time
    print(f"{'  Activation has been finished  ':*^60}")
    print("Process Duration is:\n\n")
    print("-------- %s seconds --------" %
          round((time.time() - start_time1), 2))
    print("\n\n")
    # Save the report
    u.save_report(ActivationID,TerrInputvar,1)