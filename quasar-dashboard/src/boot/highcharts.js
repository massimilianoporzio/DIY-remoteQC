import { boot } from 'quasar/wrappers'
import Highcharts from 'highcharts'
import Stock from "highcharts/modules/stock";
import HighchartsVue from 'highcharts-vue'
// "async" is optional;
// more info on params: https://v2.quasar.dev/quasar-cli/boot-files
export default boot(async ( { app }) => {
  // something to do
  Stock(Highcharts)
  app.use(HighchartsVue)
})
