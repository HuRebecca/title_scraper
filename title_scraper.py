from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#once on the webpage with list of all episodes, scrape to a csv
def scrape_titles(show_name):
    #create file
    show_name = show_name.replace(' ', '_')
    filename = str(show_name) + '.txt'
    f = open(filename, 'w')

    #parse html, grab each episode title, write to a file
    soup_level5 = soup(driver.page_source, 'html.parser')

    #grab each episode title
    titles = soup_level5.find_all('td', class_ = 'summary')

    #write to file
    for title in enumerate(titles):
        episode_title = title.get_text()
        f.write(episode_title + '\n')

    f.close()

url = 'https://en.wikipedia.org/wiki/List_of_longest-running_scripted_U.S._primetime_television_series'

#open webdriver. get url
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

#parse the base webpage
soup_level1 = soup(driver.page_source, 'html.parser')

#grab each show name
shows = soup_level1.find_all('i')
shows = shows[2:]

for i, show in enumerate(shows):
    #click each show
    #show = show[1]
    try:
        tv_show = show.a.string #.self #.a.self
        print(" :o) TV SHOW NAME: " + str(tv_show))
        print(type(tv_show))
        show_button = driver.find_element_by_link_text(str(tv_show))
        print(":o) SHOW: " + str(tv_show))
        show_button.click()
        time.sleep(3)

        list_of_episodes_button = driver.find_element_by_link_text('list of episodes')
        scrape_titles(tv_show)
    except AttributeError:
        continue
    else:
        continue

    #except selenium.common.exceptions.NoSuchElementException:
    #    print('NoSuchElementException!!!!! :o(')
    #    continue
