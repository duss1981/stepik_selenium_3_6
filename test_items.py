import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        
def test_button_add_to_basket(browser):            
    browser.get(link)
    error = False
    try:      
        #with pytest.raises(TimeoutException):
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'btn-add-to-basket'))
        )        
    except TimeoutException:
        error=True        
    finally:       
        assert error==False, "No button 'Add to basket'"
    time.sleep(30)
    
    