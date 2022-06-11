<template>
<!-- <h1>HIGHCHART STOCK D' 4 mm</h1>-->

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
    text: 'd\' 4 mm',
    style: {
      fontSize: 24,
      fontFamily: 'Georgia'
    }
  },
  series: [
    {
      name: 'd4',
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
    max: 200,
    plotLines:[
      {
      value: 0.5,
      color: 'lime',
      zIndex: 4,
      // dashStyle: 'shortdash',
      width: 2.2,
      label: {
              text: 'baseline',
              align: 'left',
              style: {
                   color: "white",

                  }
             }
      },
      {
        value: 1,
        color: '#C10015',
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
  const data = props['apiData'].map(entry => [new Date(entry.date).setHours(1,0,0,0,),
                                entry.D4? Number(entry.D4):null])
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
  const baselineD4 = baselines.length ?  Number(sortedBaselines[0].D4) : 0
  const d4Data =  props['apiData'].map(entry => Number(entry.D4))

  const yMax  =Math.max(...d4Data)
  console.log('il massimo ',yMax)
  const yMin  =Math.min(...d4Data)

  const upper = baselines ? baselineD4*1.2 : 0

  const lower = baselines ? baselineD4*0.8 : 0

  const suggestedMax = yMax > upper ? yMax : upper + 20

  const suggestedMin = yMin < lower ? yMin : lower -30

  chartOptions.yAxis.min = suggestedMin
  chartOptions.yAxis.max = suggestedMax

  chartOptions.yAxis.plotLines[0].value = baselineD4

  chartOptions.yAxis.plotLines[1].value = lower
  chartOptions.yAxis.plotLines[2].value = upper
})

</script>

<style scoped>

</style>
