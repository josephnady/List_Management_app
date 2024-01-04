import time
from Model.Deactivator import Deactivate,Deactivate_sync
from Model.Activator import Activate,Activate_listmanagment,Activate_Pool_Phase1
from Controller.id_manip import Activation_id_manip
from Controller.id_manip import Dectivation_id_manip
from Controller.id_manip import Act_Deact_id_manip
from utils import Utils as u
from multiprocessing import Pool
from View.deactiv_gui import DeactGUI as d
from selenium.webdriver.common.by import By

def main_Deactivate():
    Deactive_list = Dectivation_id_manip()
    line_terr_inputs = d.deact_gui()
    lininput = line_terr_inputs[0]
    terinput = line_terr_inputs[1]

    Deactivate(Deactive_list,lininput,terinput)

def main_Activate2(c,list):
        cores = int(c)
        p = Pool(cores)
        bulk_Ids_count = 0
        endpoint = len(list)
        while bulk_Ids_count <= endpoint+1:
            bulk_Ids = []
            for i, id in enumerate(list,1):
                bulk_Ids.append(id)
                if ((i % 10 == 0)|(list[-1]==id)):
                    ask = input(f"\n{bulk_Ids_count} Ids have been opened, Do you Want to continue? (y/n) ").lower()
                    if ask == 'y':
                        u.close_edge_browser()
                        break
                    elif input(f"\nDo you want to go to Deactivation ? (y/n) ").lower() =='y':
                        u.close_edge_browser()
                        return                                    
            
            p.map(Activate, bulk_Ids)
            bulk_Ids_count += i
            list = [item for item in list if item not in bulk_Ids]
            print(f"Next Ids to be activated {f'{list}':*>30}")
        
        p.close()
        p.join()


def main_Activate(c):
    cores = int(c)
    p = Pool(cores)
    
    ActivationIDs = Activation_id_manip()
    Active_Ids_count = len(ActivationIDs)
    bulk_Ids_count = 0
    while bulk_Ids_count <= Active_Ids_count:
        bulk_Ids = []
        # print("before for loop")
        for i, id in enumerate(ActivationIDs,1):
            print(f"{i} - {id}")
            bulk_Ids.append(id)
            if ((i % 5 == 0)|(ActivationIDs[-1]==id)):
                ask = input(f"\n{bulk_Ids_count} Ids have been opened, Do you Want to continue? (y/n) ").lower()
                if ask == 'y':
                    u.close_edge_browser()
                    break
                else:
                    ask2 = input(f"\nAre you Sure you want to Quit? (y/n) ").lower()
                    if ask2 != 'y':
                        return
                    return            
                
        # print("After for loop")
        p.map(Activate, bulk_Ids)
        bulk_Ids_count += i
        print(bulk_Ids_count)
        # print(f"Act IDs before assignement{len(ActivationIDs)}")
        ActivationIDs = [item for item in ActivationIDs if item not in bulk_Ids]
        # print(f"Act IDs After assignement{len(ActivationIDs)}")
        print(f"Next Ids to be activated {f'{ActivationIDs}':*>30}")


    p.close()
    p.join()

def main_Activate_sync(activelist):
        ActivationIDs2 = activelist
        browser = u.open_refresh_without_close("http://newcrm.liptispharma.com:88/liptis/crm/index.php")
        browser.implicitly_wait(500)
        # ________________________________Login page_____________________________________
        browser.find_element('name', 'uname').send_keys("admin")
        # write the password
        browser.find_element('name', 'upass').send_keys("S_Admin2023")
        # choose the department
        browser.find_element('name', 'atype').send_keys('Administrator')
        # choose the page
        browser.find_element('name', 'page').send_keys('Message')
        # click on login button
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, 'button').click()

        # الكود ده عشان تفتح اكتر من تاب في وقت واحد  
        # Iterate through IDs
        if ActivationIDs2:
            for i, newID in enumerate(ActivationIDs2, 1):
                try:
                    # Open link in a new tab
                    
                    browser.execute_script(f"window.open('', '_blank');")
                    print(f">>>> Start activation of {newID}  <<<<<")
                    u.navigate_to(browser,newID)
                    browser.switch_to.window(browser.window_handles[-1])
                except IndexError:
                    print("Index Error")
                    # browser.switch_to.window(browser.window_handles[i])


                # If 10 links have been opened, prompt user to continue
                if ((i % 10 == 0) | (ActivationIDs2[-1] == newID)):
                    # print(f"is ActivationIDs2[-1] == i?? {ActivationIDs2[-1] == newID}")
                    for window_handle in browser.window_handles:
                        browser.switch_to.window(window_handle)
                        if browser.current_url != 'about:blank':
                            # print(browser.find_element(By.XPATH,'//*[@id="rightlist"]/table/tbody/tr[4]').text)
                            browser.find_element(By.XPATH,'//*[@id="rightlist"]/table/tbody/tr[4]').click()

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
        else:
            browser.execute_script(f"window.open('', '_blank');")
            browser.switch_to.window(browser.window_handles[-1])   
            print("There is no Ids to be actived...Directing to Deactivation")


def main_Act_Deact(c):
    line_terr_inputs = d.deact_gui()
    lininput = line_terr_inputs[0]
    terinput = line_terr_inputs[1]
    
    results = Act_Deact_id_manip()
    # print(len(results))
    DeactIDs= results[0]
    ActIDs= results[1]
    IDs_to_be_actived = ActIDs
    
    if len(ActIDs) == 0:
        print("The Activation List equal 0\nDirecting to Deactivation .....")
    else:
        Not_Exist_list = Activate_Pool_Phase1(IDs_to_be_actived,lininput,terinput)
        
        print(f"Main function -> Deactive IDs {len(DeactIDs)}:\n\
        \nMain Function -> Activate IDs:{len(Not_Exist_list)}\n")
        
        if len(Not_Exist_list) == 0:
            print("The Activation \'Not Exist_list\' List equal 0\nDirecting to Deactivation .....")
        else:
            main_Activate2(c,Not_Exist_list)

    if input(f"\nDo you want to go to Deactivation ? (y/n) ").lower() =='y':
        u.close_edge_browser()
    else:
        u.close_edge_browser()
        return                                            
    # close_edge_browser()
    print(f"{' <><><><><><><><> ':*^60}")
    print(f"{'  Activation has been finished  ':*^60}")
    print(f"{' <><><><><><><><> ':*^60}")
    print("\n\n")
    print(f"{'  Start Deactivation  ':*^60}")
    Deactivate(DeactIDs,lininput,terinput)


def main_Act_Deact_sync():
    line_terr_inputs = d.deact_gui()
    lininput = line_terr_inputs[0]
    terinput = line_terr_inputs[1]

    # idenify the activation and deactivation lists
    results = Act_Deact_id_manip()
    print(len(results))
    DeactIDs= results[0]
    ActIDs= results[1]
    # print(f"Main function -> Deactive IDs {len(DeactIDs)}:\n\
    #       \nMain Function -> Activate IDs:{len(ActIDs)}\n")
    if input("******* DO YOU WANT TO START ACTIVATION ? (y/n) **********").lower() == "y":
        Activate_listmanagment(ActIDs,lininput,terinput)
        # close_edge_browser()

        print(f"{' <><><><><><><><> ':*^60}")
        print(f"{'  Activation has been finished  ':*^60}")
        print(f"{' <><><><><><><><> ':*^60}")
        print("\n\n")
        print(f"{'  Start Deactivation  ':*^60}")
        print("\n\n")
    
    Deactivate_sync(DeactIDs,lininput,terinput)

