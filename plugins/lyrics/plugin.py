from http.client import responses
import json
import sys
from urllib import response
sys.path.append('../../')
from pluginDefault import PluginDefault
import requests
import os

class PluginLyrics(PluginDefault):
    
    def response(self, sentence=""):
        artist=[]
        titles=[]
        themeName= self.subject.split(".")[1]

        #version 1
        if themeName == "startLyrics":
            print("Entrez nom artiste : ")
            artist=input()
            r=requests.get("https://api.deezer.com/search?q="+artist)
            info=r.content
            data= json.loads(info)
            titres=""
            for row in data["data"]:
                titles.append(row["title"])
            print(titles)
            for i in titles:
                print(i)
            print("===Tracklist de "+artist+"===")
            
            print("Choisissez un titre de la tracklist")
            title=input()
            if title in titles:
                lyrics=requests.get("https://api.lyrics.ovh/v1/"+artist+"/"+title)
                lyricsData=lyrics.content
                lyrcicsDisplay=json.loads(lyricsData)
                return lyrcicsDisplay["lyrics"]
        titles.clear()
        print(titles)