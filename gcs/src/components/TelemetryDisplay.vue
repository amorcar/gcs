<template>
  <v-card>
    <v-card-title> Telemetry </v-card-title>
    <v-data-table
      dense
      :headers="telemetryHeaders"
      :items="telemetryItems"
      hide-default-header
      hide-default-footer
      disable-pagination
      disable-sort
    >
    </v-data-table>
  </v-card>
</template>


<script>
export default {
  name: "TelemetryDisplay",
  props: {
    telemetry: Object,
  },
  data() {
    return {
      telemetryHeaders: [
        {
          text: "Topic",
          align: "start",
          value: "label",
        },
        { text: "Data", value: "value" },
      ],
      telemetryItems: [],
    };
  },
  mounted() {
    this.telemetryItems = [
      { label: "Flight Mode", value: this.flightModeString },
      { label: "Voltage (V)", value: this.telemetry.voltage },
      { label: "Remaining (%)", value: this.telemetry.battery },
      { label: "nº Sat ", value: this.telemetry.n_sat },
      { label: "GPS Fix", value: this.fixTypeString },
      { label: "GPS Lat", value: this.telemetry.gps_lat },
      { label: "GPS Lon", value: this.telemetry.gps_lon },
      { label: "GPS Alt", value: this.telemetry.gps_alt },
      { label: "Yaw", value: this.telemetry.yaw },
      { label: "Pitch", value: this.telemetry.pitch },
      { label: "Roll", value: this.telemetry.roll },
      { label: "Spd North (m/s)", value: this.telemetry.speed_n },
      { label: "Spd East (m/s)", value: this.telemetry.speed_e },
      { label: "Spd Down (m/s)", value: this.telemetry.speed_d },
      { label: "RC Signal (%)", value: this.telemetry.rc_signal },
    ];
  },
  computed: {
    fixTypeString() {
      switch (this.telemetry.gps_fix) {
        case 0:
          return "No GPS";
        case 1:
          return "No Fix";
        case 2:
          return "Fix 2D";
        case 3:
          return "Fix 3D";
        case 4:
          return "Fix DGPS";
        case 5:
          return "RTK Float";
        case 6:
          return "RTK Fixed";
        default:
          return "Unkown";
      }
    },
    flightModeString() {
      switch (this.telemetry.flight_mode) {
        case 1:
          return "Ready";
        case 2:
          return "Takeoff";
        case 3:
          return "Hold";
        case 4:
          return "Mission";
        case 5:
          return "RTL";
        case 6:
          return "Land";
        case 7:
          return "Offboard";
        case 9:
          return "Manual";
        case 10:
          return "Alt Ctl";
        case 11:
          return "Pos Ctl";
        case 13:
          return "Stab";
        default:
          return "Unkown";
      }
    },
  },
};
</script>