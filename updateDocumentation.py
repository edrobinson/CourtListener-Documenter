'''
Update the document pages

When one or  more APIs change this PY is used to
update the HTML pages. It recreates all of the pages.
'''
from classes.getapiJsonClass import getApiJsons
from classes.generateDocsClass import generateDocs
from classes.makeDocSiteClass import makeDocSite	

#1. Get a fresh set of API OPTIONS Jsons
apiGetter = getApiJsons('ClApiJson')
apiGetter.process()

#2. Generate the html pages
processor = generateDocs("all", "config.ini")
processor.process()

#3. Regenerate the web site
ms = makeDocSite()
ms.createSite('./clWebSite')
