/*!
 * app.js: Javascript that controls the Chicago Neighborhoods public pages
 */
// if (!localStorage.showWelcomeInfoModal) {
//     $('.welcome-modal').css('display', 'none');
// } else {
//     localStorage.showWelcomeInfoModal = true;
//
// }

console.log(window);
$('.navbar-custom').click(function() {
    console.log('eyyy');
});
// $('.navbar-custom').click(function() {
//     alert('me');
//     // localStorage.showWelcomeInfoModal = false;
// });

function app() {}

app.init = function() {
    // set up listeners
    app.createListeners();
    console.log(localStorage.showWelcomeInfoModal, 'value');
    if (localStorage.showWelcomeInfoModal === undefined || localStorage.showWelcomeInfoModal === true) {
        $('#welcomeModal').modal('show');
        localStorage.showWelcomeInfoModal = true;
    } else if (localStorage.showWelcomeInfoModal === false) {
        $('.welcome-modal').modal({ show: false });
    }
};

// app.collapseNavbar = function () {
//     if ($(".navbar").offset().top > 30) {
//         $(".navbar-fixed-top").addClass("top-nav-collapse");
//         $(".intro").addClass("top-nav-collapse");
//     } else {
//         $(".navbar-fixed-top").removeClass("top-nav-collapse");
//         $(".intro").removeClass("top-nav-collapse");
//     }
// }


app.createListeners = function() {
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

    $('#closeWelomeModal').click(function() {
        localStorage.showWelcomeInfoModal = false;
    });
};

app.createMap = function(mapId, drawnNeighborhood) {
    app.map[mapId] = new L.Map(mapId, {
        minZoom: 10,
        maxZoom: 18,
        center: [41.848614, -87.684616],
        zoom: 11,
        scrollWheelZoom: false,
    });

    // set a tile layer
    app.map[mapId].tiles = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png', {
        attribution: 'Map tiles by <a href=\"http://stamen.com\">Stamen Design</a>, under <a href=\"https://creativecommons.org/licenses/by/3.0/\" target=\"_blank\">CC BY 3.0</a>. Data by <a href=\"http://www.openstreetmap.org/\" target=\"_blank\">OpenStreetMap</a>, under ODbL.'
    });

    // add these tiles to our map
    app.map[mapId].addLayer(app.map[mapId].tiles);

    // create empty container for overlays
    app.overlayMaps[mapId] = {};
    app.baseMaps[mapId] = {
        "Background Map": app.map[mapId].tiles
    };
    app.layerCounter[mapId] = 1;

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
            onEachFeature: function(feature, layer) {
                // as we loop through each layer, add to map and layer controller
                // add annotations
                if (feature.properties.annotation) {
                    app.overlayMaps[mapId][feature.properties.annotation] = layer;
                    layer.bindPopup(feature.properties.annotation);
                    // add layer
                    layer.addTo(app.map[mapId]);
                } else {
                    app.overlayMaps[mapId]['Layer ' + app.layerCounter[mapId]] = layer;
                    layer.bindPopup('Layer ' + app.layerCounter[mapId]);
                    // add layer
                    layer.addTo(app.map[mapId]);
                }
                app.layerCounter[mapId]++;
            }
        });
        //app.map[mapId].GEOJSON.addTo(app.map[mapId]);

        // create map controller
        var collapsed;
        if ($('.mapContainer').width() < 500) {
            collapsed = true;
        } else {
            collapsed = false;
        }

        // var control = L.control.layers.minimap(app.baseMaps[mapId], app.overlayMaps[mapId], {
        //     overlayBackgroundLayer: app.map[mapId].tiles,
        //     collapsed: collapsed,
        // }).addTo(app.map[mapId]);

        // console.log(control);

        L.control.layers(app.baseMaps[mapId], app.overlayMaps[mapId], { collapsed: false }).addTo(app.map[mapId]);

        var bounds = app.map[mapId].GEOJSON.getBounds();
        app.map[mapId].fitBounds(bounds);

    }

}

app.getStyleFor_GEOJSON = function(feature) {
    return {
        weight: 4,
        opacity: 1,
        color: '#D7217E',
        fillOpacity: 0.5,
        fillColor: "#D7217E",
    };
}

app.invalidateMinimaps = function() {
    var minimaps = document.querySelectorAll('label[class="leaflet-minimap-container"]');
    for (var i = 0; i < minimaps.length; ++i) {
        var minimap = minimaps[i].childNodes.item(0);
        var map = minimap._miniMap;
        map.invalidateSize();
    }
};



// scoped variables
app.mapCount = 1;
app.drawnNeighborhood;
app.mapId;
app.map = {};
app.overlayMaps = {};
app.baseMaps = {};
app.layerCounter = {};
