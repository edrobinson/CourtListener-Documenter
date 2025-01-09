'''
	This PY creates a small website that can
	serve the documentation pages.
'''

import os
import shutil

class makeDocSite:
    def  createSite(self, destination):
        self.destination = destination
        #Create the destination folder. Won't return if problems occur.
        self.checkDestination()
        
        shutil.rmtree(self.destination, ignore_errors=True)
        
        shutil.copytree('htmlpages', destination + '/htmlpages')
        shutil.copytree('assets', destination + '/assets')
        self.makeRootIndex()
 
        exit(r'Site created . . .')

    #Create destination folder.
    #if it already exisit, ask the user if we can replace it.
    def checkDestination(self):
        #If the destination exists, Ask user if ok to remove. Exit if not OK.
        #else remove it.
        if os.path.isdir(self.destination):
            answer = input(r'The destination folder {self.destination}already exists. Is it OK to replace the contents (Y/N)? ')
            if answer != 'Y':
                exit('Terminated . . .')
            return True
 
    #Copy the index from templates
    def makeRootIndex(self):
        with open('./templates/clsiteindex.html', 'r') as file:
            indexcode= file.read();
        with open(f'{self.destination}/index.html', 'w') as file:
            file.write(indexcode)