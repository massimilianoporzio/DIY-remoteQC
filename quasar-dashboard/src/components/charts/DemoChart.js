import {
  Line,
  mixins
} from 'vue-chartjs'

export default {
  extends: Line,
  mixins: [mixins.reactiveProp],
  data () {
    return {
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  mounted () {
    this.renderChart({
      labels: this.chartData.map(entry => entry.date),
      datasets: [{
        label: 'Results',
        data: this.chartData.map(entry => entry.MTF50)
      }]
    }, this.options)
  }
}
