<template>
   <v-system-bar app
    :lights-out="isLightsOut"
    :color="backgroundColor"
   >
    <span>GCS v{{ version }}</span>
    <v-spacer></v-spacer>
    <span>{{ statusMessage }}</span>
    <v-spacer></v-spacer>
    <span>{{ timestamp }}</span>
    <v-spacer></v-spacer>
    <span>{{ errorMessage }}</span>
    <v-spacer></v-spacer>
    <v-btn
      icon
      color="pink"
      @click="darkMode"
    >
      <v-icon size="15">{{ bulbIcon }}</v-icon>
    </v-btn>
    <v-icon>mdi-wifi-strength-4</v-icon>
    <v-icon>mdi-signal-cellular-outline</v-icon>
    <span>{{ remainingBatteryPercentage }}%</span>
    <v-icon>mdi-battery</v-icon>
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
      version: '0.1',
      timestamp: '',
      currentStatus: status.OK,
      remainingBatteryPercentage: '100',
      statusMessage: '',
      errorMessage: '',
      bulbIcon: 'mdi-lightbulb-on-outline',

    }
  },
  created() {
    setInterval(this.setTimestamp, 60000);
  },
  mounted() {
    this.setTimestamp()
  },
  methods: {
    getNow: function() {
      const today = new Date();
      // const date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
      const time = today.getHours() + ":" + today.getMinutes()
      // const dateTime = date +' '+ time;
      const dateTime = time;
      // this.timestamp = dateTime;
      return dateTime
    },
    setTimestamp: function() {
      let now = this.getNow()
      this.timestamp = now
    },
    darkMode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
      if (this.$vuetify.theme.dark){
        this.bulbIcon = "mdi-lightbulb-outline"
      } else {
        this.bulbIcon = "mdi-lightbulb-on-outline"
      }
    }
  },
  computed: {
    backgroundColor() {
      switch(this.currentStatus){
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
    isLightsOut() {
      if (this.currentStatus == status.OK) {
        return true
      }
      else {
        return false
      }
    },
  },
};
</script>