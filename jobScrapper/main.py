# purpose of this program to scrap data of top job posting websites from google jobs feed

import os
import glob
import selenium
from selenium import webdriver
import time
import io
import bs4 as bs
import requests
import csv
import json
import pandas as pd
from datetime import datetime, timedelta
import datetime
import re
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
import sys
# from selenium.common.exceptions import ElementClickInterceptedException


def write_json(data, output_json_per_category):
    with open(output_json_per_category, 'w') as f:
        json.dump(data, f, indent=4)
#scrap jobs
    
def search_result(driver, search_query, output_json_per_category):
    
    # find element having all jobs
    load_all_jobs = driver.find_element_by_xpath('//*[@id="immersive_desktop_root"]/div/div[3]/div[1]/div[1]')

    #store last scroll hight
    last_scroll_height = 0

    while True:
        #find all job jobs
        jobs = driver.find_elements_by_class_name('nJXhWc')

        #scroll the page
        driver.execute_script("arguments[0].scrollIntoView();", jobs[-1])

        # adding artificial delay (don't tell anyone I'm using sleep here)
        time.sleep(1)

        # if scroll height has not changed - exit
        scroll_height = driver.execute_script("return arguments[0].scrollHeight;", load_all_jobs)
        if scroll_height == last_scroll_height:
            break
        else:
            last_scroll_height = scroll_height
    
    # go back to top
    driver.execute_script("return arguments[0].scrollIntoView(true);", load_all_jobs)

    '''find all job cards of left side bar'''
    # time.sleep(5)
    all_links = driver.find_elements_by_class_name('iFjolb.gws-plugins-horizon-jobs__li-ed')
    print('Total job in page', len(all_links))
    

    # '''find all job cards of left side bar'''
    # all_links = driver.find_elements_by_xpath('//*[@id="immersive_desktop_root"]/div/div[3]/div[1]/div[1]/div[3]/ul/li[3]')
    # print('Total job in page',len(all_links))

    # driver.find_elements_by_partial_link_text('Apply on App')[0].click()

    #iterate over top 5 jobs on page
    for index, link in enumerate(all_links[0:50]):
        page_start_time = time.time()
        try:
            #dictionary contains details of job card on google job feed page
            print("########### page rank {} #######".format(index+1))
            job_card_data = {}
            # try:
            link.click()
            tag_html = link.get_attribute('innerHTML')
            job_card = bs.BeautifulSoup(tag_html, 'html.parser')

            #search query
            job_card_data['search_query'] = search_query
        

            #rank of job on google job feed page
            job_card_data['rank_on_page'] = index+1
            #job title
            job_title_by_google = job_card.find('div', class_="BjJfJf PUpOsf").text
            job_card_data['job_title_by_google'] = str(job_title_by_google.strip())
            print('title:', job_title_by_google)
            #organization
            job_organization_by_google = job_card.find('div', class_="vNEEBe").text
            job_card_data['job_organization_by_google'] = job_organization_by_google
            print('org:', job_organization_by_google)
            #city
            job_city_by_google = job_card.find(
                'div', class_="oNwCmf").findChildren()[1].text
            job_card_data['job_city_by_google'] = job_city_by_google
            print('job_city:', job_city_by_google)
            #website
            website_by_google = job_card.find(
                'div', class_="oNwCmf").findChildren()[2].text
            job_card_data['website_by_google'] = website_by_google
            print('website:', website_by_google)
            # #date-time
            date_posted = job_card.find(
                'div', class_="KKh3md zfZM7e").findChildren()[0].text
            job_card_data['posted_time_string'] = date_posted
            #find current date-time
            current_datetime = datetime.datetime.now()

                        
            #block of code to convert string contains days, month and hours into datetime
            if 'month' in date_posted:
                posted_date_by_google = current_datetime - timedelta(days=31)

            elif ('day' or 'days') in date_posted:
                num_days = [int(i) for i in date_posted.split() if i.isdigit()]
                # print('num_days',num_days)
                # print(type(num_days))
                posted_date_by_google = current_datetime - timedelta(days=num_days[0])

            else:
                num_hours = [int(i) for i in date_posted.split() if i.isdigit()]
                # print('num_days',num_hours)
                # print(type(num_hours))
                posted_date_by_google = current_datetime - timedelta(hours=num_hours[0])

            job_card_data['posted_date_by_google'] = posted_date_by_google.strftime("%Y-%m-%d %H:%M:%S")
            # print('date', posted_date_by_google)

            last_crawl_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            job_card_data['scraped_date'] = last_crawl_date


        except:
            if driver.current_window_handle is not driver.window_handles[0]:   
                driver.close()
            driver.switch_to.window(driver.window_handles[0])
        

        #find html tag to scrap rating field
        rating = driver.find_element_by_xpath('//*[@id="gws-plugins-horizon-jobs__job_details_page"]')
        rating_html = rating.get_attribute('innerHTML')
        rating_soup = bs.BeautifulSoup(rating_html, 'html.parser')
        all_rating_site = rating_soup.find_all('div', class_="gaLgbc")


        # findind the job desciption
        # click
        try:
            full = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[6]/div/div/div/div/g-expandable-content/span/div/g-inline-expansion-bar/div[1]/div").click()
            time.sleep(1)
            upper = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[5]/div[1]")
            
            desc = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[6]')
            
            print(desc.text)
            
            full_desc = upper.text + desc.text           
            job_card_data['desc'] = full_desc
        except:
            try:
                upper = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[5]/div[1]")
                job_card_data['desc'] = upper.text
            except:
                desc = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[5]/span")
                job_card_data['desc'] = desc.text
            
            job_card_data['desc'] = "No Information Found"
            
       
        with open(output_json_per_category) as json_file:
            data = json.load(json_file)
            temp = data['jobs']

        temp.append(job_card_data)
        write_json(data, output_json_per_category)
        query ="insert into table ()"
        print("##### Time to process one job: ", time.time()-page_start_time)

        #store into csv file
        # with open('google_jobs_feed_top_site_seo_content_v2.csv', mode='a') as jobs_data:
        #     jobs_writer = csv.writer(jobs_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #     jobs_writer.writerow([search_query, job_title_by_google, job_organization_by_google, job_city_by_google, website_by_google, posted_date_by_google, last_crawl_date, title, meta_description, curr_url, h1_head, h2_head, json_schema])

        # except:
        #     print('error')
        #     pass

    # print(len(all_links))

    #wait to load page
    # time.sleep(3)  # sleep_between_interactions
    # driver.quit()


