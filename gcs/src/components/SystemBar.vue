<template>
   <v-system-bar app
    :lights-out="isLightsOut"
    :color="backgroundColor"
   >
      <v-spacer></v-spacer>
      <v-icon>mdi-wifi-strength-4</v-icon>
      <v-icon>mdi-signal-cellular-outline</v-icon>
      <v-icon>mdi-battery</v-icon>
      <span>12:30</span>
    </v-system-bar> 
</template>

<script>

const status = {
  OK: 0,
  WARNING: 1,
  ERROR: 2,
};
export default {
  name: 'SystemBar',
  data() {
    return {
      currentStatus: status.OK,

    }
  },
  computed: {
    backgroundColor() {
      switch(this.currentStatus){
        case status.OK:
          return 'grey lighten-3';
        case status.WARNING:
          return 'warning';
        case status.ERROR:
          return 'error';
        default:
          return '';
      }
    },
    isLightsOut() {
      if (this.currentStatus == status.OK) {
        return true
      }
      else {
        return false
      }
    }

  },
};
</script>