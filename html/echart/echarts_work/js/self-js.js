
var temp_value = 25;
var humidity_value=50;
//温度
var option_temp;
var chartDom = document.getElementById('temperature');
var myChart_temp = echarts.init(chartDom);
option_temp = {
    series: [{
        type: 'gauge',
        startAngle: 200,
        endAngle: -20,
        min: 0,
        max: 60,
        splitNumber: 3,
        axisLine: {
            lineStyle: {
                width: 15,
                color: [
                    [0.3, '#67e0e3'],
                    [0.7, '#37a2da'],
                    [1, '#fd666d']
                ]
            }
        },
        pointer: {
            itemStyle: {
                color: 'auto',
            }
        },
        axisTick: {
            distance: -30,
            length: 8,
            lineStyle: {
                color: '#fff',
                width: 2
            }
        },
        splitLine: {
            distance: -30,
            length: 30,
            lineStyle: {
                color: '#fff',
                width: 4
            }
        },
        axisLabel: {
            color: 'auto',
            distance: 16,
            fontSize: 10
        },
        detail: {
            valueAnimation: true,
            fontSize: 10,
            formatter: '温度：'+'{value} ℃',
            color: 'auto'
        },
        data: [{
            value: temp_value,
        }]
    }
    ]
};
//湿度
var chartDom1 = document.getElementById('humidity');
var myChart_humidity = echarts.init(chartDom1);
var humidity;

humidity = {
    series: [{
        type: 'gauge',
        startAngle: 200,
        endAngle: -20,
        min: 0,
        max: 100,
        splitNumber: 5,
        axisLine: {
            lineStyle: {
                width: 15,
                color: [
                    [0.3, '#67e0e3'],
                    [0.7, '#37a2da'],
                    [1, '#fd666d']
                ]
            }
        },
        pointer: {
            itemStyle: {
                color: 'auto',
            }
        },
        axisTick: {
            distance: -30,
            length: 8,
            lineStyle: {
                color: '#fff',
                width: 2
            }
        },
        splitLine: {
            distance: -30,
            length: 30,
            lineStyle: {
                color: '#fff',
                width: 4
            }
        },
        axisLabel: {
            color: 'auto',
            distance: 16,
            fontSize: 10
        },
        detail: {
            valueAnimation: true,
            fontSize: 10,
            formatter: '湿度：'+'{value} %',
            color: 'auto'
        },
        data: [{
            value: humidity_value,
        }]
    }
    ]
};
/*
//假设获取到数据（随机数）
setInterval(function () {
    //湿度
    let random = (Math.random() * 100).toFixed(2) - 0;
    humidity.series[0].data[0].value = random;
    myChart_humidity.setOption(humidity, true);

    //温度
    let random1 = (Math.random() * 60).toFixed(2) - 0;
    option_temp.series[0].data[0].value = random1;
    myChart_temp.setOption(option_temp, true);
}, 2000);
*/



//数据分析曲线
var chartDom_analyse_line = document.getElementById('analyse_line');
var myChart_analyse_line = echarts.init(chartDom_analyse_line);
var option_analyse_line;

option_analyse_line = {
    title: {
        text: '一天内温湿度曲线变化趋势'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['温度', '湿度']
    },
    grid: {
        left: '2%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['0点', '2点', '4点', '6点', '8点', '10点', '12点','14点','16点', '18点', '20点', '22点', '24点']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: '温度',
            type: 'line',
            stack: '总量',
            data: [23, 24, 25, 24, 26, 22, 23, 23, 25, 23, 24, 25,]
        },
        {
            name: '湿度',
            type: 'line',
            stack: '总量',
            data: [52 ,42 ,32 ,52 ,32 ,32 ,22 ,62 ,42 ,52 ,42 ,32,]
        }
    ]
};

option_analyse_line && myChart_analyse_line.setOption(option_analyse_line);
option_temp && myChart_temp.setOption(option_temp);
humidity && myChart_humidity.setOption(humidity);


