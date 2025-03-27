
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import smtplib
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage
from email.mime.multipart import MIMEMultipart
import time

sender_email="exampleemail@gmail.com"
receiver_email="youremail@gmail.com"
password_for_email="yourpassword"

chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=webdriver.Chrome()
driver.get("https://portal.nts.org.pk/login")
cnic=driver.find_element(By.CSS_SELECTOR, "input[type='text']")
cnic.click()
cnic.send_keys("your_cnic")

password=driver.find_element(By.CSS_SELECTOR,"input[type='password']")
password.click()
password.send_keys("your_password")

submit=driver.find_element(By.CSS_SELECTOR,"button[type='submit'], input[type='submit']")
submit.click()

bar=driver.find_element(By.XPATH,"//*[@id='navbar-mobile']/div/ul[1]/li/a")
bar.click()

locator=driver.find_element(By.XPATH,"//*[@id='main-menu-navigation']/li[5]")
open_application = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(locator))
open_application.click()


parent_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "accordionWrapar2"))
)

child_elements = parent_element.find_elements(By.CLASS_NAME, "card.collapse-header.bg-light")

data = [child.text for child in child_elements]
print("Extracted Data:", data)
nat="National Aptitude Test (NAT 2025-IV)"

if nat in data:
    message=MIMEMultipart()
    message["To"]=receiver_email
    message["From"]=sender_email
    message["Subject"]="Nat Application Open"

    body="It's time to apply to hurry up and open the NTS portal for applications."
    message.attach(MIMEText(body,"plain"))
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email,password_for_email)
            text=message.as_string()
            server.sendmail(sender_email,receiver_email,text)
            print("Email Sent Succesfully")
    except Exception as e:
        print(f"Error ending message :{e}")
     

time.sleep(60)
driver.close()

