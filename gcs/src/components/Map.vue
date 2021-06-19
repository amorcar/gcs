<template>
<v-card class="flex mt-3" elevation>
  <div id="mapid"></div>
</v-card>
</template>

<script>
import '@geoman-io/leaflet-geoman-free';
import { mapGetters } from 'vuex'

export default {
  name: 'Map',
  props: {
    initial_mission: Object,
    initial_drone_position: Object,
    initial_position: {
      default() {
        return {
          latitude: 28.071637,
          longitude: -15.457188,
        }
      } 
    }
  },
  data() {
    return {
      mission: this.initial_mission,
      dronePosition: this.initial_drone_position,
      initialPosition: this.initial_position,
      map: null,
      missionLayer: null,
      droneLayer: null,
    };
  },
  // watch: {
  //   // whenever waypoints changes, this function will run
  //   waypoints: function (newWaypoints) {
  //     console.log('watching waypoints in map: ' + newWaypoints.length)
  //     this.updateteWaypointsMarkers()
  //   }
  // },
  methods:{
    setupMap() {
      // navigator.geolocation.getCurrentPosition( position => {
      //   console.log(position)
        // this.initialPosition = {
        //   latitude: position.coords.latitude,
        //   longitude: position.coords.longitude,
        // }
        // this.map.setView(L.latLng(position.coords.latitude, position.coords.longitude))
      // })

      this.map = L.map('mapid').setView([this.initialPosition.latitude, this.initialPosition.longitude], 18);

      // setup map layer
      var OPSLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
      });
      var	esriWorldImagery = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
      }).addTo(this.map);
      var esriWorldStreetMap = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012'
      });

      // create layers
      var baseMaps = {
        "OpenStreetMap": OPSLayer,
        "esriWorldImagery": esriWorldImagery,
	      "esriWorldStreetMap": esriWorldStreetMap,
      };

      this.droneLayer = L.layerGroup().addTo(this.map);
      this.missionLayer = L.layerGroup().addTo(this.map);
      this.missionLayer.on('pm:vertexadded', e => {
        console.log(e);
      });

      // show a marker on the map
      var homeIcon = L.icon({
        iconUrl: require('@/assets/home.svg'),
        iconSize:     [28, 28], // size of the icon
      });

      var marker = L.marker()
      if (!isNaN(this.dronePosition)){
        marker = L.marker([28.071637, -15.457188], {icon: homeIcon, pmIgnore: true});
      } 
      this.homeLayer = L.layerGroup([marker]).addTo(this.map);
      marker.bindPopup("<b>Home Position</b><br>28.071637, -15.457188");

      var overlayMaps = {
          "Home": this.homeLayer,
          "Mission": this.missionLayer,
          "Drone": this.droneLayer,
      };
      L.control.layers(baseMaps, overlayMaps) .addTo(this.map);

      // show the scale bar on the lower left corner
      L.control.scale().addTo(this.map);

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

      // listen to vertexes being added to currently drawn layer (called workingLayer)
      var self = this
      this.map.on('pm:create', e => {
        console.log(e);
        if (e.shape === 'Marker') {
          var newWaypoints = self.mission.waypoints
          newWaypoints.push({
            index: self.mission.waypoints.length,
            latitude: e.layer._latlng.lat,
            longitude: e.layer._latlng.lng,
            altitude: 0,
            loiter: 0,
            speed: 0,
            action: 0,
          })
          // self.$store.commit('setWaypoints', newWaypoints)
          self.$emit('new-waypoints', newWaypoints)
          e.layer.remove()
        }
      });
      // removemarker event
      var self = this
      this.map.on('pm:remove', e => {
        console.log(e);
        if (e.shape === 'Marker') {
          let index = e.layer.index
          var newWaypoints = this.mission.waypoints
          newWaypoints.splice(index, 1)
          self.$emit('new-waypoints', newWaypoints)
          // self.$store.commit('setWaypoints', newWaypoints)
        }
      });

    },
    updateteWaypointsMarkers() {
      var self = this;
      console.log('updating waypoints markers ' + this.mission.waypoints.length)
      var markers = []
      for (const wp of this.mission.waypoints) {
        var m = L.marker([wp.latitude, wp.longitude]).bindPopup('id: '+wp.index)
        m.index = wp.index
        m.on('pm:dragend', function (e) {
          let index = e.layer.index
          var newWaypoints = self.mission.waypoints
          let newLat = e.layer._latlng.lat
          let newLon = e.layer._latlng.lng
          newWaypoints.forEach(function(wp) {
            if (wp.index === index) {
              wp.latitude = newLat
              wp.longitude = newLon
            }
          });
          // self.$store.commit('setWaypoints', newWaypoints)
          self.$emit('new-waypoints', newWaypoints)
          console.log('after:' + self.mission.waypoints[index].latitude)
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
      // this.$store.commit('setWaypoints', wp_list)
      this.$emit('new-waypoints', newWaypoints)
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
    console.log(2)
    this.addFakeDrone()
    console.log(3)
    // this.createFakeWaypoints()
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
    padding: 0px;
    /* margin-top: 12px; */
    height: 100%;
    display: flex;
    flex-flow: column wrap;
    flex: 1 1;
    order: 2;
    display: flex;

    height: 480px;
    flex: 1;
  }
</style>