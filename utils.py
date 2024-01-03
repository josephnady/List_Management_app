import subprocess
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import psutil


class Utils():
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
