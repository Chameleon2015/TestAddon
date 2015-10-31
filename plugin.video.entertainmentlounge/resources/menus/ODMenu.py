import re, sys, os, xbmc, xbmcaddon, xbmcplugin, xbmcgui, urllib, urllib2
from resources.modules import modules, yt


ADDON_ID = 'plugin.video.entertainmentlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
BaseURL = 'http://chameleon.x10host.com/test/links/'
ART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/icons/'))
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))

#********** Test Text Files YouTube**********
TwentyFS = 'ONDeMaND/TWENTYFOURSEVEN.m3u'
NrlYTGames = 'ONDeMaND/NRLGAMESYT.m3u'
YTMatchOfTheDay = 'ONDeMaND/YTMatchOfTheDay.m3u'

def TV_SHOWS():
	modules.addDir('TV Shows','',2,ART+'TvShows.png',FANART,'')
	AUTO_VIEW('500')

def TwentyFour_Seven():
	url = BaseURL + TwentyFS
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')

def NRL_YT_RP():
	url = BaseURL + NrlYTGames
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')

def YT_Match_Of_The_Day():
	url = BaseURL + YTMatchOfTheDay
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')

def MOVIES_OD():
	modules.addDir('Movies','',2,ART+'MoviesOD.png',FANART,'')
	modules.AUTO_VIEW('500')

def Adult_OD():
	modules.addDir('Adult OD Test','',2,ART+'MoviesOD.png',FANART,'')
	modules.AUTO_VIEW('500')