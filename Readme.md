#### CourtListener API Documentation Generator  

##### What is CL?
From the Courtlistener site: "CourtListener is a free legal research website containing millions of legal opinions from federal and state courts. With CourtListener, lawyers, journalists, academics, and the public can research an important case, stay up to date with case law as it develops, or do deep analysis using our raw data." 

Users can browse to the Courtlistenerwebsite and make queries against their databases to aid in legal research.  

##### What this project does:

Courtlistenerprovides a set of APIs that open up their data up to developers wanting to develop legal research tools. See here: https://www.courtlistener.com/help/api/  

Courtlistenersuggests that developers learn the APIs by studying the JSON returned from an HTTP OPTIONS request to the API url.  
JSON files can be  quite long and complex making it dificult to comprehend.  

 
This Python project produces HTML versions of the API JSON in a nice, easy to read HTML tables inside of a set of HTML pages.
  
 The basic process is to obtain the JSON from HTTP OPTIONS requests to the CourtListener rest APIs endpoints,
 translate the JSON to HTML and create an HTML page containing the translation and, finally, create a small   
 wensite that can be deployed on anything from localhost to a hosting site. 
 
 The premise is that it is easier to learn an API from a nice HTML table than it is from a JSON file.
 
 ##### Basic usage:
 1. Download the code zip file.
 2. Extract it into a local folder.
 3. Install the json2html GitHub repo. See: https://github.com/softvar/json2html
 3. At a command line:  
		1. Navigate to the folder you just created.  
		2. Run: python updateDocumentation.py
		
The update command runs the entire process including regenerating the clWebSiter folder  
contiaining a small website that runs the documentation.  

##### Folders and Files:  
###### Folders:
1. assets - css and js files
1. ClApiJSON - The JSON files for the API options requests.
1. classes - contains Py classes that do all of the heavy lifting.
1. clWebSite - the web site generated by the updateDocumenttion.py module..
1. hemlPages - holds all of the generated HTML pages.
1. templates - contains the templates for the HTML pages, the navbartemplate, the generated navbar,  
the index.HTML template and the help.HTML template.   

###### Root Files:
1. config.ini - Simple configuration file.
2. getApiJSON.py - makes a folder - ClApiJJSON - using getApiJSONs class.
3. makeSite.py - generates the clWebSite folder for the current state.
4. runit.py - generates the HTML pages using the generateDocs class.
5. updateDocumenttion.py runs steps 2, 3 and 4 to regenerate everything.
6. utils.py is a module of shared utility procedures.
7. Readme.md - this file.  
 
 The files getApiJsion.py, makeSite.py and runit.py run the individual classes and are ment to be used for development and testing.

 
 
 
