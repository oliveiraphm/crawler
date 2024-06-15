import os
from selenium import webdriver

class GenericBrowser:
    browser = None
    options = webdriver.ChromeOptions()

    default_options = [
        "--no-sandbox",
        "--disable--web-security",
        "--disable-dev-shm-usage",
        "--memmory_pressure-off",
        "--ignore-certificate-errors"
    ]

    def get_browser(self):
        return webdriver.Chrome()

    def is_headless(self):
        headless = os.getenv('HEADLESS')
        if headless is None:
            self.options.add_argument("--headless")

    def set_options(self, args: list[str] | None):
        self.is_headless()
        self.set_proxy()
        if args:
            for arg in args:
                self.options.add_argument(arg)

    def set_proxy(self):
        if os.getenv("USE_PROXY"):
            user = os.getenv("PROXY_USER")
            password = os.getenv("PROXY_PASSWORD")
            url = os.getenv("PROXY_URL")
            port = os.getenv("PROXY_PORT")
            proxy_provider = f'http://{user}:{password}@{url}:{port}'
            self.options.add_argument(f'--proxy-server={proxy_provider}')

    def close(self):
        return self.browser.quit()