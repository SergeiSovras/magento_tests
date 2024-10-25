from selenium.webdriver.common.by import By

title_locator = (By.TAG_NAME, 'h1')

first_name_locator = (By.ID, 'firstname')
last_name_locator = (By.ID, 'lastname')
email_locator = (By.ID, 'email_address')
password_locator = (By.ID, 'password')
password_confirmation_locator = (By.ID, 'password-confirmation')
submit_button_locator = (By.CSS_SELECTOR, '[title="Create an Account"]')
error_first_name_locator = (By.ID, 'firstname-error')

sorting_title = (By.CLASS_NAME, 'sorter-label')
product_item = (By.CLASS_NAME, 'product-item-link')

compare_products = (By.ID, 'block-compare-heading')
whats_new = (By.ID, 'ui-id-3')
