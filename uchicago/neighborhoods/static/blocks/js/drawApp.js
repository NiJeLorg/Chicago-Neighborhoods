/*!
 * drawApp.js: Javascript that controls the Chicago Neighborhoods drawing tools
 */

function drawApp() {}

drawApp.init = function (mapPrefix) {
    var mapId = 'map_' + mapPrefix;
    drawApp.map = {};
    drawApp.map[mapId] = new L.Map(mapId, {
        minZoom:10,
        maxZoom:18,
        center: [41.848614, -87.684616],
        zoom: 11,
        scrollWheelZoom: false,
        zoomControl: false,
    });

    // add new zoom control in lower right
    new L.Control.Zoom({ position: 'bottomright' }).addTo(drawApp.map[mapId]);

    // set a tile layer
    drawApp.map[mapId].tiles = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png', { attribution: 'Map tiles by <a href=\"http://stamen.com\">Stamen Design</a>, under <a href=\"https://creativecommons.org/licenses/by/3.0/\" target=\"_blank\">CC BY 3.0</a>. Data by <a href=\"http://www.openstreetmap.org/\" target=\"_blank\">OpenStreetMap</a>, under ODbL.'
    });

    // add these tiles to our map
    drawApp.map[mapId].addLayer(drawApp.map[mapId].tiles);

    // create feature group for draw tools 
    drawApp.map[mapId].FEATURELAYER = new L.FeatureGroup().addTo(drawApp.map[mapId]);

    // set up popup listeners
    drawApp.map[mapId].FEATURELAYER.on('popupopen', function(e) { 
        //console.log(e.layer);
        // populate field if that exists
        $('.textAnnotation').val(e.layer.options.title);
        
        // set up keydown listener
        $('.textAnnotation').keydown(function(event) {
            // close popup if enter is pushed
            if ( event.which == 13 ) {
                event.preventDefault();
                // save annotation in layer.options.title
                //console.log($('.textAnnotation').val());
                e.layer.options.title = $('.textAnnotation').val();

                //close popup
                e.layer.closePopup();

            }
        });

        // set up keydown listener
        $('.textAnnotation').keyup(function(event) {
            // save annotation in layer.options.title
            //console.log($('.textAnnotation').val());
            e.layer.options.title = $('.textAnnotation').val();
        });


    });

    // move annotations from popup fields to geojson properties
    drawApp.map[mapId].FEATURELAYER.on('popupclose', function(e) { 
        setRadiusAddAnnotations(e.target._map);
    });

    // clear previous data
    drawApp.map[mapId].GEOJSON = null;

    // load drawnNeighborhood if it exists, if not start with create free draw
    loadDrawnGeojson();


    function loadDrawnGeojson (){
        drawApp.map[mapId].savedGeojson = $("#"+mapPrefix+"-drawnNeighborhood").val();
        if (drawApp.map[mapId].savedGeojson && drawApp.map[mapId].savedGeojson != '{"type":"FeatureCollection","features":[]}') {
            console.log(JSON.parse(drawApp.map[mapId].savedGeojson));
            drawApp.map[mapId].GEOJSON = L.geoJson(JSON.parse(drawApp.map[mapId].savedGeojson));

            drawApp.map[mapId].GEOJSON.eachLayer(function(layer) {
                // if there's a radius in the feature properties, then draw a circle
                // bindPopups

                if (layer.feature.properties.radius) {
                    var circle = L.circle(layer._latlng, layer.feature.properties.radius);
                    circle.bindPopup('<h2>Annotate this feature (optional)</h2><p><input class="form-control textAnnotation" maxlength="500" type="text"></p></select>');
                    circle.options.title = layer.feature.properties.annotation;
                    drawApp.map[mapId].FEATURELAYER.addLayer(circle);
                } else {
                    layer.bindPopup('<h2>Annotate this feature (optional)</h2><p><input class="form-control textAnnotation" maxlength="500" type="text"></p></select>');
                    // create latlngs array from feature layer
                    layer.options.title = layer.feature.properties.annotation;
                    drawApp.map[mapId].FEATURELAYER.addLayer(layer);
                }

            });             

            var bounds = drawApp.map[mapId].FEATURELAYER.getBounds();
            drawApp.map[mapId].fitBounds(bounds);
            drawApp.map[mapId].zoomCenter = bounds.getCenter();
       
        }

        // load draw tools
        loadDrawTools();

    }


    function loadDrawTools (){

        // use leaflet.draw tools instead
        drawApp.map[mapId].addControl(new L.Control.Draw({
            edit: { featureGroup: drawApp.map[mapId].FEATURELAYER }
        }));

        // set up listeners for drawing
        drawApp.map[mapId].on('draw:created', function(event) {
            var layer = event.layer, type = event.layerType;
            // TO DO:set up annotation popups
            if (type === "polyline" || type === "polygon" || type === "rectangle") {
                layer.bindPopup('<h2>Annotate this feature (optional)</h2><p><input class="form-control textAnnotation" maxlength="500" type="text"></p>');
                // bind popup for annotation and requesting solid or dashed line
                //layer.bindPopup('<h2>Annotate this feature (optional)</h2><p><input class="form-control textAnnotation" maxlength="500" type="text"></p><h2>Choose a solid or dashed boundary</h2><select><option value="solid">Solid</option><option value="dashed">Dashed</option></select>');
            } else {
                layer.bindPopup('<h2>Annotate this feature (optional)</h2><p><input class="form-control textAnnotation" maxlength="500" type="text"></p>');
            }
            if (type === "circle") {   
                // save radius
                var circleGeoJSON = layer.toGeoJSON();
                var radius = layer.getRadius();
                circleGeoJSON.properties.radius = radius;
                circleGeoJSON = L.geoJson(circleGeoJSON);
                circleGeoJSON.eachLayer(function (stripOutLayer) {
                    layer.feature = stripOutLayer.feature;
                });
            } 
            event.target.FEATURELAYER.addLayer(layer);
            setRadiusAddAnnotations(event.target);           
        });

        drawApp.map[mapId].on('draw:edited', function (event) {
            setRadiusAddAnnotations(event.target);
        }); 
        drawApp.map[mapId].on('draw:deleted', function (event) {
            setRadiusAddAnnotations(event.target);
        }); 
    
    }

    function setRadiusAddAnnotations (target){
        target.FEATURELAYER.eachLayer(function (layer) {
            var layerGeoJSON = layer.toGeoJSON();
            // add annotation
            if (layer.options.title) {
                layerGeoJSON.properties.annotation = layer.options.title;
            }

            // add radius
            if (layer._mRadius) {   
                var radius = layer.getRadius();
                layerGeoJSON.properties.radius = radius;
            }

            layerGeoJSON = L.geoJson(layerGeoJSON);
            // now add the leaflet layer from this geojson to the feature layer
            layerGeoJSON.eachLayer(function (stripOutLayer) {
                layer.feature = stripOutLayer.feature;
            });
   
        });
        // save geojson
        $("#"+mapPrefix+"-drawnNeighborhood").val(JSON.stringify(target.FEATURELAYER.toGeoJSON())); 
    }


}



