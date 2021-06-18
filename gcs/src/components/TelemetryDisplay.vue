<template>
  <v-card flat>
    <v-card-title>
      Telemetry
    </v-card-title>
    <v-data-table
      dense
      :headers="telemetryHeaders"
      :items="telemetryItems"
      hide-default-header
      hide-default-footer
      disable-pagination
      disable-sort
    > </v-data-table>
  </v-card>
</template>


<script>
export default {
  name: "TelemetryDisplay",
  data () {
    return {
      flightMode: 0,
      battery: {
        voltage: 0,
        remaining: 0,
      },
      gpsInfo: {
        satellites: 0,
        fixType: 0
      },
      position: {
        latitude: 0.000,
        longitude: 0.000,
        altitude: 0.000,
      },
      euler: {
        yaw: 0.00,
        pitch: 0.00,
        roll: 0.00,
      },
      speedNed: {
        north: 0.00,
        east: 0.00,
        down: 0.00,
      },
      rc_signal_strength: 0,
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
      { label: 'Flight Mode', value: this.flightModeString },
      { label: 'Voltage (V', value: this.battery.voltage },
      { label: 'Remaining (%)', value: this.battery.remaining },
      { label: 'nº Satellites ', value: this.gpsInfo.satellites },
      { label: 'GPS Fix Type', value: this.fixTypeString },
      { label: 'GPS Latitude', value: this.position.latitude },
      { label: 'GPS Longitude', value: this.position.longitude },
      { label: 'GPS Altitude', value: this.position.altitude },
      { label: 'Yaw', value: this.euler.yaw },
      { label: 'Pitch', value: this.euler.pitch },
      { label: 'Roll', value: this.euler.roll },
      { label: 'Speed North (m/s)', value: this.speedNed.north },
      { label: 'Speed East (m/s)', value: this.speedNed.east },
      { label: 'Speed Down (m/s)', value: this.speedNed.down },
      { label: 'RC Signal Strength (%)', value: this.rc_signal_strength },
    ];
  },
  computed: {
    fixTypeString() {
      switch (this.fixType) {
        case 0:
          return 'No GPS'
        case 1:
          return 'No Fix'
        case 2:
          return 'Fix 2D'
        case 3:
          return 'Fix 3D'
        case 4:
          return 'Fix DGPS'
        case 5:
          return 'RTK Float'
        case 6:
          return 'RTK Fixed'
        default:
          return 'Unkown'
      }
    },
    flightModeString() {
      switch (this.flightMode) {
        case 1:
          return 'Ready'
        case 2:
          return 'Takeoff'
        case 3:
          return 'Hold'
        case 4:
          return 'Mission'
        case 5:
          return 'RTL'
        case 6:
          return 'Land'
        case 7:
          return 'Offboard'
        case 9:
          return 'Manual'
        case 10:
          return 'Altitude Control'
        case 11:
          return 'Position Control'
        case 13:
          return 'Stabilize'
        default:
          return 'Unkown'
      }
    }

  },
};
</script>