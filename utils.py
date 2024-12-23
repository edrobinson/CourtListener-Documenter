"""
Utility functions for the documentation project
"""

import glob
import os
import datetime
import json
from pathlib import *
import configparser

config = " "


# Set up the config processor
def setupConfig(iniPath):
    global config
    config = configparser.ConfigParser()
    try:
        config.read(iniPath)
    except:
        exit(
            f'Fatal Error: Failed to load the configuration file "{iniPath}". Terminating . . .'
        )


# Return a config value or False
def configVal(key):
    try:
        return config["all"][key]
    except:
        return False


# Return the type of a py variable
def getType(value):
    return type(value).__name__


def fileGetContents(path):
    return readFile(path)
 

# Return a template from the templates folder
def getTemplate(name):
    """
    This loads the named element template
    Param name is the template name
    Returns the template text or false if the template cannot be opened
    """
    path = f"{config['all']['templateFolder']}/{name}"
    return readFile(path)
 

# Get the page template an load its css and js
def loadPageTemplate():
    return getTemplate("fullpage.html")


# Build the navbar using the navbar template.
# Get the file names from the CLApiJson folder's json folders.
#Save the navbar into templates/navbar.html
def buildNavbar(folder):
    #listitemTemplate = "            <li onclick=\"showPage('[url]')\">[name] </li>"
    listitemTemplate = '              <li><a class="dropdown-item" href="[url]">[name]</a></li>'
    files = [f for f in glob.glob(f"{folder}/*.json")]
    if len(files) == 0:
        print(f"buildNavbar failed. No HTML files in {folder}\n")
        return False

    items = ""
    for filename in files:
        tpl = listitemTemplate
        # Get the api name and replace in the template
        fname = os.path.basename(filename)
        apiName, ext = fname.split(".")
        pageName = apiName + '.html'
        tpl = tpl.replace("[name]", apiName)
        tpl = tpl.replace("[url]", pageName)
        items += f"{tpl}\n"

    # Load the navbar template
    menutpl = getTemplate("navbartemplate.html")
    # Replace the pagelinks tag
    menutpl = menutpl.replace("[pagelinks]", items)
    # Save it
    tplFolder = config["all"]["templateFolder"]
    file_path = f"{tplFolder}/navbar.html"
    writeFile(file_path, menutpl)
    return menutpl


# Generate an html page from the fullpage template
# Param content is the generated page content to insert in the skeleton
def buildFullPage(content, title):
    page = getTemplate("fullpage.html")  # The skeleton
    navbar = getTemplate("navbar.html")
    page = page.replace("[title]", title)
    page = page.replace("[navbar]", navbar)
    page = page.replace("[content]", content)
    return page


# Load a json andapplyjson,loads to it.
# Return the resulting sictionary.
def getApiFileAsDictionary(filename):
    content = readFIle(filename)
    return json.loads(content)


# Simple "logging"'defaults to printing the message.
# Otherwise, it writes it into doclog.log
def logMsg(msg, printmsg=True):
    x = datetime.datetime.now()
    TandD = x.strftime("%c")
    msg = f"{TandD}: {msg}"
    if printmsg == True:
        print(f"{msg}\n")
        return
    else:
        f = open("doclog.log", "a")
        f.write(f"{msg}\n")
        f.close()

#File Write shortcut
def writeFile(fpath, content):
    try:
        with open(fpath, "w") as file:
            file.write(content)
        return True
    except Exception as  e:
        print(e)
        return False
        
#File read Shortcut
def readFile(fpath):
    try:
        with open(fpath,  'r') as file:
            return file.read()
    except Exception as e:
        print(e)
        return False;