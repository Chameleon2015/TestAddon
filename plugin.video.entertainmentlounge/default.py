import xbmc, xbmcgui, xbmcplugin, xbmcaddon, os, sys
import time, urllib, urllib2
import re, urlparse, json, hashlib

import server, config, load_channels

#import PremiumTV
#from PremiumTV import *

from resources.modules import modules, yt
from resources.modules.parsers import parser
from resources.menus import LiveTvMenu, ODMenu
from resources.scrapers import Wsimpsons
from addon.common.addon import Addon
from addon.common.net import Net

#---------------------------------------------------------------------------------------------------------------
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addondir    = xbmc.translatePath( addon.getAddonInfo('profile') ) 

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
go = True;
#---------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Variables **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PATH = "Entertainment Lounge"
VERSION = "0.0.10"
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
	modules.addDir('ChristmasFilms','http://chameleon.x10host.com/test/links/newtest/ChristmasFilms.php',34,ART+'LiveTv.png','','')
	modules.addDir('Movies','',7,ART+'Movies.png',FANART,'')
	modules.addDir('Adult','',6,ART+'Adult.png',FANART,'')
	modules.addDir('Music','',8,ART+'Music.png',FANART,'')
	xbmcplugin.endOfDirectory(addon_handle);
	AUTO_VIEW('504')

def LIVE_TV():
	try:
		modules.addDir('All Channels','http://chameleon.x10host.com/test/links/newtest/?list=GetCat',20,ART+'LiveTv.png','','')
	except:
		pass
	
	try:
		parser.Categories('GetCat')
	except:
		pass
	
	try:
		modules.addDir('Premium TV','',35,ART+'PremiumTV.png','','')
	except:
		pass
	
	AUTO_VIEW('504')

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

def PremiumTVMenu():
	global portal_1, portal_2, portal_3, portal_4, portal_5, portal_6, portal_7, portal_8, portal_9, portal_10, go;
	
	#todo - check none portal

	if go:
		addPortal(portal_1);
		addPortal(portal_2);
		addPortal(portal_3);
		addPortal(portal_4);
		addPortal(portal_5);
		addPortal(portal_6);
		addPortal(portal_7);
		addPortal(portal_8);
		addPortal(portal_9);
		addPortal(portal_10);
	
		xbmcplugin.endOfDirectory(addon_handle);

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

#---------------------------------------------------------------------------------------------------------------

def addPortal(portal):


	if portal['url'] == '':
		return;

	url = build_url({
		'mode': 'genres', 
		'portal' : json.dumps(portal)
		});
	
	cmd = 'XBMC.RunPlugin(' + base_url + '?mode=cache&stalker_url=' + portal['url'] + ')';	
	
	li = xbmcgui.ListItem(portal['name'], iconImage=ART+'PremiumTV.png')
	li.addContextMenuItems([ ('Clear Cache', cmd) ]);

	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
	
	
def build_url(query):
	return base_url + '?' + urllib.urlencode(query)


def homeLevel():
	global portal_1, portal_2, portal_3, portal_4, portal_5, portal_6, portal_7, portal_8, portal_9, portal_10, go;
	
	#todo - check none portal

	if go:
		addPortal(portal_1);
		addPortal(portal_2);
		addPortal(portal_3);
		addPortal(portal_4);
		addPortal(portal_5);
		addPortal(portal_6);
		addPortal(portal_7);
		addPortal(portal_8);
		addPortal(portal_9);
		addPortal(portal_10);
	
		xbmcplugin.endOfDirectory(addon_handle);
	
	AUTO_VIEW('504')

def genreLevel():
	
	try:
		data = load_channels.getGenres(portal['mac'], portal['url'], portal['serial'], addondir);
		
	except Exception as e:
		xbmcgui.Dialog().notification(addonname, str(e), xbmcgui.NOTIFICATION_ERROR );
		
		return;

	data = data['genres'];
		
	url = build_url({
		'mode': 'vod', 
		'portal' : json.dumps(portal)
	});
			
	li = xbmcgui.ListItem('VoD', iconImage='DefaultVideo.png')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
	
	
	for id, i in data.iteritems():

		title 	= i["title"];
		
		url = build_url({
			'mode': 'channels', 
			'genre_id': id, 
			'genre_name': title.title(), 
			'portal' : json.dumps(portal)
			});
			
		if id == '10':
			iconImage = 'OverlayLocked.png';
		else:
			iconImage = 'DefaultVideo.png';
			
		li = xbmcgui.ListItem(title.title(), iconImage=iconImage)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
		

	xbmcplugin.endOfDirectory(addon_handle);

