import xbmc, xbmcgui, xbmcplugin, xbmcaddon, os, sys
import urllib, urllib2
from resources.modules import common

ADDON_ID = 'plugin.video.entertainmentlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
ART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/icons/'))
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))
localizedString = ADDON.getLocalizedString

addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ).decode("utf-8"), ADDON_ID)
if not os.path.exists(addon_data_dir):
	os.makedirs(addon_data_dir)

tmpListFile = os.path.join(addon_data_dir, 'tempList.txt')

def TestMenuDIR(url):
	tmpList = []
	list = common.m3u2list(url)

	for channel in list:
		name = common.GetEncodeString(channel["display_name"])
		AddTestDir(name ,channel["url"], 28, "", isFolder=False)
		tmpList.append({"url": channel["url"], "image": "", "name": name.decode("utf-8")})

	common.SaveList(tmpListFile, tmpList)

	AUTO_VIEW('518')

def TestMenuDIR2(url):
	tmpList = []
	list = common.m3u2list(url)

	for channel in list:
		name = common.GetEncodeString(channel["display_name"])
		AddTestDir(name ,channel["url"], 31, "", isFolder=True)
		tmpList.append({"url": channel["url"], "image": "", "name": name.decode("utf-8")})

	common.SaveList(tmpListFile, tmpList)

	AUTO_VIEW('518')

def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==19 :
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def AddTestDir(name, url, mode, iconimage, description="", isFolder=True, background=None):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)

	liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description})
	if background:
		liz.setProperty('fanart_image', background)
	if mode == 1 or mode == 2:
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10008).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=22)'.format(sys.argv[0], urllib.quote_plus(url)))])
	elif mode == 28:
		liz.setProperty('IsPlayable', 'true')
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10009).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), iconimage, name))])
	elif mode == 32:
		liz.setProperty('IsPlayable', 'true')
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10010).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=33&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), iconimage, name))])
		
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)


def addYTVID(type,name,url,mode,iconimage = '',fanart = '',video = '',description = ''):
    if type != 'folder2' and type != 'addon':
        if len(iconimage) > 0:
            iconimage = ART + iconimage
        else:
            iconimage = 'DefaultFolder.png'
    if type == 'addon':
        if len(iconimage) > 0:
            iconimage = iconimage
        else:
            iconimage = 'http://totalxbmc.tv/addons/cache/images/4c79319887e240789ca125f144d989_addon-dummy.png'
    if fanart == '':
        fanart = FANART
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)+"&video="+urllib.quote_plus(video)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
    liz.setProperty( "Fanart_Image", fanart )
    liz.setProperty( "Build.Video", video )
    if (type=='folder') or (type=='folder2') or (type=='tutorial_folder') or (type=='news_folder'):
        ok=Add_Directory_Item(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    else:
        ok=Add_Directory_Item(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def Add_Directory_Item(handle, url, listitem, isFolder):
    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder) 
	
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link 

def Play_URL(name, url, iconimage, forcePlayer=False):
	image = iconimage
	title = name
	addon_handle = int(sys.argv[1])
	xbmcplugin.setContent(addon_handle, 'movies')
	
	li = xbmcgui.ListItem(title, iconImage=image)
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

def TestPlayUrl(name, url, iconimage=None):
	print '--- Playing "{0}". {1}'.format(name, url)
	listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
	listitem.setInfo(type="Video", infoLabels={ "Title": name })
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

def AUTO_VIEW(Vmode = ''):
	xbmc.executebuiltin("Container.SetViewMode(" + Vmode +")")

def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)