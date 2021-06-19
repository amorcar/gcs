import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    info: Object,
    mission: Object,
    status: Object,
  },
  mutations: {
    setWaypoints(state, waypoints) {
      state.mission.waypoints = []
      console.log('New waypoints in store: ' + waypoints.length)
      for (const [index, waypoint] of waypoints.entries()) {
        state.mission.waypoints.push({
          index: index,
          latitude: waypoint.latitude,
          longitude: waypoint.longitude,
          altitude: waypoint.altitude,
          speed: waypoint.speed,
          loiter: waypoint.loiter,
          action: waypoint.action
        })
      }
    },
    setMission(state, mission) {
      console.log("New mission in store")
      state.mission = mission
    },
    setInfo(state, info) {
      console.log("New info in store")
      state.info = info
    },
    setStatus(state, status) {
      console.log("New status in store")
      state.status = status
    },
  },
  actions: {
  },
  modules: {
  },
  getters: {
    getWaypoints: state => {
      return state.waypoints
    },
    getStatus: state => {
      return state.status
    },
    getInfo: state => {
      return state.info
    }
  }
})