def vodLevel():
	
	try:
		data = load_channels.getVoD(portal['mac'], portal['url'], portal['serial'], addondir);
		
	except Exception as e:
		xbmcgui.Dialog().notification(addonname, str(e), xbmcgui.NOTIFICATION_ERROR );
		return;
	
	
	data = data['vod'];
	
		
	for i in data:
		name 	= i["name"];
		cmd 	= i["cmd"];
		logo 	= i["logo"];
		
		
		if logo != '':
			logo_url = portal['url'] + logo;
		else:
			logo_url = 'DefaultVideo.png';
				
				
		url = build_url({
				'mode': 'play', 
				'cmd': cmd, 
				'tmp' : '0', 
				'title' : name.encode("utf-8"),
				'genre_name' : 'VoD',
				'logo_url' : logo_url, 
				'portal' : json.dumps(portal)
				});
			

		li = xbmcgui.ListItem(name, iconImage=logo_url, thumbnailImage=logo_url)
		li.setInfo(type='Video', infoLabels={ "Title": name })

		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_UNSORTED);
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
	xbmcplugin.endOfDirectory(addon_handle);

def channelLevel():
	stop=False;
		
	try:
		data = load_channels.getAllChannels(portal['mac'], portal['url'], portal['serial'], addondir);
		
	except Exception as e:
		xbmcgui.Dialog().notification(addonname, str(e), xbmcgui.NOTIFICATION_ERROR );
		return;
	
	
	data = data['channels'];
	genre_name 	= args.get('genre_name', None);
	
	genre_id_main = args.get('genre_id', None);
	genre_id_main = genre_id_main[0];
	
	if genre_id_main == '10' and portal['parental'] == 'true':
		result = xbmcgui.Dialog().input('Parental', hashlib.md5(portal['password'].encode('utf-8')).hexdigest(), type=xbmcgui.INPUT_PASSWORD, option=xbmcgui.PASSWORD_VERIFY);
		if result == '':
			stop = True;

	
	if stop == False:
		for i in data.values():
			
			name 		= i["name"];
			cmd 		= i["cmd"];
			tmp 		= i["tmp"];
			number 		= i["number"];
			genre_id 	= i["genre_id"];
			logo 		= i["logo"];
		
			if genre_id_main == '*' and genre_id == '10' and portal['parental'] == 'true':
				continue;
		
		
			if genre_id_main == genre_id or genre_id_main == '*':
		
				if logo != '':
					logo_url = portal['url'] + '/stalker_portal/misc/logos/320/' + logo;
				else:
					logo_url = 'DefaultVideo.png';
				
				
				url = build_url({
					'mode': 'play', 
					'cmd': cmd, 
					'tmp' : tmp, 
					'title' : name.encode("utf-8"),
					'genre_name' : genre_name,
					'logo_url' : logo_url,  
					'portal' : json.dumps(portal)
					});
			

				li = xbmcgui.ListItem(name, iconImage=logo_url, thumbnailImage=logo_url);
				li.setInfo(type='Video', infoLabels={ 
					'title': name,
					'count' : number
					});

				xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li);
		
		xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_PLAYLIST_ORDER);
		xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
		xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_PROGRAM_COUNT);
		
		
		xbmcplugin.endOfDirectory(addon_handle);

def playLevel():
	
	dp = xbmcgui.DialogProgressBG();
	dp.create('Channel', 'Loading ...');
	
	title 	= args['title'][0];
	cmd 	= args['cmd'][0];
	tmp 	= args['tmp'][0];
	genre_name 	= args['genre_name'][0];
	logo_url 	= args['logo_url'][0];
	
	try:
		if genre_name != 'VoD':
			url = load_channels.retriveUrl(portal['mac'], portal['url'], portal['serial'], cmd, tmp);
		else:
			url = load_channels.retriveVoD(portal['mac'], portal['url'], portal['serial'], cmd);

	
	except Exception as e:
		dp.close();
		xbmcgui.Dialog().notification(addonname, str(e), xbmcgui.NOTIFICATION_ERROR );
		return;

	
	dp.update(80);
	
	title = title.decode("utf-8");
	
	title += ' (' + portal['name'] + ')';
	
