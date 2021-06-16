<template>
  <v-app id="gcs-app">

    <SystemBar/>
    <Navigation/>

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
