/*!
 * drawApp.js: Javascript that controls the Chicago Neighborhoods drawing tools
 */

function drawApp() {}

drawApp.init = function () {
    var mapId = 'map_' + prefix;
    drawApp.map = new L.Map(mapId, {
        minZoom:10,
        maxZoom:18,
        center: [41.848614, -87.684616],
        zoom: 11,
        scrollWheelZoom: false,
        zoomControl: false,
    });

    // add new zoom control in lower right
    new L.Control.Zoom({ position: 'bottomright' }).addTo(drawApp.map);

    // set a tile layer
    drawApp.tiles = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png', { attribution: 'Map tiles by <a href=\"http://stamen.com\">Stamen Design</a>, under <a href=\"https://creativecommons.org/licenses/by/3.0/\" target=\"_blank\">CC BY 3.0</a>. Data by <a href=\"http://www.openstreetmap.org/\" target=\"_blank\">OpenStreetMap</a>, under ODbL.'
    });

    // add these tiles to our map
    drawApp.map.addLayer(drawApp.tiles);

    // create feature group for draw tools 
    drawApp.FEATURELAYER = new L.FeatureGroup().addTo(drawApp.map);

    // clear previous data
    drawApp.GEOJSON = null;

    // load drawnNeighborhood if it exists, if not start with create free draw
    drawApp.loadDrawnGeojson();

}

drawApp.loadDrawnGeojson = function (){
    drawApp.savedGeojson = $("#"+prefix+"-drawnNeighborhood").val();
    if (drawApp.savedGeojson) {
        drawApp.GEOJSON = L.geoJson(JSON.parse(drawApp.savedGeojson));

        drawApp.GEOJSON.eachLayer(function(layer) {
            // create latlngs array from feature layer
            drawApp.FEATURELAYER.addLayer(layer);
        });             

        var bounds = drawApp.FEATURELAYER.getBounds();
        drawApp.map.fitBounds(bounds);
        drawApp.zoomCenter = bounds.getCenter();
   
    }

    // load draw tools
    drawApp.loadDrawTools();

}


drawApp.loadDrawTools = function (){

    // use leaflet.draw tools instead
    drawApp.map.addControl(new L.Control.Draw({
        edit: { featureGroup: drawApp.FEATURELAYER },
        draw: { circle: true },
    }));

    // set up listeners for drawing
    drawApp.map.on('draw:created', function(event) {
        var layer = event.layer;
        drawApp.FEATURELAYER.addLayer(layer);
        drawApp.GEOJSON = drawApp.FEATURELAYER.toGeoJSON();
        $("#"+prefix+"-drawnNeighborhood").val(JSON.stringify(drawApp.GEOJSON));        
    });

    drawApp.map.on('draw:edited', function (event) {
        console.log(event);
        drawApp.GEOJSON = drawApp.FEATURELAYER.toGeoJSON();
        $("#"+prefix+"-drawnNeighborhood").val(JSON.stringify(drawApp.GEOJSON));  
    }); 
    drawApp.map.on('draw:deleted', function (event) {
        drawApp.GEOJSON = drawApp.FEATURELAYER.toGeoJSON();
        $("#"+prefix+"-drawnNeighborhood").val(JSON.stringify(drawApp.GEOJSON));  
    }); 

     

    //add freedraw now so we can set mode in a bit
    // depreciated for now
/*    drawApp.freedraw = new L.FreeDraw({
        mode: L.FreeDraw.MODES.CREATE | L.FreeDraw.MODES.EDIT | L.FreeDraw.MODES.APPEND
    });

    drawApp.freedraw.on('markers', function getMarkers(eventData) {
        drawApp.FEATURELAYER.clearLayers();
        for (var i = drawApp.freedraw.polygons.length - 1; i >= 0; i--) {
            drawApp.FEATURELAYER.addLayer(drawApp.freedraw.polygons[i]); 
        }
        drawApp.GEOJSON = drawApp.FEATURELAYER.toGeoJSON();
        $('#draw_neighborhood-0-value-drawnNeighborhood').val(JSON.stringify(drawApp.GEOJSON));
    });

    drawApp.map.addLayer(drawApp.freedraw);

    for (var i = drawApp.LATLNGS.length - 1; i >= 0; i--) { 
        // test if drawApp.LATLNGS is and array of arrays
        if (typeof drawApp.LATLNGS[0][0].lat === "undefined") {
            // loop again
            for (var j = drawApp.LATLNGS[i].length - 1; j >= 0; j--) {
                drawApp.freedraw.createPolygon(drawApp.LATLNGS[i][j]);
            }
        } else {
            // add our poly
            drawApp.freedraw.createPolygon(drawApp.LATLNGS[i]);
        }
    }
*/



}


