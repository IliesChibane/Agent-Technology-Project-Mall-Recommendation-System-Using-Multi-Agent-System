<template>
  <v-container fluid>
    <v-card-title class="justify-center"><u> Select facts</u></v-card-title>
    <v-row class="mt-5">
        <v-col cols="6">
            <v-combobox 
                label="Category" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Category_items"
                :rules="rules"
                v-model="places.Category"
            ></v-combobox>
        </v-col>
        <v-col cols="6">
            <v-combobox 
                label="Type" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Type_items"
                :rules="rules"
                v-model="places.Type"
            ></v-combobox>
        </v-col>
    </v-row>

    <v-row class="mt-5">
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
                v-model="places.Size"
            ></v-combobox>
        </v-col>
        <v-col cols="6">
            <v-combobox 
                label="Function" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Function_items"
                :rules="rules"
                v-model="places.Function"
            ></v-combobox>
        </v-col>
    </v-row>

    <v-row class="mt-5">
        <v-col cols="4">
            <v-combobox 
                label="Portable" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Portable_items"
                :rules="rules"
                v-model="places.Portable"
            ></v-combobox>
        </v-col>

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
            <h2>List of places to visit</h2>
                <div v-for="r in results" :key="r"> 
                    <h3>{{r["lieu_a_visiter"]}}</h3>
                </div>
        </v-col>
    </v-row>
</v-container>
</template>

<script>
import axios from 'axios'
export default {
    // component data
    data() {
        return {
            rules: [(value) => !!value || "This field is required"],
            results:[],
            Category_items: ["Audio","Mobile","Computers","Video","Electronic","Doesn't matter"],
            Type_items: ["Device","Component","Doesn't matter"],
            Size_items: ["Small","Medium","Big","Doesn't matter"],
            Function_items: ["Receiver","Sender","Doesn't matter"],
            Portable_items: ["Yes","No","Doesn't matter"],
            places: {
                Category: "",
                Localisation: "",
                Size: "",
                Function: "",
                Portable: ""
            },
        };
    },
    methods: {
        // fetching products
        async getData() {
            try {
                const response = await axios.post(
                    "http://localhost:5000/api/products",
                    {
                        Category: this.places.Category,
                        Localisation: this.places.Localisation,
                        Size: this.places.Size,
                        Function: this.places.Function,
                        Portable: this.places.Portable,
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
