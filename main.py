import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(
        ChromeDriverManager().install()
    )
)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url) # Метод открывает указанный URL в текущем окне браузера
driver.maximize_window()

# Сохраняем данные пользователя в переменные
user_name = "standard_user"
user_password = "secret_sauce"
# Находим и сохраняем ссылки на поля: "Username" и "Password"
user_name_field = driver.find_element(By.XPATH, "//input[@name='user-name']")
user_password_field = driver.find_element(By.XPATH, "//input[@name='password']")
# Находим и сохраняем ссылку на кнопку "Login"
login_button = driver.find_element(By.XPATH, "//input[@name='login-button']")
# Заполняем поля: "Username" и "Password" - логинными данными пользователя
user_name_field.send_keys(user_name)
user_password_field.send_keys(user_password)
# Ждем 2-е секунды и воспроизводим нажатие кнопки "Login"
time.sleep(2)
login_button.click()
# Закрываем браузер через 5 секунд
time.sleep(5)
driver.close()
