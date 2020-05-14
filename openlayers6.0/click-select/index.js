import 'ol/ol.css';
import Map from 'ol/Map';
import View from 'ol/View';
import {click, pointerMove, altKeyOnly} from 'ol/events/condition';
import GeoJSON from 'ol/format/GeoJSON';
import Select from 'ol/interaction/Select';
import {Tile as TileLayer, Vector as VectorLayer} from 'ol/layer';
import OSM from 'ol/source/OSM';
import VectorSource from 'ol/source/Vector';
var raster = new TileLayer({
  source: new OSM()
});

var vector = new VectorLayer({
  source: new VectorSource({
    /*url: 'data/geojson/countries.geojson',*/
   url: 'https://geo.datav.aliyun.com/areas_v2/bound/100000.json',

    format: new GeoJSON()
  })
});

var map = new Map({
  layers: [raster, vector],
  target: 'map',
  view: new View({
    center: [106.70, 26.62],
    zoom: 2
  })
});

var select = null; // ref to currently selected interaction

// select interaction working on "singleclick"
var selectSingleClick = new Select();

// select interaction working on "click"
var selectClick = new Select({
  condition: click
});

// select interaction working on "pointermove"
var selectPointerMove = new Select({
  condition: pointerMove
});

var selectAltClick = new Select({
  condition: function(mapBrowserEvent) {
    return click(mapBrowserEvent) && altKeyOnly(mapBrowserEvent);
  }
});

var selectElement = document.getElementById('type');

var changeInteraction = function() {
  if (select !== null) {
    map.removeInteraction(select);
  }
  var value = selectElement.value;
  if (value == 'singleclick') {
    select = selectSingleClick;
  } else if (value == 'click') {
    select = selectClick;
  } else if (value == 'pointermove') {
    select = selectPointerMove;
  } else if (value == 'altclick') {
    select = selectAltClick;
  } else {
    select = null;
  }
  if (select !== null) {
    map.addInteraction(select);
    select.on('select', function(e) {
      document.getElementById('status').innerHTML = '&nbsp;' +
          e.target.getFeatures().getLength() +
          ' selected features (last operation selected ' + e.selected.length +
          ' and deselected ' + e.deselected.length + ' features)';
    });
  }
};


/**
 * onchange callback on the select element.
 */
selectElement.onchange = changeInteraction;
changeInteraction();