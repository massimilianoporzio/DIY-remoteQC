<template>
<div>
    <q-card>
      <q-card-section>
        <Line chart-id="EI" :chart-data="chartData" :chartOptions="chartOptions" height="300"></Line>
      </q-card-section>

    </q-card>
  </div>
</template>

<script setup>

import annotationPlugin from 'chartjs-plugin-annotation';

import 'chartjs-adapter-date-fns';
import { parseJSON } from 'date-fns'
import {Line} from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, PointElement, BarElement, LineElement, CategoryScale, LinearScale, TimeScale, TimeSeriesScale} from 'chart.js'
import {onMounted, reactive, ref} from "vue";
import dateformat from "dateformat";

ChartJS.register(annotationPlugin,
  Title, Tooltip, LineElement, Legend,BarElement, PointElement, CategoryScale, LinearScale, CategoryScale, TimeScale, TimeSeriesScale)

const chartData = reactive({
  labels: [],
  datasets: [{
    label: 'Exposure index (EI)',
    borderColor: 'black',
    borderWidth: 1.5,

    data: []
  }]

})

const chartOptions = reactive({
  scales: { y: {
                suggestedMin: 0,
                suggestedMax: 1.0,
                  title:{
                    display: true,
                    text: 'Exposure index (EI)'
                  }
              },
            x: {
                type: 'timeseries',
                time: {
                    unit: 'day',
                    displayFormats: {
                        day: 'dd MMM yy'
                    },
                    tooltipFormat: 'dd MMM yy'
                }
            }
        },
  plugins: {
    title: {
        display: true,
        text: 'Exposure index (EI)',
        font: {
          family: 'serif',
          size:24
        }
      },
    legend:{
      display: false
    },
    autocolors: false,
    annotation: {
      annotations: {
        line1: {
          type: 'line',
          yMin: 0.5,
          yMax: 0.5,
          borderColor: '#099D0D',
          borderWidth: 1,
          borderDash: [5,5],
          label: {
          enabled: true,
            backgroundColor: 'rgba(0,0,0,0)',
            color: 'black',
            content: 'baseline',
            position: 'end',
            yAdjust: -10,
            font:{
              size: 10
            },

        }

        },
        line2: {
          type: 'line',
          yMin: 0.5,
          yMax: 0.5,
          borderColor: '#DB2808',
          borderWidth: 0.9,
          label: {
            font:{
              size: 10
            },
          enabled: true,
            backgroundColor: 'rgba(0,0,0,0)',
            color: 'black',
            content: 'lower',
            position: 'end',
            yAdjust: -10

        }

        },
        line3: {
          type: 'line',
          yMin: 0.5,
          yMax: 0.5,
          borderColor: '#0A77D7',
          borderWidth: 0.9,
          label: {
          enabled: true,
            backgroundColor: 'rgba(0,0,0,0)',
            color: 'black',
            content: 'upper',
            position: 'end',
            yAdjust: -10,
            font:{
              size: 10
            },

        }

        }
      }
    }
  }
})

const props = defineProps( {
    apiData: [],

  })

onMounted(()=>{
  console.log("MOUNTED EI")
  console.log("dataset data: ",props.apiData)
  // const xLabels = props['apiData'].map(entry => dateformat(entry.date,'mediumDate'))
  const xLabels = props['apiData'].map(entry =>  entry.date)
  console.log("xLabels: ",xLabels)
  const EIData =  props['apiData'].map(entry => Number(entry.EI))
  chartData.labels = xLabels
  chartData.datasets[0].data = EIData
  const baselines= props['apiData'].filter(entry=>entry.baseline===true)
  const sortedBaselines = baselines.sort((a,b)=>{
         return new Date(b.date) - new Date(a.date)
       })
  // console.log(baselines)
  // console.log(sortedBaselines)
  const baselineEI = Number(sortedBaselines[0].EI)

  chartOptions.plugins.annotation.annotations.line1.yMin = baselineEI
  chartOptions.plugins.annotation.annotations.line1.yMax = baselineEI
  const yMax  =Math.max(...EIData)
  const yMin  =Math.min(...EIData)
  const upper = baselineEI*1.2
  const lower = baselineEI*0.8

  const suggestedMax = yMax > upper ? yMax+0.1 : upper
  const suggestedMin = yMin < lower ? yMin-0.1 : lower

  chartOptions.plugins.annotation.annotations.line2.yMin = lower
  chartOptions.plugins.annotation.annotations.line2.yMax = lower

  chartOptions.plugins.annotation.annotations.line3.yMin = upper
  chartOptions.plugins.annotation.annotations.line3.yMax = upper

  chartOptions.scales.y.suggestedMin = suggestedMin - 0.5*baselineEI
  chartOptions.scales.y.suggestedMax = suggestedMax + 0.1*baselineEI



})
</script>

<style scoped>

</style>
