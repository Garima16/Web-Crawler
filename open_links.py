from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://www.amazon.in/')
try:
    search_element = browser.find_element_by_id('twotabsearchtextbox')
    phone_name = 'Moto G4 Plus'
    search_element.send_keys(phone_name)
    search_element.submit()
    next_url = browser.current_url
    print next_url
except:
    print 'No such element'
