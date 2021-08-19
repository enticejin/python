//温度
var option2;
var chartDom = document.getElementById('temperature');
var myChart2 = echarts.init(chartDom);
option2 = {
    series: [{
        type: 'gauge',
        startAngle: 200,
        endAngle: -20,
        min: 0,
        max: 100,
        splitNumber: 10,
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
            value: 50
        }]
    }
    ]
};
//湿度
var chartDom1 = document.getElementById('humidity');
var myChart1 = echarts.init(chartDom1);
var humidity;

humidity = {
    series: [{
        type: 'gauge',
        startAngle: 200,
        endAngle: -20,
        min: 0,
        max: 100,
        splitNumber: 10,
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
            value: 50
        }]
    }
    ]
};

//假设获取到数据（随机数）
setInterval(function () {
    //湿度
    let random = (Math.random() * 100).toFixed(2) - 0;
    humidity.series[0].data[0].value = random;
    myChart1.setOption(humidity, true);

    //温度
    let random1 = (Math.random() * 60).toFixed(2) - 0;
    option2.series[0].data[0].value = random1;
    myChart2.setOption(option2, true);
}, 2000);
option2 && myChart2.setOption(option2);
humidity && myChart1.setOption(humidity);
//将获取到的楼层及房间打印出来
function getCascaderObj(val, opt) {
    return val.map(function (value, index, array) {
        for (var itm of opt) {
            if (itm.value == value) {
                opt = itm.children;
                return itm;
            }
        }
        return null;
    });
}
