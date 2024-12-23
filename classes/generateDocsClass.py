"""
    This script is a tool that produces an html page from JSON files.
    It can process an entire folder or a single file.
    
    
"""

from json2html import *
import glob
import os
import configparser
import utils


class generateDocs:
    '''
        Use the init to store the cl options etc.
    '''
    def __init__(self, mode, iniPath, oneFile=" "):
        # Get the config handler setup
        utils.setupConfig(iniPath)
        self.mode = mode
        self.source = utils.configVal("sourceFolder")
        self.destination = utils.configVal("destinationFolder")
        self.templates = utils.configVal("templateFolder")
        
        #Build a new navbar using the file names from the JSON folder
        #and load it for the generation functions to plug into the new html
        if not utils.buildNavbar(self.source):
            exit('Failed to build a new navbar. Terminated.')
        self.navbar = utils.getTemplate('navbar.html')
        
        # Get a copy of the html page template
        self.pageTemplate = utils.loadPageTemplate()

        # The source directory must exist if the mode is all.
        if mode == "all" and not os.path.isdir(self.source):
            exit(f"The source directory {source} does not exist. Terminating.")

        # Create the destination folder if it does not exist.
        if not os.path.isdir(self.destination):
            try:
                os.mkdir(self.destination)
                print(f"Created the destinion directory {self.destination}\n")
            except:
                exit(f"The destinstion directory, {destination}, does not exist and the attempt to create it failed. Terminating.\n")
    
    # Convert all or just one JSON?
    def process(self):
        #Update the index and help pages
        #They need new navbars
        self.updateStaticPages()
        
        if self.mode == "all":
            self.processAll()
        else:
            self.processOneFile(self.oneFile)

    # Process all JSONs in the source directory
    def processAll(self):
        files = [f for f in glob.glob(self.source + "/*.json")]

        if len(files) == 0:
            exit(f"{source} does not contain any JSON files.\n")

        # Generate the HTML files
        for filename in files:
            self.processFile(filename)

        # Add the navbar to them
        #self.addNavbars(self.destination)

    # Process a single file given it's path.
    def processOneFile(self, path):
        # generate the HTML for the requested file path
        if not self.processFile(path):
            return
        #self.addNavbars(self.destination)
        exit(f"Generated HTML file for {path}\n")

    # Process the file whose name is pased in
    def processFile(self, filename):
        json = utils.readFile(filename)
        if not json:   
            return False

        # setup the path to the finished html page
        fname = os.path.basename(filename).split(".")[0]
        path = f"{self.destination}/{fname}.html"

        # Convert the json to html
        html = json2html.convert(json, utils.configVal("tableStyle"))

        # Copy HTML the page template  and do the tag replacements
        page = self.pageTemplate
        page = page.replace("[pagehead]", fname.capitalize())
        page = page.replace("[title]", fname.capitalize())
        page = page.replace("[content]", html)
        page = page.replace('[navbar]', self.navbar)

        # save it
        page.encode(
            "utf-8"
        )  # Some templates have unicodes in them that f.write complains about.
        fpath = f"{self.destination}/{fname}.html"
        return utils.writeFile(fpath, page)


    #Whenever we generate a new set of pages, we need to update
    #any pages that dont change with a new navbar.
    #Initially these are the index and help [ages]
    def updateStaticPages(self):
        index = utils.getTemplate('index.html')
        index= index.replace('[navbar]', self.navbar)
        f = open('htmlpages/index.html', "w", encoding="utf-8")
        f.write(index)
        f.close()
        
        hlp = utils.getTemplate('help.html')
        hlp= hlp.replace('[navbar]', self.navbar)
        f = open('htmlpages/help.html', "w", encoding="utf-8")
        f.write(hlp)
        f.close()
