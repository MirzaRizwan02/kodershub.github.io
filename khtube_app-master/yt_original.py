from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from subprocess import call
import os
import pandas as pd 
from selenium.webdriver.common.by import By  
from selenium.webdriver.support import expected_conditions as EC
import requests
import datetime
import argparse


def word_count(str,channel):
    counts = 0
    channel = str.split()

    for word in channel:
        if word == str:
            counts += 1

    if counts ==0:
        if str in channel:
            counts = 1
    return counts


def getChannelUrls(keyword, driver):
    vid_count = []
    links = []
    baseUrl = "https://youtube.com/"
    driver.get(f"{baseUrl}/results?search_query="+keyword+"&sp=EgIQAg%253D%253D")
    driver.maximize_window()
    ### SCROLLING SHUGAL START HERE!
    SCROLL_PAUSE_TIME = 1.0   # 1.0

    ## Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    linklist =[]
    while True:
        scroll_height = 2000
        document_height_before = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script(f"window.scrollTo(0, {document_height_before + scroll_height});")
        time.sleep(SCROLL_PAUSE_TIME)
        document_height_after = driver.execute_script("return document.documentElement.scrollHeight")
        if document_height_after == document_height_before:
            break
        
        
    allChannelList = driver.find_elements_by_xpath('//*[@id="main-link"]')
    links = list(dict.fromkeys(map(lambda a: a.get_attribute("href"),allChannelList)))
        
    vids = driver.find_elements_by_id("video-count")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Loading all details... Please wait. This can take upto 7 - 15mins, depending on your internet")
    
    i =0
    for x in vids:
        try:
            if vids:
                vid_c = vids[i].text.replace(",","").replace(" videos","").replace(" video","")
                if vid_c == "":
                    vid_c = vid_c.replace("","0")
                vid_count.append(int(vid_c))
                i = i+1
        except:
            break
    return links,vid_count


def getChannelDetails(urls,vid_count, driver):

    avgviewslist =[]
    cnamelist  = []
    csubslist = []
    cdesclist = []
    cviewslist = []
    urllist = []

    x = 0
    for url in urls:
        driver.get(f"{url}/about")
        # print(url)
        # time.sleep(1.0)  # 0.5
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Loading all details... Please wait. This can take upto 7 - 12mins, depending on your internet")
        header = driver.find_elements_by_xpath('//*[@id="channel-container"]')
        name = driver.find_elements_by_xpath('//*[@id="channel-name"]')
        subs = driver.find_elements_by_xpath('//*[@id="subscriber-count"]')
        desc = driver.find_elements_by_xpath('//*[@id="description"]')
        views = driver.find_elements_by_css_selector("#right-column > yt-formatted-string:nth-child(3)")
        x=x+1
        if(x/5>=100):
            print("Almost done...!")
        else:
            print(int(x/5),".. Loading")
        # time.sleep(1.0)

        urllist.append(url)

        print("..")

        if not header:
            print("Empty")
        else:
            if name:
                cnamelist.append(name[0].text)
                
            if subs:
                csubs = subs[0].text.replace(" subscribers","")
                csubslist.append(csubs)
                
            if desc:
                cdesclist.append(desc[0].text)
                
            if views:
                cviews = views[0].text.replace(" views","").replace(" view","")
                cviews = cviews.replace(",","")
                if cviews == "" or cviews == None:
                    cviews = "0"
                cviews = int(cviews)
                cviewslist.append(cviews)

    return avgviewslist, cnamelist, csubslist, cdesclist, cviewslist, urllist


# def scrape(text, driver):
def scrape(user_kw, driver):
    
    driver = driver
    keyword = str.strip(user_kw)
    kw= keyword
    keyword = keyword.replace(" ","+")

    allChannelUrls,vid_count = getChannelUrls(keyword, driver = driver)
    avgviewslist, cnamelist, csubslist, cdesclist, cviewslist, urllist = getChannelDetails(allChannelUrls,vid_count, driver = driver)
    driver.close()

    for i,j in zip(cviewslist,vid_count):
        if j == 0:
            avgviewslist.append(0)
        else:
            avgviewslist.append(int(i/j))
    kwlist = [word_count(kw,i) for i in cnamelist[:500]]

    
    detailsdict ={
        "Channel Name":cnamelist[:500],
        "URL": urllist[:500],
        "Subscribers": csubslist[:500],
        "Avg. Views": avgviewslist[:500],
        "Keyword Count": kwlist[:500],
        "Channel Views": cviewslist[:500],
        "Video Count": vid_count[:500],
        "Description":cdesclist[:500]
    }
    os.system('cls' if os.name == 'nt' else 'clear')
    
    now = datetime.datetime.now()

    print("len of views: ", len(avgviewslist))
    print("len of cname: ", len(cnamelist))
    print("len of csub: ", len(csubslist))
    print("len of cdesc: ", len(cdesclist))
    print("len of cviews: ", len(cviewslist))
    print("len of url: ", len(urllist))
    
    file = pd.DataFrame.from_dict(detailsdict)
        
    excel_writer = pd.ExcelWriter(f"{keyword}_"+now.strftime("%Y%m%d%H%M%S")+".xlsx")
    file.to_excel(excel_writer, engine='openpyxl',index=False)
    excel_writer.save()
    # file.to_csv(f"{keyword}_"+now.strftime("%Y%m%d%H%M%S")+".csv", index=False, header=True, encoding='utf-8')
    print("Data has been exported to an Excel file saved in the same directory")

if __name__=="__main__":
    ### Edited code here for cmd line
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--user_kw', type=str, required=True)

    option = Options()
    option.headless = True
    cwd = os.getcwd()
    # driver = webdriver.Chrome(cwd+"/chromedriver",options=option)
    driver = webdriver.Chrome(cwd+"/chromedriver",options=option)


    args = parser.parse_args()

    user_kw = args.user_kw
    
    scrape(user_kw, driver)
