from urllib.request import urlopen
import re
from bs4 import BeautifulSoup


url = "https://bizflycloud.vn/tin-tuc/loi-ich-cua" + \
    "-cdn-trong-livestreaming-20210622162336569.htm"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()

# get text
text_raw = soup.select(".detail-content")

text = ""

for el in text_raw:
    text = text + el.get_text()


# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines

contents = ' '.join(chunk for chunk in chunks if chunk)
# print(contents)
delimiters = '.', '\xa0', '?', '!', '(', ')', '|', ':',
', ', '  ', '"', ' – ', ',…'
regex_pattern = "|".join(map(re.escape, delimiters))
contents = " ".join(re.split(regex_pattern, contents))

file_content = open("content.txt", "w", encoding="utf-8")
file_content.write(contents)
file_content.close()

dict_words = {}
for content in contents.split(" "):
    if content in dict_words:
        dict_words[content] = dict_words[content] + 1
    else:
        dict_words[content] = 1

file_out = open("out.txt", "w", encoding="utf-8")
for word, value in dict_words.items():
    string = f"{word}: {value}"
    file_out.write('%s: %s\n' % (word, value))
file_out.close()