if __name__ == "__main__":

    #iterate over the search keywords and cities

    '''############################## step-1 ############################################'''
    #method to make browser window invisible so it can be run in background
    display = Display(visible=0)
    display.start()

    #Install Driver
    options = Options()
    # chrome_options.add_argument('--disable-accelerated-2d-canvas')
    # chrome_options.add_argument('--disable-accelerated-jpeg-decoding')
    # chrome_options.add_argument('--disable-accelerated-mjpeg-decode')
    # chrome_options.add_argument('--disable-accelerated-video-decode')
    # chrome_options.add_argument('--disable-account-consistency')
    # chrome_options.add_argument('--disable-add-to-shelf')
    # chrome_options.add_argument('--disable-affiliation-based-matching')
    # chrome_options.add_argument('--disable-app-info-dialog-mac[5]')
    # chrome_options.add_argument('--disable-app-list-dismiss-on-blur')
    # chrome_options.add_argument('--disable-app-window-cycling[5]')
    # chrome_options.add_argument('--disable-appcontainer')
    # chrome_options.add_argument('--disable-async-dns')
    # chrome_prefs = {}
    # chrome_options.experimental_options["prefs"] = chrome_prefs
    # chrome_prefs["profile.default_content_settings"] = {"images": 2}
    # chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
    prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2,
                            'plugins': 2, 'popups': 2, 'geolocation': 2, 
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
                            'mouselock': 2, 'media_stream': 2, 
                            'media_stream_mic': 2, 'media_stream_camera': 2, 
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
                            'durable_storage': 2}}
    options.add_experimental_option('prefs', prefs)
    options.add_argument("disable-infobars")
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-extensions")
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    

    #json schema to store jobs feed data
    google_jobs_feed = {'jobs': []}

    # #file name
    # if len(sys.argv) != 2:
    #     print("Please give one args as output_json_per_category ex. output.json ")
    #     sys.exit(0)

    #list of all categories files
    all_job_ategoies = glob.glob('data/*.csv')

    for job_cat in all_job_ategoies:
        print(job_cat)
        output_json_per_category = 'jsondata/'+job_cat.split('/')[1].split('.')[0]+".json"
        with open(output_json_per_category, "w") as outfile:
            json.dump(google_jobs_feed, outfile)

        df = pd.read_csv(job_cat)
        search_keyword = df['generic_keyword']

        # dma_location = pd.read_csv('dma_us_rank_wise.csv')


        
        for keyword in search_keyword:
            driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
            # driver = webdriver.Chrome(executable_path="/home/himanshu/Desktop/google_job_scraper/chromedriver_linux64/chromedriver",
            #                                 options=options)
            driver.set_page_load_timeout(30)
            driver.implicitly_wait(10)
            start_time = time.time()

            search_query = keyword+' jobs in usa'

            #split query into words
            words = search_query.split(' ')
            #join splited words with '+' in order to create search string
            # ex. los angeles => los+angeles
            search_string = '+'.join([word for word in words])
            #Specify Search URL
            search_url = "https://www.google.com/search?q={}"
            #get request
            driver.get(search_url.format(search_string))

            #wait to load page
            time.sleep(1)  # sleep_between_interactions

            print('############################### '+keyword +' ###########################################\n')
            #find element and click
            '''Click on job feed box'''
            try:
                driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div').click()
                search_result(driver, search_query, output_json_per_category)
                end_time = time.time()
                driver.quit()
                print('############################### Total processed time: '+ str(int(end_time-start_time))+' seconds ###########################################\n')
            except:
                try:
                    driver.find_element_by_class_name('IRgoif').click()
                    search_result(driver, search_query, output_json_per_category)
                    end_time = time.time()
                    driver.quit()
                    print('############################### Total processed time: '+ str(int(end_time-start_time))+' seconds ###########################################\n')
                except:
                    continue
            
    display.stop()