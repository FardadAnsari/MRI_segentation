from selenium.webdriver.chrome.options import Options
from selenium import webdriver as Wee
import random
from time import sleep
from selenium.webdriver.common.keys import Keys
import mysql.connector
import wget
import os
import sys
import zipfile
import datetime
import warnings
import urllib.request



# for turning the warning off 
warnings.simplefilter("ignore")



# defining function for cleaning cmd 

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



#get the time and date
now = datetime.datetime.now()
proxy_list = []
device_list=[]
    

url = "https://raw.githubusercontent.com/FardadAnsari/User_agent/main/user_agent_total.txt"
file = urllib.request.urlopen(url)
for line in file:

	decoded_line = line.decode("utf-8")
	decoded_line=decoded_line.strip() 
	device_list.append(decoded_line)
	
	
	
def proxy_finder():

    proxy_list=[]
    
    
    url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
        decoded_line=decoded_line.strip() 
        proxy_list.append(decoded_line)




    url = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
        decoded_line=decoded_line.strip() 
        proxy_list.append(decoded_line)
        #print(len(proxy_list))

    return proxy_list


certain=True  


def visit_pp(PROXY,USERAGENT):
    option = Options()
    option.add_argument('--disable-infobars')
    option.add_argument("start-maximized")
    option.add_argument("--window-size=1920,1080")
    option.add_argument('--disable-gpu')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--allow-running-insecure-content')
    option.add_argument('--no-sandbox')
    option.add_argument("--disable-extensions")
    option.add_argument('lang=en')
    #option.add_argument('--log-level=OFF')
    option.add_argument("--proxy-server=%s" % PROXY)
    option.add_argument('--user-agent=%s' % USERAGENT)
    option.add_argument('--headless')

    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
    })

    chromedriver_path = "C:\chromedriver.exe"
    browser = Wee.Chrome(options=option, executable_path=chromedriver_path)

    return browser


count_s = 0
count_fail=0
visit = 0


proxy_list=proxy_finder()
print(len(proxy_list))

while True:
    #print(sys.argv[1])
    
    
    
    for ip in proxy_list:
        for device in device_list:
            now = datetime.datetime.now()

            if 2 <= now.hour and 23 >= now.hour:
                certain=True

                try:
                    random.shuffle(device_list)
                    print(sys.argv[1])
                    s_1 = random.randint(2, 6)
                    sleep(s_1)
                    
                    interact = visit_pp(ip,device)
                    interact.get(sys.argv[2])
                    sleep(15)
                    print("I found the website")
                    interact.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    sleep(5)
                    button=interact.find_elements_by_tag_name('a')
                    print(len(button))
                    #print(len(button))
                    #print("I found the donwload app link")
                    sleep(5)
                    button[random.randint(44,48)].click()
                    sleep(int(sys.argv[3]))
                    count_s = count_s + 1
                    visit = visit + 1
                    
                    print("The total number of visits is  " + str(visit) + " !")
                    print(device)
                    interact.quit()
                    print(" Interaction number " + str(count_s) + " was successful !")
                    #random.shuffle(device_list)
                
                    for user_agent in device_list[1000:1050]:
                        try:
                            proxy=ip
                            interact_1=visit_pp(proxy,user_agent)
                            interact_1.get(sys.argv[2])
                            sleep(20)
                            interact_1.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(10)
                            button=interact_1.find_elements_by_tag_name('a')
                            button[random.randint(44,48)].click()
                            sleep(22)
                            #random.shuffle(device_list)
                            count_s = count_s + 1
                            visit = visit + 1
                            print(device)
                            interact_1.quit()
                            print(" Interaction number " + str(count_s) + " was successful !")
                            print("Visit was with same ip ......")
                        except:
                            print("Try agian with same working ip different user-agent...")
                            continue




                except:

                    print(" Interaction number " + str(count_fail) + " was Unsuccessful !")
                    count_fail=count_fail+1
                    interact.quit()                   
                    #if count_fail == 200:
                    #    proxy_list=proxy_finder()
                    proxy_list.remove(ip)
                    print("Bad proxy was thrown away.")
                    print("Proxy has been Changed")
                    random.shuffle(proxy_list)
                    break 


                # waiting for 3 hours
                sleep(20)
            else:

                while now.hour==int(sys.argv[4]) and certain:
                    mydb = mysql.connector.connect(
                        host="79.170.40.237",
                        user="cl22-data",
                        password="Wee%159125w$",
                        database="cl22-data"
                    )

                    sleep(5)

                    mycursor = mydb.cursor()
                    name=sys.argv[1]
                    domain=sys.argv[2]
                    date=str(now.date())
                    num_visit=str(visit)

                    sql = "INSERT INTO visitdatabaseFeb (shopid, name, domain, date, views) VALUES (%s, %s ,%s, %s , %s )"

                    val = (sys.argv[5], name , domain, date, num_visit)
                    mycursor.execute(sql, val)

                    mydb.commit()

                    print(mycursor.rowcount, "record inserted.")
                    print("Total Number of Successful Visits is "+ str(count_s))
                    visit=0
                    certain=False
                    break





    











