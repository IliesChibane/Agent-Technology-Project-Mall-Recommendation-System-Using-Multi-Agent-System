<template>
    <v-container>
        <v-card-title class="justify-center"><u> Facts </u></v-card-title>
        <v-row class="mt-5">
            <v-col cols="6">
                <div>
                    <h2>List of vehicles facts</h2>
                    <div v-for="facts in VF" :key="facts"> 
                    <div v-for="(value, key) in facts" :key="key" class="mt-5">
                        <h3>
                            {{key}} :
                        </h3>
                        <h4>
                            {{value}}
                        </h4>
                    </div>
                    </div>
                </div>
            </v-col>

            <v-col cols="6">
                <div>
                    <h2>List of products facts</h2>
                    <div v-for="facts in TF" :key="facts"> 
                    <div v-for="(value, key) in facts" :key="key" class="mt-5">
                        <h3>
                            {{key}} :
                        </h3>
                        <h4>
                            {{value}}
                        </h4>
                    </div>
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
         VF: [],
         TF: []
     }
    },
    // Fetch the todos on load
    async created() {
        this.getVF();
        this.getTF();
    },
    methods:{
        // fetching results
        async getVF() {
            try {
                const response = await axios.get(
                    "http://localhost:5000/api/VehiclesFacts"
                );
                this.VF = response.data;
            } catch (error) {
                console.log(error);
            }
        },
        async getTF() {
            try {
                const response = await axios.get(
                    "http://localhost:5000/api/productsFacts"
                );
                this.TF = response.data;
            } catch (error) {
                console.log(error);
            }
        },
    }

}
</script>