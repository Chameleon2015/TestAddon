import re, xbmcaddon, urllib, urllib2
from resources.modules import modules, yt

ADDON_ID = 'plugin.video.entertainmentlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
BaseURL = 'http://chameleon.x10host.com/test/links/'

#********** Test Text Files YouTube**********
LMovies = 'NRLGAMESYT.txt'
LKids = 'NRLGAMESYT.txt'
LSports = 'NRLGAMESYT.txt'


def AllLiveTV():
	LiveMovies()
	LiveKids()
	LiveSport()
	
	modules.AUTO_VIEW('500')

def LiveMovies():
	link = modules.OPEN_URL(BaseURL + LMovies).replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	for name,url,iconimage,fanart,description in match:
		modules.addYTVID('',name,url,9,iconimage,fanart,'',description)
	modules.AUTO_VIEW('500')

def LiveKids():
	link = modules.OPEN_URL(BaseURL + LKids).replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	for name,url,iconimage,fanart,description in match:
		modules.addYTVID('',name,url,9,iconimage,fanart,'',description)
	modules.AUTO_VIEW('500')

def LiveSport():
	link = modules.OPEN_URL(BaseURL + LSports).replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	for name,url,iconimage,fanart,description in match:
		modules.addYTVID('',name,url,9,iconimage,fanart,'',description)
	modules.AUTO_VIEW('500')