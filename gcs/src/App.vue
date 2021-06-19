<template>
  <v-app id="gcs-app">
    <SystemBar/>
    <div class="hidden-sm-and-down">
      <Navigation/>
    </div>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import SystemBar from '@/components/SystemBar'
import Navigation from '@/components/Navigation'

export default {
  name: 'App',

  data: () => ({
    //
  }),
  components: {
    SystemBar,
    Navigation,
  }
};
</script>
