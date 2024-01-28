import os
import psutil
import subprocess
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException



class Utils:
    '''
    ## Static func that help in the project
    '''
    def __init__(self):
        pass

    @staticmethod
    def flush_dns():
        try:
            # Run the ipconfig /flushdns command
            subprocess.run(['ipconfig', '/flushdns'], check=True)
            print("DNS cache flushed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error flushing DNS cache: {e}")

    # for testing
    @staticmethod
    def print_ids_bulk(id):
        print(id)


    @staticmethod
    def cpu_count():
        cpu_count = os.cpu_count()
        return(int(cpu_count))
    
    @staticmethod
    def close_edge_browser():
        # Get a list of all running processes
        all_processes = psutil.process_iter(['pid', 'name'])

        # Define the name of the Edge browser process
        edge_browser_name = 'msedge.exe'

        # Iterate through the processes and terminate Edge browser processes
        for process in all_processes:
            if process.info['name'].lower() == edge_browser_name:
                try:
                    # Create a Process object for the Edge browser process
                    edge_process = psutil.Process(process.info['pid'])

                    # Terminate the Edge browser process
                    edge_process.terminate()

                    print(f"Terminated Edge browser process with PID {process.info['pid']}")

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # Handle exceptions if the process cannot be terminated
                    print(f"Failed to terminate Edge browser process with PID {process.info['pid']}")
    
    @staticmethod
    def open_and_refresh_page(url, max_attempts=3):
        attempts = 0

        while attempts < max_attempts:
            run = webdriver.EdgeOptions()
            run.add_experimental_option('detach', True)
            run.add_experimental_option('excludeSwitches', ['enable-logging'])
            browser = webdriver.Edge(options=run)

            try:
                # Open the URL
                browser.get(url)

                # You can add additional wait conditions if needed
                WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located(('name','uname'))
                )

                # If the page loads successfully, break out of the loop
                break

            except Exception as e:
                # print(f"Error: {str(e)}")
                print(f"Error: {e}")
                attempts += 1

                browser.close()
                # Refresh the page and retry
                print("Refreshing the page...")
                continue
        return browser


    @staticmethod
    def open_refresh_without_close(url, max_attempts=3):
        attempts = 0

        while attempts < max_attempts:
            run = webdriver.EdgeOptions()
            run.add_experimental_option('detach', True)
            run.add_experimental_option('excludeSwitches', ['enable-logging'])
            browser = webdriver.Edge(options=run)

            try:
                # Open the URL
                browser.get(url)

                # You can add additional wait conditions if needed
                WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located(('name','uname'))
                )

                # If the page loads successfully, break out of the loop
                break

            except Exception as e:
                # print(f"Error: {str(e)}")
                print(f"Error: {e}")
                attempts += 1

                browser.refresh()
                # Refresh the page and retry
                print("Refreshing the page...")
                continue
        return browser
    
    @staticmethod
    def navigate_to_clinic(browser,id):

        attempts = 0
        max_attempts = 3

        while attempts < max_attempts:
            try:
                # Open the URL
                browser.get( "http://newcrm.liptispharma.com:88/liptis/crm/clinic.php?lang=")
                
                # You can add additional wait conditions if needed
                WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                     '//*[@id="right"]/table[1]/tbody/tr[2]/td/form/table/tbody/tr[1]/td[2]/input'))
                )

                # If the page loads successfully, break out of the loop
                break

            except Exception as e:
                # print(f"Error: {str(e)}")
                print(f"Error: {e}")
                attempts += 1

                browser.refresh()
                # Refresh the page and retry
                print("Refreshing the page...")
                continue
            
        id_box = browser.find_element(
        By.XPATH, '//*[@id="right"]/table[1]/tbody/tr[2]/td/form/table/tbody/tr[1]/td[2]/input')
        id_box.send_keys(id)

        search_btn = browser.find_element(
            By.XPATH, '//*[@id="right"]/table[1]/tbody/tr[2]/td/form/table/tbody/tr[5]/td/img')
        search_btn.click()

    @staticmethod
    def navigate_to_am(browser,id):
        attempts = 0
        max_attempts = 3
        while attempts < max_attempts:
            try:
                # Open the URL
                browser.get(
                    "http://newcrm.liptispharma.com:88/liptis/crm/hospitals.php?lang=")

                # You can add additional wait conditions if needed
                WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                     '//*[@id="right"]/table[1]/tbody/tr[2]/td/form/table/tbody/tr[1]/td[2]/input')))
                # If the page loads successfully, break out of the loop
                break
            except Exception as e:
                # print(f"Error: {str(e)}")
                print(f"Error: {e}")
                attempts += 1
                browser.refresh()
                # Refresh the page and retry
                print("Refreshing the page...")
                continue
        id_box = browser.find_element(
        By.XPATH, '//*[@id="right"]/table[1]/tbody/tr[2]/td/form/table/tbody/tr[1]/td[2]/input')
        id_box.send_keys(id)

        search_btn = browser.find_element(
        By.XPATH, '//*[@id="right"]/table[1]/tbody/tr[2]/td/form/table/tbody/tr[5]/td/img')
        search_btn.click()
        try:
            errors = [NoSuchElementException, ElementNotInteractableException,TimeoutException]
            clinic = WebDriverWait(driver=browser, timeout=2, ignored_exceptions=errors).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="rightlist"]/table/tbody/tr[4]')))
            # print(clinic)
        except TimeoutException as e:
            return (id)

        
    @staticmethod
    def waitforclinic(browser):
        attempts = 0
        max_attempts = 3

        while attempts < max_attempts:
            try:
                WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,
                                                                               '//*[@id="new"]/form/table/tbody/tr[1]/td/fieldset/table'))                                                                 )
            except Exception as e:
                # print(f"Error: {str(e)}")
                # print(f"Error: {e}")
                attempts += 1

                browser.refresh()
                # Refresh the page and retry
                print("Refreshing the page...")
                continue

    @staticmethod
    def save_report(list,terrname,type:int):
        '''type: 1 for activation 2 for deactivation'''
        if type == 1:
            ActivedIDsDF = pd.DataFrame({
                "Actived IDs": list})
            print(
                f"data frame :\n {ActivedIDsDF}\nNo. of IDs that not found in crm is : {len(ActivedIDsDF)}\n")
            reportdirectory = f"{str(os.getcwd())}\Report"
            export_path = f"{str(os.getcwd())}\Report\{terrname}_Activation.xlsx"
            if os.path.isdir(reportdirectory) == False:
                os.mkdir(reportdirectory)
            else:
                ActivedIDsDF.to_excel(export_path, index=False)
            print(f"\nReport Saved in\n{export_path}\n")
        elif type == 2:
                # Save the report
            DeactivatedIDsDF = pd.DataFrame({
                "Deactivated IDs": list})
            print(
                f"data frame :\n {DeactivatedIDsDF}\nNo. of IDs that not found in crm is : {len(DeactivatedIDsDF)}\n")
            reportdirectory = f"{str(os.getcwd())}\Report"
            export_path = f"{str(os.getcwd())}\Report\{terrname}_Deactivation.xlsx"
            if os.path.isdir(reportdirectory) == False:
                os.mkdir(reportdirectory)
            else:
                DeactivatedIDsDF.to_excel(export_path, index=False)
            print(f"\nReport Saved in\n{export_path}\n")
        else:
            print("kindly choose the type and check for the arguments")
