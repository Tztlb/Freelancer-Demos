from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

# تابع برای جستجو در گوگل و کلیک بر روی لینک وبسایت مشخص شده
def search_and_click(keyword, website, browser='chrome'):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError("Browser should be either 'chrome' or 'firefox'")

    # باز کردن گوگل
    driver.get('https://www.google.com')

    # یافتن جعبه جستجو و وارد کردن کلیدواژه
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)  # مکث برای بارگذاری نتایج

    # گرفتن تمامی لینک‌های نتایج جستجو
    search_results = driver.find_elements(By.XPATH, '//a')  # همه لینک‌ها

    # جستجو و کلیک بر روی لینک‌های سایت مشخص شده
    for result in search_results:
        link = result.get_attribute('href')
        if link and website in link:  # بررسی وجود دامنه اصلی در لینک
            print(f"Found {website} in link: {link}")
            result.click()  # کلیک بر روی لینک
            break
    else:
        print(f"{website} not found in the search results.")

    # توقف برنامه تا زمانی که مرورگر توسط کاربر بسته شود
    try:
        while len(driver.window_handles) > 0:  # بررسی تعداد پنجره‌های باز مرورگر
            time.sleep(1)  # منتظر می‌مانیم و وضعیت مرورگر را چک می‌کنیم
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()  # بستن مرورگر

# استفاده از تابع
if __name__ == "__main__":
    keyword = "موبایل"  # کلیدواژه جستجو
    website = "digikala.com"  # دامنه وبسایت مورد نظر (فقط دامنه اصلی)
    browser_choice = "chrome"  # می‌توانید "firefox" یا "chrome" انتخاب کنید

    search_and_click(keyword, website, browser_choice)
