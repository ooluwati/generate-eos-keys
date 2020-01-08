from selenium import webdriver

def gen_eos_key_pair():
    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/bin/google-chrome-stable'
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://eosauthority.com/generate_eos_private_key')
    keys = {"pb": None, "pr": None}
    elem = driver.find_element_by_id("eos_private_key")
    keys["pr"] = elem.text
    elem = driver.find_element_by_id("eos_public_key")
    keys["pb"] = elem.text
    driver.quit()
    return keys

#main only used for testing
def main():
    keys = gen_eos_key_pair()
    
if __name__ == "__main__":
    main()
