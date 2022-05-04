<template>
<div>
    <q-card>
      <q-card-section>
        <Line chart-id="d03" :chart-data="chartData" :chartOptions="chartOptions" height="200"></Line>
        <div class="row">
          <div class="q-px-sm">
            <q-input clearable hint="Start date" filled v-model="startdate" mask="date" @clear="filterData" >
              <template v-slot:append>
                <q-icon name="event" class="cursor-pointer">
                  <q-popup-proxy ref="qDateProxy" cover transition-show="scale" transition-hide="scale">
                    <q-date v-model="startdate" default-year-month="2017/12" @update:model-value="filterData">
                      <div class="row items-center justify-end">
                        <q-btn v-close-popup label="Close" color="primary" flat />
                      </div>
                    </q-date>
                  </q-popup-proxy>
                </q-icon>
              </template>
            </q-input>
           </div>
        <div>
         <q-input clearable hint="Start date" filled v-model="enddate" mask="date" @clear="filterData" >
              <template v-slot:append>
                <q-icon name="event" class="cursor-pointer">
                  <q-popup-proxy ref="qDateProxy" cover transition-show="scale" transition-hide="scale">
                    <q-date v-model="enddate" default-year-month="2017/12" @update:model-value="filterData">
                      <div class="row items-center justify-end">
                        <q-btn v-close-popup label="Close" color="primary" flat />
                      </div>
                    </q-date>
                  </q-popup-proxy>
                </q-icon>
              </template>
            </q-input>
        </div>
        </div>


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
import {computed, onMounted, reactive, ref} from "vue";
import dateformat from "dateformat";

ChartJS.register(annotationPlugin,
  Title, Tooltip, LineElement, Legend,BarElement, PointElement, CategoryScale, LinearScale, CategoryScale, TimeScale, TimeSeriesScale)

const startdate = ref('')
const enddate = ref('')

let maxDate = 0
let minDate = 0



const filterData = ()=>{
  console.log("FILTERING DATA")
  const start1 = new Date(startdate.value)
  const start2 = start1.setHours(0,0,0,0)
  const start =  start2 ? Math.max(start2,minDate) : minDate
  console.log("START IS: ",start)
  const end1 = new Date(enddate.value)
  const end2 = end1.setHours(0,0,0,0)
  const end = end2? Math.min(maxDate,end2) : maxDate
  console.log("END IS: ",end)
  const convertedDates = chartData.labels.map(date=>new Date(date).setHours(0,0,0,0))
console.log('convertedDates: ',convertedDates)
  const filterDates = convertedDates.filter(d=> d>=start && d <=end)
  console.log('filteredates: ',filterDates)
  chartData.labels = filterDates
  //working on data points
  const startArray = convertedDates.indexOf(filterDates[0])
  const endArray = convertedDates.indexOf(filterDates[filterDates.length-1])
  //using slice would modify the original unfiltered data so I'll copy
  const copydatapoints = [...chartData.datasets[0].data]
  //remove the end values so order is modified
  copydatapoints.splice(endArray+1,filterDates.length)
  copydatapoints.splice(0, startArray)
  chartData.datasets[0].data = copydatapoints

}

const chartData = reactive({
  labels: [],
  datasets: [{
    label: 'd\' 0.3 mm',
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
                    text: 'd\' 0.3 mm'
                  }
              },
            x: {
                type: 'time',
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
        text: 'd\' 0.3 mm',
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
          display: false,
          type: 'line',
          yMin: 0.5,
          yMax: 0.5,
          borderColor: '#099D0D',
          borderWidth: 1,
          borderDash: [5,5],
          label: {
          enabled: false,
            backgroundColor: 'rgba(0,0,0,0)',
            color: 'black',
            content: 'baseline',
            position: 'end',
            yAdjust: -10

        }

        },
        line2: {
          display: false,
          type: 'line',
          yMin: 0.5,
          yMax: 0.5,
          borderColor: '#DB2808',
          borderWidth: 0.9,
          label: {
            font:{
              size: 12
            },
          enabled: false,
            backgroundColor: 'rgba(0,0,0,0)',
            color: 'black',
            content: 'lower',
            position: 'end',
            yAdjust: -10

        }

        },
        line3: {
          display: false,
          type: 'line',
          yMin: 0.5,
          yMax: 0.5,
          borderColor: '#0A77D7',
          borderWidth: 0.9,
          label: {
          enabled: false,
            backgroundColor: 'rgba(0,0,0,0)',
            color: 'black',
            content: 'upper',
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
  console.log("MOUNTED D03")
  console.log("dataset data: ",props.apiData)
  // const xLabels = props['apiData'].map(entry => dateformat(entry.date,'mediumDate'))
  const xLabels = props['apiData'].map(entry =>  entry.date)

  console.log("xLabels: ",xLabels)
  const d03Data =  props['apiData'].map(entry => Number(entry.D03))
  chartData.labels = xLabels
  chartData.datasets[0].data = d03Data
  const baselines= props['apiData'].filter(entry=>entry.baseline===true)
  console.log("BASELINES FOR D03: ",baselines)
    const sortedBaselines = baselines.sort((a,b)=>{
         return new Date(b.date) - new Date(a.date)
       })

 const baselineD03 = baselines.length ?  Number(sortedBaselines[0].D03) : 0
 chartOptions.plugins.annotation.annotations.line1.yMin = baselineD03
  chartOptions.plugins.annotation.annotations.line1.yMax = baselineD03
  const yMax  =Math.max(...d03Data)
  const yMin  =Math.min(...d03Data)



  const upper = baselines ? baselineD03*1.2 : 0

  const lower = baselines ? baselineD03*0.8 : 0

  const suggestedMax = yMax > upper ? yMax+0.1 : upper

  const suggestedMin = yMin < lower ? yMin-0.1 : lower

  chartOptions.plugins.annotation.annotations.line2.yMin = lower
  chartOptions.plugins.annotation.annotations.line2.yMax = lower

  chartOptions.plugins.annotation.annotations.line3.yMin = upper
  chartOptions.plugins.annotation.annotations.line3.yMax = upper

  chartOptions.scales.y.suggestedMin = suggestedMin - 0.1*suggestedMin
  chartOptions.scales.y.suggestedMax = suggestedMax + 0.1*suggestedMax

  if(baselines.length){
    chartOptions.plugins.annotation.annotations.line1.display = true
    chartOptions.plugins.annotation.annotations.line2.display = true
    chartOptions.plugins.annotation.annotations.line3.display = true

    chartOptions.plugins.annotation.annotations.line1.label.enabled = true
    chartOptions.plugins.annotation.annotations.line2.label.enabled = true
    chartOptions.plugins.annotation.annotations.line3.label.enabled = true
  }

  //SET MIN AND MAX DATE
  const convertedDates = chartData.labels.map(date=>new Date(date).setHours(0,0,0,0))
  console.log('convertedDates: ',convertedDates)
  minDate =  Math.min(...convertedDates)
  maxDate =  Math.max(...convertedDates)



})
</script>

<style scoped>

</style>
