<template>

  <q-page class="q-pa-sm " style="height: 1px">
    <div class="column full-height" >

        <q-tabs dense v-model="tab"
        align="left"
        class="bg-primary text-white shadow-2"
        :breakpoint="0">
          <q-tab name="overview" class="text-capitalize" >Overview</q-tab>
          <q-tab name="charts" class="text-capitalize">Charts</q-tab>
        </q-tabs>
      <div class="bg-amber col" >

           <q-tab-panels v-model="tab" class="bg-primary full-height"  >
          <q-tab-panel name="overview" >
              <table-dark-mode :api-data="dbData" v-if="loaded"/>
          </q-tab-panel>

          <q-tab-panel name="charts" class="text-white">
            <q-scroll-area dark style="height: 100%">
              <div class="row q-col-gutter-sm q-py-sm justify-center text-h6"  v-if="!emptyData">
                    Detectability charts
                </div>
            <div class="row q-col-gutter-sm q-px-sm q-py-sm ">

                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12" >
                    <D03 v-if="loaded" :api-data="dbData" />
                </div>
              <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12" >
                    <D4 v-if="loaded" :api-data="dbData" />
                </div>
            </div>
            <div class="row q-col-gutter-sm q-px-sm q-py-sm justify-center text-h6">
            Spatial Resolution (MTF) charts
            </div>
            <div class="row q-col-gutter-sm q-px-sm q-py-sm ">
            <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
              <MTF50 v-if="loaded" :api-data="dbData"/>
              </div>
              <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                  <MTF20 v-if="loaded" :api-data="dbData"/>
              </div>
              <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                  <MTF10 v-if="loaded" :api-data="dbData"/>
              </div>
            </div>
              <div class="row q-col-gutter-sm q-px-sm q-py-sm justify-center text-h6">
                  Signal related charts
              </div>
              <div class="row q-col-gutter-sm q-px-sm q-py-sm ">
                <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                  <PV v-if="loaded" :api-data="dbData"/>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                  <SNR v-if="loaded" :api-data="dbData"/>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                  <SDNR v-if="loaded" :api-data="dbData"/>
                </div>
              </div>
                <div class="row q-col-gutter-sm q-px-sm q-py-sm justify-center text-h6">
                  Exposure related charts
              </div>
              <div class="row q-col-gutter-sm q-px-sm q-py-sm ">
                <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                  <EI v-if="loaded" :api-data="dbData"/>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                  <DI v-if="loaded" :api-data="dbData"/>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                  <MAS v-if="loaded" :api-data="dbData"/>
                </div>
              </div>
            </q-scroll-area>

          </q-tab-panel>


        </q-tab-panels>


      </div>

    </div>
  </q-page>

</template>



<script>
import {defineComponent, defineAsyncComponent} from 'vue'
import axios from "axios";
import {ref} from 'vue'
export default defineComponent({
  name: "Charts",
  components: {
    PieChart: defineAsyncComponent(() => import('components/charts/PieChart')),
    ScatterPlot: defineAsyncComponent(() => import('components/charts/ScatterPlot')),
    LineChart: defineAsyncComponent(() => import('components/charts/LineChart')),
    BarChart: defineAsyncComponent(() => import('components/charts/BarChart')),
    AreaChart: defineAsyncComponent(() => import('components/charts/AreaChart')),
    GuageChart: defineAsyncComponent(() => import('components/charts/GuageChart')),
    D03: defineAsyncComponent(()=>import('components/charts/highcharts/detect/D03_highchart')),
    D4: defineAsyncComponent(()=> import('components/charts/highcharts/detect/D4_highchart')),
    MTF50: defineAsyncComponent(()=>import('components/charts/highcharts/MTF/MTF50_highchart')),
    MTF20: defineAsyncComponent(()=>import('components/charts/highcharts/MTF/MTF20_highchart')),
    MTF10: defineAsyncComponent(()=>import('components/charts/highcharts/MTF/MTF10_highchart')),
    PV: defineAsyncComponent(()=>import('components/charts/highcharts/signal/PV_highchart')),
    SNR: defineAsyncComponent(()=>import('components/charts/highcharts/signal/SNR_highchart')),
    SDNR: defineAsyncComponent(()=>import('components/charts/highcharts/signal/SDNR_highchart')),
    EI: defineAsyncComponent(()=>import('components/charts/highcharts/exposure/EI_highchart')),
    DI: defineAsyncComponent(()=>import('components/charts/highcharts/exposure/DI_highchart')),
    MAS: defineAsyncComponent(()=>import('components/charts/highcharts/exposure/MAS_highchart')),
    TableDarkMode: defineAsyncComponent(() => import('components/tables/TableDarkModeQCremote')),
  },

  data() {
    return {
      tab: ref('overview'),

      emptyData: false,
      loaded: false,
      dbData: []

      }
  },
   methods:{

     requestData () {
      axios.get('http://localhost:3000/results')
        .then(response => {
          console.log("USED AXIOS ",response.data)
          this.dbData = response.data

          this.loaded = true
          if(!response.data.length){
            this.emptyData = true
            console.log("SORRY NO DATA FROM THE API")
          }
          console.log("LOADED - dbData are in parent: ",this.dbData)
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
