<template>
  <q-page class="q-pa-sm">
    <div class="row q-col-gutter-sm q-py-sm">
      <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
<!--        <D03lineChart v-if="loaded" :api-data="chartsData"/>-->
            <D03_highchart v-if="loaded" :api-data="chartsData" />
            <div v-else>No charts data</div>
      </div>
      <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
<!--        <D4lineChart v-if="loaded" :api-data="chartsData"/>-->
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">

<!--        <MTF50lineChart v-if="loaded" :api-data="chartsData"/>-->
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
<!--        <MTF20lineChart v-if="loaded" :api-data="chartsData"/>-->
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
<!--        <MTF10lineChart v-if="loaded" :api-data="chartsData"/>-->
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
<!--        <PVlineChart v-if="loaded" :api-data="chartsData"/>-->
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
<!--        <SNRlineChart v-if="loaded" :api-data="chartsData"/>-->
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
<!--        <SDNRlineChart v-if="loaded" :api-data="chartsData"/>-->
      </div>

      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
<!--        <EIlineChart v-if="loaded" :api-data="chartsData"/>-->
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
<!--        <DIlineChart v-if="loaded" :api-data="chartsData"/>-->
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
<!--        <MAslineChart v-if="loaded" :api-data="chartsData"/>-->
      </div>

    </div>
  </q-page>
</template>

<script>
import {defineComponent, defineAsyncComponent} from 'vue'
import axios from "axios";
import MTF10lineChart from "components/charts/chartjs/MTF/MTF10lineChart";
import MTF50lineChart from "components/charts/chartjs/MTF/MTF50lineChart";
import MTF20lineChart from "components/charts/chartjs/MTF/MTF20lineChart";
import D03lineChart from "components/charts/chartjs/detect/D03lineChart"
import D4lineChart from "components/charts/chartjs/detect/D4lineChart";
import PVlineChart from "components/charts/chartjs/signal/PVlineChart";
import SNRlineChart from "components/charts/chartjs/signal/SNRlineChart";
import SDNRlineChart from "components/charts/chartjs/signal/SDNRlineChart";
import EIlineChart from "components/charts/chartjs/exposure/EIlineChart";
import DIlineChart from "components/charts/chartjs/exposure/DIlineChart";
import MAslineChart from "components/charts/chartjs/exposure/MAslineChart";
import D03_highchart from "components/charts/highcharts/D03_highchart"

export default defineComponent({
  name: "Charts",
  components: {
    MAslineChart,
    DIlineChart,
    EIlineChart,
    SDNRlineChart,
    SNRlineChart,
    PVlineChart,
    D4lineChart,
    MTF10lineChart,
    MTF20lineChart,
    MTF50lineChart,
    D03lineChart,
    D03_highchart,

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
