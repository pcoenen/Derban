import ConfigParser
import sys

Config = ConfigParser.ConfigParser()
if(not Config.read("settings.ini")):
    sys.exit("Settingsfile 'settings.ini' is missing, create file 'settings.ini'")

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1