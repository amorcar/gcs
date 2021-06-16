<template>
  <v-navigation-drawer
    app
    color="grey lighten-3"
    mini-variant
    permanent
    lights-out
  >
    <v-list>
      <v-list-item to="/" color="rgba(0, 0, 0, 0)">
        <v-avatar
          class="d-block text-center mx-auto mt-4"
          color="grey darken-1"
          size="36"
        >
          <v-icon color="black">
            mdi-map-marker
          </v-icon>
        </v-avatar>
      </v-list-item>

      <v-list-item to="about" color="rgba(0, 0, 0, 0)">
      <v-avatar
        class="d-block text-center mx-auto mt-4"
        color="grey darken-1"
        size="36"
      >
        <v-icon color="black">
          mdi-antenna
        </v-icon>
      </v-avatar>
      </v-list-item>

      <v-list-item link color="rgba(0, 0, 0, 0)">
      <v-avatar
        class="d-block text-center mx-auto mt-4"
        color="grey darken-1"
        size="36"
      >
        <v-icon color="black">
          mdi-chart-line-variant
        </v-icon>
      </v-avatar>
      </v-list-item>

      <v-list-item link color="rgba(0, 0, 0, 0)">
      <v-avatar
        class="d-block text-center mx-auto mt-4"
        color="grey darken-1"
        size="36"
      >
        <v-icon color="black">
          mdi-wrench
        </v-icon>
      </v-avatar>
      </v-list-item>

    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "Navigation",

  data: () => ({
    return: {},
  }),
};
</script>