<template>
<!-- <v-responsive min-height="1000"> -->
  <v-row no-gutters>
    <v-col>
      <TelemetryDisplay/>
  <!-- <div class="d-block pa-2 blue white--text">First</div> -->
    </v-col>
    <v-col cols="6">
      <div class="d-block pa-2 green white--text">
        Second
      </div>
    </v-col>
    <v-col>
      <div class="d-block pa-2 yellow white--text">
        Third
      </div>
    </v-col>
  </v-row>
<!-- </v-responsive> -->
</template>

<script>
import TelemetryDisplay from '@/components/TelemetryDisplay'

  export default {
    name: 'Home',

    components: {
      TelemetryDisplay,
    },
  }
</script>
