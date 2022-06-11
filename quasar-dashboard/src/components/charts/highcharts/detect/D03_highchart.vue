<template>
<!-- <h1>HIGHCHART STOCK D' 0.3 mm</h1>-->

  <highcharts :constructor-type="'stockChart'" :options="chartOptions" />
</template>

<script setup>

import {onMounted, reactive} from "vue";




const chartData = reactive({
  data: []
})


const chartOptions = reactive({
  rangeSelector:{
   // inputDateFormat: " %b %Y"
  },
  tooltip:{
     xDateFormat: '%A, %b %e, %Y',

  },
  title: {
    text: 'd\' 0.3 mm',
    style: {
      fontSize: 24,
      fontFamily: 'Georgia'
    }
  },
  series: [
    {
      name: 'd03',
      data: chartData.data,
      lineWidth: 5

    },
  ],
  yAxis: {
    title: {
      // text: 'd\''
    },
    gridZIndex: -1,
    opposite: false,
    min: 0,
    max: 10,
    plotLines:[
      {
      value: 0.5,
      color: 'lime',
      // dashStyle: 'shortdash',
      width: 2.2,
        zIndex: 4,
      label: {
              text: 'baseline',
              align: 'left',
              style: {
                   color: "white"
                  }
             }
      },
      {
        value: 1,
        color: '#DB2808',
        dashStyle: 'shortdash',
        width: 2,
        label: {
                text: 'lower',
                style: {
                  color: 'white'
                }
               }
      },
       {
        value: 1,
        color: '#0A77D7',
        dashStyle: 'shortdash',
         width: 2,
        label: {
                text: 'upper',
                style: {
                  color: 'white',
                  zIndex: 10000
                }
               }
      }
    ]

  },


})

const props = defineProps( {
    apiData: [],

  })

onMounted(()=>{

  console.log("MOUNTED HIGHCHARTS D03")
  console.log("dataset data: ",props.apiData)
  const data = props['apiData'].map(entry => [new Date(entry.date).setHours(1,0,0,0,),entry.D03? Number(entry.D03):null])
  console.log("date: ",data)
  chartData.data = data
  chartOptions.series[0].data=chartData.data
  console.log("chartData data: ",chartData.data)
  console.log("chartOptions: ",chartOptions)
  const baselines= props['apiData'].filter(entry=>entry.baseline===true)
  console.log("BASELINES FOR D03: ",baselines)
    const sortedBaselines = baselines.sort((a,b)=>{
         return new Date(b.date) - new Date(a.date)
       })
  const baselineD03 = baselines.length ?  Number(sortedBaselines[0].D03) : 0
  const d03Data =  props['apiData'].map(entry => Number(entry.D03))

  const yMax  =Math.max(...d03Data)
  console.log(yMax)
  const yMin  =Math.min(...d03Data)

  const upper = baselines ? baselineD03*1.2 : 0

  const lower = baselines ? baselineD03*0.8 : 0

  const suggestedMax = yMax > upper ? yMax : upper + 1

  const suggestedMin = yMin < lower ? yMin : lower - 2

  chartOptions.yAxis.min = suggestedMin
  chartOptions.yAxis.max = suggestedMax

  chartOptions.yAxis.plotLines[0].value = baselineD03

  chartOptions.yAxis.plotLines[1].value = lower
  chartOptions.yAxis.plotLines[2].value = upper
})

</script>

<style scoped>

</style>
