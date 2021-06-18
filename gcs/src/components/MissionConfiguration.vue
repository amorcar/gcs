<template>
  <v-row no-gutters>
    <v-card
      flat 
      style="max-height: 800px"
      class="overflow-y-auto flex"
    >
    <v-expansion-panels accordion flat multiple
      v-model="panel"
    >
      <!-- Main Mission Configuration -->
      <v-expansion-panel
      >
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
  </v-row>
  
</template>


<script>
export default {
  name: 'MissionConfiguration',
  data() {
    return {
      waypoints: [],
      altitude: 0,
      type: 'Regular',
      finishAction: 'ReturnHome',
      panel: [0, 1],
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
          text: 'Index',
          align: 'start',
          value: 'index',
        },
        {
          text: 'Latitude',
          value: 'latitude'
        },
        {
          text: 'Longitude',
          value: 'longitude'
        },
        {
          text: 'Altitude',
          value: 'altitude'
        },
        {
          text: 'Loiter Time',
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
    }
  },
  mounted() {
    this.updateConfigTable()
    this.createFakeWaypoints()
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
    updateWaypointsTable() {
      var newWaypoints = []
      for (const [index, waypoint] of this.waypoints.entries()) {
        newWaypoints.push(
          {
            index: index,
            latitude: waypoint.latitude.toFixed(4),
            longitude: waypoint.longitude.toFixed(4),
            altitude: this.altitude,
            loiter: 0,
            action: 0,
          }
        ) 
      }
      this.waypointsValues = newWaypoints
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
      this.waypoints.splice(index, 1)
      this.updateWaypointsTable()
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
      for (var i=0; i<2; i++) { wp_list = wp_list.concat(wp_list)}
      this.waypoints = wp_list;
    },
  }
}
</script>