<template>
<v-container fluid>
    <v-card-title class="justify-center"><u> Select facts </u></v-card-title>
    <v-row class="mt-5">
        <v-col cols="6">
            <v-combobox 
                label="Motors" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Motor_items"
                :rules="rules"
                v-model="vehicle.Motor"
            ></v-combobox>
        </v-col>
        <v-col cols="6">
            <v-combobox 
                label="Size" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Size_items"
                :rules="rules"
                v-model="vehicle.Size"
            ></v-combobox>
        </v-col>
    </v-row>

    <v-row class="mt-5">
        <v-col cols="4">
            <v-combobox 
                label="Vehicule type" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Vehicule_Type_items"
                :rules="rules"
                v-model="vehicle.Vehicule_Type"
            ></v-combobox>
        </v-col>
        <v-col cols="4">
            <v-combobox 
                label="Number of wheels" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Number_of_wheels_items"
                :rules="rules"
                v-model="vehicle.Number_of_wheels"
            ></v-combobox>
        </v-col>
        <v-col cols="4">
            <v-combobox 
                label="Number of doors" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Number_of_doors_items"
                :rules="rules"
                v-model="vehicle.Number_of_doors"
            ></v-combobox>
        </v-col>
    </v-row>

    <v-row class="text-center">
        <v-col>
            <v-btn
                elevation="5"
                large
                outlined
                rounded
                small
                @click="getData"
            >Reason</v-btn>
        </v-col>
    </v-row>

    <v-row class="text-center">
        <v-col v-if="results.length > 0">
            <h2>List of vehicle</h2>
                <div v-for="r in results" :key="r"> 
                    <h3>{{r["Vehicle"]}}</h3>
                </div>
        </v-col>
    </v-row>
</v-container>
</template>

<script>
import axios from 'axios'
export default {
   data() {
     return {
       rules: [(value) => !!value || "This field is required"],
       results: [],
       Motor_items: ["yes","no","Doesn't matter"],
       Size_items: ["small","medium","large","Doesn't matter"],
       Vehicule_Type_items: ["automobile","cycle","Doesn't matter"],
       Number_of_wheels_items: ["2","3","4","Doesn't matter"],
       Number_of_doors_items: ["2","3","4","Doesn't matter"],
       vehicle: {
         Motor: "",
         Size: "",
         Vehicule_Type: "",
         Number_of_wheels: "",
         Number_of_doors: ""
       },
     };
   },
   methods: {
        // fetching results
        async getData() {
            try {
                const response = await axios.post(
                    "http://localhost:5000/api/vehicles",
                    {
                        Motor: this.vehicle.Motor,
                        Size: this.vehicle.Size,
                        Vehicule_Type: this.vehicle.Vehicule_Type,
                        Number_of_wheels: this.vehicle.Number_of_wheels,
                        Number_of_doors: this.vehicle.Number_of_doors
                    }
                );
                this.results = response.data;
            } catch (error) {
                console.log(error);
            }
        },
    }
}
</script>

