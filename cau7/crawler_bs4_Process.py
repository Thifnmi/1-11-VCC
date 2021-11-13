from urllib.request import urlopen
import re
import csv
from bs4 import BeautifulSoup
import time
from multiprocessing import Process, Manager


manager = Manager()
urls = []
url_post = manager.list()


# kill all script and style elements
def kill_script(soup):
    for script in soup(["script", "style"]):
        script.extract()


def gen_url(num):
    url = "https://bizflycloud.vn/tin-tuc/tin-tuc/trang-"+str(num)+".htm"
    # print(url)
    urls.append(url)


def get_total_page():
    url = "https://bizflycloud.vn/tin-tuc/tin-tuc.htm"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    kill_script(soup)
    total_page = soup.find('li', attrs={'class': "total-page"}).text
    for num in range(1, int(total_page)+1):
        gen_url(num)


def get_link_post(url_page):
    print(url_page)
    html = urlopen(url_page).read()
    soup = BeautifulSoup(html, features="html.parser")
    kill_script(soup)
    post_tag = soup.find_all(
        'a', attrs={'class': 'entry-title td-module-title'})
    for post in post_tag:
        if(f"https://bizflycloud.vn{post['href']}" not in url_post):
            print(f"https://bizflycloud.vn{post['href']}")
            url_post.append(f"https://bizflycloud.vn{post['href']}")
    print(f"{len(post_tag)}, {len(url_post)}")


def write_file(file_name, data):
    print(f"Start write file name {file_name}")
    header = ['name', 'title', 'content', 'created date', 'url']
    with open(file_name, "w", encoding="utf-8", newline="") as file:
        write_hander = csv.writer(file)
        write_hander.writerow(header)
        write_hander.writerow(data)
    # file.close()
    print(f"Done file {file_name}")


def crawler(url):
    print(url)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    kill_script(soup)
    title = soup.title.string
    file_name = re.sub('\W+', '', title)
    file_name = "result_Process\\" + file_name + ".csv"
    author = soup.find('div', attrs={'class': 'author'}).text
    created_date = soup.find('div', attrs={'class': 'divided read-time'}).text
    content_tag = soup.find(
        'div', attrs={'class': 'col-12 col-lg-8 detail-content'})
    contents = content_tag.find_all('p')
    content = " ".join(content.text for content in contents if content)
    # print(f"{author}, {created_date}, {content}")
    data = (author, title, content, created_date, url)
    # print(file_name, data)
    write_file(file_name, data)


def get_link_post_with_process():
    get_total_page()
    processes = []
    for url in urls:
        p = Process(target=get_link_post, args=[url])
        p.start()
        processes.append(p)
    for process in processes:
        process.join()


def crawler_with_process(url_post):
    processes = []
    t1 = time.perf_counter()
    for url in url_post:
        p = Process(target=crawler, args=[url])
        p.start()
        processes.append(p)
    for process in processes:
        process.join()

    print(f"Done in {time.perf_counter() - t1} seconds")


def crawler_multi_process(url_post):
    t1 = time.perf_counter()
    get_link_post_with_process()
    crawler_with_process(url_post)
    print(f"Done in {time.perf_counter() - t1} seconds")


if __name__ == "__main__":
    print("Start crawler with multi process")
    crawler_multi_process(url_post)
    print("Done crawler with multi thread")
