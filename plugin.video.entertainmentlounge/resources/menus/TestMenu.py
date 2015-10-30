import re, sys, os, xbmc, xbmcaddon, xbmcplugin, xbmcgui, urllib, urllib2
from resources.modules import modules, yt, common

ADDON_ID = 'plugin.video.entertainmentlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
BaseURL = 'http://chameleon.x10host.com/test/links/'
ART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/icons/'))
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))


#********** Test Text Files YouTube**********
LEntertainment = 'TESTTV.txt'

addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ).decode("utf-8"), ADDON_ID)
if not os.path.exists(addon_data_dir):
	os.makedirs(addon_data_dir)

tmpListFile = os.path.join(addon_data_dir, 'tempList.txt')
	
def TestMenuDIR(url):
	tmpList = []
	list = common.m3u2list(url)

	for channel in list:
		name = common.GetEncodeString(channel["display_name"])
		modules.AddTestDir(name ,channel["url"], 28, "", isFolder=False)
		tmpList.append({"url": channel["url"], "image": "", "name": name.decode("utf-8")})

	common.SaveList(tmpListFile, tmpList)

	modules.AUTO_VIEW('518')