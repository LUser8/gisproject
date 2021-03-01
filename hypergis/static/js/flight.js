require([
    "esri/config",
    "esri/Map",
    "esri/views/MapView",
    "esri/layers/TileLayer"
   ], function(esriConfig, Map, MapView, TileLayer){
    esriConfig.apiKey = "AAPK02da015eace04b4e9907e38d261b4fe0jFOsilMKpbnUNqY2Gs2L_H9QieuIPqgMJRx83Bp3HHir-u26sZvJ3adIgu12PQI-";
    var transportationLayer = new TileLayer({
        url: "https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Transportation/MapServer",
        id: "streets",
        opacity: 0.7
    });

    var housingLayer = new TileLayer({
        url: "https://tiles.arcgis.com/tiles/nGt4QxSblgDfeJn9/arcgis/rest/services/New_York_Housing_Density/MapServer",
        id: "ny-housing"
    })

    var map = new Map({
        basemap: "osm-standard",
        layers: [housingLayer]
    });
    var view = new MapView({
        container: "viewDiv",
        map: map,
        zoom: 3
    })

    map.layers.add(transportationLayer)
});