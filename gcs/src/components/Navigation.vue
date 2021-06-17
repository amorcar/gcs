<template>
  <v-navigation-drawer
    app
    color="grey lighten-3"
    mini-variant
    permanent
    lights-out
    mini-variant-width="54"
  >
    <v-list
      rounded
      flat
    >
      <v-list-item to="/" >
        <v-avatar
          class="d-block text-center mx-auto"
          color="accent"
          size="36"
        >
          <v-icon color="white">
            mdi-map-marker
          </v-icon>
        </v-avatar>
      </v-list-item>

      <v-list-item to="about">
      <v-avatar
        class="d-block text-center mx-auto"
        color="accent"
        size="36"
      >
        <v-icon color="white">
          mdi-antenna
        </v-icon>
      </v-avatar>
      </v-list-item>

      <v-list-item link>
      <v-avatar
        class="d-block text-center mx-auto"
        color="accent"
        size="36"
      >
        <v-icon color="white">
          mdi-chart-line-variant
        </v-icon>
      </v-avatar>
      </v-list-item>

      <v-list-item link>
      <v-avatar
        class="d-block text-center mx-auto"
        color="accent"
        size="36"
      >
        <v-icon color="white">
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