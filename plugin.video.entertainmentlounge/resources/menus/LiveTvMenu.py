import re, sys, os, xbmc, xbmcaddon, xbmcplugin, xbmcgui, urllib, urllib2
from resources.modules import modules, yt

ADDON_ID = 'plugin.video.entertainmentlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
BaseURL = 'http://chameleon.x10host.com/test/links/'
ART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/icons/'))
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))

#********** Test Text Files YouTube**********
LEntertainment = 'LIVETV.txt'
LMovies = 'LIVEMOVIES.txt'
LKids = 'LIVEKIDS.txt'
LSports = 'LIVESPORTS.txt'
LSSports = 'LiveStalkerSport.txt'
TwentyFS = 'TWENTYFOURSEVEN.txt'


def AllLiveTV():
	LiveEntertainment()
	LiveMovies()
	LiveKids()
	LiveSport()
	
	modules.AUTO_VIEW('518')

def LiveEntertainment():
	link = modules.OPEN_URL(BaseURL + LEntertainment).replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	for name,url,iconimage,fanart,description in match:
		image = iconimage
		addon_handle = int(sys.argv[1])
		xbmcplugin.setContent(addon_handle, 'movies')
		li = xbmcgui.ListItem(name, description, iconImage=image)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

	modules.AUTO_VIEW('518')

def LiveMovies():
	link = modules.OPEN_URL(BaseURL + LMovies).replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	for name,url,iconimage,fanart,description in match:
		image = iconimage
		addon_handle = int(sys.argv[1])
		xbmcplugin.setContent(addon_handle, 'movies')
		li = xbmcgui.ListItem(name, description, iconImage=image)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	modules.AUTO_VIEW('518')

def LiveKids():
	link = modules.OPEN_URL(BaseURL + LKids).replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	for name,url,iconimage,fanart,description in match:
		image = iconimage
		addon_handle = int(sys.argv[1])
		xbmcplugin.setContent(addon_handle, 'movies')
		li = xbmcgui.ListItem(name, description, iconImage=image)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	modules.AUTO_VIEW('518')

def LiveSport():
	link = modules.OPEN_URL(BaseURL + LSports).replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	for name,url,iconimage,fanart,description in match:
		image = iconimage
		addon_handle = int(sys.argv[1])
		xbmcplugin.setContent(addon_handle, 'movies')
		li = xbmcgui.ListItem(name, description, iconImage=image)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
		
	modules.addDir('IPTV Stalker Live Sports','',26,ART+'LiveSport.png',FANART,'')
	modules.AUTO_VIEW('518')

def TwentyFour_Seven():
	link = modules.OPEN_URL(BaseURL + TwentyFS).replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	for name,url,iconimage,fanart,description in match:
		image = iconimage
		addon_handle = int(sys.argv[1])
		xbmcplugin.setContent(addon_handle, 'movies')
		li = xbmcgui.ListItem(name, description, iconImage=image)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	modules.AUTO_VIEW('518')

def LiveStalkerSport():
	link = modules.OPEN_URL(BaseURL + LSSports).replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	for name,url,iconimage,fanart,description in match:
		image = iconimage
		addon_handle = int(sys.argv[1])
		xbmcplugin.setContent(addon_handle, 'movies')
		li = xbmcgui.ListItem(name, description, iconImage=image)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	modules.AUTO_VIEW('518')