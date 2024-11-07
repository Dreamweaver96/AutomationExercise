from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import pytest

def test_CreateDeleteAccount():
    # 1. Launch browser
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    # 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")
    # 3. Verify that page is visible successfully
    PageVisible = driver.find_element(By.XPATH, '//div[@aria-label="This site asks for consent to use your data"]')
    assert PageVisible.is_displayed() == True, "Page didn't load"
    print("Page has been accessed successfully")
    # 3b. Agree to the data usage conditions
    # Option1
    # consent_button = driver.find_element(By.CSS_SELECTOR, ".fc-primary-button .fc-button-label")
    # Option2 XPATH extracted using Chrome
    # consent_button = driver.find_element(By.XPATH, "//html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")
    # Option3 - the most explicit
    consent_button = driver.find_element(By.XPATH, "//button[@aria-label='Consent']/p[@class='fc-button-label']")
    consent_button.click()
    # 4. Click on 'Signup / Login' button
    login_button = driver.find_element(By.LINK_TEXT, "Signup / Login")
    login_button.click()
    time.sleep(2)
    # 5. Verify 'New User Signup!' is visible
    NewUserSignup = driver.find_element(By.CSS_SELECTOR, '.signup-form h2')
    assert NewUserSignup.is_displayed() == True, "'New User Signup!' not found"
    print(NewUserSignup.text + " OK")
    # 6. Enter name and email address
    driver.find_element(By.XPATH, "//input[@data-qa='signup-name']").send_keys("randommmmmmm")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("randommmmmmm@randommmmmmm")
    # 7. Click 'Signup' button
    signup_button = driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
    time.sleep(2)
    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    EnterAccInfo = driver.find_element(By.CSS_SELECTOR, '.login-form h2')
    assert EnterAccInfo.is_displayed() == True, "'Enter Account Information' not found"
    print(EnterAccInfo.text + " OK")
    # 9. Fill details: Title, Name, Email, Password, Date of birth
    # Title
    driver.find_element(By.ID, "uniform-id_gender1").click()
    # Name and e-mail are already filled, password will be filled with loop in #12.
    # Date of birth
    day = Select(driver.find_element(By.XPATH, "//select[@data-qa='days']"))
    day.select_by_index(3)
    month = Select(driver.find_element(By.XPATH, "//select[@data-qa='months']"))
    month.select_by_index(3)
    year = Select(driver.find_element(By.XPATH, "//select[@data-qa='years']"))
    year.select_by_index(3)
    time.sleep(2)
    # 10. Select checkbox 'Sign up for our newsletter!'
    driver.find_element(By.ID, "newsletter").click()
    # 11. Select checkbox 'Receive special offers from our partners!'
    driver.find_element(By.ID, "optin").click()
    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    # country is already selected by default
    # script below selects all the inputs, ignores those listed in "input_ignore" to select only valid ones and fills them with the same string
    input_tags = driver.find_elements(By.TAG_NAME, "input")
    input_ignore = [None, "name", "email"]
    input_list = [field.get_attribute("data-qa") for field in input_tags if
                  field.get_attribute("data-qa") not in input_ignore]
    for InputInstance in input_list:
        driver.find_element(By.XPATH, f'//input[@data-qa="{InputInstance}"]').send_keys("randommmmmmm")
    time.sleep(2)
    # 13. Click 'Create Account button'
    driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()
    # 14. Verify that 'ACCOUNT CREATED!' is visible
    AccountCreated = driver.find_element(By.XPATH, "//h2[@data-qa='account-created']")
    assert AccountCreated.is_displayed() == True, "'Account created' not found"
    print(AccountCreated.text + " OK")
    # 15. Click 'Continue' button
    driver.find_element(By.LINK_TEXT, "Continue").click()
    # 16. Verify that 'Logged in as username' is visible
    LoggedInAsUsername = driver.find_element(By.PARTIAL_LINK_TEXT, "Logged in")
    assert LoggedInAsUsername.is_displayed() == True, "'Logged in as username' not found"
    print(LoggedInAsUsername.text + " OK")
    # 17. Click 'Delete Account' button
    driver.find_element(By.LINK_TEXT, "Delete Account").click()
    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    AccountDeleted = driver.find_element(By.XPATH, "//h2[@data-qa='account-deleted']")
    assert AccountDeleted.is_displayed() == True, "'Account deleted' not found"
    print(AccountDeleted.text + " OK")
    driver.find_element(By.LINK_TEXT, "Continue").click()