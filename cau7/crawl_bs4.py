from urllib.request import urlopen
from bs4 import BeautifulSoup
import time


urls = []
url_post = []


# kill all script and style elements
def kill_script(soup):
    for script in soup(["script", "style"]):
        script.extract()


def gen_url(num):
    url = "https://bizflycloud.vn/tin-tuc/tin-tuc/trang-"+str(num)+".htm"
    # print(url)
    urls.append(url)


def get_link_post(url_page):
    print(url_page)
    html = urlopen(url_page).read()
    soup = BeautifulSoup(html, features="html.parser")
    post_tag = soup.find_all(
        'a', attrs={'class': 'entry-title td-module-title'})
    for post in post_tag:
        if(f"https://bizflycloud.vn/tin-tuc{post['href']}" not in url_post):
            print(f"https://bizflycloud.vn/tin-tuc{post['href']}")
            url_post.append(f"https://bizflycloud.vn/tin-tuc{post['href']}")
    print(len(post_tag), len(url_post))


def get_total_page():
    url = "https://bizflycloud.vn/tin-tuc/tin-tuc.htm"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    kill_script(soup)
    total_page = soup.find('li', attrs={'class': "total-page"}).text
    for num in range(1, int(total_page)+1):
        gen_url(num)
    # print(urls)


t1 = time.perf_counter()
get_total_page()
for url in urls:
    get_link_post(url)
print(f"Done in {time.perf_counter() - t1} seconds")
