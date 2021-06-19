<template>
<!-- <v-responsive min-height="1000"> -->
  <v-row class="pa-auto ma-auto">
    <!-- left column -->
    <v-col cols="2" class="hidden-sm-and-down">
      <TelemetryDisplay/>
      <!-- <div class="d-block blue white--text">First</div> -->
    </v-col>

    <!-- center column -->
    <v-col cols="5">
      <v-row>
        <!-- <div class="d-block pa-2 pink white--text flex">Map</div> -->
        <Map/>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-0 mt-2">
          <PlotCard/>
          <!-- <PlotCard/> -->
          <!-- <div class="d-block blue white--text">Radio</div> -->
        <!-- </v-col> -->
        <!-- <v-col> -->
          <div class="d-block green white--text">Logger</div>
        </v-col>
      </v-row>
    </v-col>

    <!-- rigth column -->
    <v-col>
      <!-- <div class="d-block pa-2 yellow white--text">Mission</div> -->
      <MissionConfiguration/>
    </v-col>
  </v-row>
<!-- </v-responsive> -->
</template>

<script>
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
  }
</script>
