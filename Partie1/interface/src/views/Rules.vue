<template>
<v-container>
    <v-card-title class="justify-center"><u> Rules </u></v-card-title>
     <v-row class="mt-5">
            <v-col cols="6">
                <div>
                    <h2 align="center">List of vehicles facts</h2>
                    <div v-for="(value1, key1) in VR" :key="key1"> 
                        <h3>
                            {{key1}} :
                        </h3>
                    <div v-for="(value, key) in value1" :key="key" class="mt-5">
                        <h4 v-if="key != result && key != cond">
                           IF {{value}} AND
                        </h4>
                        <h4 v-if="key == cond">
                           IF {{value}} 
                        </h4>
                        <h4 v-if="key == result">
                           THEN {{value}} 
                        </h4>
                    </div>
                    <h5>---------------------------------------</h5>
                    </div>
                </div>
            </v-col>

            <v-col cols="6">
                <div>
                    <h2 align="center">List of products facts</h2>
                    <div v-for="(value1, key1) in TR" :key="key1"> 
                        <h3>
                            {{key1}} :
                        </h3>
                    <div v-for="(value, key) in value1" :key="key" class="mt-5">
                        <h4 v-if="key != result && key != cond">
                           IF {{value}} AND
                        </h4>
                        <h4 v-if="key == cond">
                           IF {{value}} 
                        </h4>
                        <h4 v-if="key == result">
                           THEN {{value}} 
                        </h4>
                    </div>
                    <h5>---------------------------------------</h5>
                    </div>
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
         VR: [],
         TR: [],
         result: "result",
         cond: "condition f"
     }
    },
    // Fetch the todos on load
    async created() {
        this.getVR();
        this.getTR();
    },
    methods:{
        // fetching results
        async getVR() {
            try {
                const response = await axios.get(
                    "http://localhost:5000/api/VehicleRules"
                );
                this.VR = response.data;
            } catch (error) {
                console.log(error);
            }
        },
        async getTR() {
            try {
                const response = await axios.get(
                    "http://localhost:5000/api/productsRules"
                );
                this.TR = response.data;
            } catch (error) {
                console.log(error);
            }
        },
    }

}
</script>