<template>
  <div id="mapid"></div>
</template>

<script>
import '@geoman-io/leaflet-geoman-free';

export default {
  name: 'Map',

  data() {
    return {
      waypoints: [],
      dronePosition: {
        latitude: null,
        longitude: null,
      },
      map: null,
      missionLayer: null,
      droneLayer: null,
    }
  },
  methods:{
    setupMap() {
      // create the map 28.071637, -15.457188
      this.map = L.map('mapid').setView([28.071637, -15.457188], 18);

      // setup map layer
      var OPSLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
      }).addTo(this.map);

      // show the scale bar on the lower left corner
      L.control.scale().addTo(this.map);

      // create layers
      var baseMaps = {
        "OpenStreetMap": OPSLayer,
      };

      this.missionLayer = L.layerGroup()
      this.droneLayer = L.layerGroup()

      var overlayMaps = {
          "Mission": this.missionLayer,
          "Drone": this.droneLayer,
      };
      L.control.layers(baseMaps, overlayMaps) .addTo(this.map);

      // show a marker on the map
      var homeIcon = L.icon({
        iconUrl: require('@/assets/home.svg'),
        iconSize:     [38, 38], // size of the icon
      });
      var marker = L.marker([28.071637, -15.457188], {icon: homeIcon}).addTo(this.map);
      marker.bindPopup("<b>Home Position</b><br>28.071637, -15.457188");

      // add Leaflet-Geoman controls with some options to the map  
      this.map.pm.addControls({  
        position: 'topleft',  
        drawCircle: false,  
      });

    },
    updateteWaypointsMarkers() {
      var markers = []
      for (const wp of this.waypoints) {
        markers.push(
          L.marker([wp.latitude, wp.longitude]).bindPopup('WP ' + wp.index)
        )
      }
      let newMissionLayer = L.layerGroup(markers)
      this.missionLayer.clearLayers()
      this.missionLayer.addLayer(newMissionLayer)

    },
    updateDronePosition() {
      // show a marker on the map
      var droneIcon = L.icon({
        iconUrl: require('@/assets/drone.png'),
        iconSize:     [38, 38], // size of the icon
      }); 
      var marker = L.marker([this.dronePosition.latitude, this.dronePosition.longitude], {icon: droneIcon});
      let newDroneLayer = L.layerGroup([marker])
      this.droneLayer.clearLayers()
      this.droneLayer.addLayer(newDroneLayer)
    },
    createFakeWaypoints() {
      let wp_list = [
        {
          index: 0,
          latitude: 28.0710182,
          longitude: -15.4573374,
        },
        {
          index: 1,
          latitude: 28.0717907,
          longitude: -15.4564991,
        },
        {
          index: 2,
          latitude: 28.0718918,
          longitude: -15.4566183,
        },
        {
          index: 3,
          latitude: 28.0711174,
          longitude: -15.4574566,
        },
      ];
      this.waypoints = wp_list;
    },
    addFakeDrone() {
      // this.dronePosition.latitude = 28.071432;
      // this.dronePosition.longitude = -15.456958;
      this.dronePosition = {
        latitude: 28.071432,
        longitude: -15.456958,
      };
      this.updateDronePosition()
    },
  },
  mounted() {
    this.setupMap()
    this.createFakeWaypoints()
    this.updateteWaypointsMarkers()
    this.addFakeDrone()
  },
};
</script>

<style scoped>
  #mapid {
    /* configure the size of the map */
    width: 100%;
    height: 100%;
  }
  #mapid { height: 600px; }
</style>