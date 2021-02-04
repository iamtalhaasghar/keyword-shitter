from selenium import webdriver

master_keyword = input('Enter something to search for: ')
total_keywords = int(input('Enter maximum number of keywords to fetch: '))

opts = webdriver.ChromeOptions()
opts.binary_location = r"C:\chrome 74.0\Chrome-bin\chrome.exe"
driver = webdriver.Chrome(options = opts)
driver.get('https://keywordshitter.com/')
text_area = driver.find_element_by_id('input')
text_area.send_keys(master_keyword)
start_job = driver.find_element_by_id('startjob')
start_job.click()
keyword_div = driver.find_element_by_id('numofkeywords')
shouldLoop = True
keywords_list = list
while(shouldLoop):
    keyword_count_text = keyword_div.text.split(':')
    keyword_count_1 = int(keyword_count_text[0])
    keyword_count_2 = int(keyword_count_text[1])
    if(keyword_count_1 >= total_keywords or keyword_count_2 >= total_keywords):
        start_job.click()
        stop_alert = driver.switch_to.alert
        stop_alert.dismiss()
        shouldLoop = False
        data = text_area.get_attribute('value')
        keywords_list = data.split('\n')
        keywords_list = [i for i in keywords_list if(len(i.strip())!=0)]

for k in keywords_list:
    print(k)
