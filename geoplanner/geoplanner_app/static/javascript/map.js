


const raster =  new ol.layer.Tile({
  source: new ol.source.OSM(),
});

const source = new ol.source.Vector({wrapX: false});

const vector = new ol.layer.Vector({
  source: source,
});

const map = new ol.Map({
  layers: [raster, vector],
  target: 'map',
  view: new ol.View({
    center: [-11000000, 4600000],
    zoom: 4,
  }),
});

var markers = new ol.layer.Vector({
  source: new ol.source.Vector(),
  style: new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.5, 1],
      anchorXUnits: "fraction",
      anchorYUnits: "fraction",
      src: static_url+"images/borehole.png"
    })
  })
});
map.addLayer(markers);


const typeSelect = document.getElementById('type');

let draw; // global so we can remove it later
function addInteraction() {
  const value = typeSelect.value;
  if (value !== 'None') {
    draw = new ol.interaction.Draw({
      source: source,
      type: typeSelect.value,
    });
    map.addInteraction(draw);
  }

  draw.on('drawstart', function(e) {
    map.getLayers().getArray()[1].getSource().clear();
  });

  document.getElementById("clear").onclick = function() {
    map.getLayers().getArray()[1].getSource().clear();
  }

}



/**
 * Handle change event.
 */
typeSelect.onchange = function () {
  map.removeInteraction(draw);
  addInteraction();
};

document.getElementById('undo').addEventListener('click', function () {
  draw.removeLastPoint();
});

addInteraction();

document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("search").onclick = function() {
        console.log('click')
        lat_holder = parseFloat(document.getElementById("search_lat").value)
        long_holder = parseFloat(document.getElementById("search_long").value)

        coords = ol.proj.fromLonLat([long_holder,lat_holder], 'EPSG:3857');

        console.log(coords)

        scale = 20000
        minx = coords[0]-scale
        miny = coords[1]-scale
        maxx = coords[0]+scale
        maxy = coords[1]+scale

        var extent=[minx,miny,maxx,maxy];

        map.getView().fit(extent,map.getSize());

    }

})

