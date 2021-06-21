<template>
  <v-card class="container" min-height="480">
  <!-- <v-card class="flex mt-3" elevation> -->
    <div id="mapid"></div>
  </v-card>
</template>

<script>
import '@geoman-io/leaflet-geoman-free';

export default {
  name: 'Map',
  props: {
    initialPosition: {
      type: Object,
      default() {
        return {
          latitude: 28.071637,
          longitude: -15.457188,
        }
      } 
    },
    homePosition: Object,
    dronePosition: Object,
    mission: Object,
    useGeolocation: {
      type: Boolean,
      default: false,
    }
  },
  data() {
    return {
      initMapPosition: this.initialPosition,
      map: null,
      homeLayer: null,
      // droneLayer: null,
      droneMarker: null,
      missionLayer: null,
    };
  },
  watch: {
    // whenever waypoints changes, this function will run
    mission: function (newMission) {
      console.log('watching waypoints in map: ' + newMission.waypoints.length)
      this.updateWaypointsMarkers()
    }
  },
  methods:{
    setupMap() {
      this.map = L.map('mapid').setView([this.initialPosition.latitude, this.initialPosition.longitude], 18);

      if (this.usePCGeolocation) {
        this.setCurrentLocationInMap()
      }

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

      // setup base-map layers
      var baseMaps = {
        "OpenStreetMap": OPSLayer,
        "esriWorldImagery": esriWorldImagery,
	      "esriWorldStreetMap": esriWorldStreetMap,
      };

      // setup overlays
      var homeIcon = L.icon({
        iconUrl: require('@/assets/home.svg'),
        iconSize:     [28, 28], // size of the icon
      });

      this.droneIcon = L.icon({
        iconUrl: require('@/assets/drone.png'),
        iconSize:     [38, 38], // size of the icon
      }); 

      var droneLayer = null
      var homeLayer = null

      if (this.dronePosition){
        this.droneMarker = L.marker([this.dronePosition.latitude, this.dronePosition.longitude], {icon: this.droneIcon, pmIgnore: true});
      } else {
        this.droneMarker = L.marker([this.homePosition.latitude, this.homePosition.longitude], {icon: homeIcon, pmIgnore: true});
      }
      if (this.homePosition){
        this.homeMarker = L.marker([this.dronePosition.latitude, this.dronePosition.longitude], {icon: homeIcon, pmIgnore: true});
      } else {
        this.homeMarker = L.marker([this.homePosition.latitude, this.homePosition.longitude], {icon: homeIcon, pmIgnore: true});
      }
      droneLayer = L.layerGroup([this.droneMarker]).addTo(this.map);
      homeLayer = L.layerGroup([this.homeMarker]).addTo(this.map);
      this.homeMarker.bindPopup("<b>Home Position</b><br>" + this.homePosition.latitude + ', ' + this.homePosition.longitude);

      this.missionLayer = L.layerGroup().addTo(this.map);

      var overlayMaps = {
          "Home": homeLayer,
          "Mission": this.missionLayer,
          "Drone": droneLayer,
      };
      L.control.layers(baseMaps, overlayMaps) .addTo(this.map);

      L.control.scale().addTo(this.map);

      this.map.pm.addControls({  
        position: 'topleft',  
        drawCircle: false,  
        drawCircleMarker: false,  
        drawRectangle: false,
        cutPolygon: false,
        rotateMode: false,
        editMode: false,
        drawPolyline: false,
        drawPolygon: false,
      });

      // listen to vertexes being added to currently drawn layer (called workingLayer)
      var self = this
      this.map.on('pm:create', e => {
        if (e.shape === 'Marker') {
          self.onMarkerCreated(e)
        }
      });
      // remove marker event
      var self = this
      this.map.on('pm:remove', e => {
        if (e.shape === 'Marker') {
          self.onMarkerDeleted(e)
        }
      });

    },
    updateWaypointsMarkers() {
      var self = this;
      console.log('updating waypoints markers ' + this.mission.waypoints.length)
      var markers = []
      for (const wp of this.mission.waypoints) {
        var m = L.marker([wp.latitude, wp.longitude]);//.bindPopup('id: '+wp.index)
        m.index = wp.index
        m.on('pm:dragend', function (e) {
          self.onMarkerDragged(e)
        })
        markers.push(m)
      }
      let newMissionLayer = L.layerGroup(markers)
      this.missionLayer.clearLayers()
      this.missionLayer.addLayer(newMissionLayer)
    },
    updateHomePosition() {
      this.homeMarker.setLatLng(L.latLng(this.homePosition.latitude, this.homePosition.longitude))
    },
    updateDronePosition() {
      this.droneMarker.setLatLng(L.latLng(this.dronePosition.latitude, this.dronePosition.longitude))
    },
    setCurrentLocationInMap() {
      navigator.geolocation.getCurrentPosition( position => {
        this.initMapPosition = {
          latitude: position.coords.latitude,
          longitude: position.coords.longitude,
        }
        this.map.setView(L.latLng(this.initMapPosition.latitude, this.initMapPosition.longitude))
      })
    },
    onMarkerDragged(e) {
      let index = e.layer.index
      var newWaypoints = [...this.mission.waypoints]
      let newLat = e.layer._latlng.lat
      let newLon = e.layer._latlng.lng
      newWaypoints.forEach(function(wp) {
        if (wp.index === index) {
          wp.latitude = newLat
          wp.longitude = newLon
        }
      });
      this.$emit('new-waypoints', newWaypoints)

    },
    onMarkerCreated(e) {
      var self = this
      var newWaypoints = [...this.mission.waypoints]
      newWaypoints.push({
        index: this.mission.waypoints.length,
        latitude: e.layer._latlng.lat,
        longitude: e.layer._latlng.lng,
        altitude: this.mission.altitude,
        loiter: 0,
        speed: 0,
        action: 0,
      })
      e.layer.index = this.mission.waypoints.length
      e.layer.addTo(this.missionLayer)
      e.layer.on('pm:dragend', function (e) {
        self.onMarkerDragged(e)
      })
      this.$emit('new-waypoints', newWaypoints)
    },
    onMarkerDeleted(e) {
      let index = e.layer.index
      var newWaypoints = [...this.mission.waypoints]
      newWaypoints.splice(index, 1)
      var newMission = {...this.mission}
      newMission.waypoints = newWaypoints
      this.$emit('update-mission', newMission)
    }
  },
  mounted() {
    this.setupMap()
    this.updateWaypointsMarkers()
  },
};
</script>

<style scoped>
.container {
    display: block;
    overflow: hidden;
    white-space: nowrap;
    /* height: 100%;
    width: 100%; */
}

.container div {
    position: relative;
    display: inline-block;
}
  #mapid {
    height: 100%;
    width: 100%;
  }
</style>