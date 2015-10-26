import re, xbmcaddon, urllib, urllib2
from resources.modules import modules, yt

ADDON_ID = 'plugin.video.entertainmentlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
BaseURL = 'http://chameleon.x10host.com/test/links/'

#********** Test Text Files YouTube**********
NrlYTGames = 'NRLGAMESYT.txt'

def NRL_YT_RP():
	link = modules.OPEN_URL(BaseURL + NrlYTGames).replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	for name,url,iconimage,fanart,description in match:
		modules.addYTVID('',name,url,9,iconimage,fanart,'',description)
	modules.AUTO_VIEW('500')