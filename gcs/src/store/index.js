import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    waypoints: [],
  },
  mutations: {
    setWaypoints(state, waypoints) {
      state.waypoints = []
      console.log('new waypoints in store: ' + waypoints.length)
      for (const [index, waypoint] of waypoints.entries()) {
        state.waypoints.push({
          latitude: waypoint.latitude,
          longitude: waypoint.longitude,
          index: index,
        })
      }
    }
  },
  actions: {
  },
  modules: {
  },
  getters: {
    getWaypoints: state => {
      return state.waypoints
    }
  }
})
