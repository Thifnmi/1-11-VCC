from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Thread, Lock
import concurrent.futures
from multiprocessing import Process
import time
import csv
import re


browser = None
# links is list link post
links = []
# urls is list link page
urls = []
lock = Lock()

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")


def gen_url(num):
    url = "https://bizflycloud.vn/tin-tuc/tin-tuc/trang-"+str(num)+".htm"
    print(url)
    urls.append(url)
    # return urls


def get_total_page(options):
    global browser
    url = "https://bizflycloud.vn/tin-tuc/tin-tuc.htm"
    browser = webdriver.Chrome(
        executable_path='chromedriver.exe', chrome_options=options)
    browser.get(url)
    browser.maximize_window()
    total_page = browser.find_element_by_class_name("total-page").text
    return int(total_page)


def get_link(url):
    global browser
    with lock:
        browser.get(url)
        print(url)
        # posts = browser.find_elements_by_class_name("blog-highlight")
        # for post in posts:
        link_tag = browser.find_elements_by_class_name("entry-title")
        for link in link_tag:
            if link.get_attribute("href") not in links:
                print(f'get {link.get_attribute("href")} from {url}')
                links.append(link.get_attribute("href"))


def get_link1(url):
    global browser
    browser.get(url)
    print(url)
    # posts = browser.find_elements_by_class_name("blog-highlight")
    # for post in posts:
    link_tag = browser.find_elements_by_class_name("entry-title")
    for link in link_tag:
        if link.get_attribute("href") not in links:
            print(f'get {link.get_attribute("href")} from {url}')
            links.append(link.get_attribute("href"))


def get_linkkk(options):
    global links, browser
    print("runnnnnn")
    for i in range(1, int(get_total_page(options))+1):
        url = "https://bizflycloud.vn/tin-tuc/tin-tuc/trang-"+str(i)+".htm"
        print(url)
        browser = webdriver.Chrome(
            executable_path='chromedriver.exe', chrome_options=options)
        browser.get(url)
        browser.maximize_window()
        if len(links) < 300:
            link_tag = browser.find_elements_by_class_name("entry-title")
            for link in link_tag:
                if link.get_attribute("href") not in links:
                    links.append(link.get_attribute("href"))
    print(len(links))


def write_file(file_name, data):
    print(f"Start write file name {file_name}")
    header = ['name', 'title', 'content', 'created date', 'url']
    with open(file_name, "w", encoding="utf-8", newline="") as file:
        write_hander = csv.writer(file)
        write_hander.writerow(header)
        write_hander.writerow(data)
    file.close()
    print(f"Done file {file_name}")


# print(links)


# name/title, content, created date, url
def crawler(link):
    global browser
    print(f"recived link: {link}")
    with lock:
        print(f"get link: {link}")
        browser.get(link)
        title = browser.find_element_by_class_name("page-title-content").text
        # delimiters = '. ', ' ', '?', '! ', '(', ')', ': ', ' - ', '"', '/', ' | '
        # regex_pattern = "|".join(map(re.escape, title))
        # file_name = "_".join(re.split(regex_pattern, title))
        file_name = re.sub('\W+', '', title)
        # file_name = "".join(e for e in title if e.isalnum())
        file_name = "result\\" + file_name + ".csv"
        name = browser.find_element_by_class_name("author").text
        created_date = browser.find_element_by_class_name("read-time").text
        content_tag = browser.find_element_by_class_name("detail-content")
        contents = content_tag.find_elements_by_tag_name("p")
        contents = (content.text for content in contents)
        content = " ".join(content for content in contents if content)
        data = (name, title, content, created_date, link)
        write_file(file_name, data)


def crawler1(link):
    global browser
    print(f"recived link: {link}")
    print(f"get link: {link}")
    browser.get(link)
    title = browser.find_element_by_class_name("page-title-content").text
    file_name = re.sub('\W+', '', title)
    # file_name = "".join(e for e in title if e.isalnum())
    file_name = "result\\" + file_name + ".csv"
    name = browser.find_element_by_class_name("author").text
    created_date = browser.find_element_by_class_name("read-time").text
    content_tag = browser.find_element_by_class_name("detail-content")
    contents = content_tag.find_elements_by_tag_name("p")
    contents = (content.text for content in contents)
    content = " ".join(content for content in contents if content)
    data = (name, title, content, created_date, link)
    write_file(file_name, data)


def crawler_default():
    global browser, links
    t1 = time.perf_counter()
    for link in links:
        print(links.index(link))
        crawler(browser, link)
    browser.close()

    print(f"Done in {time.perf_counter() - t1} second(s)")


def crawler_with_thread():
    global browser, links
    threads = []
    t1 = time.perf_counter()
    for link in links:
        t = Thread(target=crawler, args=(browser, link, ))
        t.start()
        threads.append(t)
    # for thread in threads:
    #     thread.join()
    print(f"Done crawler with thread in {time.perf_counter() - t1} second(s)")


def crawler_with_process():
    global browser, links
    threads = []
    t1 = time.perf_counter()
    for link in links:
        t = Process(target=crawler, args=(browser, link, ))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    print(f"Done craler with process in {time.perf_counter() - t1} second(s)")
# setup_option_crawl()
# print(get_total_page(options))

# setup_option_crawl()
# get_linkkk(options)
# print(f"Done get links in {time.perf_counter() - t1 } sencond(S)")
# crawler_with_thread()
# crawler_with_process()


def pro():
    t1 = time.perf_counter()
    # total_page = int(get_total_page(options))+1
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(gen_url, range(1, get_total_page(options)+1))
        # executor.map(gen_url, range(1, get_total_page(options)+1))
        # for page in total_page:
        #     executor.submit(gen_url, str(page))

    # for url in urls:
    #     print(url)
    # urls = [url for url in urls]
    with concurrent.futures.ProcessPoolExecutor(8) as executor1:
        executor1.map(get_link1, urls)
        # for url in urls:
        #     executor1.submit(get_link, url)
    print(urls)
    print(links)
    # print(len(urls), len(links))

    with concurrent.futures.ProcessPoolExecutor(8) as executor2:
        executor2.map(crawler1, links)
        # for link in links:
        #     executor2.submit(crawler, link)

    print(f"{time.perf_counter() - t1} seconds")


def thre():
    # global urls, links
    t1 = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(gen_url, range(1, get_total_page(options)+1))

    with concurrent.futures.ThreadPoolExecutor() as executor1:
        for url in urls:
            executor1.submit(get_link, url)
    print(urls)
    print(links)
    print(len(urls), len(links))

    with concurrent.futures.ThreadPoolExecutor() as executor2:
        for link in links:
            executor2.submit(crawler, link)

    print(f"{time.perf_counter() - t1} seconds")


pro()
# thre()