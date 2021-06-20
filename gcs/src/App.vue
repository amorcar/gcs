<template>
  <v-app id="gcs-app">
    <SystemBar/>
    <div class="hidden-sm-and-down">
      <Navigation/>
    </div>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import SystemBar from '@/components/SystemBar'
import Navigation from '@/components/Navigation'

export default {
  name: 'App',

  data: () => ({
    //
  }),
  components: {
    SystemBar,
    Navigation,
  },
  methods: {
    initializeInfo() {
      let info = {
        productName: "GCS",
        productVersion: 0.1,
      }
      this.$store.commit("setInfo", info)
    },
    initializeMission() {
      let mission = {
        altitude: 50,
        finish_action: "ReturnHome",
        type: "Regular",
        waypoints: [
          {
            index: 0,
            latitude: 28.0710182,
            longitude: -15.4573374,
            altitude: 30,
            speed: 5.0,
            loiter: 3.0,
            action: 0,
          },
          {
            index: 1,
            latitude: 28.0717907,
            longitude: -15.4564991,
            altitude: 30,
            speed: 5.0,
            loiter: 0.0,
            action: 1,
          },
          {
            index: 2,
            latitude: 28.0718918,
            longitude: -15.4566183,
            altitude: 30,
            speed: 5.0,
            loiter: 3.0,
            action: 0,
          },
          {
            index: 3,
            latitude: 28.0711174,
            longitude: -15.4574566,
            altitude: 30,
            speed: 5.0,
            loiter: 0,
            action: 2,
          },
        ]
      }
      this.$store.commit("setMission", mission)
    },
    initializeStatus() {
      let status = {
        battery: null,
        signal: null,
        status: 0,
        radio_ready: false,
      }
      this.$store.commit("setStatus", status)
    },
  },
  created() {
    this.initializeInfo()
    this.initializeStatus()
    // this.initializeMission()
  }
};
</script>
