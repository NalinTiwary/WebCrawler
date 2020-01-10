# WebCrawler
My code for a Web Crawler. This code uses urllib to extract HTML code for Web Scrapping and  'cleans' up the code using Beautiful Soup. The code then recursively looks for hyperlinks embedded in the page and follows them.

## Beautiful Soup
Pygame is a python library used commonly to process HTML code in Python Programs.

### Installation 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Beautiful Soup.
```bash
pip install beautifulsoup4
```
### Usage

```python
import beautifulsoup4

clean=BeautifulSoup(html, 'html.parser')  #Using Beautiful Soup to clean retrived HTML5 code stored in 'html'
tags=clean('a')  #retrieving every anchor tag in the cleaned code(to get every embedded hyperlinks from the page)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
