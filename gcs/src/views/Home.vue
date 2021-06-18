<template>
<!-- <v-responsive min-height="1000"> -->
  <v-row no-gutters>
    <!-- left column -->
    <v-col cols="2" md="2">
      <TelemetryDisplay/>
  <!-- <div class="d-block pa-2 blue white--text">First</div> -->
    </v-col>

    <!-- center column -->
    <v-col cols="6">
      <v-row no-gutters>
        <!-- <div class="d-block pa-2 pink white--text flex">Map</div> -->
        <Map/>
      </v-row>
      <v-row no-gutters>
        <v-col>
          <div class="d-block pa-2 blue white--text">Radio</div>
        </v-col>
        <v-col>
          <div class="d-block pa-2 green white--text">Logger</div>
        </v-col>
      </v-row>
    </v-col>

    <!-- rigth column -->
    <v-col>
      <div class="d-block pa-2 yellow white--text">Mission</div>
    </v-col>
  </v-row>
<!-- </v-responsive> -->
</template>

<script>
import TelemetryDisplay from '@/components/TelemetryDisplay'
import Map from '@/components/Map'

  export default {
    name: 'Home',

    components: {
      TelemetryDisplay,
      Map,
    },
  }
</script>
