from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import time

# inisialisasi opsi
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chrome_options.add_argument("--headless")
chrome_service = Service(r".E:\Skripsi\Scrap_Twiter\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://twitter.com/login")

username = driver.find_element(By.NAME, "session[username_or_email]")
username.send_keys("your_username")

password = driver.find_element(By.NAME, "session[password]")
password.send_keys("your_password")

login = driver.find_element(By.XPATH, "//div[@data-testid='LoginForm_Login_Button']/div")
login.click()



# klik tombol login
login_button = driver.find_element_by_xpath('//div[@data-testid="LoginForm_Login_Button"]/div')
login_button.click()

# tunggu proses login selesai
time.sleep(5)

# masukkan keyword pencarian
search_box = driver.find_element_by_xpath('//input[@data-testid="SearchBox_Search_Input"]')
search_box.send_keys("presiden 2024")
search_box.submit()

# tunggu hasil pencarian selesai dimuat
time.sleep(5)

# scroll halaman hingga seluruh tweet ter-load
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# ambil seluruh tweet yang ada pada halaman
tweets = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')

# tulis setiap tweet ke dalam file CSV
with open('hasil_tweet.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)

    for tweet in tweets:
        writer.writerow([tweet.text])

# tutup webdriver
driver.quit()
