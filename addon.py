import xbmc
import xbmcaddon
 
__addon__       = xbmcaddon.Addon(id='plugin.video.nhlgamecenter')
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')
 
title = "Hello World"
text = "FIRST PLUGINNN@@@@"
time = 5000  # ms
 
xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(title, text, time, __icon__))