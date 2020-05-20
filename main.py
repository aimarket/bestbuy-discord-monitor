from headers_list import header_dict
from products_list import products_list
from time import strftime, localtime, time
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
import requests
import time
import random
import bs4 as soup
import json

"""
=================================================================================================
BESTBUY Monitor

This uses the selenium webdriver for javascript websites(BESTBUY) to load in a headless browser
I tried my best to add comments but if something needs better explination please let me know

DISCORD: Line 76 enter webhook to embed a post on discord

TIME: Line 70 Please change this to reflect the number of proxies
    LESS proxies = Higher delay

Products: Products_list.py enter product(s) url as a string in the dictionary 

PROXIES: Enter https proxies in Proxy-List.txt
Free proxie website: http://free-proxy.cz/en/proxylist/country/US/https/date/all
    For example:
        HOST:PORT
        209.97.138.116:8080
        173.82.55.156:5836

Future Updates hopefully:
    *Add a way to webscrape more than just one website
    *More than one thread


=================================================================================================
"""

#initiate proxy list and format for selenium
proxy_dict = {}
with open('Proxy-List.txt') as li:
    proxy = li.readline()
    cnt = 0
    
    while proxy:
        proxy_dict[cnt] = {"http":"{}".format(proxy.strip())}
        proxy = li.readline()
        cnt += 1
li.close()

#booleans
online = True
timeoutonweb = False

# number of items
header_length = header_dict.__len__()
proxy_length = proxy_dict.__len__()
product_length = products_list.__len__()

#counters dont touch!!!
headercounter = 0
proxycounter = 0
productcounter = 0

#be reasonable, unless you have a long list of proxies, stick with longer delay
delaylimit = 15

#Proxy organization
timeoutdict = {}
#discord post
discord_queue = []
webhook = 'YOUR WEBHOOK ON A STRING'




#send to discord
def send_notification(code, website):
    data = {}
    embed = {}
    data["embeds"] = []
    if(code == 0):
        embed['color']= 15400704
        data['username']= 'error'
        data["content"] = website
    elif(code == 1):
        embed['color']= 65301
        data['username']= 'IN-STOCK'
        embed["url"] = website
        embed["title"] = website.split("/")[4]
    else:
        embed['color']= 16717056
        data['username']= 'sold out'
        embed["url"] = website
        embed["title"] = website.split("/")[4]
    #for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
    data["embeds"].append(embed)
    requests.post(webhook,data=json.dumps(data), headers={"Content-Type": "application/json"})
    #print("posting on discord",website)

#check status of add-to-cart-button
def check_status(html):
    raw_page = soup.BeautifulSoup(html,'html.parser')
    try:
        button_text = raw_page.find("button", class_="add-to-cart-button").get_text()
        print(button_text)
        if(button_text.upper() == "Sold Out".upper() or button_text.upper() == "Check Stores".upper()):
            return False
        else:
            #print(button_text)
            return True
    except:
        return True

def proxyorganize(dic):
    #makes key values in dictonary in order
    p = []
    new_dic={}
    for x in list(range(dic.__len__())):
        p.append(x)
    new_dic=dict(zip(p,list(dic.values()))) 
    return(new_dic)

def resetcounter(counter, length):
    #if the counter reaches the end of the list reset
    if(counter >= length-1):
        counter = 0
    else:
        counter += 1
    return counter

def listmaker(length):
    #random list of numbers with size of length from 0 to length
    return random.sample(range(length),length)

'''
Main program in a while loop of spagetti code
TODO optimize for easy redability
'''
while(online):
    # if proxies run out
    if (len(timeoutdict)>proxy_length):
        break

    #random number generators
    if(headercounter == 0):
        headerlist = listmaker(header_length)
    if(proxycounter == 0):
        proxylist = listmaker(proxy_length)
    if(productcounter == 0):
        productlist = listmaker(product_length)
    #print(proxylist)

    #selenium setup
    options = Options()
    options.page_load_strategy = 'normal'
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    #options.add_argument("--no-sandbox") # linux only

    #headless mode needs both arguments below
    options.add_argument("--headless")
    options.add_argument("window-size=1920x1080")

    # send request to GET website
    try:
        
        PROXY = proxy_dict[proxylist[proxycounter]]['http']

        webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
            "httpProxy":PROXY,
            "ftpProxy":PROXY,
            "sslProxy":PROXY,
            #"noProxy":None,
            "proxyType":"MANUAL",
            #"class":"org.openqa.selenium.Proxy",
            #"autodetect":True
        }
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", header_dict[headerlist[headercounter]]['User-Agent'])
        driver = webdriver.Firefox(options=options,firefox_profile=profile)
        #website request timeout
        driver.set_page_load_timeout(20)
        #serches url in the product_list.py file
        driver.get(products_list[productlist[productcounter]])
        #Grab html content
        html = driver.page_source
    except TimeoutException as e:
        timeoutonweb = True
    

    # debugging
    date = strftime("%Y-%m-%d %H:%M:%S", localtime())
    if(timeoutonweb==False):
        status = check_status(html)
        #print('status ', status)
        if(status):
            if(products_list[productlist[productcounter]] not in discord_queue):
                #print("website not in queue")
                discord_queue.append(products_list[productlist[productcounter]])
                send_notification(1,products_list[productlist[productcounter]])
        else:
            # product sold out again
            for itm in discord_queue:
                if(itm == products_list[productlist[productcounter]]):
                    discord_queue.pop(itm)
                    send_notification(2,products_list[productlist[productcounter]])
        #TODO make a document to log all this information for debugging
        print(products_list[productlist[productcounter]][12:], "online at ", date, " code: ", 200, " using header #", headerlist[headercounter], "proxy ",proxy_dict[proxylist[proxycounter]]['http']," #", proxylist[proxycounter])
    else:
        print(products_list[productlist[productcounter]][12:], "offline at", date, " code", 400, " using header #",headerlist[headercounter], "proxy ",proxy_dict[proxylist[proxycounter]]['http']," #", proxylist[proxycounter])
        
        # put proxie in timeout dictoinary
        time_key = time.time()
        timeoutdict[time_key]=proxy_dict[proxylist[proxycounter]]
        # take proxie out of active proxies
        proxy_dict.pop(proxylist[proxycounter])
        # reorder dictionary
        proxy_dict = proxyorganize(proxy_dict)
        # increase time per request
        delaylimit += 2
        timeoutonweb = False
        # used to make new list of random numbers
        proxycounter = proxy_dict.__len__()
    
    #add proxie back into active
    for x in timeoutdict.keys():
        if(x+400 < time.time()):
            proxy_dict[proxy_dict.__len__()] = timeoutdict[x]
            proxycounter = proxy_dict.__len__()
            timeoutdict.pop(x)



    #nap time
    time.sleep(random.uniform(10.0,delaylimit))
    #update proxy size
    proxy_length = proxy_dict.__len__()

    #reset counter after max items are reached
    headercounter = resetcounter(headercounter,header_length)
    proxycounter = resetcounter(proxycounter, proxy_length)
    productcounter = resetcounter(productcounter, product_length)

    #kill driver window
    driver.quit()

send_notification(0,"Notify Creator I used up my proxies :(")
exit()
