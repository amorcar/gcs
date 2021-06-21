<template>
  <div class="home-page">
    <v-container fluid>
      <v-row>
        <v-col cols="2" md="0">
          <TelemetryDisplay :telemetry="telemetry" />
        </v-col>

        <v-col cols="5">
          <v-row class="ma-auto">
            <Map
              :mission="mission"
              :homePosition="homePosition"
              :dronePosition="dronePosition"
              v-on:new-waypoints="updateWaypoints($event)"
              v-on:update-mission="updateMission($event)"
            />
          </v-row>
          <v-row>
            <v-col>
              <PlotCard />
              <div class="d-block green white--text">Logger</div>
            </v-col>
          </v-row>
        </v-col>

        <v-col>
          <MissionConfiguration
            :mission="mission"
            v-on:update-mission="updateMission($event)"
            v-on:new-waypoints="updateWaypoints($event)"
          />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import TelemetryDisplay from "@/components/TelemetryDisplay";
import Map from "@/components/Map";
import MissionConfiguration from "@/components/MissionConfiguration";
import PlotCard from "@/components/PlotCard";

export default {
  name: "Home",
  components: {
    TelemetryDisplay,
    Map,
    MissionConfiguration,
    PlotCard,
  },
  data() {
    return {
      status: {},
      mission: {},
      telemetry: {},
      dronePosition: {
        latitude: 28.071432,
        longitude: -15.456958,
      },
      homePosition: {
        latitude: 28.071637,
        longitude: -15.457188,
      },
    };
  },
  computed: {},
  created() {
    this.retrieveStatusFromStore();
    this.retrieveMissionFromStore()
    this.getTelemetryUpdateFromBackend();
    // setInterval(this.getStatusUpdateFromBackend, 1000*2)
    // setInterval(this.getTelemetryUpdateFromBackend, 1000*5)
  },
  methods: {
    retrieveStatusFromStore() {
      this.status = this.$store.state.status;
    },
    retrieveMissionFromStore() {
      this.mission = this.$store.state.mission;
    },
    setMission() {
      this.$store.commit("setMission", this.mission.setMission);
    },
    getStatusUpdateFromBackend() {
      console.log("Getting status updates from backend");
    },
    getTelemetryUpdateFromBackend() {
      console.log("Getting telemetry updates from backend");
      this.telemetry = this.mockTelemetry();
    },
    sendMissionToVehicle() {
      console.log("Sending mission to vehicle");
    },
    sendStartMissioToVehicle() {
      console.log("Sending start mission to vehicle");
    },
    sendRTLToVehicle() {
      console.log("Sending RTL to vehicle");
    },
    sendLandToVehicle() {
      console.log("Sending Land to vehicle");
    },
    updateWaypoints(newWaypoints) {
      console.log("updating waypoints in home: " + newWaypoints.length);
      newWaypoints.forEach(function (wp, i) {
        wp.index = i;
      });
      this.mission.waypoints = newWaypoints;
    },
    updateMission(newMission) {
      console.log("updating mision in home: " + newMission.waypoints.length);
      var newWaypoints = [...newMission.waypoints];
      newWaypoints.forEach(function (wp, i) {
        wp.index = i;
      });
      newMission.waypoints = newWaypoints;
      this.mission = newMission;
    },
    mockTelemetry() {
      console.log("Using mock telemetry");
      return {
        flight_mode: 1,
        voltage: 14.2,
        battery: 0.75,
        n_sat: 8,
        gps_fix: 2,
        gps_lat: 28.071637,
        gps_lon: -15.457188,
        gps_alt: 23.1,
        yaw: 123.39,
        pitch: 4.32,
        roll: 2.97,
        speed_n: 20.29,
        speed_e: 3.51,
        speed_d: 0.23,
        rc_signal: 0.3,
      };
    },
  },
};
</script>
