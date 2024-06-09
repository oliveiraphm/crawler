from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

browser = webdriver.Chrome(chrome_options)
browser.get("https://globo.com")

print(browser.page_source)