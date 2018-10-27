import mechanicalsoup
import json
from random import randint
import os

## https://developers.whatismybrowser.com/useragents/explore/
agents = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Mwendo/1.1.5 Safari/537.21',
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991'
]
index = randint(0, len(agents)-1)
agent = agents[index]
url = 'https://www.glassdoor.ie/Job/sydney-research-engineer-jobs-SRCH_IL.0,6_IC2235932_KO7,24.htm'
browser = mechanicalsoup.StatefulBrowser(
    soup_config = {'features': 'lxml'},  # Use the lxml HTML parser
    raise_on_404 = True,
    user_agent = agent,
)
browser.open(url)
soup = browser.get_current_page()
links = soup.find_all(name='div',attrs={'class':'flexbox jobTitle'})
locations = soup.find_all(name='div',attrs={'class':'flexbox empLoc'})
print(len(links), len(locations))
base_url = 'https://www.glassdoor.com'

# for i in links:
#     print({'title':i.div.a.string, 'url':base_url + i.div.a['href']})

# for i in locations:
#     print({'employer':i.div.contents[0].strip(), 'location':i.div.contents[1].string})

title_url = [{'title':i.div.a.string, 'url':base_url + i.div.a['href']} for i in links]
emp_loc = [{'employer':i.div.contents[0].strip(), 'location':i.div.contents[1].string} for i in locations]

dict_list = list(zip(title_url, emp_loc))
# print(dict_list[0])
r = [{**i[0], **i[1]} for i in zip(title_url, emp_loc)]
print(r)

ans = soup.prettify()
# print(ans)
print(index, agent)
filename = os.path.join(os.getcwd(), 'spider.txt')
print(filename)
with open(filename, 'w') as text_file:
    print(ans, file=text_file)
browser.close()

# import sys
# print(os.getcwd())
# print(sys.argv[0])
# print(os.path.dirname(os.path.realpath('__file__')))
