<template>
<!-- <h1>HIGHCHART STOCK D' 0.3 mm</h1>-->
  >
  <highcharts :constructor-type="'stockChart'" :options="chartOptions"></highcharts>
</template>

<script setup>

import {onMounted, reactive} from "vue";




const chartData = reactive({
  data: []
})


const chartOptions = reactive({
  title: {
    text: 'd\' 0.3 mm'
  },
  series: [
    {
      name: 'd03',
      data: chartData.data

    },
  ]
})

const props = defineProps( {
    apiData: [],

  })

onMounted(()=>{

  console.log("MOUNTED HIGHCHARTS D03")
  console.log("dataset data: ",props.apiData)
  const data = props['apiData'].map(entry => [new Date(entry.date).setHours(0,0,0,0),Number(entry.D03)])
  console.log("date: ",data)
  chartData.data = data
  chartOptions.series[0].data=chartData.data
  console.log("chartData data: ",chartData.data)
  console.log("chartOptions: ",chartOptions)
})

</script>

<style scoped>

</style>
