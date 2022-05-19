<template>
  <q-page class="q-pa-sm">
        <div v-if="loaded">
      <div class="row q-col-gutter-sm q-py-sm" v-if="!emptyData">
      <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12" >
        <D03 v-if="loaded" :api-data="chartsData" />
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
      <div v-else>
        <div class="col-12 text-blue" >
          NO DATA FROM API SERVICE
          <NoData/>
        </div>


      </div>
    </div>
    <div v-else>
      NO API SERVICE AVAILABLE
    </div>
  </q-page>
</template>

<script>
import {defineComponent, defineAsyncComponent} from 'vue'
import axios from "axios";
export default defineComponent({
  name: "Charts",
  components: {
    PieChart: defineAsyncComponent(() => import('components/charts/PieChart')),
    ScatterPlot: defineAsyncComponent(() => import('components/charts/ScatterPlot')),
    LineChart: defineAsyncComponent(() => import('components/charts/LineChart')),
    BarChart: defineAsyncComponent(() => import('components/charts/BarChart')),
    AreaChart: defineAsyncComponent(() => import('components/charts/AreaChart')),
    GuageChart: defineAsyncComponent(() => import('components/charts/GuageChart')),
    D03: defineAsyncComponent(()=>import('components/charts/highcharts/D03_highchart'))
  },
  data() {
    return {
      emptyData: false,
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

          this.loaded = true
          if(!response.data.length){
            this.emptyData = true
            console.log("SORRY NO DATA FROM THE API")
          }
          console.log("LOADED - chartsData are in parent: ",this.chartsData)
        }).catch(()=>{
          this.loaded = false
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
