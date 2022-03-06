from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.bestbuy.com/?intl=nosplash')


def search(search_term, pages):
    result_list = []
    # Close Subscription Popup
    browser.find_element(
        by=By.CLASS_NAME, value="c-modal-close-icon").click()

    # Close Survey Popup
    try:
        browser.find_element(
            by=By.ID, value="survey_invite_no").click()
    except:
        pass

    # Search for product
    browser.find_element(
        by=By.CLASS_NAME, value="search-input").click()

    browser.find_element(
        by=By.CLASS_NAME, value="search-input").send_keys(search_term)

    browser.find_element(
        by=By.CLASS_NAME, value="header-search-button").click()

    # Get all products
    # Get Product Image
    product_images = browser.find_elements(
        by=By.CLASS_NAME, value="product-image")
    # Get Product Name and Link
    product_names = browser.find_elements(
        by=By.CLASS_NAME, value="sku-header")

    # Get Product Price
    product_prices = browser.find_elements(
        by=By.CLASS_NAME, value="priceView-hero-price.priceView-customer-price")

    # Storing Data in a List
    for i in range(len(product_images)):
        result_list.append(
            [product_names[i].find_element(by=By.TAG_NAME, value='a').get_attribute('href'),
             product_images[i].get_attribute('src'),
             product_names[i].find_element(by=By.TAG_NAME, value='a').text,
             product_prices[i].find_element(by=By.TAG_NAME, value='span').text])

    return result_list


result = search('iphone', 1)
print(result)
# Quit
# browser.quit()
