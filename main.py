import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
import json


def get_driver(driver_path,target_url):
    
    os.environ['PATH'] += driver_path
    
    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True)
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(target_url)

    return driver


def login(driver,username,password,button_path):
    # Enter username and password
    driver.find_element(By.ID, 'id_username').send_keys(username)
    driver.find_element(By.ID, 'id_password').send_keys(password)
    
    # Click the login button
    login_button = driver.find_element(By.XPATH, button_path)
    login_button.click()
    

def go_to_home(driver,home_path):       
    # Click the home link
    home_link = driver.find_element(By.XPATH, home_path)
    home_link.click()


def get_temperature(driver,temperature_element_path): 
    # Get the temperature
    temperature_element = driver.find_element(By.XPATH, temperature_element_path)
    
    return temperature_element


def clean_text(text):
    # Extract only the temperature
    output = float(text.split(': ')[1])
    return output


def write_in_file(temperature_element,directory):
        
        # Clean text
        cleansed_text = clean_text(temperature_element.text)
        
        now = datetime.now()
        path_to_file = directory + str(now.strftime('%Y-%m-%d-%H-%M-%S')) + '.txt'
        
        with open(path_to_file, 'w') as f:
            f.write(str(cleansed_text))
            

def get_json_data(json_file_path):

    f = open(json_file_path)
    data = json.load(f)

    return data


def main():
    # Get json data containing username, password, url
    data = get_json_data('login-then-scrape-temperature/info.json')
    
    # Get Google Chrome Driver
    driver = get_driver(data['driver_path'],data['target_url'])
    
    # Login
    username = data['username']
    password = data['password']
    button_path = data['button_path']
    login(driver,username,password,button_path)
    
    # Go to the Home Page
    home_path = data['home_path']
    go_to_home(driver,home_path)
    
    # # Get the temperature
    for i in range (5):
        time.sleep(2)
        temperature_element_path = data['temperature_element_path']
        temperature_element = get_temperature(driver,temperature_element_path)
        
        # Clean the return value
        cleansed_text = clean_text(temperature_element.text)
        
        # Create text file then write the temperature
        directory = data['save_file_here']
        write_in_file(temperature_element,directory)

    return cleansed_text


main()