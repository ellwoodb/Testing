from configparser import ConfigParser

config_path = "config.ini"

config = ConfigParser()
config.read(config_path)

user_value = input("Enter a number:\n")

config.set("settings", "value", user_value)

with open(config_path, "w") as configfile:
    config.write(configfile)
