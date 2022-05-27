<template>
  <q-page class="q-pa-sm">

<!--    <tables-basic></tables-basic>-->

<!--    <table-actions class="q-mt-lg"></table-actions>-->
<div v-if="loaded">
    <table-dark-mode class="q-mt-lg" :api-data="tableData"/>
</div>
<!--    <table-progress class="q-mt-lg"></table-progress>-->

<!--    <table-custom-grid class="q-mt-lg"></table-custom-grid>-->

  </q-page>
</template>

<script>
import {defineComponent, defineAsyncComponent} from 'vue';
import axios from "axios";

export default defineComponent({
  name: "Tables",
  components: {
    TableProgress: defineAsyncComponent(() => import('components/tables/TableProgress')),
    TableCustomGrid: defineAsyncComponent(() => import('components/tables/TableCustomGrid')),
    TableDarkMode: defineAsyncComponent(() => import('components/tables/TableDarkModeQCremote')),
    TableActions: defineAsyncComponent(() => import('components/tables/TableActions')),
    TablesBasic: defineAsyncComponent(() => import('components/tables/TableBasic'))
  },
  methods: {
    requestData () {
      axios.get('http://localhost:3000/results')
        .then(response => {
          console.log("USED AXIOS ",response.data)
          this.tableData = response.data

          this.loaded = true
          if(!response.data.length){
            this.emptyData = true
            console.log("SORRY NO DATA FROM THE API")
          }

        }).catch(()=>{
          this.loaded = false
      })
    },
  },
  data() {
    return {
      loaded: false,
      emptyData: false,
      tableData: []
    }
  },
  async mounted() {
    this.loaded = false
    this.requestData()
  }
})
</script>

<style>

</style>
