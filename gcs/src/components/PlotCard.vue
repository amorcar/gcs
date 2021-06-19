<template>
  <v-card class="mx-auto" >
    <v-card-title>
      <v-icon
        :color="checking ? 'red lighten-2' : 'indigo'"
        class="mr-12"
        size="32"
        @click="reload"
      >
        {{ iconName }}
      </v-icon>
      <v-row align="start">
        <div class="text-caption grey--text text-uppercase">
          {{ titleLabel }}
        </div>
        <div>
          <span class="font-weight-black" v-text="avg || '—'"></span>
          <strong v-if="avg">{{ units }}</strong>
        </div>
      </v-row>

      <v-spacer></v-spacer>

      <v-btn icon class="align-self-start" size="28">
        <v-icon>mdi-arrow-right-thick</v-icon>
      </v-btn>
    </v-card-title>

    <v-sheet color="transparent">
      <v-sparkline
        :key="String(avg)"
        :smooth="10"
        :gradient="['#1feaea', '#ffd200', '#f72047', ]"
        :line-width="1"
        :value="data"
        auto-draw
        stroke-linecap="round"
        height="40"
      ></v-sparkline>
    </v-sheet>
  </v-card>
</template>

<script>
// :gradient="['#f72047', '#ffd200', '#1feaea']"
const exhale = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
export default {
  name: "PlotCard",
  data: () => ({
    titleLabel: "Altitude",
    units: "m",
    iconName: "mdi-arrow-up",
    checking: false,
    data: [],
    nPointsToPlot: 20
  }),

  computed: {
    avg() {
      const sum = this.data.reduce((acc, cur) => acc + cur, 0);
      const length = this.data.length;

      if (!sum && !length) return 0;

      return Math.ceil(sum / length);
    },
  },

  created() {
    this.reload(false);
  },

  methods: {
    heartbeat() {
      return Math.ceil(Math.random() * (50 - 5) + 5);
    },
    async reload(inhale = true) {
      this.checking = true;
      inhale && (await exhale(1000));
      this.data = Array.from({ length: this.nPointsToPlot }, this.heartbeat);
      this.checking = false;
    },

  },
};
</script>