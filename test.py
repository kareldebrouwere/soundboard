import sys
import os
import cherrypy
print (sys.version)

class SoundBoard(object):
    @cherrypy.expose
    def index(self):
        return("SoundBoard")

if __name__ == "__main__":
    config = os.path.join(os.path.dirname(__file__),'cherrypy.conf')
    cherrypy.quickstart(SoundBoard(),config = config)