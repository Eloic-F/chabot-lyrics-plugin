from http.client import responses
import json
import sys
from urllib import response

from matplotlib import artist
sys.path.append('../../')
from pluginDefault import PluginDefault
import requests
import os

artistName= None
titleSong= None
firstCall= True
titles= []

class PluginLyrics(PluginDefault):
    
    def response(self, sentence=""):
        global artistName
        global titleSong
        global firstCall
        global titles
        
        #version 1
        if artistName is None and firstCall:
            firstCall = False  
            return "Entrez nom artiste"

        elif artistName is None:
            artistName= sentence

        elif titleSong is None:
            titleSong= sentence

        if titleSong is None :
            r=requests.get("https://api.deezer.com/search?q="+artistName)
            info=r.content
            data= json.loads(info)
            titres=""
            for row in data["data"]:
                titres+= (row["title"])+"\n"
                titles.append(row["title"])
            
            titres += "Choisissez un titre de la tracklist"
            return titres
        print(titles)
        if titleSong in titles:
            lyrics=requests.get("https://api.lyrics.ovh/v1/"+artistName+"/"+titleSong)
            lyricsData=lyrics.content
            lyrcicsDisplay=json.loads(lyricsData)

            artistName= None
            titleSong= None
            firstCall= True
            return lyrcicsDisplay["lyrics"]
        else:
            reponse= "Titre non correct : "+titleSong
            titleSong= None
            return reponse
