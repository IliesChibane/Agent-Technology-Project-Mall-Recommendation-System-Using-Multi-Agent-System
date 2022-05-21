<template>
<v-container>
    <v-card-title class="justify-center"><u> Agent2 Products </u></v-card-title>
     <v-row class="mt-5">
            <v-col cols="6">
             <div v-for="(value1, key1) in products" :key="key1"> 
                        <h3 style="text-align: center">
                         </h3>
                        <v-card v-for="(value2, key2) in value1" :key="key2">
                            <v-card-title>{{key2}}</v-card-title>
                            <v-card-text v-for="(value3, key3) in value2" :key="key3">
                                {{key3}} : {{value3}}
                            </v-card-text>
                        </v-card>
                        <br>
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
         products: [],
     }
    },
    // Fetch the todos on load
    async created() {
        this.getProducts();
    },
    methods:{
        // fetching results
        async getProducts() {
            try {
                const response = await axios.get(
                    "http://localhost:5000/api/productsMagasin2"
                );
                this.products = response.data;
            } catch (error) {
                console.log(error);
            }
        },
    }

}
</script>