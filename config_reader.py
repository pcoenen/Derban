import ConfigParser
import sys

Config = ConfigParser.ConfigParser()


if not Config.read("settings.ini"):
    sys.exit("Settingsfile 'settings.ini' is missing, create file 'settings.ini'")


def get_setting(section,option):
    global standard_settings
    try:
        return Config.get(section, option)
    except:
        if section in standard_settings:
            return standard_settings.get(section).get(option, None)
        return None


def get_bool_setting(section,option):
    result = get_setting(section, option)
    if result is not None and result.lower() == "true":
        return True
    return False

detection_methods = {'SSH' : "true"}
standard_settings = {'Detection Methods' : detection_methods}