from selenium import webdriver
from time import sleep
import pandas as pd

USERNAME = 'lupnjqlljb59@gmail.com'
PASSWORD = 'SoSrSQRByp57'
COMPANY_NAME = 'Xpanxion'
LOCATION = 'Pune (India)'


path = r"S:\Coding\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
url = "https://www.glassdoor.co.in/index.htm"

driver.get(url)

fb = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/article/section[1]/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div')
fb.click()

sleep(5)

base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
sleep(1)
fb_user = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
fb_user.send_keys(USERNAME)
fb_pwd = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
fb_pwd.send_keys(PASSWORD)
sleep(1)
fb_login_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]')
fb_login_button.click()

driver.switch_to.window(base_window)
sleep(10)

location_input = driver.find_element_by_xpath('/html/body/header/nav[1]/div/div/div/div[4]/div[3]/form/div/div[3]/div/input')
location_input.send_keys(LOCATION)
sleep(1)
type_select1 = driver.find_element_by_xpath('/html/body/header/nav[1]/div/div/div/div[4]/div[3]/form/div/div[2]')
type_select1.click()
sleep(1)
type_select2 = driver.find_element_by_xpath('/html/body/header/nav[1]/div/div/div/div[4]/div[3]/form/div/div[2]/div/div[2]/div/ul/li[2]')
type_select2.click()
sleep(1)
company_name_input = driver.find_element_by_xpath('/html/body/header/nav[1]/div/div/div/div[4]/div[3]/form/div/div[1]/div/div/input')
company_name_input.send_keys(COMPANY_NAME)
sleep(1)
search_button = driver.find_element_by_xpath('/html/body/header/nav[1]/div/div/div/div[4]/div[3]/form/div/button')
search_button.click()
sleep(5)
reviews_select = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div/div[1]/article[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/a[1]')
reviews_select.click()
sleep(5)

star_list = []
emp_type_list = []
review_title_list = []
designation_list = []
pros_list = []
cons_list = []

for i in range(23):
    sleep(3)
    for i in range(1,11):
        star1 = driver.find_element_by_xpath(f'/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[8]/main/div/div/div[1]/div[2]/div/ol/li[{i}]/div/div/div[1]/div/div/div/span[1]')
        star_rating =star1.text
        star_list.append(star_rating)

        emp_type1 = driver.find_element_by_xpath(f'/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[8]/main/div/div/div[1]/div[2]/div/ol/li[{i}]/div/div/div[1]/div/span')
        emp_type = emp_type1.text
        emp_type_list.append(emp_type)

        review_title1 = driver.find_element_by_xpath(f'/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[8]/main/div/div/div[1]/div[2]/div/ol/li[{i}]/div/div/div[2]/div/div[1]/h2/a')
        review_title = review_title1.text
        review_title_list.append(review_title)

        designation1 = driver.find_element_by_xpath(f'/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[8]/main/div/div/div[1]/div[2]/div/ol/li[{i}]/div/div/div[2]/div/div[1]/span')
        designation = designation1.text
        designation_list.append(designation)

        pros1 = driver.find_element_by_xpath(f'/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[8]/main/div/div/div[1]/div[2]/div/ol/li[{i}]/div/div/div[2]/div/div[2]/div[1]/p[2]')
        pros = pros1.text
        pros_list.append(pros)

        cons1 = driver.find_element_by_xpath(f'/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[8]/main/div/div/div[1]/div[2]/div/ol/li[{i}]/div/div/div[2]/div/div[2]/div[2]/p[2]')
        cons = cons1.text
        cons_list.append(cons)

    next = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[8]/main/div/div/div[1]/div[3]/div/div[1]/button[2]')
    next.click()

# star_list = []
# emp_type_list = []
# review_title_list = []
# designation_list = []
# pros_list = []
# cons_list = []

df = pd.DataFrame({"star":star_list,
                   "emp type":emp_type_list,
                   "review title":review_title_list,
                   "designation":designation_list,
                   "pros":pros_list,
                   "cons":cons_list})

df.to_csv("reviews.csv")


# print(f'star:{star_rating}\nemp type:{emp_type}\nreview:{review_title}\ndesignation:{designation}\npros:{pros}\ncons:{cons}')





# /html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[8]/main/div/div/div[1]/div[2]/div/ol/li[2]/div