//vue组件

     var app = new Vue({
        el: '#app',
        data: {
            isCascaderShow: 0,
            dataJson: {},
            state1: '',
            //级联选择器
            vals: [],
            val: [],
            return: {
                dataJson: this.getDataJSon,
                restaurants: [],
            },
            options: [{
                value: 'F6',
                label: '六楼',
                children: [{
                    value: 'F6-001',
                    label: 'F6-001',
                },
                    {
                        value: 'F6-002',
                        label: 'F6-002',
                    },
                    {
                        value: 'F6-003',
                        label: 'F6-003',
                    },
                    {
                        value: 'F6-004',
                        label: 'F6-004',
                    },
                    {
                        value: 'F6-005',
                        label: 'F6-005',
                    },
                ]
            }, {
                value: 'F7',
                label: '七楼',
                children: [
                    {
                        value: 'F7-001',
                        label: 'F7-001',
                    },
                    {
                        value: 'F6-002',
                        label: 'F6-002',
                    },
                    {
                        value: 'F7-002',
                        label: 'F7-002',
                    },
                    {
                        value: 'F7-003',
                        label: 'F7-003',
                    },
                    {
                        value: 'F7-004',
                        label: 'F7-004',
                    },
                    {
                        value: 'F7-005',
                        label: 'F7-005',
                    },
                    {
                        value: 'F7-006',
                        label: 'F7-006',
                    },
                    {
                        value: 'F7-007',
                        label: 'F7-007',
                    },
                    {
                        value: 'F7-008',
                        label: 'F7-008',
                    },
                    {
                        value: 'F7-009',
                        label: 'F7-009',
                    }
                ]

            },],
            options_search: [{
                value: 'F6',
                label: '六楼',
                children: [{
                    value: 'F6-001',
                    label: 'F6-001',
                },
                    {
                        value: 'F6-002',
                        label: 'F6-002',
                    },
                    {
                        value: 'F6-003',
                        label: 'F6-003',
                    },
                    {
                        value: 'F6-004',
                        label: 'F6-004',
                    },
                    {
                        value: 'F6-005',
                        label: 'F6-005',
                    },
                ]
            }, {
                value: 'F7',
                label: '七楼',
                children: [
                    {
                        value: 'F7-001',
                        label: 'F7-001',
                    },
                    {
                        value: 'F6-002',
                        label: 'F6-002',
                    },
                    {
                        value: 'F7-002',
                        label: 'F7-002',
                    },
                    {
                        value: 'F7-003',
                        label: 'F7-003',
                    },
                    {
                        value: 'F7-004',
                        label: 'F7-004',
                    },
                    {
                        value: 'F7-005',
                        label: 'F7-005',
                    },
                    {
                        value: 'F7-006',
                        label: 'F7-006',
                    },
                    {
                        value: 'F7-007',
                        label: 'F7-007',
                    },
                    {
                        value: 'F7-008',
                        label: 'F7-008',
                    },
                    {
                        value: 'F7-009',
                        label: 'F7-009',
                    }
                ]

            },],
        },
        //把方法赋值给window
        mounted() {
            window.handleChange = this.handleChange;
            this.restaurants = this.loadAll();
        },

        methods: {

            //获取温度
            getTemperature(floor_name, room_name) {
                return 25;
            },
            //获取湿度
            getHumidity(floor_name, room_name) {
                return 50;
            },
            //根据楼层房间号加载温湿度
            handleChange() {
                    let floor_arr = this.$refs["cascader-panel"].getCheckedNodes()[0].pathLabels;
                    let floor_name = floor_arr[0];
                    let room_name = floor_arr[1];
                    let temp = this.getTemperature(floor_name, room_name);
                    let humidity = this.getHumidity(floor_name, room_name);
                    let dataJson = {};
                    dataJson.floor_name = floor_name;
                    dataJson.room_name = room_name;
                    dataJson.temp = temp;
                    dataJson.humidity = humidity;
                    this.dataJson = JSON.stringify(dataJson);
                    this.getDataJSon()
            },
            //点击设置温湿度的值
            getDataJSon() {
                let random = (Math.random() * 100).toFixed(2) - 0;
                let random1 = (Math.random() * 60).toFixed(2) - 0;
                myChart_temp.setOption({
                    series: [{
                        //data: [{value: this.dataJson.temp}]
                        data: [{value: random}]
                    }]
                });
                myChart_humidity.setOption({
                    series: [{
                        //data: [{value: this.dataJson.humidity}]
                        data: [{value: random1}]
                    }]
                });
                return this.dataJson;
            },

            //查询
            querySearch(queryString, cb) {
                var restaurants = this.restaurants;
                var results = queryString ? restaurants.filter(this.createFilter(queryString)) : restaurants;
                // 调用 callback 返回建议列表的数据
                cb(results);
            },
            createFilter(queryString) {
                return (restaurant) => {
                    return (restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
                };
            },
            loadAll() {
                let array_floor_rooms = new Array();
                array_floor_rooms = Object.values(this.options[0].children.concat(this.options[1].children));
                return array_floor_rooms;
            },
            handleSelect(item) {
                //console.log(item);
            },

            //获取楼层房间值
            getFloorRoom(item) {
                let result = '';
                if(typeof(this.$refs["el-cascader-search"].getCheckedNodes()[0]) === "undefined"){
                    result  = this.options_search[0].value + "&" +this.options_search[0].children[0].value;
                }else{
                    let floor_arr = this.$refs["el-cascader-search"].getCheckedNodes()[0].pathLabels;
                    let floor_name = floor_arr[0];
                    let room_name = floor_arr[1];
                    ++this.isCascaderShow;
                    result= floor_name + "&" + room_name;
                }
                return result;
            },
            //级联选择器选择查找
            searchValue(item) {
                let floorRoom = this.getFloorRoom();
                let name_arr = floorRoom.split("&");
                let room_name = name_arr[1];
                let floor_name = name_arr[0];
                if (this.options.length === 1) {
                    this.options = this.options_search;
                }
                for (let i = 0; i < this.options.length; i++) {
                    //console.log("this.options[i].children="+JSON.stringify(this.options[i].children));
                    if (this.options[i].label === floor_name) {
                        for (let j = 0; j < this.options[i].children.length; j++) {
                            if (this.options[i].children[j].label === room_name) {
                                this.options = [],
                                    this.options = [{
                                        value: floor_name,
                                        label: floor_name,
                                        children: [{
                                            value: room_name,
                                            label: room_name,
                                        },],
                                    }];
                                this.getDataJSon();
                            }
                        }
                    }
                }
            },

            //文本框输入查找
            searchRoom() {
                let searchText = document.getElementById('searchText').value;
                let room_name = searchText;
                let floor_label = [];
                let floor_value = [];
                let room_label = [];
                let room_value = [];
                if (this.options === null || this.options[0].children.length === 1) {
                    this.options = this.options_search;
                }
                for (let i = 0; i < this.options.length; i++) {
                    //console.log(i+'----------'+"this.options："+JSON.stringify(this.options))
                    for (let j = 0; j < this.options[i].children.length; j++) {
                        if (this.options[i].children[j].label === room_name) {
                            floor_label.push(this.options[i].label);
                            floor_value.push(this.options[i].value);
                            room_label.push(this.options[i].children[j].label);
                            room_value.push(this.options[i].children[j].value);
                            this.getDataJSon();
                        }
                    }
                }
                let arr_options = [];
                for (let i = 0; i < floor_label.length; i++) {
                    arr_options.push({
                                value: floor_value[i],
                                label: floor_label[i],
                                children: [{
                                    value: room_value[i],
                                    label: room_label[i],
                                },],
                            }) ;
                }
                this.options = arr_options;
                if (room_name === null || room_name.length === 0) {
                    this.$alert('输入内容为空,加载所有数据以供选择', '警告', {});
                    this.options = this.options_search;
                } else if (this.options.length ===0 ) {
                    this.$alert('输入内容不存在', '错误', {});
                    this.options = null;
                }
            },
        }
    })