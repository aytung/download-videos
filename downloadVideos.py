import bs4 as bs 
import subprocess
import urllib.parse
import sys
from urllib.request import Request, urlopen
from urllib.parse import quote

# need to use special header so that
# website will accept request
def getSoup(url):
	# site = 'https://dictionary.goo.ne.jp/jn/'
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = Request(url, headers=hdr)
	page = urlopen(req)
	soup = bs.BeautifulSoup(page, 'lxml')

	return soup

def findVideoUrls(soup):
    videos = soup.find('div', {"class" : "videoUList"}).find_all("span", {"class" : "title"})
    return [video.a.get('href') for video in videos]

url = sys.argv[1]
soup = getSoup(url)
video_urls = findVideoUrls(soup)
tld = urllib.parse.urlparse(url).netloc


for video_number, video_url in enumerate(video_urls, 1):
    print("Processing " + str(video_number) + " of " + str(len(video_urls)))
    subprocess.run(["youtube-dl", tld + video_url])
    
