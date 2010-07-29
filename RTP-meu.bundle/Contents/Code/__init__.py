# -*- coding: utf-8 -*-
from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *

from urlparse import urlparse


PLUGIN_PREFIX	= "/video/RTP"
CACHE_TIME      = 1800
MENU_URL		= "http://tv.rtp.pt/multimedia/php/ajax_links.php?menu=video&pesquisa=a_z"

divs = None

####################################################################################################
def Start():
	# Add the MainMenu prefix handler‎
	Log('(RTP) Initializing the plug-in')
	Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, L("RTP"), thumb="icon-default.png", art="art-default.png")
	Plugin.AddViewGroup("List", viewMode="List", mediaType="items")
	HTTP.SetCacheTime(CACHE_TIME)
	MediaContainer.title1 = 'RTP'
	MediaContainer.content = 'List'
	divs = XML.ElementFromURL(MENU_URL, True, encoding="iso-8859-1").xpath("//div[matches(@id,'tit_area_menu')]")
	
	Log(divs)
	Log('(RTP) Finished initializing the plug-in')


####################################################################################################
def MainMenu():
	Log('(RTP) Main Menu Begins')
	dir = MediaContainer(art = None, title1="RTP", viewGroup="List")
	  	
  	#dir.Append(Function(DirectoryItem(GetProgramas, title="Informação"), index=0, title1="Informação"))
  	#dir.Append(Function(DirectoryItem(GetProgramas, title="Entretenimento"), index=1, title1="Entretenimento"))
  	#dir.Append(Function(DirectoryItem(GetProgramas, title="Desporto"), index=2, title1="Desporto"))
  	#dir.Append(Function(DirectoryItem(GetProgramas, title="Especiais"), index=3, title1="Especiais"))
	#dir.Append(Function(DirectoryItem(DivinasComedias, "As Divinas Comédias",subtitle=None,summary = None,thumb = None)))
	#dir.Append(Function(DirectoryItem(Directo, title="Em Directo"), index=0, title1="Em Directo"))
	
	Log('(RTP) Main Menu Ends')
	return dir

"""	
def Directo(sender, index, title1):
	Log('(RTP) Live TV Menu Begins')
	dir = MediaContainer(art = None, title1="Em Directo", viewGroup="List")
	# WebVideoItem( key, title, subtitle=None, summary=None, thumb=None, art=None, **kwargs)
	dir.Append(VideoItem("mms://195.245.168.21/c1?MSWMExt=.asf", "RTP 1", date="", summary=None, thumb=None))
	dir.Append(VideoItem("http://195.245.168.21/c2", "RTP 2", date="", summary=None, thumb=None))
	dir.Append(VideoItem("http://195.245.168.21/RTPN", "RTP N", date="", summary=None, thumb=None))
	Log('(RTP) Live TV Menu Ends')
	return dir
"""
"""
def GetProgramas(sender, index, title1):
	Log('(RTP) Getting Programs...')
	
	global divs
	div = divs[index]
	
	dir = MediaContainer(title1=title1)
	for programa in div.xpath("a"):
		nome = programa.text.encode('iso-8859-1', 'replace')
		href = programa.get('href')
		params = ParseURL(href)

		page = XML.ElementFromURL(PROGRAM_INFO_URL + params['tvprog'], True, encoding="iso-8859-1")
		
		try:
			img_src = page.xpath('//div[@class="CampoAzulEspecial Img_BG_Repeat_Y Padding"]/div[@class="Img"]/img')[0].get("src")
		except Exception, e:
			img_src = None
			
		dir.Append(Function(DirectoryItem(Vazia,title = nome,subtitle=None,summary = None,thumb = img_src)))	
		#dir.Append(Function(DirectoryItem(Vazia,title = nome,subtitle=None,summary = None,thumb = None)))
	
	Log('(RTP) Finished getting Programs...')
	return dir

def DivinasComedias(sender):
	Log('(RTP) Level One Menu Begins')
	dir = MediaContainer(art = None, title1="As Divinas Comedias", viewGroup="List")
	# WebVideoItem( key, title, subtitle=None, summary=None, thumb=None, art=None, **kwargs)
	dir.Append(WebVideoItem("http://ww1.rtp.pt/multimedia/index.php?tvprog=25161&idpod=28412&formato=flv", "Episódio 1", date="", summary=None, thumb=None))
	dir.Append(WebVideoItem("http://ww1.rtp.pt/multimedia/index.php?tvprog=25161&idpod=28411&formato=flv", "Episódio 2", date="", summary=None, thumb=None))
	dir.Append(WebVideoItem("http://ww1.rtp.pt/multimedia/index.php?tvprog=25161&idpod=28413&formato=flv", "Episódio 3", date="", summary=None, thumb=None))
	dir.Append(WebVideoItem("http://ww1.rtp.pt/multimedia/index.php?tvprog=25161&idpod=28424&formato=flv", "Episódio 4", date="", summary=None, thumb=None))
	
	Log('(RTP) Level One Menu Ends')
	return dir

def Vazia():
	return None

def ParseURL(url):
	return dict([part.split('=') for part in urlparse(url)[4].split('&')])
"""

#os.system("clear")
#for div in XML.ElementFromURL(MENU_URL, True, encoding="iso-8859-1").xpath("//div[starts-with(@class,'m')]"):
"""
divs = XML.ElementFromURL(MENU_URL, True, encoding="iso-8859-1").xpath("//div[starts-with(@class,'m')]")
div = divs[3]
for programa in div.xpath("a"):
	nome = programa.text.encode('iso-8859-1', 'replace')
	href = programa.get('href')
	params = ParseURL(href)
	print params['tvprog']
		
#		print type(programa.text)
#		print(XML.StringFromElement(programa, encoding="iso-8859-1", method="html"))
"""
#print XML.ElementFromURL(PROGRAM_INFO_URL, True, encoding="iso-8859-1").xpath('//div[@class="CampoAzulEspecial Img_BG_Repeat_Y Padding"]/div[@class="Img"]/img')[0].get("src")
#print type(XML.ElementFromURL(PROGRAM_INFO_URL, True, encoding="iso-8859-1").xpath('//div[@class="CampoAzulEspecial Img_BG_Repeat_Y Padding"]/div[@class="Img"]/img')[0].get("src"))
