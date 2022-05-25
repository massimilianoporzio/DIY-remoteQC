<template>
  <div class="row">
    <div>
      <h1>QC relativi al mammografo con id: {{impianto_id}}</h1>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

import {onMounted, ref} from "vue";
const route = useRoute()
const impianto_id = ref(null)
onMounted(()=>{
  impianto_id.value = route.params.impianto_id
  console.log("IMPIANTO ID :",impianto_id.value)
})
</script>

<style scoped>

</style>
