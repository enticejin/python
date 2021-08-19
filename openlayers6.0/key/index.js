import 'ol/ol.css';
import Feature from 'ol/Feature';
import Map from 'ol/Map';
import View from 'ol/View';
import IGC from 'ol/format/IGC';
import {LineString, Point} from 'ol/geom';
import {Tile as TileLayer, Vector as VectorLayer} from 'ol/layer';
import OSM, {ATTRIBUTION} from 'ol/source/OSM';
import VectorSource from 'ol/source/Vector';
import {Circle as CircleStyle, Fill, Stroke, Style} from 'ol/style';
import {getVectorContext} from 'ol/render';


var colors = {
  'Clement Latour': 'rgba(0, 0, 255, 0.7)',
  'Damien de Baesnt': 'rgba(0, 215, 255, 0.7)',
  'Sylvain Dhonneur': 'rgba(0, 165, 255, 0.7)',
  'Tom Payne': 'rgba(0, 255, 255, 0.7)',
  'Ulrich Prinz': 'rgba(0, 215, 255, 0.7)'
};

var styleCache = {};
var styleFunction = function(feature) {
  var color = colors[feature.get('PLT')];
  var style = styleCache[color];
  if (!style) {
    style = new Style({
      stroke: new Stroke({
        color: color,
        width: 3
      })
    });
    styleCache[color] = style;
  }
  return style;
};

var vectorSource = new VectorSource();

var igcUrls = [
  'data/igc/Clement-Latour.igc',
  'data/igc/Damien-de-Baenst.igc',
  'data/igc/Sylvain-Dhonneur.igc',
  'data/igc/Tom-Payne.igc',
  'data/igc/Ulrich-Prinz.igc'
];

function get(url, callback) {
  var client = new XMLHttpRequest();
  client.open('GET', url);
  client.onload = function() {
    callback(client.responseText);
  };
  client.send();
}

var igcFormat = new IGC();
for (var i = 0; i < igcUrls.length; ++i) {
  get(igcUrls[i], function(data) {
    var features = igcFormat.readFeatures(data,
      {featureProjection: 'EPSG:3857'});
    vectorSource.addFeatures(features);
  });
}

var time = {
  start: Infinity,
  stop: -Infinity,
  duration: 0
};
vectorSource.on('addfeature', function(event) {
  var geometry = event.feature.getGeometry();
  time.start = Math.min(time.start, geometry.getFirstCoordinate()[2]);
  time.stop = Math.max(time.stop, geometry.getLastCoordinate()[2]);
  time.duration = time.stop - time.start;
});

var vectorLayer = new VectorLayer({
  source: vectorSource,
  style: styleFunction
});

var map = new Map({
  layers: [
    new TileLayer({
      source: new OSM({
        attributions: [
          'All maps © <a href="https://www.opencyclemap.org/">OpenCycleMap</a>',
          ATTRIBUTION
        ],
        url: 'https://{a-c}.tile.thunderforest.com/cycle/{z}/{x}/{y}.png' +
            '?apikey=1332d3dd141b4c47b44f662541af194b'
      })
    }),
    vectorLayer
  ],
  target: 'map',
  view: new View({
    center: [703365.7089403362, 5714629.865071137],
    zoom: 9
  })
});


var point = null;
var line = null;
var displaySnap = function(coordinate) {
  var closestFeature = vectorSource.getClosestFeatureToCoordinate(coordinate);
  var info = document.getElementById('info');
  if (closestFeature === null) {
    point = null;
    line = null;
    info.innerHTML = '&nbsp;';
  } else {
    var geometry = closestFeature.getGeometry();
    var closestPoint = geometry.getClosestPoint(coordinate);
    if (point === null) {
      point = new Point(closestPoint);
    } else {
      point.setCoordinates(closestPoint);
    }
    var date = new Date(closestPoint[2] * 1000);
    info.innerHTML =
        closestFeature.get('PLT') + ' (' + date.toUTCString() + ')';
    var coordinates = [coordinate, [closestPoint[0], closestPoint[1]]];
    if (line === null) {
      line = new LineString(coordinates);
    } else {
      line.setCoordinates(coordinates);
    }
  }
  map.render();
};

map.on('pointermove', function(evt) {
  if (evt.dragging) {
    return;
  }
  var coordinate = map.getEventCoordinate(evt.originalEvent);
  displaySnap(coordinate);
});

map.on('click', function(evt) {
  displaySnap(evt.coordinate);
});

var stroke = new Stroke({
  color: 'rgba(255,0,0,0.9)',
  width: 1
});
var style = new Style({
  stroke: stroke,
  image: new CircleStyle({
    radius: 5,
    fill: null,
    stroke: stroke
  })
});
vectorLayer.on('postrender', function(evt) {
  var vectorContext = getVectorContext(evt);
  vectorContext.setStyle(style);
  if (point !== null) {
    vectorContext.drawGeometry(point);
  }
  if (line !== null) {
    vectorContext.drawGeometry(line);
  }
});

var featureOverlay = new VectorLayer({
  source: new VectorSource(),
  map: map,
  style: new Style({
    image: new CircleStyle({
      radius: 5,
      fill: new Fill({
        color: 'rgba(255,0,0,0.9)'
      })
    })
  })
});

document.getElementById('time').addEventListener('input', function() {
  var value = parseInt(this.value, 10) / 100;
  var m = time.start + (time.duration * value);
  vectorSource.forEachFeature(function(feature) {
    var geometry = /** @type {import("../src/ol/geom/LineString.js").default} */ (feature.getGeometry());
    var coordinate = geometry.getCoordinateAtM(m, true);
    var highlight = feature.get('highlight');
    if (highlight === undefined) {
      highlight = new Feature(new Point(coordinate));
      feature.set('highlight', highlight);
      featureOverlay.getSource().addFeature(highlight);
    } else {
      highlight.getGeometry().setCoordinates(coordinate);
    }
  });
  map.render();
});
