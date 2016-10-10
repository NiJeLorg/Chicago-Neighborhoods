/*!
 * app.js: Javascript that controls the Chicago Neighborhoods public pages
 */

function app() {}

app.init = function () {
    // set up listeners
    app.createListeners();
}

app.collapseNavbar = function () {
    if ($(".navbar").offset().top > 30) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
        $(".intro").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
        $(".intro").removeClass("top-nav-collapse");
    }    
}


app.createListeners = function () {
    $(window).scroll(app.collapseNavbar);
    $(document).ready(app.collapseNavbar);

    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });

    $('.navbar-collapse ul li a').click(function() {
        $(this).closest('.collapse').collapse('toggle');
    });

}

app.createMap = function (mapId, drawnNeighborhood) {
    app.map = {};
    app.map[mapId] = new L.Map(mapId, {
        minZoom:10,
        maxZoom:18,
        center: [41.848614, -87.684616],
        zoom: 11,
        scrollWheelZoom: false,
    });

    // set a tile layer
    app.map[mapId].tiles = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png', { attribution: 'Map tiles by <a href=\"http://stamen.com\">Stamen Design</a>, under <a href=\"https://creativecommons.org/licenses/by/3.0/\" target=\"_blank\">CC BY 3.0</a>. Data by <a href=\"http://www.openstreetmap.org/\" target=\"_blank\">OpenStreetMap</a>, under ODbL.'
    });

    // add these tiles to our map
    app.map[mapId].addLayer(app.map[mapId].tiles);

    if (drawnNeighborhood) {
        app.map[mapId].GEOJSON = L.geoJson(JSON.parse(drawnNeighborhood), {
                    style: app.getStyleFor_GEOJSON,
                    pointToLayer: function(feature, latlng) {
                        if (typeof feature.properties.radius !== 'undefined') {
                            return new L.Circle(latlng, feature.properties.radius);
                        } else {
                            return new L.marker(latlng);
                        }
                    },
                    onEachFeature: function (feature, layer) {
                        if (feature.properties.annotation) {
                            layer.bindPopup(feature.properties.annotation);
                        } 
                    }
                });
        app.map[mapId].GEOJSON.addTo(app.map[mapId]);

        var bounds = app.map[mapId].GEOJSON.getBounds();
        app.map[mapId].fitBounds(bounds);
   
    }

}

app.getStyleFor_GEOJSON = function (feature){
    return {
        weight: 4,
        opacity: 1,
        color: '#D7217E',
        fillOpacity: 0.5,
        fillColor: "#D7217E",
    };
}

// scoped variables
app.mapCount = 1;
app.drawnNeighborhood;
app.mapId;













