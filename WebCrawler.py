import urllib.parse, urllib.request, urllib.error
import ssl
import random
from bs4 import BeautifulSoup

def crawl(url):

    ctx=ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE

    html=urllib.request.urlopen(url, context=ctx).read()
    clean=BeautifulSoup(html, 'html.parser')

    tags=clean('a')

    all_links=list()

    for tag in tags:
        if ('twitter' in tag.get('href',None))==False:
            all_links.append(tag.get('href',None))

    temp=random.randrange(0,(len(all_links)-1))
    return all_links[temp]

URL=crawl(input('Enter the starting url: '))
i=0
while i<9:
    print(URL)
    URL=crawl(URL)
    i=i+1

print(URL)
