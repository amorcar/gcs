import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    waypoints: [],
  },
  mutations: {
    setWaypoints(state, waypoints) {
      console.log('new waypoints in store: ' + waypoints.length)
      state.waypoints = waypoints
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
