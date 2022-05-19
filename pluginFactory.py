from pluginDefault import PluginDefault
from plugins.alarm.plugin import PluginAlarm
from plugins.remote.plugin import PluginRemote
from plugins.lyrics.plugin import PluginLyrics

#permet de renvoyer le plugin à appeler suivant le jeu de données
class PluginFactory:

    def getPlugin(subject, typeS):
        themeName= subject.split(".")[0]    
        if themeName== "alarm":
            return PluginAlarm(subject, typeS)
        elif themeName== "remote":
            return PluginRemote(subject, typeS)
        elif themeName== "lyrics":
            return PluginLyrics(subject, typeS)
        return PluginDefault(subject, typeS)