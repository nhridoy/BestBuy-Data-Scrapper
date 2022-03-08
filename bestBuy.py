from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.bestbuy.com/?intl=nosplash')
browser.implicitly_wait(10)


def search(search_term, pages):
    result_list = []
    # Close Subscription Popup
    try:
        browser.find_element(
            by=By.CLASS_NAME, value="c-modal-close-icon").click()
    except:
        pass

    # Close Survey Popup
    def close_survey():
        try:
            browser.find_element(
                by=By.ID, value="survey_invite_no").click()
        except:
            pass

    close_survey()

    # Search for product
    browser.find_element(
        by=By.CLASS_NAME, value="search-input").click()

    browser.find_element(
        by=By.CLASS_NAME, value="search-input").send_keys(search_term)

    browser.find_element(
        by=By.CLASS_NAME, value="header-search-button").click()

    # Get all products
    def get_products():
        close_survey()
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

    for page in range(pages):
        if page+1 == pages:
            return result_list
        else:
            get_products()

        if 'disabled' not in browser.find_element(
                by=By.CLASS_NAME, value="sku-list-page-next").get_attribute('class'):
            browser.find_element(
                by=By.CLASS_NAME, value="sku-list-page-next").click()
        else:
            return result_list

    return result_list


result = search('access point', 4)
print(result)
print(len(result))
# Quit
browser.quit()
