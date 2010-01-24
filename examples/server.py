import os, sys
import cherrypy
import heatlayer

tilelayer_js = open("tilelayer.js").read()
tilemaster = heatlayer.TileMaster()

class Handler(object):
    def __init__(self):
        pass

    @cherrypy.expose
    def tile(self, zoom, tx, ty):
        tile_image = tilemaster.process(int(zoom), int(tx), int(ty))
        cherrypy.response.headers['Content-Type'] = "image/png"
        cherrypy.response.body = tile_image
        return cherrypy.response.body

    @cherrypy.expose
    def map(self):
        yield """
<html>
<head>
    <script src="http://maps.google.com/maps?file=api&amp;v=2&amp;key=ABQIAAAA-LQou8q_sKeS5aYUTmi6cBTwM0brOpm-All5BF6PoaKBxRWWERTLoTYiIZTo0Y148gT7RR7GgXyJLA"></script>
    <script>
%s
    </script>
    <style>
        body {
            margin: 0;
            padding: 0;
        }
        #map {
            margin: 0;
            padding: 0;
            width: 100%%;
            height: 100%%;
        }
    </style>
</head>
<body onload="initialize()" onunload="GUnload()">
    <div id="map">&nbsp;</div>       
</body>
</html>
        """ % tilelayer_js

def start():
    root = os.path.abspath(os.curdir)
    
    conf = {
        '/': {
            'tools.encode.on': True,
            'tools.encode.encoding': "utf-8",
            'tools.decode.on': True,
            'tools.flatten.on': True,
            'tools.trailing_slash.on': True,
        },
    }

    cherrypy.tree.mount(Handler(), config=conf)
    cherrypy.engine.start()

if __name__ == '__main__':
    start()