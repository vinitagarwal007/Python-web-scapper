from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
import time
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vinitagarwal",
    database="medicine"
)


def getalpha(i):
    match i:
        case 1: return 'a'
        case 2: return 'b'
        case 3: return 'c'
        case 4: return 'd'
        case 5: return 'e'
        case 6: return 'f'
        case 7: return 'g'
        case 8: return 'h'
        case 9: return 'i'
        case 10: return 'j'
        case 11: return 'k'
        case 12: return 'l'
        case 13: return 'm'
        case 14: return 'n'
        case 15: return 'o'
        case 16: return 'p'
        case 17: return 'q'
        case 18: return 'r'
        case 19: return 's'
        case 20: return 't'
        case 21: return 'u'
        case 22: return 'v'
        case 23: return 'w'
        case 24: return 'x'
        case 25: return 'y'
        case 26: return 'z'


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(
    "user-data-dir=C:\\Users\\KIIT\\Desktop\\selenium\\chromedata")
alphanum = int(input("Enter which alphabet to start from "))
x = int(input("Which page to start from "))
z = int(input("Which element to start from "))
driver = webdriver.Chrome('chromedriver', options=options)
alpha = getalpha(alphanum)
driver.get("https://www.1mg.com/drugs-all-medicines?page=1&label="+str(alpha))
original_tab = driver.current_window_handle
pagenoelem = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'link-page')))
pageno = pagenoelem[len(pagenoelem)-1].text
for pageno in range(x, int(pageno)+1):
    time.sleep(5)
    # for pageno in range(x, int(3)):
    driver.get("https://www.1mg.com/drugs-all-medicines?page=" +
               str(pageno)+"&label="+str(alpha))
    a = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "style__product-name___HASYw")))
    links = []
    mrplist = []
    packinglist = []
    for i in range(len(a)):
        time.sleep(1)
        # for i in range(2):
        links.append(a[i].get_attribute('href'))
        mrpelem = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="container"]/div/div/div[4]/div['+str(i+1)+']/div/a/div[2]/div[1]/div[2]')))
        mrplist.append(mrpelem.text)

        packingelem = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="container"]/div/div/div[4]/div['+str(i+1)+']/div/a/div[2]/div[3]/div[1]')))
        packinglist.append(packingelem.text)
    for z in range(len(links)):
        link = links[z]
        driver.switch_to.new_window('tab')
        driver.get(link)
        try:
            name = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "DrugHeader__title-content___2ZaPo")))
            dbname = name[0].text
        except NoSuchElementException:
            print("error name no such element:",
                  alphanum, ":", pageno, ":", z+1)
        except:
            dbname = ""
            print("error name:", alphanum, ":", pageno, ":", z+1)

        try:
            company = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "DrugHeader__meta-value___vqYM0")))
            dbcompany = company[0].text
        except NoSuchElementException:
            print("error company no such element:",
                  alphanum, ":", pageno, ":", z)
        except:
            dbcompany = ""
            print("error company:", alphanum, ":", pageno, ":", z+1)
        try:
            salt = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "saltInfo")))
            dbsalt = salt[0].text
        except NoSuchElementException:
            print("error salt no such element:",
                  alphanum, ":", pageno, ":", z+1)
        except:
            dbsalt = ""
            print("error salt:", alphanum, ":", pageno, ":", z+1)
        try:
            # mrp = WebDriverWait(driver, 10).until(
            #     EC.presence_of_all_elements_located(
            #         (By.CLASS_NAME, "PriceBoxPlanOption__margin-right-4___2aqFt")))
            # dbmrp = mrp[0].text
            dbmrp = mrplist[z]
        except NoSuchElementException:
            print("error mrp no such element:",
                  alphanum, ":", pageno, ":", z+1)
        except:
            dbmrp = "NA"
            print("error mrp:", alphanum, ":", pageno, ":", z+1)
        try:
            # packing = WebDriverWait(driver, 10).until(
            #     EC.presence_of_all_elements_located(
            #         (By.CLASS_NAME, "DrugPriceBox__quantity___2LGBX")))
            # dbpacking = packing[0].text

            dbpacking = packinglist[z]
        except NoSuchElementException:
            print("error packing no such element:",
                  alphanum, ":", pageno, ":", z+1)
        except:
            dbpacking = ""
            print("error packing:", alphanum, ":", pageno, ":", z+1)
        try:
            use = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "DrugOverview__uses___1jmC3")))
            finaluse = ""
            for li in use:
                finaluse += li.text + ","
        except NoSuchElementException:
            print("error use no such element:",
                  alphanum, ":", pageno, ":", z+1)
        except:
            finaluse = "NA"
            print("error use:", alphanum, ":", pageno, ":", z)
        try:
            side = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "DrugOverview__list-container___2eAr6")))
            finalside = ""
            for li in side:
                finalside += li.text + ","
        except NoSuchElementException:
            print("error side no such element:",
                  alphanum, ":", pageno, ":", z+1)
        except:
            finalside = ""
            print("error side:", alphanum, ":", pageno, ":", z+1)
        mycursor = mydb.cursor()
        sql = "INSERT INTO data(name,company,composition,use_med,side_effect,packing,mrp,onemglink) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
        val = (dbname, dbcompany, dbsalt, finaluse,
               finalside, dbpacking, dbmrp, link)
        mycursor.execute(sql, val)
        mydb.commit()
        print(alphanum, ":", pageno, ":", z, "record inserted.")
        driver.close()
        driver.switch_to.window(original_tab)
driver.quit()
