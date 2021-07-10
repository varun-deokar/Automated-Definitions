from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

word = input("Enter word")
driver = webdriver.Chrome()  # Opens the homepage using Google Chrome
driver.get("https://www.google.com/")
sleep(2)

driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(word + " meaning")
driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.RETURN)
sleep(1)
meaning = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/span/div/div/div[3]/div/div[4]/div[1]/div/ol/li/div/div/div[1]/div/div/div[1]/span")
print(meaning.text)

while True:
    word = input("Enter word")
    driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.dRYYxd > div.clear-button.XoaYSb > span.lBbtTb.z1asCe.rzyADb > svg > path").click()
    driver.find_element_by_xpath("/html/body/div[3]/form/div[2]/div[1]/div[2]/div/div[2]/input").send_keys(word + " meaning")
    driver.find_element_by_xpath("/html/body/div[3]/form/div[2]/div[1]/div[2]/div/div[2]/input").send_keys(Keys.RETURN)
    meaning = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/span/div/div/div[3]/div/div[4]/div[1]/div/ol/li/div/div/div[1]/div/div/div[1]/span")
    print(meaning.text)