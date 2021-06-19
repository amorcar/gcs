<template>
  <v-card class="scrollable-x">
    <v-expansion-panels accordion flat multiple
      v-model="panel"
    >
      <!-- Controls -->
      <v-expansion-panel >
        <v-expansion-panel-header>
          Controls
        </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-row
              align="center"
              justify="space-around"
            >
              <v-btn depressed>
                Start Mission
              </v-btn>
              <v-btn
                depressed
                color="error"
              >
                RTL
              </v-btn>
              <v-btn
                depressed
                color="primary"
              >
                Land
              </v-btn>
              <v-btn
                depressed
                disabled
              >
                Send Mission
              </v-btn>
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>
        <!-- Main Mission Configuration -->
        <v-expansion-panel
        >
          <v-expansion-panel-header>
            Configuration
            <v-spacer></v-spacer>
            <v-file-input
              small-chips
              prepend-icon="mdi-attachment"
              label="upload file"
              @change="onNewMissionFileUploaded"
            ></v-file-input>
            <!-- <v-spacer></v-spacer> -->
          </v-expansion-panel-header>

          <v-expansion-panel-content>
            <v-data-table
              dense
              hide-default-header
              hide-default-footer
              disable-pagination
              disable-sort
              :headers="configurationItemsHeader"
              :items="configurationItems"
            >
            <template v-slot:item.value="props">
              <v-edit-dialog
                :return-value.sync="props.item.value"
                @save="saveGeneralConfig"
              >
                {{ props.item.value }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.value"
                    label="Edit"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
          </v-data-table>
          </v-expansion-panel-content>
        </v-expansion-panel>
        <!-- Main Mission Configuration -->
        <v-expansion-panel>
          <v-expansion-panel-header>
            Waypoints
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-data-table
              :headers="waypointsHeader"
              :items="waypointsValues"
              height="400"
              dense
              hide-default-footer
              fixed-header
              disable-pagination
              disable-sort
            >
            <template v-slot:item.altitude="props">
              <v-edit-dialog
                :return-value.sync="props.item.altitude"
                @save="saveWaypoints"
              >
                {{ props.item.altitude }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.altitude"
                    label="Edit"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
            <template v-slot:item.loiter="props">
              <v-edit-dialog
                :return-value.sync="props.item.loiter"
                @save="saveWaypoints"
              >
                {{ props.item.loiter }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.loiter"
                    label="Edit"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
            <template v-slot:item.action="props">
              <v-edit-dialog
                :return-value.sync="props.item.action"
                @save="saveWaypoints"
              >
                {{ props.item.action }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.action"
                    label="Edit"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
            <template v-slot:item.actions="{ item }">
              <v-icon
                small
                @click="deleteWaypoint(item)"
              >
                mdi-close
              </v-icon>
            </template>
          </v-data-table>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-card>
</template>


<script>
import { mapGetters } from 'vuex'

export default {
  name: 'MissionConfiguration',
  data() {
    return {
      altitude: 0,
      type: 'Regular',
      finishAction: 'ReturnHome',
      panel: [0, 1, 2],
      configurationItemsHeader: [
        {
          text: 'Option',
          align: 'start',
          value: 'label',
        },
        { text: 'Value', value: 'value' },
      ],
      configurationItems: [],
      waypointsHeader: [
        {
          text: 'Id',
          align: 'start',
          value: 'index',
        },
        {
          text: 'Lat',
          value: 'latitude'
        },
        {
          text: 'Lon',
          value: 'longitude'
        },
        {
          text: 'Alt',
          value: 'altitude'
        },
        {
          text: 'Loiter',
          value: 'loiter'
        },
        {
          text: 'Action',
          value: 'action'
        },
        {
          text: 'Remove',
          value: 'actions',
        },
      ],
      waypointsValues: [],
    };
  },
  watch: {
    // whenever waypoints changes, this function will run
    waypoints: function (newWaypoints) {
      console.log('watching waypoints in table: ' + newWaypoints.length)
      this.updateWaypointsTable(true)
    }
  },
  mounted() {
    this.updateConfigTable()
    // this.createFakeWaypoints()
    this.updateWaypointsTable()
  },
  methods: {
    updateConfigTable() {
      this.configurationItems = [
        {
          id: 0,
          label: "Mission Type",
          value: this.type,
        },
        {
          id: 1,
          label: "Flying altitude (m)",
          value: this.altitude,
        },
        {
          id: 2,
          label: "Finish Action",
          value: this.finishAction,
        },
        {
          id: 3,
          label: "Test Action",
          value: this.finishAction,
        },
      ]
    },
    updateWaypointsTable(auto=false) {
      var newWaypoints = []
      for (const [index, waypoint] of this.waypoints.entries()) {
        newWaypoints.push(
          {
            index: waypoint.index,
            latitude: waypoint.latitude.toFixed(4),
            longitude: waypoint.longitude.toFixed(4),
            altitude: this.altitude,
            loiter: 0,
            action: 0,
          }
        ) 
      }
      console.log('updating waypoints table...' + this.waypoints.length)
      this.waypointsValues = newWaypoints
      // if (!auto){
      //   console.log('some waypoint has been removed')
      //   this.$store.commit('setWaypoints', this.waypoints)
      // }
    },
    updateBothTables(){
      this.updateConfigTable()
      this.updateWaypointsTable()
    },
    saveGeneralConfig(){
      for (const configItem of this.configurationItems) {
        if (configItem.id === 0){
          this.type = configItem.value
        }
        else if (configItem.id === 1){
          this.altitude = configItem.value
        }
        else if (configItem.id === 2){
          this.finishAction = configItem.value
        }
        else if (configItem.id === 3){
          this.finishAction = configItem.value
        }
      }
      // this.updateConfigTable()
      this.updateBothTables()
    },
    saveWaypoints() {
      console.log(this.waypointsValues)
    },
    deleteWaypoint(waypoint){
      let index = Number(waypoint.index)
      var newWaypoints = this.waypoints
      newWaypoints.splice(index, 1)
      this.$store.commit('setWaypoints', newWaypoints)
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
      // for (var i=0; i<2; i++) { wp_list = wp_list.concat(wp_list)}
      // this.waypoints = wp_list;
      this.$store.commit('setWaypoints', wp_list)
    },
    onNewMissionFileUploaded(file) {
      self = this
      if (!file) {
        console.log('File removed')
        return
      }
      if (file.type === "application/json"){
        console.log('New file')
        var read = new FileReader();
        read.readAsBinaryString(file);
        read.onloadend = function(){
          let mission = JSON.parse(read.result)
          self.configureUploadedMission(mission)
        }
      }
      else {
        console.log('bad file type')
      }
      
    },
    configureUploadedMission(mission){
      console.log(mission)
      this.altitude = mission.height;
      // this.type = mission.type;
      this.finishAction = mission.finish_action;
      var newWaypoints = [];
      for (const wp of mission.waypoints) {
        const simpleWP = {
          latitude: wp.latitude,
          longitude: wp.longitude,
          index: wp.index
        };
        newWaypoints.push(simpleWP)
      }
      this.$store.commit('setWaypoints', newWaypoints)
      this.waypointsValues = [];
      for (const wp of mission.waypoints) {
        const fullWP = {
          latitude: wp.latitude,
          longitude: wp.longitude,
          altitude: wp.altitude,
          index: wp.index,
          loiter: wp.loiter,
          action: wp.action,
        };
        this.waypointsValues.push(fullWP)
      }
      // this.updateBothTables()
      this.updateConfigTable()


    }
  },
  computed: {
    ...mapGetters({
      waypoints: 'getWaypoints'
    })
  }
};
</script>


<style scoped>
  #scrollable-x {
    width: calc(100vh - 200px); 
    overflow-x: auto;
  }
</style>