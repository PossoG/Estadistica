from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://datosmacro.expansion.com/comercio/balanza"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window() 

data = {'Country': [], 'Date': [], 'Exports': [], 'Imports': [], 'Trade balance' : [], 'Coverage rate': [], 'Balanza comercial %% GDP': [], 'Change': []}
  
boton = driver.find_element(By.ID, "didomi-notice-agree-button")
boton.click()

elements = driver.find_elements(By.CSS_SELECTOR, "#tb1 tbody > tr") 
for item in elements:
    
    data["Country"].append(item.find_element(By.CSS_SELECTOR, "td:nth-child(1) a").text)
    data["Date"].append(item.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text)
    data["Exports"].append(item.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text)
    data["Imports"].append(item.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text) 
    data["Trade balance"].append(item.find_element(By.CSS_SELECTOR, "td:nth-child(7)").text)
    data["Coverage rate"].append(item.find_element(By.CSS_SELECTOR, "td:nth-child(9)").text)
    data["Balanza comercial %% GDP"].append(item.find_element(By.CSS_SELECTOR, "td:nth-child(10)").text) 
    data["Change"].append(item.find_element(By.CSS_SELECTOR, "td:nth-child(11)").text) 

driver.quit()

df = pd.DataFrame(data)
df.to_csv("NombreDelaBasedeDatos.csv", index=False) 