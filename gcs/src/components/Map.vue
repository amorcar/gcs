<template>
  <div id="mapid"></div>
</template>

<script>
import '@geoman-io/leaflet-geoman-free';
import { mapGetters } from 'vuex'

export default {
  name: 'Map',

  data() {
    return {
      dronePosition: {
        latitude: null,
        longitude: null,
      },
      map: null,
      missionLayer: null,
      droneLayer: null,
    };
  },
  watch: {
    // whenever waypoints changes, this function will run
    waypoints: function (newWaypoints) {
      console.log('watching waypoints: ' + newWaypoints.length)
      this.updateteWaypointsMarkers()
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

      this.droneLayer = L.layerGroup().addTo(this.map);
      this.missionLayer = L.layerGroup().addTo(this.map);
      this.missionLayer.on('pm:vertexadded', e => {
        console.log(e);
      });

      // show a marker on the map
      var homeIcon = L.icon({
        iconUrl: require('@/assets/home.svg'),
        iconSize:     [38, 38], // size of the icon
      });
      var marker = L.marker([28.071637, -15.457188], {icon: homeIcon, pmIgnore: true});
      this.homeLayer = L.layerGroup([marker]).addTo(this.map);

      marker.bindPopup("<b>Home Position</b><br>28.071637, -15.457188");

      var overlayMaps = {
          "Home": this.homeLayer,
          "Mission": this.missionLayer,
          "Drone": this.droneLayer,
      };
      L.control.layers(baseMaps, overlayMaps) .addTo(this.map);


      // add Leaflet-Geoman controls with some options to the map  
      this.map.pm.addControls({  
        position: 'topleft',  
        drawCircle: false,  
        drawCircleMarker: false,  
        drawRectangle: false,
        cutPolygon: false,
        rotateMode: false,
        editMode: false,
      });

      // map events
      this.map.on('pm:dragend', e => {
        console.log(e);
      });

      // listen to vertexes being added to currently drawn layer (called workingLayer)
      this.map.on('pm:drawstart', ({ workingLayer }) => {
        workingLayer.on('pm:vertexadded', e => {
          console.log(e);
        });
      });

    },
    updateteWaypointsMarkers() {
      var self = this;
      console.log('updating waypoints markers ' + this.waypoints.length)
      var markers = []
      for (const wp of this.waypoints) {
        var m = L.marker([wp.latitude, wp.longitude]);//.bindPopup('WP ' + wp.index)
        m.index = wp.index
        m.on('pm:dragend', function (e) {
          let index = e.layer.index
          let newLat = e.layer._latlng.lat
          let newLon = e.layer._latlng.lon
          console.log('marker ' + e.layer.index + ' dragged');
          console.log(e)
          console.log(self)
          var waypointToEdit = self.waypoints.filter(wp => {
            return wp.index === index
          })
          waypointToEdit.latitude = newLat
          waypointToEdit.longitude = newLon
        })
        markers.push(m)
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
      // this.waypoints = wp_list;
      this.$store.commit('setWaypoints', wp_list)
    },
    addFakeDrone() {
      this.dronePosition = {
        latitude: 28.071432,
        longitude: -15.456958,
      };
      this.updateDronePosition()
    },
  },
  mounted() {
    this.setupMap()
    this.updateteWaypointsMarkers()
    this.addFakeDrone()
    this.createFakeWaypoints()
  },
  computed: {
    ...mapGetters({
      waypoints: 'getWaypoints'
    })
  }
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