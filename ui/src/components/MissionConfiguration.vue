<template>
  <v-card class="scrollable-x">
    <v-expansion-panels accordion flat multiple v-model="panel">
      <!-- Controls -->
      <v-expansion-panel>
        <v-expansion-panel-header> Controls </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-container>
            <v-row align="center" justify="space-around">
              <v-btn depressed> Start Mission </v-btn>
              <v-btn depressed color="error"> RTL </v-btn>
              <v-btn depressed color="primary"> Land </v-btn>
              <v-btn depressed disabled> Send Mission </v-btn>
            </v-row>
          </v-container>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <!-- Main Mission Configuration -->
      <v-expansion-panel>
        <v-expansion-panel-header>
          Configuration
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
                    v-if="[1, 3].includes(props.item.id)"
                    v-model="props.item.value"
                    single-line
                    counter
                    type="number"
                  ></v-text-field>
                  <v-select
                    v-if="props.item.id == 0"
                    :items="allowedMissionTypes"
                    v-model="props.item.value"
                  ></v-select>
                  <v-select
                    v-if="props.item.id == 2"
                    :items="allowedFinishActions"
                    v-model="props.item.value"
                  ></v-select>
                </template>
              </v-edit-dialog>
            </template>
          </v-data-table>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <!-- Main Mission Configuration -->
      <v-expansion-panel>
        <v-expansion-panel-header> User Markers </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-data-table
            :headers="userMarkersHeader"
            :items="userMarkers"
            height="200"
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
            
            <template v-slot:item.actions="{ item }">
              <v-icon small @click="deleteUserMarker(item)"> mdi-close </v-icon>
            </template>
          </v-data-table>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header> Waypoints </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-data-table
            :headers="waypointsHeader"
            :items="mission.waypoints"
            height="200"
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
              <v-icon small @click="deleteWaypoint(item)"> mdi-close </v-icon>
            </template>
          </v-data-table>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header> Export/Import </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-row align="center" justify="space-around">
            <!-- <div class="text-center">
            <v-dialog
              v-model="showSaveFileDialog"
              width="500"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                  Generate JSON
                </v-btn>
              </template>

              <v-card>
                <v-card-title>
                  Save mission as JSON file
                </v-card-title>
                <v-card-text>
                  Lorem ipsum dolor sit amet.
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="showSaveFileDialog = false"
                  >
                    Cancel
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </div>
            <!-- <v-btn depressed> Generate JSON </v-btn> -->
            <v-btn @click="exportMissionToJSON">
              Download mission
            </v-btn>
            <v-spacer></v-spacer>
            <v-file-input
              outlined
              dense
              prepend-icon="mdi-file-upload"
              full-width
              hide-details
              label="upload a mission file"
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
  name: "MissionConfiguration",
  props: {
    mission: Object,
    userMarkers: Array, 
    allowedMissionTypes: {
      type: Array,
      default() {
        return [
          "Regular",
          "Offboard",
        ]
      }
    },
    allowedFinishActions: {
      type: Array,
      default() {
        return [
          "ReturnHome",
          "Land",
        ]
      }
    }

  },
  data() {
    return {
      showSaveFileDialog: false,
      panel: [0, 1, 2],
      configurationItemsHeader: [
        {
          text: "Option",
          align: "start",
          value: "label",
        },
        { text: "Value", value: "value" },
      ],
      configurationItems: [],
      waypointsHeader: [
        {
          text: "Id",
          align: "start",
          value: "index",
        },
        {
          text: "Lat",
          value: "latitude",
        },
        {
          text: "Lon",
          value: "longitude",
        },
        {
          text: "Alt",
          value: "altitude",
        },
        {
          text: "Loiter",
          value: "loiter",
        },
        {
          text: "Action",
          value: "action",
        },
        {
          text: "Remove",
          value: "actions",
        },
      ],
      userMarkersHeader: [
        {
          text: "Lat",
          value: "latitude",
        },
        {
          text: "Lon",
          value: "longitude",
        },
        {
          text: "Remove",
          value: "actions",
        },
      ],
      waypointsValues: [],
    };
  },
  /*computed: {
    waypointsHeader() {
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          return this.allWaypointsHeader.filter((s) =>
            ["index"].includes(s.value)
          );
        case "sm":
          return this.allWaypointsHeader.filter((s) =>
            ["latitude", "longitude"].includes(s.value)
          );
        case "md":
          return this.allWaypointsHeader.filter((s) =>
            ["latitude", "longitude", "action"].includes(s.value)
          );
        case 'lg': return this.allWaypointsHeader;
          // return this.allWaypointsHeader.filter((s) =>
          //   ["latitude", "longitude", "actions"].includes(s.value)
          // );
        case 'xl': return this.allWaypointsHeader;
        default:
          return this.allWaypointsHeader;
      }
    },
  },*/
  mounted() {
    this.updateConfigTable();
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
      ];
    },
    saveGeneralConfig() {
      
      var newMission = { ...this.mission };
      console.log(this.configurationItems[2])
      for (const configItem of this.configurationItems) {
        console.log(configItem)
        if (configItem.id === 0) {
          newMission.type = configItem.value;
        } else if (configItem.id === 1) {
          newMission.altitude = configItem.value;
          newMission.waypoints.forEach(function (wp, i) {
            wp.altitude = configItem.value;
          });
        } else if (configItem.id === 2) {
          newMission.finish_action = configItem.value;
        } else if (configItem.id === 3) {
          newMission.overlap = configItem.value;
        }
      }
      console.log(newMission)
      this.$emit("update-mission", newMission);
    },
    saveWaypoints() {
      console.log("wp table modified")
    },
    deleteWaypoint(waypoint) {
      let index = Number(waypoint.index);
      console.log("remove " + index);
      var newWaypoints = [...this.userMarkers];
      var newMission = { ...this.mission };
      newWaypoints.splice(index, 1);
      newWaypoints.forEach(function (wp, i) {
        wp.index = i;
      });
      newMission.waypoints = newWaypoints;
      // this.$emit('new-waypoints', newWaypoints)
      this.$emit("update-mission", newMission);
    },
    deleteUserMarker(marker) {
      let index = Number(marker.index);
      console.log("removing marker " + index);
      var newUserMarkers = [...this.userMarkers];
      newUserMarkers.splice(index, 1);
      newUserMarkers.forEach(function (marker, i) {
        marker.index = i;
      });
      this.$emit('new-usermarkers', newUserMarkers)
    },
    onNewMissionFileUploaded(file) {
      self = this;
      if (!file) {
        console.log("File removed");
        return;
      }
      if (file.type === "application/json") {
        console.log("New file");
        var read = new FileReader();
        read.readAsBinaryString(file);
        read.onloadend = function () {
          let mission = JSON.parse(read.result);
          self.configureUploadedMission(mission);
        };
      } else {
        console.log("bad file type");
      }
    },
    configureUploadedMission(mission) {
      this.$emit("update-mission", mission);
    },
    exportMissionToJSON() {
      const data = JSON.stringify(this.mission)
      const blob = new Blob([data], {type: 'application/json'})
      const link = window.URL.createObjectURL(blob);
      // const blob = new Blob([this.mission], { type: 'application/json' })
      console.log('exporting')
      console.log(this.mission)
      // link.download = label
      // link.click()
      // URL.revokeObjectURL(link.href)
      window.open(link)
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