import xbmc, xbmcgui, xbmcplugin, xbmcaddon, os, sys
import time
import urllib, urllib2
import re
from resources.modules import modules, yt
from resources.menus import SportsReplayMenu, LiveTvMenu
from addon.common.addon import Addon
from addon.common.net import Net

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Variables **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PATH = "Entertainment Lounge"
VERSION = "0.0.1"
ADDON_ID = 'plugin.video.entertainmentlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
HOME = ADDON.getAddonInfo('path')
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID, 'icon.png'))
ART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/icons/'))
BaseURL = 'http://chameleon.x10host.com/test/links/'

#********** Test Text Files YouTube**********


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Menu's **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def HOME_MENU():
	modules.addDir('Live TV','',1,ART+'LiveTv.png','','')
#	modules.addDir('TV Shows','',2,ART+'TvShows.png',FANART,'')
#	modules.addDir('Live Sports','',3,ART+'LiveSport.png',FANART,'')
	modules.addDir('Sports Replays','',4,ART+'SportReplay.png',FANART,'')
#	modules.addDir('Live Movies','',6,ART+'LiveMovies.png',FANART,'')
#	modules.addDir('Movies','',7,ART+'Movies.png',FANART,'')
#	modules.addDir('Music','',8,ART+'Music.png',FANART,'')
	AUTO_VIEW('500')

def LIVE_TV():
	modules.addDir('All','',20,ART+'LiveTv.png','','')
	modules.addDir('Movies','',21,ART+'LiveTv.png','','')
	modules.addDir('Kids','',22,ART+'LiveTv.png','','')
	modules.addDir('Sport','',23,ART+'LiveTv.png','','')
	AUTO_VIEW('500')

def TV_SHOWS():
	modules.addDir('TV Shows','',2,ART+'TvShows.png',FANART,'')
	AUTO_VIEW('500')

def LIVE_SPORTS():
	modules.addDir('Live Sports','',2,ART+'LiveSport.png',FANART,'')
	AUTO_VIEW('500')

def SPORTS_RP():
	modules.addDir('NRL','',10,ART+'LiveTv.png','','')
	AUTO_VIEW('500')

def LIVE_MOVIES():
	modules.addDir('Live Movies','',2,ART+'family.png',FANART,'')
	AUTO_VIEW('500')

def MOVIES_OD():
	modules.addDir('Movies','',2,ART+'family.png',FANART,'')
	AUTO_VIEW('500')

def MUSIC():
	modules.addDir('Movies','',2,ART+'family.png',FANART,'')
	AUTO_VIEW('500')

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

def AUTO_VIEW(content = ''):
    if not content:
        return

    xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view') != 'true':
        return

    if content == 'addons':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting('addon_view'))
    else:
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting('default-view'))

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
elif mode == 2		: TV_SHOWS()
elif mode == 3		: LIVE_SPORTS()
elif mode == 4		: SPORTS_RP()
elif mode == 6		: LIVE_MOVIES()
elif mode == 7		: MOVIES_OD()
elif mode == 8		: MUSIC()
elif mode == 9		: yt.PlayVideo(url)
elif mode == 10		: SportsReplayMenu.NRL_YT_RP()
elif mode == 20		: LiveTvMenu.AllLiveTV()
elif mode == 21		: LiveTvMenu.LiveMovies()
elif mode == 22		: LiveTvMenu.LiveKids()
elif mode == 23		: LiveTvMenu.LiveSport()


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** ADDON FINISH **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
xbmcplugin.endOfDirectory(int(sys.argv[1]))