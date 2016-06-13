$(window).ready(function() {
    'use strict';
    /* Google Maps */
    var contact_map;
    var ny = new google.maps.LatLng(40.7142700, -74.0059700);
    var neighborhoods = [
      new google.maps.LatLng(40.7232700, -73.8059700),
      new google.maps.LatLng(40.7423500, -74.0656600),
      new google.maps.LatLng(40.7314600, -74.0458500),
      new google.maps.LatLng(40.7151800, -74.1557400)
    ];
    var markers = [];
    var iterator = 0;
    var map;

    function initialize() {
        var mapOptions = {
            zoom: 12,
            center: ny,
            panControl: false,
            streetViewControl: false,
            mapTypeControl: false,
            overviewMapControl: false,
            styles: [
                {
                        "featureType": "water",
                        "stylers": [
                            {
                                "saturation": 43
                        },
                            {
                                "lightness": -11
                        },
                            {
                                "hue": "#0088ff"
                        }
                    ]
                },
                    {
                        "featureType": "road",
                        "elementType": "geometry.fill",
                        "stylers": [
                            {
                                "hue": "#ff0000"
                        },
                            {
                                "saturation": -100
                        },
                            {
                                "lightness": 99
                        }
                    ]
                },
                    {
                        "featureType": "road",
                        "elementType": "geometry.stroke",
                        "stylers": [
                            {
                                "color": "#808080"
                        },
                            {
                                "lightness": 54
                        }
                    ]
                },
                    {
                        "featureType": "landscape.man_made",
                        "elementType": "geometry.fill",
                        "stylers": [
                            {
                                "color": "#ece2d9"
                        }
                    ]
                },
                    {
                        "featureType": "poi.park",
                        "elementType": "geometry.fill",
                        "stylers": [
                            {
                                "color": "#ccdca1"
                        }
                    ]
                },
                    {
                        "featureType": "road",
                        "elementType": "labels.text.fill",
                        "stylers": [
                            {
                                "color": "#767676"
                        }
                    ]
                },
                    {
                        "featureType": "road",
                        "elementType": "labels.text.stroke",
                        "stylers": [
                            {
                                "color": "#ffffff"
                        }
                    ]
                },
                    {
                        "featureType": "poi",
                        "stylers": [
                            {
                                "visibility": "off"
                        }
                    ]
                },
                    {
                        "featureType": "landscape.natural",
                        "elementType": "geometry.fill",
                        "stylers": [
                            {
                                "visibility": "on"
                        },
                            {
                                "color": "#b8cb93"
                        }
                    ]
                },
                    {
                        "featureType": "poi.park",
                        "stylers": [
                            {
                                "visibility": "on"
                        }
                    ]
                },
                    {
                        "featureType": "poi.sports_complex",
                        "stylers": [
                            {
                                "visibility": "on"
                        }
                    ]
                },
                    {
                        "featureType": "poi.medical",
                        "stylers": [
                            {
                                "visibility": "on"
                        }
                    ]
                },
                    {
                        "featureType": "poi.business",
                        "stylers": [
                            {
                                "visibility": "simplified"
                        }
                    ]
                }
            ]
        };
        map = new google.maps.Map(document.getElementById('contact-map1'), mapOptions);
    }

    if($('#contact-map1').length){
        google.maps.event.addDomListener(window, 'load', initialize);
    }
    

    /* FULL MAP */
    var google_maps_circle_color = '#319db5';
    var google_maps_landscape_color = '#3C3C3C';
    var google_maps_water_color = '#232323';
    if ($('#full-map').length){
        map_height();
        fullMap();
    } 
    
    $(window).resize(function() {
        map_height();
    });

    function map_height() {
        $('#full-map').height('');
        var window_h = $(window).height();
        var html_h = $(document).height();
        $('#full-map').css({
            'height': window_h
        });
    }

    function fullMap() {
        var myOptions = {
            zoom: 4,
            center: new google.maps.LatLng(25.7738889, -80.1938889),
            navigationControlOptions: {
                style: google.maps.NavigationControlStyle.NORMAL,
                position: google.maps.ControlPosition.RIGHT_TOP
            },
            streetViewControl: false,
            scrollwheel: false,
            zoomControl: false,
            panControl: false,
            zoomControlOptions: {
                style: google.maps.ZoomControlStyle.DEFAULT,
                position: google.maps.ControlPosition.RIGHT_TOP
            },
            mapTypeControl: false,
            mapTypeControlOptions: {
                style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
                position: google.maps.ControlPosition.TOP_RIGHT,
                mapTypeIds: ["ptMap"]
            }
        };

        map = new google.maps.Map(document.getElementById('full-map'), myOptions);

        var mapStyle = [
            {
                featureType: "administrative",
                elementType: "all",
                stylers: [{
                    visibility: "off"
                }]
            },
            {
                featureType: 'landscape',
                elementType: 'all',
                stylers: [{
                    color: google_maps_landscape_color
                }, {
                    visibility: 'on'
                }]
            },
            {
                featureType: "poi",
                elementType: "all",
                stylers: [{
                    visibility: "off"
                }]
            },
            {
                featureType: "road",
                elementType: "all",
                stylers: [{
                    visibility: "on"
                }, {
                    lightness: -30
                }]
            },
            {
                featureType: "transit",
                elementType: "all",
                stylers: [{
                    visibility: "off"
                }]
            },
            {
                featureType: "water",
                elementType: "all",
                stylers: [{
                    color: google_maps_water_color
                }]
            }
          ];
        var styledMapOptions = {
            name: "Map"
        };
        var ptMapType = new google.maps.StyledMapType(mapStyle, styledMapOptions);
        map.mapTypes.set("ptMap", ptMapType);
        map.setMapTypeId("ptMap");
        var circle = {
            path: google.maps.SymbolPath.CIRCLE,
            fillOpacity: 0.6,
            fillColor: google_maps_circle_color,
            strokeWeight: 0,
            scale: 12
        };
        var markerFull = new MarkerWithLabel({
            position: map.getCenter(),
            icon: {
                path: google.maps.SymbolPath.CIRCLE,
                scale: 0
            },
            map: map,
            draggable: true,
            labelAnchor: new google.maps.Point(10, 10),
            labelClass: 'pulse-label'
        });
    }
    var map_bottom;
    var ny = new google.maps.LatLng(40.7142700, -74.0059700);
    var neighborhoods = [
      new google.maps.LatLng(40.7232700, -73.8059700),
      new google.maps.LatLng(40.7423500, -74.0656600),
      new google.maps.LatLng(40.7314600, -74.0458500),
      new google.maps.LatLng(40.7151800, -74.1557400)
    ];
    var markers = [];
    var iterator = 0;



    function initializeBottom() {
        var mapOptions = {
            zoom: 12,
            center: ny,
            panControl: false,
            streetViewControl: false,
            mapTypeControl: false,
            overviewMapControl: false,
            zoomControl: false,
            styles: [{"featureType":"landscape","stylers":[{"saturation":-100},{"lightness":65},{"visibility":"on"}]},{"featureType":"poi","stylers":[{"saturation":-100},{"lightness":51},{"visibility":"simplified"}]},{"featureType":"road.highway","stylers":[{"saturation":-100},{"visibility":"simplified"}]},{"featureType":"road.arterial","stylers":[{"saturation":-100},{"lightness":30},{"visibility":"on"}]},{"featureType":"road.local","stylers":[{"saturation":-100},{"lightness":40},{"visibility":"on"}]},{"featureType":"transit","stylers":[{"saturation":-100},{"visibility":"simplified"}]},{"featureType":"administrative.province","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"labels","stylers":[{"visibility":"on"},{"lightness":-25},{"saturation":-100}]},{"featureType":"water","elementType":"geometry","stylers":[{"hue":"#ffff00"},{"lightness":-25},{"saturation":-97}]}]
        };

        if($('#contact-map-bottom').length){
            map_bottom = new google.maps.Map(document.getElementById('contact-map-bottom'), mapOptions);
        }
        if($('#contact-map-side').length){
            map_bottom = new google.maps.Map(document.getElementById('contact-map-side'), mapOptions);
        }
        
    }

    function drop() {
        setTimeout(function() {
            for (var i = 0; i < neighborhoods.length; i++) {
                setTimeout(function() {
                    addMarker();
                }, i * 350);
            }
        }, 1500);
    }

    function addMarker() {
        markers.push(new google.maps.Marker({
            position: neighborhoods[iterator],
            map: map_bottom,
            draggable: false,
            animation: google.maps.Animation.DROP,
            icon: '../../common-files/images/map-marker.png' // null = default icon
        }));
        iterator++;
    }
    google.maps.event.addDomListener(window, 'load', initializeBottom);
    drop();
});