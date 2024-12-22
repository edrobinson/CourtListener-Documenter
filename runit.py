# Run the HTML generation
from classes.generateDocsClass import generateDocs

"""
    Instance the page generation class.
    Params: 
    The mode "all" or "one"
    The ini file section name - only on is used it is [all]
    The name of ths ini file. 
    Optional file path when the mode is "one"
"""
processor = generateDocs("all", "config.ini")
processor.process()
