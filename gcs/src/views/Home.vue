<template>
  <v-row no-gutters>
    <v-col>
      <TelemetryDisplay/>
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
