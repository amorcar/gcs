import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    info: Object,
    // mission: Object,
    status: Object,
  },
  mutations: {
    setMission(state, mission) {
      console.log("New mission in store")
      state.mission = mission
    },
    setUserMarkers(state, markers) {
      console.log("New markers in store")
      state.userMarkers = markers
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
    getMission: state => {
      return state.mission
    },
    getUserMarkers: state => {
      return state.userMarkers
    },
    getStatus: state => {
      return state.status
    },
    getInfo: state => {
      return state.info
    }
  }
})
