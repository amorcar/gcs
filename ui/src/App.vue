<template>
  <v-app id="gcs-app">
    <SystemBar/>
    <!-- <div class="hidden-md-and-down"> -->
    <div>
      <Navigation/>
    </div>
    <v-main id="main-router">
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
  created() {
    this.setInitialDarkMode()
    this.initializeInfo()
    this.initializeStatus()
    this.initializeMission()
    this.initializeUserMarkers()
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
        type: "Regular",
        finish_action: "ReturnHome",
        altitude: 0,
        overlap: 0,
        waypoints: [],
      };
      this.$store.commit("setMission", mission)
    },
    initializeUserMarkers(){
      let userMarkers = [];
      this.$store.commit("setUserMarkers", userMarkers)
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
    setInitialDarkMode() {
      const systemIsDarkMode = window.matchMedia("(prefers-color-scheme: dark)");
      if (systemIsDarkMode.matches) {
        // Theme set to dark.
        this.$vuetify.theme.dark = true
      } else {
        // Theme set to light.
        this.$vuetify.theme.dark = false
      }
    },
  },
};
</script>

<style scoped>
@media (max-width: 960px) {
    #main-router {
      padding-left:0px;
      margin:0;
    }
}
</style>