<template>
  <q-page class="q-pa-sm">
    <div class="row q-col-gutter-sm q-py-sm">
      <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
        <h2>d' 0.3 mm charts</h2>
      </div>
      <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
        <h2>d' 4 mm charts</h2>
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">

        <MTF50lineChart v-if="loaded" :api-data="chartsData"></MTF50lineChart>
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
        <MTF20lineChart v-if="loaded" :api-data="chartsData"></MTF20lineChart>
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
        <MTF10lineChart v-if="loaded" :api-data="chartsData"></MTF10lineChart>
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
        <h2>Signal (PV chart)</h2>
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
        <h2>SNR chart</h2>
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
        <h2>SDNR chart</h2>
      </div>

      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
        <h2>EI chart</h2>
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
        <h2>DI chart</h2>
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
        <h2>mAs chart</h2>
      </div>

    </div>
  </q-page>
</template>

<script>
import {defineComponent, defineAsyncComponent} from 'vue'
import axios from "axios";
import MTF10lineChart from "components/charts/chartjs/MTF10lineChart";
import MTF50lineChart from "components/charts/chartjs/MTF50lineChart";
import MTF20lineChart from "components/charts/chartjs/MTF20lineChart";

export default defineComponent({
  name: "Charts",
  components: {
    MTF10lineChart,
    MTF20lineChart,
    MTF50lineChart,

    PieChart: defineAsyncComponent(() => import('components/charts/PieChart')),
    ScatterPlot: defineAsyncComponent(() => import('components/charts/ScatterPlot')),
    LineChart: defineAsyncComponent(() => import('components/charts/LineChart')),

    BarChart: defineAsyncComponent(() => import('components/charts/BarChart')),
    AreaChart: defineAsyncComponent(() => import('components/charts/AreaChart')),
    GuageChart: defineAsyncComponent(() => import('components/charts/GuageChart')),
  },
  data() {
    return {
      loaded: false,
        chartsData: []

      }
  },
  methods:{
     requestData () {
      axios.get('http://localhost:3000/results')
        .then(response => {
          console.log("USED AXIOS ",response.data)
          this.chartsData = response.data
        //   this.chartsData = {
        //     labels: [ 'January', 'February', 'March' ],
        //     datasets: [
        //   {
        //     label: 'MTF50',
        //     backgroundColor: '#0A77D7',
        //     data: [40, 20, 12]
        //   }
        // ]
        //   }


          // this.rawData = response.data.rows
          this.loaded = true
          console.log("LOADED - chartsData are in parent: ",this.chartsData)
        })
    },
  },
  async mounted() {
    this.loaded = false
    this.requestData()

  }
})
</script>

<style scoped>

</style>
