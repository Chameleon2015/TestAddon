import re, xbmcaddon, xbmcplugin, xbmcgui, urllib, urllib2, sys
from resources.modules import modules, yt

ADDON_ID = 'plugin.video.entertainmentlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
BaseURL = 'http://chameleon.x10host.com/test/links/'

#********** Test Text Files YouTube**********
NrlYTGames = 'NRLGAMESYT.txt'
YTMatchOfTheDay = 'YTMatchOfTheDay.txt'

def NRL_YT_RP():
	link = modules.OPEN_URL(BaseURL + NrlYTGames).replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	for name,url,iconimage,fanart,description in match:
		modules.addYTVID('',name,url,9,iconimage,fanart,'',description)
	modules.AUTO_VIEW('500')

def YT_Match_Of_The_Day():
	link = modules.OPEN_URL(BaseURL + YTMatchOfTheDay).replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	for name,url,iconimage,fanart,description in match:
		image = iconimage
		addon_handle = int(sys.argv[1])
		xbmcplugin.setContent(addon_handle, 'movies')
		li = xbmcgui.ListItem(name, description, iconImage=image)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	modules.AUTO_VIEW('500')