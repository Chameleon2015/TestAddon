import re, sys, os, xbmc, xbmcaddon, xbmcplugin, xbmcgui, urllib, urllib2
from resources.modules import modules, yt


ADDON_ID = 'plugin.video.entertainmentlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
BaseURL = 'http://chameleon.x10host.com/test/links/'
ART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/icons/'))
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))

#********** Test Text Files YouTube**********
LEntertainment = 'LiVE/LIVETV.m3u'
LMovies = 'LiVE/LIVEMOVIES.m3u'
LKids = 'LiVE/LIVEKIDS.m3u'
LSports = 'LiVE/LIVESPORTS.m3u'
LSSports = 'LiVE/LiveStalkerSport.m3u'

def AllLiveTV():
	LiveEntertainment()
	LiveMovies()
	LiveKids()
	LiveSport()
	
	modules.AUTO_VIEW('518')

def LiveEntertainment():
	url = BaseURL + LEntertainment
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')

def LiveMovies():
	url = BaseURL + LMovies
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')

def LiveKids():
	url = BaseURL + LKids
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')

def LiveSport():
	url = BaseURL + LSports
	modules.TestMenuDIR(url)
	modules.addDir('IPTV Stalker','',26,ART+'IPTVStalker.png',FANART,'')
	modules.AUTO_VIEW('518')

def Music():
	modules.addDir('MTV TEST','',2,ART+'UKTop100.png',FANART,'')
	modules.AUTO_VIEW('500')

def Adult_Live():
	modules.addDir('Adult Live TEST','',2,ART+'UKTop100.png',FANART,'')
	modules.AUTO_VIEW('500')

def LiveStalkerSport():
	url = BaseURL + LSSports
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')