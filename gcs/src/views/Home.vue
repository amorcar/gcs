<template>
<!-- <v-responsive min-height="1000"> -->
  <v-row class="pa-auto ma-auto">
    <v-col cols="2" class="hidden-sm-and-down">
      <TelemetryDisplay :initialTelemetry="telemetry"/>
      <!-- <div class="d-block blue white--text">First</div> -->
    </v-col>

    <v-col cols="5">
      <v-row>
        <!-- <div class="d-block pa-2 pink white--text flex">Map</div> -->
        <Map
          :initial_mission="mission"
          :initial_drone_position="null"
          v-on:new-waypoints="updateWaypoints($event)"
        />
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-0 mt-2">
          <PlotCard/>
          <!-- <div class="d-block blue white--text">Radio</div> -->
          <div class="d-block green white--text">Logger</div>
        </v-col>
      </v-row>
    </v-col>

    <v-col>
      <!-- <div class="d-block pa-2 yellow white--text">Mission</div> -->
      <MissionConfiguration :initial_mission="mission"/>
    </v-col>
  </v-row>
<!-- </v-responsive> -->
</template>

<script>
import { mapGetters } from 'vuex'

import TelemetryDisplay from '@/components/TelemetryDisplay'
import Map from '@/components/Map'
import MissionConfiguration from '@/components/MissionConfiguration'
import PlotCard from '@/components/PlotCard'

export default {
  name: 'Home',
  components: {
    TelemetryDisplay,
    Map,
    MissionConfiguration,
    PlotCard,
  },
  data() {
    return {
      status: {},
      mission: {},
      telemetry: {},
    }
  },
  computed: {
  },
  created() {
    this.retrieveStatusFromStore()
    this.retrieveMissionFromStore()
    this.getTelemetryUpdateFromBackend()
    // setInterval(this.getStatusUpdateFromBackend, 1000*2)
    // setInterval(this.getTelemetryUpdateFromBackend, 1000*5)
  },
  methods: {
    retrieveStatusFromStore() {
      this.status = this.$store.state.status
    },
    retrieveMissionFromStore() {
      this.mission = this.$store.state.mission
    },
    setWaypoints(){
      this.$store.commit('setWaypoints', this.mission.setWaypoints)
    },
    setMission(){
      this.$store.commit('setMission', this.mission.setMission)
    },
    getStatusUpdateFromBackend(){
      console.log('Getting status updates from backend')
    },
    getTelemetryUpdateFromBackend(){
      console.log('Getting telemetry updates from backend')
      this.telemetry = this.mockTelemetry()
    },
    sendMissionToVehicle() {
      console.log('Sending mission to vehicle')
    },
    sendStartMissioToVehicle(){
      console.log('Sending start mission to vehicle')
    },
    sendRTLToVehicle(){
      console.log('Sending RTL to vehicle')
    },
    sendLandToVehicle(){
      console.log('Sending Land to vehicle')
    },
    updateWaypoints(newWaypoints) {
      this.mission.waypoints = newWaypoints
    },
    mockTelemetry() {
      console.log('Using mock telemetry')
      return {
        flight_mode: 1,
        voltage: 14.2,
        battery: 0.75,
        n_sat: 8,
        gps_fix: 2,
        gps_lat: 28.071637,
        gps_lon: -15.457188,
        gps_alt: 23.1,
        yaw: 123.39,
        pitch: 4.32,
        roll: 2.97,
        speed_n: 20.29,
        speed_e: 3.51,
        speed_d: 0.23,
        rc_signal: 0.3,
      }
    }
  },
}
</script>
