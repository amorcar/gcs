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
              :items="mission.waypoints"
              height="300"
              dense
              hide-default-footer
              fixed-header
              disable-pagination
              disable-sort
            >
            <template v-slot:item.latitude="props">
              {{ props.item.latitude.toFixed(4) }}
            </template>
            <template v-slot:item.longitude="props">
              {{ props.item.longitude.toFixed(4) }}
            </template>
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
      <v-expansion-panel>
        <v-expansion-panel-header>
          Export/Import
        </v-expansion-panel-header>
        <v-expansion-panel-content>
            <v-row
              align="center"
              justify="space-around"
            >
              <v-btn depressed>
                Generate JSON
              </v-btn>
              <v-spacer></v-spacer>
              <v-file-input
                small-chips
                prepend-icon="mdi-attachment"
                label="upload file"
                @change="onNewMissionFileUploaded"
              ></v-file-input>
            </v-row>

        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-card>
</template>


<script>

export default {
  name: 'MissionConfiguration',
  props:{
    mission: Object,
  },
  data() {
    return {
      panel: [0, 1, 2,],
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
  mounted() {
    this.updateConfigTable()
  },
  methods: {
    updateConfigTable() {
      this.configurationItems = [
        {
          id: 0,
          label: "Mission Type",
          value: this.mission.type,
        },
        {
          id: 1,
          label: "Flying altitude (m)",
          value: this.mission.altitude,
        },
        {
          id: 2,
          label: "Finish Action",
          value: this.mission.finish_action,
        },
        {
          id: 3,
          label: "Overlap",
          value: 0.2,
        },
      ]
    },
    saveGeneralConfig(){
      var newMission = { ...this.mission }
      for (const configItem of this.configurationItems) {
        if (configItem.id === 0){
          newMission.type = configItem.value
        }
        else if (configItem.id === 1){
          newMission.altitude = configItem.value
          newMission.waypoints.forEach(function (wp, i) {
            wp.altitude = configItem.value
          });
        }
        else if (configItem.id === 2){
          newMission.finish_action = configItem.value
        }
        else if (configItem.id === 3){
          newMission.finish_action = configItem.value
        }
      }
      this.$emit('update-mission', newMission)
    },
    saveWaypoints() {
      console.log(this.mission.waypoints)
    },
    deleteWaypoint(waypoint){
      let index = Number(waypoint.index)
      console.log('remove ' + index)
      var newWaypoints = [...this.mission.waypoints]
      var newMission = {...this.mission}
      newWaypoints.splice(index, 1)
      newWaypoints.forEach(function (wp, i) {
        wp.index = i
      });
      newMission.waypoints = newWaypoints
      // this.$emit('new-waypoints', newWaypoints)
      this.$emit('update-mission', newMission)
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
      this.$emit('update-mission', mission)
    }
  },
};
</script>


<style scoped>
  #scrollable-x {
    width: calc(100vh - 200px); 
    overflow-x: auto;
  }
</style>