(function($, window) {
  function CC(opts) {
    var me = this;


    me.conf = {
      // 追踪模式
      monitor: {
        // 起点坐标
        p: [106.6280289, 26.6220112],

        // 波动系数
        set_num: 0.05,

        // 线的样式
        line_style: new ol.style.Style({
          stroke: new ol.style.Stroke({
            width: 10,
            color: [34, 139, 34, 0.6],
            // lineDash: [10, 10],
          })
        }),
        // 点的样式
        p_style: new ol.style.Style({
          // 设置一个标识
          image: new ol.style.Icon({
            src: './img/user.png',

            // 这个是相当于是进行切图了
            // size: [50,50],

            // 注意这个，竟然是比例 左上[0,0]  左下[0,1]  右下[1，1]
            anchor: [0.5, 0.5],
            // 这个直接就可以控制大小了
            scale: 0.5,

            // 开启转向
            rotateWithView: true,
            // rotation: 0,
          }),

          text: new ol.style.Text({
            // 对其方式
            textAlign: 'center',
            // 基准线
            textBaseline: 'middle',
            offsetY: -30,
            // 文字样式
            font: 'normal 16px 黑体',
            // 文本内容
            text: "name:王老二",
            // 文本填充样式
            fill: new ol.style.Fill({
              color: 'rgba(255,255,255,1)'
            }),
            padding: [5, 5, 5, 5],
            backgroundFill: new ol.style.Fill({
              color: 'rgba(0,0,255,0.6)'
            }),
          })
        }),

        // 刷新时间
        time: 1000,
      },


      center: [106.6280289, 26.6220112],
    };


    me.all_obj = {

      // =======================追踪
      monitor: {
        // 
        layer: null,

        // 数据层
        data_c: null,

        // marker
        p_data: null,

        // 定时器标识
        timer: null,
      },
    };

  };
  CC.prototype = {
    init: function() {
      var me = this;
      me._bind();


      me._map();

      me._monitor();
    },
    _bind: function() {
      var me = this;

      var fn = {


        // 图最优
        _map_fit: function(data_c) {
          // console.log(data_c.getFeatures());

          // 整个容器每个元素的最小最大 集合数组
          var point_arr = [];
          data_c.getFeatures().forEach(function(ele, index) {
            point_arr.push(_one(ele.getGeometry()));
          });


          // 假设第一个点为最合适的点
          var fit_point = point_arr[0];
          point_arr.forEach(function(point, index) {

            // 最小经度
            if (point[0] < fit_point[0]) {
              fit_point[0] = point[0];
            }

            // 最小纬度
            if (point[1] < fit_point[1]) {
              fit_point[1] = point[1];
            }

            // 最大经度
            if (point[2] > fit_point[2]) {
              fit_point[2] = point[2];
            }

            // 最大纬度
            if (point[3] > fit_point[3]) {
              fit_point[3] = point[3];
            }
          });

          // 没有数据
          if (data_c.getFeatures().length == 0) {
            return;
          }
          // 单个DOM
          else if (data_c.getFeatures().length == 1) {

            me.map.getView()
              .centerOn(
                [fit_point[0], fit_point[1]],
                me.map.getSize(), [$(document).width() / 2, $(document).height() / 2]);

            me.map.getView().setZoom(12);
          }
          // 多个dom
          else {
            me.map.getView()
              .fit(fit_point, {
                size: me.map.getSize(),
                padding: [100, 100, 100, 100],
                constrainResolution: false
              });
          }


          // 单个点的最小经纬度/最大经纬度
          function _one(dom) {
            // 4点数组
            var one_p = null;
            // 类型
            var type = dom.getType();

            // 每个类型的坐标值
            var path = dom.getCoordinates();

            if (type == 'Point') {
              one_p = [path[0], path[1], path[0], path[1]];
            }
            // 多边形
            else if (type == 'Polygon') {

              var line_path = path[0];
              one_p = [line_path[0][0], line_path[0][1], line_path[0][0], line_path[0][1]];

              line_path.forEach(function(p, index) {
                // 最小经度
                if (p[0] < one_p[0]) {
                  one_p[0] = p[0];
                }
                // 最小纬度
                if (p[1] < one_p[1]) {
                  one_p[1] = p[1];
                }


                // 最大经度
                if (p[0] > one_p[2]) {
                  one_p[2] = p[0];
                }
                // 最大纬度
                if (p[1] > one_p[3]) {
                  one_p[3] = p[1];
                }
              });
            }
            // 线
            else if (type == 'LineString') {
              one_p = [path[0][0], path[0][1], path[0][0], path[0][1]];

              path.forEach(function(p, index) {
                // 最小经度
                if (p[0] < one_p[0]) {
                  one_p[0] = p[0];
                }
                // 最小纬度
                if (p[1] < one_p[1]) {
                  one_p[1] = p[1];
                }


                // 最大经度
                if (p[0] > one_p[2]) {
                  one_p[2] = p[0];
                }
                // 最大纬度
                if (p[1] > one_p[3]) {
                  one_p[3] = p[1];
                }
              });
            }
            // 圆
            else if (type == 'Circle') {
              path = dom.getCenter();
              one_p = [path[0], path[1], path[0], path[1]];
            }

            return one_p;
          }
        },
        // 点的转向角度设置  new_p 上一点的坐标 old_p 下一点的坐标
        _map_p_rotation: function(new_p, old_p) {
          // 90度的PI值
          var pi_90 = Math.atan2(1, 0);
          // 当前点的PI值
          var pi_ac = Math.atan2(new_p[1] - old_p[1], new_p[0] - old_p[0]);

          return pi_90 - pi_ac;
        },
        _map: function() {
          me.map = new ol.Map({
            target: 'map',
            // 设置地图图层
             layers: [
                 //引入高德地图的图层和标注
                new ol.layer.Tile({
                  source: new ol.source.XYZ({
                      url: 'http://wprd0{1-4}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&style=7&x={x}&y={y}&z={z}'
                  })
              }),
            ],
            view: new ol.View({
              zoom: 12,
              projection: 'EPSG:4326',
              center: [106.6280289, 26.6220112],
            }),
          });
        },


        // 
        _monitor: function() {
          // 层构建
          me._monitor_layer();

          // 打点
          me._monitor_p();

          // 开始移动
          me._monitor_init();
        },

        // 层数据
        _monitor_layer: function() {

          // 层
          me.all_obj.monitor.layer = new ol.layer.Vector();

          // 数据容器
          me.all_obj.monitor.data_c = new ol.source.Vector();

          // 注入层
          me.all_obj.monitor.layer.setSource(me.all_obj.monitor.data_c);

          // 打到地图上
          me.map.addLayer(me.all_obj.monitor.layer);
        },

        // 点
        _monitor_p: function() {
          // console.log(mk_data_c);
          // 创建一个活动图标需要的Feature，并设置位置
          var p_data = new ol.Feature({
            // 就一个参数啊，定义坐标
            geometry: new ol.geom.Point(me.conf.monitor.p)
          });

          // console.log(me.conf.monitor.p_style);
          // 
          p_data.setStyle(me.conf.monitor.p_style);

          // 数据层收集marker
          me.all_obj.monitor.data_c.addFeature(p_data);

          // 最优一次
          // 最优一次
          me._map_fit(me.all_obj.monitor.data_c);

          // 拿到全局
          me.all_obj.monitor.p_data = p_data;

          // 
          p_data = null;
        },
        // 开始追踪
        _monitor_init: function() {

          // 追踪
          var old_p = null;
          var new_p = [0, 0];

          // 得到旧的点
          old_p = me.all_obj.monitor.p_data.getGeometry().flatCoordinates;


          // ***********************************模拟数据
          if (Math.random() > 0.5) {
            new_p[0] = old_p[0] + Math.random() * me.conf.monitor.set_num;
          } else {
            new_p[0] = old_p[0] - Math.random() * me.conf.monitor.set_num;
          }


          if (Math.random() > 0.5) {
            new_p[1] = old_p[1] + Math.random() * me.conf.monitor.set_num;
          } else {
            new_p[1] = old_p[1] - Math.random() * me.conf.monitor.set_num;
          }
          // *******************************************

          // 移动点
          me.all_obj.monitor.p_data
            .setGeometry(new ol.geom.Point(new_p));

          // 设置转向
          me.all_obj.monitor.p_data
            .getStyle()
            .getImage()
            .setRotation(me._map_p_rotation(new_p, old_p));

          // 线的渲染
          me._monitor_init_line(new_p, old_p);

          // 清除
          old_p = null;
          new_p = null;


          me.all_obj.monitor.timer = setTimeout(function() {



            // 
            me._monitor_init();
          }, me.conf.monitor.time);
        },

        // 初始化线
        _monitor_init_line: function(new_p, old_p) {

          var line_data = new ol.Feature({
            geometry: new ol.geom.LineString([old_p, new_p])
          });
          line_data.setStyle(me.conf.monitor.line_style);

          // 注入容器
          me.all_obj.monitor.data_c.addFeature(line_data);
        },
      };

      // 
      for (var k in fn) {
        me[k] = fn[k];
      };
    },
  };
  window.CC = CC;
})(jQuery, window);
