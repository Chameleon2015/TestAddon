import xbmc, xbmcgui, xbmcplugin, xbmcaddon, os, sys
import time
import urllib, urllib2
import re, urlparse, json
import hashlib
from resources.modules import modules, yt
from resources.modules.parsers import parser
from resources.menus import LiveTvMenu, ODMenu
from resources.scrapers import Wsimpsons
from addon.common.addon import Addon
from addon.common.net import Net

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Variables **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PATH = "Entertainment Lounge"
VERSION = "0.0.7"
ADDON_ID = 'plugin.video.entertainmentlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
HOME = ADDON.getAddonInfo('path')
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID, 'icon.png'))
ART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/icons/'))
BaseURL = 'http://chameleon.x10host.com/test/links/'


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Menu's **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def HOME_MENU():
	#modules.addDir('Test Menu', BaseURL + 'LiVE/Entertainment.m3u',27,ART+'TestMenu.png','','')
	#modules.addDir('Watch Simpsons Test','',32,ART+'TestMenu.png','','')
	modules.addDir('Live TV','',1,ART+'LiveTv.png','','')
	modules.addDir('OnDemand','',3,ART+'OnDemand.png',FANART,'')
	modules.addDir('Movies','',7,ART+'Movies.png',FANART,'')
	modules.addDir('Adult','',6,ART+'Adult.png',FANART,'')
	modules.addDir('Music','',8,ART+'Music.png',FANART,'')
	
	AUTO_VIEW('518')

def LIVE_TV():
	modules.addDir('All Channels','http://chameleon.x10host.com/test/links/TestChannel.php',20,ART+'LiveTv.png','','')
	parser.Categories('http://chameleon.x10host.com/test/links/TestChannel.php')
	AUTO_VIEW('518')

def On_Demand():
	modules.addDir('TV Shows','',2,ART+'TvShows.png',FANART,'')
	modules.addDir('24/7 Shows','',11,ART+'24_7TVShows.png',FANART,'')
	modules.addDir('Sports Replays','',4,ART+'SportReplay.png',FANART,'')
	AUTO_VIEW('500')

def SPORTS_RP():
	modules.addDir('NRL','',10,ART+'LiveTv.png','','')
	modules.addDir('Match Of The Day','',25,ART+'LiveTv.png','','')
	AUTO_VIEW('500')

def Adult_XxX():
	modules.addDir('Live','',30,ART+'LiveTv.png',FANART,'')
	modules.addDir('OnDemand','',12,ART+'OnDemand.png',FANART,'')
	AUTO_VIEW('500')

def MUSIC():
	modules.addDir('Hot UK Top 100','',2,ART+'UKTop100.png',FANART,'')
	AUTO_VIEW('500')

def IPTVplayLevel():
	tvscraper.playLevel()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Modules **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Text_Boxes(heading,anounce):
  class TextBox():
    WINDOW=10147
    CONTROL_LABEL=1
    CONTROL_TEXTBOX=5
    def __init__(self,*args,**kwargs):
      xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
      self.win=xbmcgui.Window(self.WINDOW) # get window
      xbmc.sleep(500) # give window time to initialize
      self.setControls()
    def setControls(self):
      self.win.getControl(self.CONTROL_LABEL).setLabel(heading) # set heading
      try: f=open(anounce); text=f.read()
      except: text=anounce
      self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
      return
  TextBox() 

def AUTO_VIEW(Vmode = ''):
	xbmc.executebuiltin("Container.SetViewMode(" + Vmode +")")

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** ADDON SWITCH **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)


if mode == None		: HOME_MENU()
elif mode == 1		: LIVE_TV()
elif mode == 2		: ODMenu.TV_SHOWS()
elif mode == 3		: On_Demand()
elif mode == 4		: SPORTS_RP()
elif mode == 6		: Adult_XxX()
elif mode == 7		: GenVideos.ScrapData()
elif mode == 8		: MUSIC()
elif mode == 9		: yt.PlayVideo(url)
elif mode == 10		: ODMenu.NRL_YT_RP()
elif mode == 11		: ODMenu.TwentyFour_Seven()
elif mode == 12		: ODMenu.Adult_OD()
elif mode == 19		: modules.Play_URL(name, url, iconimage)
elif mode == 20		: LiveTvMenu.AllLiveTV(url)
elif mode == 21		: LiveTvMenu.LiveMovies()
elif mode == 22		: LiveTvMenu.LiveKids()
elif mode == 23		: LiveTvMenu.LiveSport()
elif mode == 24		: LiveTvMenu.LiveEntertainment()
elif mode == 25		: ODMenu.YT_Match_Of_The_Day()
elif mode == 26		: LiveTvMenu.LiveStalkerSport()
elif mode == 27		: modules.TestMenuDIR(url)
elif mode == 28		: modules.TestPlayUrl(name, url, iconimage)
elif mode == 29		: LiveTvMenu.Music()
elif mode == 30		: LiveTvMenu.Adult_Live()
elif mode == 31		: Wsimpsons.ParseURL(url)
elif mode == 32		: ODMenu.watchSimp()
elif mode == 33		: parser.Categories(url)
elif mode == 34		: parser.Category(name, url)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** ADDON FINISH **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
xbmcplugin.endOfDirectory(int(sys.argv[1]))