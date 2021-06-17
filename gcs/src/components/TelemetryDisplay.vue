<template>
  <v-data-table
    :headers="telemetryHeaders"
    :items="telemetryItems"
    hide-default-header
    hide-default-footer
  > </v-data-table>
  <!-- <div class="d-block pa-2 blue white--text">First</div> -->
</template>


<script>
export default {
  name: "TelemetryDisplay",
  data () {
    return {
      battery: {
        voltage: 15,
        remaining: 70,
      },
      gpsInfo: {
        satellites: 2,
        fixType: '2D Position'
      },
      telemetryHeaders: [
          {
            text: 'Topic',
            align: 'start',
            value: 'label',
          },
          { text: 'Data', value: 'value' },
        ],
      telemetryItems: [],
    }
  },
  mounted() {
    this.telemetryItems = [
      { label: 'Voltage (V:', value: this.battery.voltage },
      { label: 'Remaining (%):', value: this.battery.remaining },
      { label: 'nº Satellites: ', value: this.gpsInfo.satellites },
      { label: 'GPS Fix Type', value: this.gpsInfo.fixType },
    ];
  },
  methods: {

  },
};
</script>