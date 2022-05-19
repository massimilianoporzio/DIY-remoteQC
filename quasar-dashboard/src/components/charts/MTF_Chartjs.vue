<template>

<q-chart
  identifier="myMTFChart"
  stilo="height:300px; width: 100%"
  :type="line"
  :labels="labels"
  :datasets="datasets"
/>
</template>

<script>

import 'chartjs-adapter-date-fns';
import parseJSON from 'date-fns/parseJSON'
export default {
  name: "MTF_Chartjs",
  components: { QChart },
  props: [
     'chartsData'
  ],
  data() {
    return {
      labels: ["1","2"],
      datasets: [{
        label: 'MTF50',
        data:[0.5,0.5]
      }],
      options: {}
    }
  },
  mounted() {
    console.log('PASSED PROPS: ',this.$props.chartsData)
    const xLabels = this.$props.chartsData.map(entry => parseJSON(entry.date))
    // this.labels = xLabels;
    const MTF50data =  this.$props.chartsData.map(entry => entry.MTF50)
    // this.datasets[0].data=MTF50data
  }
}

import QChart from 'quasar-components-chart'


</script>

<style scoped>

</style>
