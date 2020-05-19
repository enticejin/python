import 'ol/ol.css';
import Map from 'ol/Map';
import View from 'ol/View';
import GeoJSON from 'ol/format/GeoJSON';
import {Tile as TileLayer, Vector as VectorLayer} from 'ol/layer';
import {OSM, Vector as VectorSource} from 'ol/source';

var map = new Map({
    layers: [
      new TileLayer({
         source: new OSM()
      }),
      new VectorLayer({
          source: new VectorSource({
              url: 'data/geojson/countries.geojson',
              format: new GeoJSON()
          }),
          opacity: 0.5
      })
    ],
    target: 'map',
    view: new View({
        center: ol.proj.transform(
        [106.70, 26.62], 'EPSG:4326', 'EPSG:3857'),
        zoom: 10
    })
});

document.getElementById('export-png').addEventListener('click', function () {
    map.once('rendercomplete', function () {
        var mapCanvas = document.createElement('canvas');
        var size = map.getSize();
        mapCanvas.width = size[0];
        mapCanvas.height = size[1];
        var mapContext = mapCanvas.getContext('2d');
        Array.prototype.forEach.call(document.querySelectorAll('.ol-layer canvas'), function (canvas) {
            if (canvas.width > 0) {
                var opacity = canvas.parentNode.style.opacity;
                mapContext.globalAlpha = opacity === '' ? 1 : Number(opacity);
                var transform = canvas.style.transform;
                // Get the transform parameters from the style's transform matrix
                var matrix = transform.match(/^matrix\(([^\(]*)\)$/)[1].split(',').map(Number);
                // Apply the transform to the export map context
                CanvasRenderingContext2D.prototype.setTransform.apply(mapContext, matrix);
                mapContext.drawImage(canvas, 0, 0);
            }
        });
        if (navigator.msSaveBlob) {
            // link download attribuute does not work on MS browsers
            navigator.msSaveBlob(mapCanvas.msToBlob(), 'map.png');
        } else {
            var link = document.getElementById('image-download');
            link.href = mapCanvas.toDataURL();
            link.click();
        }
    });
    map.renderSync();
})