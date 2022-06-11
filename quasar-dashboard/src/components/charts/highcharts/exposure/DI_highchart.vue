<template>
<!-- <h1>HIGHCHART STOCK DI</h1>-->

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
    text: 'Deviation Index (DI)',
    style: {
      fontSize: 24,
      fontFamily: 'Georgia'
    }
  },
  series: [
    {
      name: 'di',
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


  const data = props['apiData'].map(entry => [new Date(entry.date).setHours(1,0,0,0,),
                                entry.DI? Number(entry.DI):null])

  chartData.data = data
  chartOptions.series[0].data=chartData.data

  const baselines= props['apiData'].filter(entry=>entry.baseline===true)

    const sortedBaselines = baselines.sort((a,b)=>{
         return new Date(b.date) - new Date(a.date)
       })
  const baseline = baselines.length ?  Number(sortedBaselines[0].DI) : 0
  const diData =  props['apiData'].map(entry => Number(entry.DI))

  const yMax  =Math.max(...diData)
  console.log('il massimo ',yMax)

  const yMin  =Math.min(...diData)

  const upper = baselines ? baseline*1.2 : 0

  const lower = baselines ? baseline*0.8 : 0

  const suggestedMax = yMax > upper ? yMax : upper + 0.1

  const suggestedMin = yMin < lower ? yMin : lower -0.2

  chartOptions.yAxis.min = suggestedMin
  chartOptions.yAxis.max = suggestedMax

  chartOptions.yAxis.plotLines[0].value = baseline

  chartOptions.yAxis.plotLines[1].value = lower
  chartOptions.yAxis.plotLines[2].value = upper
})

</script>

<style scoped>

</style>
