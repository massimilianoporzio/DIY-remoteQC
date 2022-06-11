import { boot } from 'quasar/wrappers'
import Highcharts from 'highcharts'
import Stock from "highcharts/modules/stock";
import HighchartsVue from 'highcharts-vue'
import exportingInit from 'highcharts/modules/exporting'
import exportingDataInit from 'highcharts/modules/export-data'
import darkUnica from "highcharts/themes/dark-unica";
import darkGreen from "highcharts/themes/dark-green";
import highContrastDark from "highcharts/themes/high-contrast-dark"
// "async" is optional;
// more info on params: https://v2.quasar.dev/quasar-cli/boot-files
export default boot(async ( { app }) => {
  // something to do
  Stock(Highcharts)
  exportingInit(Highcharts)
  exportingDataInit(Highcharts)
  //darkUnica(Highcharts);
  // darkGreen(Highcharts)
  highContrastDark(Highcharts)
  app.use(HighchartsVue)
})
