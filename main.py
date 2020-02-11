from selenium import webdriver
from time import sleep

import json

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/app/Python36/chromedriver.exe')
    
    def login(self):
        self.driver.get("https://tinder.com/")
        sleep(5)

        # Login with facebook when the pop-up appears on the Tinder homepage
        facebook_login_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button/span')
        facebook_login_btn.click()

        # Switch from the main Tinder page into the facebook login pop-up that appears on screen in order to insert your email and password
        # Store the Tinder page into the 'tinder_window' in order to bring it back in focus later on
        tinder_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        # The credentials for the facebook login will be read from a JSON file
        with open("credentials.json") as json_file:
            credentials = json.load(json_file)
        
        # Fill in the form information for the email field
        email_form = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_form.send_keys(credentials['username'])

        # Fill in the form information for the password field
        password_form = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_form.send_keys(credentials['password'])
        
        # Click on the login button for the facebook pop-up window
        facebook_submit_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        facebook_submit_btn.click()

        # Bring back into focus the main window
        self.driver.switch_to_window(tinder_window)
        sleep(2)

        # Click on the button asking for permission to use your location
        allow_location_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_location_btn.click()

        # Click on the button asking for permission to send notifications
        allow_notifications_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_notifications_btn.click()

bot = Bot()
bot.login()