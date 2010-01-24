bounds = new GLatLngBounds( new GLatLng(-90, -180)
                          , new GLatLng(90, 180)
                          );
                              
copyright = new GCopyright( 'your-copyright'
                          , bounds
                          , 0
                          , "(c) 2008 Your Organization <http://www.example.org/>"
                          );
                              
copyrights = new GCopyrightCollection();
copyrights.addCopyright(copyright);

heatmap = new GTileLayer(copyrights, 10, 0);
heatmap.getTileUrl = function (tile, zoom) {
    return 'http://localhost:8080/tile/' + zoom + '/' + tile.x + '/' + tile.y;
};
heatmap.isPng = function () { return true; };
heatmap.getOpacity = function () { return 1.0; };

function initialize () {
    var map = new GMap2(document.getElementById("map"));
    var lebanon = new GLatLng(39.81447,-98.565388);
    map.setCenter(lebanon, 4);
    map.addOverlay(new GTileLayerOverlay(heatmap));
}