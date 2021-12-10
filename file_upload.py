from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.plupload.com/examples")
element=driver.find_element(By.XPATH, "//div[@id='uploader_buttons']/div/input")
element.send_keys("/home/kali/Pentest/Task 1/File_Uploader/upload_image.png")
