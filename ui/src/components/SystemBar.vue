<template>
   <v-system-bar app
    :color="backgroundColor"
   >
    <span>{{ info.productName }} v{{ info.productVersion }}</span>
    <v-spacer></v-spacer>
    <span>{{ timestamp }}</span>
    <v-spacer></v-spacer>
    <v-btn
      icon
      @click="toggleTheme"
    >
      <v-icon size="15">{{ toggleThemeButtonIcon }}</v-icon>
    </v-btn>
    <v-icon>{{ signalLevelIcon }}</v-icon>
    <!-- <v-icon>mdi-signal-cellular-outline</v-icon> -->
    <span v-if="status.battery" >{{ status.battery }}%</span>
    <v-icon>{{ batteryIcon }}</v-icon>
</v-system-bar> 
</template>


<script>
import { mapGetters } from 'vuex'

const status = {
  OK: 0,
  WARNING: 1,
  ERROR: 2,
};

export default {
  name: 'SystemBar',
  data() {
    return {
      timestamp: '',
      toggleThemeButtonIcon: 'mdi-lightbulb-on-outline',

    }
  },
  created() {
    setInterval(this.updateClock, 60000);
  },
  mounted() {
    this.updateClock()
  },
  methods: {
    getNow: function() {
      const today = new Date();
      const time = today.getHours() + ":" + today.getMinutes()
      return time
    },
    updateClock: function() {
      let now = this.getNow()
      this.timestamp = now
    },
    toggleTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
      if (this.$vuetify.theme.dark){
        this.toggleThemeButtonIcon = "mdi-lightbulb-on-outline"
      } else {
        this.toggleThemeButtonIcon = "mdi-lightbulb-outline"
      }
    }
  },
  computed: {
    ...mapGetters({
      status: 'getStatus',
      info: 'getInfo',
    }),
    batteryIcon(){
      if (!this.status.battery) {
        return "mdi-battery-off-outline"
      }
      else if (Number(this.battery) > 0.8) {
        return "mdi-battery-high"
      }
      else if (Number(this.battery) > 0.5) {
        return "mdi-battery-medium"
      }
      else {
        return "mdi-battery-low"
      }
    },
    signalLevelIcon(){
      if (!this.status.radio_ready) {
        return "mdi-wifi-off"
      }
      if (!this.status.signal) {
        return "mdi-wifi-off"
      }
      else if (this.status.signal > 0.9) {
        return "mdi-wifi-strength-4"
      }
      else if (this.status.signal > 0.7) {
        return "mdi-wifi-strength-3"
      }
      else if (this.status.signal > 0.5) {
        return "mdi-wifi-strength-2"
      }
      else if (this.status.signal > 0.3) {
        return "mdi-wifi-strength-1"
      }
      else {
        return "wifi-strength-outline"
      }
    },
    backgroundColor() {
      switch(this.status.status){
        case status.OK:
          let color = 'grey lighten-3'; 
          if (this.$vuetify.theme.dark){
            color = 'grey darken-4'; 
          }
          return color
        case status.WARNING:
          return 'warning';
        case status.ERROR:
          return 'error';
        default:
          return '';
      }
    },
  },
};
</script>