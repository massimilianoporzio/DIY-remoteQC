<template>
<div>
    <q-card>
      <q-card-section>
       CIAO
        <Line :chart-data="chartData" :chartOptions="chartOptions" height="200"></Line>
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
    label: 'MTF\u2085\u2080',
    data: []
  }]

})

const chartOptions = reactive({
  scales: { y: {
                suggestedMin: 0,
                suggestedMax: 1.0
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
    autocolors: false,
    annotation: {
      annotations: {
        line1: {
          type: 'line',
          yMin: 0.5,
          yMax: 0.5,
          borderColor: '#099D0D',
          borderWidth: 2,
          label: {
          enabled: true,
            backgroundColor: 'rgba(0,0,0,0)',
            color: 'black',
            content: 'baseline',
            position: 'end',
            yAdjust: -10

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
  console.log("MOUNTED CHARTS")
  console.log("dataset data: ",props.apiData)
  // const xLabels = props['apiData'].map(entry => dateformat(entry.date,'mediumDate'))
  const xLabels = props['apiData'].map(entry =>  entry.date)
  console.log("xLabels: ",xLabels)
  const MTF50data =  props['apiData'].map(entry => entry.MTF50)
  console.log("MTFdata: ",MTF50data)
  chartData.labels = xLabels
  chartData.datasets[0].data = MTF50data
})
</script>

<style scoped>

</style>