#	li = xbmcgui.ListItem(title, iconImage=logo_url); <modified 9.0.19
	li = xbmcgui.ListItem(title, iconImage='DefaultVideo.png', thumbnailImage=logo_url);
	li.setInfo('video', {'Title': title, 'Genre': genre_name});
	xbmc.Player().play(item=url, listitem=li);
	
	dp.update(100);
	
	dp.close();


mode = args.get('mode', None);
portal =  args.get('portal', None)


if portal is None:
	portal_1 = config.portalConfig('1');
	portal_2 = config.portalConfig('2');
	portal_3 = config.portalConfig('3');
	portal_4 = config.portalConfig('4');
	portal_5 = config.portalConfig('5');
	portal_6 = config.portalConfig('6');
	portal_7 = config.portalConfig('7');
	portal_8 = config.portalConfig('8');
	portal_9 = config.portalConfig('9');
	portal_10 = config.portalConfig('10');

else:
	portal = json.loads(portal[0]);

#  Modification to force outside call to portal_1 (9.0.19)

	portal_2 = config.portalConfig('2');
	portal_3 = config.portalConfig('3');
	portal_4 = config.portalConfig('4');
	portal_5 = config.portalConfig('5');
	portal_6 = config.portalConfig('6');
	portal_7 = config.portalConfig('7');
	portal_8 = config.portalConfig('8');
	portal_9 = config.portalConfig('9');
	portal_10 = config.portalConfig('10');

	if not ( portal['name'] == portal_2['name'] or portal['name'] == portal_3['name'] or portal['name'] == portal_4['name'] or portal['name'] == portal_5['name'] or portal['name'] == portal_6['name'] or portal['name'] == portal_7['name'] or portal['name'] == portal_8['name'] or portal['name'] == portal_9['name'] or portal['name'] == portal_10['name']) :
		portal = config.portalConfig('1');

if mode is None:
	HOME_MENU();

elif mode[0] == 'cache':	
	stalker_url = args.get('stalker_url', None);
	stalker_url = stalker_url[0];	
	load_channels.clearCache(stalker_url, addondir);

elif mode[0] == 'genres':
	genreLevel();
		
elif mode[0] == 'vod':
	vodLevel();

elif mode[0] == 'channels':
	channelLevel();
	
elif mode[0] == 'play':
	playLevel();
	
elif mode[0] == 'server':
	port = addon.getSetting('server_port');
	
	action =  args.get('action', None);
	action = action[0];
	
	dp = xbmcgui.DialogProgressBG();
	dp.create('IPTV', 'Just A Second ...');
	
	if action == 'start':
	
		if server.serverOnline():
			xbmcgui.Dialog().notification(addonname, 'Server already started.\nPort: ' + str(port), xbmcgui.NOTIFICATION_INFO );
		else:
			server.startServer();
			time.sleep(5);
			if server.serverOnline():
				xbmcgui.Dialog().notification(addonname, 'Server started.\nPort: ' + str(port), xbmcgui.NOTIFICATION_INFO );
			else:
				xbmcgui.Dialog().notification(addonname, 'Server not started. Wait one moment and try again. ', xbmcgui.NOTIFICATION_ERROR );
				
	else:
		if server.serverOnline():
			server.stopServer();
			time.sleep(5);
			xbmcgui.Dialog().notification(addonname, 'Server stopped.', xbmcgui.NOTIFICATION_INFO );
		else:
			xbmcgui.Dialog().notification(addonname, 'Server is already stopped.', xbmcgui.NOTIFICATION_INFO );
			
	dp.close();

#---------------------------------------------------------------------------------------------------------------

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
elif mode == 35		: PremiumTVMenu()
elif mode == 36		: parser.ChannelLinks(name, url)

#-----------------------------------------------------

#-----------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** ADDON FINISH **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
xbmcplugin.endOfDirectory(int(sys.argv[1]))