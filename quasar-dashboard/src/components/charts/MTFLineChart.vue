<template>
  <div>
    <q-card>
      <q-card-section class="text-h6">
        MTF
      </q-card-section>
      <q-card-section>
        <div ref="mtflinechart" id="mtf_LineChart" style="height: 300px;"></div>
      </q-card-section>
      <q-resize-observer @resize="onResize"/>
    </q-card>
  </div>
</template>

<script>
import axios from "axios";
import dateformat from 'dateformat'

export default {
  name: "mtf_LineChart",
   props:{
    chartsData: []
  },
  data() {
    return {
      model: false,

      options: {

        color: ['#0A77D7'],
        tooltip: {
          trigger: 'item',

        },

        legend: {
          data: ['MTF\u2085\u2080'],
          bottom: 10,
        },
        grid: {
          left: '5%',
          right: '9%',
          bottom: '20%',
          top: '5%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: []
          }
        ],
        yAxis: [
          {
            type: 'value',
            max: 3,
            min: 0
          }
        ],
        series: [
          {
            name: 'MTF\u2085\u2080',
            type: 'line',
            stack: 'Total',
            smooth: false,
            symbol: 'circle',
            symbolSize: 10,
            lineStyle: {
              width: 2
            },
            markLine: {
              silent: true,
                 data: [
                   {name: ' baseline', yAxis: 0.5, symbol: 'none', xAxis: '',
                     lineStyle: {

                     }},
                   {name: '+15%', yAxis: 0.25, symbol: 'none', xAxis: '',
                     lineStyle: {
                      color: '#DB2808',
                       position: 'start'
                     }
                   },
                   {name: '-15%', yAxis: 0.25, symbol: 'none', xAxis: '',
                     lineStyle: {
                      color: '#099D0D'
                     }
                   },
                 ],
                 symbol:['none', 'none'],
              label:{
                   show: true,
                position: 'end',
                formatter: '{b}'
              }
            },
            toolbox: {
              show: true
            },
            showSymbol: true,
            // areaStyle: {
            //   opacity: 0.8,
            //   color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
            //     offset: 0,
            //     color: 'rgba(128, 255, 165)'
            //   }, {
            //     offset: 1,
            //     color: 'rgba(1, 191, 236)'
            //   }])
            // },
            emphasis: {
              focus: 'series'
            },
            data: [],




          }
          // {
          //   name: 'MTF20',
          //   type: 'line',
          //   stack: 'Total',
          //   smooth: true,
          //   lineStyle: {
          //     width: 1
          //   },
          //   showSymbol: false,
          //   // areaStyle: {
          //   //   opacity: 0.8,
          //   //   color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
          //   //     offset: 0,
          //   //     color: 'rgba(0, 221, 255)'
          //   //   }, {
          //   //     offset: 1,
          //   //     color: 'rgba(77, 119, 255)'
          //   //   }])
          //   // },
          //   emphasis: {
          //     focus: 'series'
          //   },
          //   data: []
          // },
          // {
          //   name: 'MTF10',
          //   type: 'line',
          //   stack: 'Total',
          //   smooth: true,
          //   lineStyle: {
          //     width: 1
          //   },
          //   showSymbol: false,
          //   // areaStyle: {
          //   //   opacity: 0.8,
          //   //   color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
          //   //     offset: 0,
          //   //     color: 'rgba(55, 162, 255)'
          //   //   }, {
          //   //     offset: 1,
          //   //     color: 'rgba(116, 21, 219)'
          //   //   }])
          //   // },
          //   emphasis: {
          //     focus: 'series'
          //   },
          //   data: []
          // },

        ]
      },
      mtf_line_chart: null
    }
  },


 mounted() {

    console.log("init chart")
    this.init();
  },
  watch: {
    '$q.dark.isActive': function () {
      this.init();
    }
  },
  methods: {

     init() {

      // console.log("INIT",this.chartData)
      let mtf_LineChart = document.getElementById('mtf_LineChart');

      echarts.dispose(mtf_LineChart);
      let theme = this.model ? 'dark' : 'light';
      this.mtf_line_chart = echarts.init(mtf_LineChart, theme);
      const xLabels = this.$props.chartsData.map(entry => dateformat(entry.date,'mediumDate'))
       this.options.xAxis[0].data=xLabels
       const MTF50data =  this.$props.chartsData.map(entry => entry.MTF50)
       const baseline= this.$props.chartsData.filter(entry=>entry.baseline===true)
       const baselineMTF50 = baseline[0].MTF50
       const maxValue = Math.max( ...MTF50data );
       const minValue = Math.min( ...MTF50data );
        this.options.yAxis[0].max = maxValue+0.3;


       const baselineDate = this.options.xAxis[0].data[0]

       this.options.series[0].markLine.data[0].yAxis=baselineMTF50
       this.options.series[0].markLine.data[0].xAxis=baselineDate
       this.options.series[0].markLine.data[1].xAxis=baselineDate
       this.options.series[0].markLine.data[1].yAxis=baselineMTF50*1.15
       this.options.series[0].markLine.data[2].xAxis=baselineDate
       this.options.series[0].markLine.data[2].yAxis=baselineMTF50*0.85

       this.options.series[0].data= MTF50data
       // console.log("MTF50 data: ",this.options.series[0].data)
       // this.options.series[1].data= MTF20data
       //
       // this.options.series[2].data= MTF10data
       // console.log("MTF10 data: ",this.options.series[2].data)
       this.mtf_line_chart.setOption(this.options)
    },
    onResize() {
      if (this.mtf_line_chart) {
        this.mtf_line_chart.resize();
      }
    }
  }
}
</script>

<style scoped>
</style>
