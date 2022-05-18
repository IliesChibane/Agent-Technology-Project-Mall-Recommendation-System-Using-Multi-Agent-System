<template>
  <v-container fluid>
    <v-card-title class="justify-center"><u> Select facts</u></v-card-title>
    <v-row class="mt-5">
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
        <v-col cols="6">
            <v-combobox 
                label="Localisation" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Localisation_items"
                :rules="rules"
                v-model="places.Localisation"
            ></v-combobox>
        </v-col>
    </v-row>

    <v-row class="mt-5">
        <v-col cols="6">
            <v-combobox 
                label="Price" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Prix_items"
                :rules="rules"
                v-model="places.Prix"
            ></v-combobox>
        </v-col>
        <v-col cols="6">
            <v-combobox 
                label="Place to relax" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Endroit_pour_se_detendre_items"
                :rules="rules"
                v-model="places.Endroit_pour_se_detendre"
            ></v-combobox>
        </v-col>
    </v-row>

    <v-row class="mt-5">
        <v-col cols="4">
            <v-combobox 
                label="Climat" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Climat_items"
                :rules="rules"
                v-model="places.Climat"
            ></v-combobox>
        </v-col>
        <v-col cols="4">
            <v-combobox 
                label="Type of place" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Type_lieu_items"
                :rules="rules"
                v-model="places.Type_lieu"
            ></v-combobox>
        </v-col>
        <v-col cols="4">
            <v-combobox 
                label="Construction period" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Periode_items"
                :rules="rules"
                v-model="places.Periode"
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
            Type_items: ["Lieu Historique","Lieu Culturel","Hauteurs et montagnes","Lieu Aquatique","Parc National","Doesn't matter"],
            Localisation_items: ["Alger","Bejaia","Tipaza","Sahara","Oran","Blida","Doesn't matter"],
            Prix_items: ["Payant","Gratuit","Visite Guidée Payante","Doesn't matter"],
            Climat_items: ["Regulier","Froid","Humide","Chaud","Doesn't matter"],
            Type_lieu_items: ["Construction humaine","Plage","Grotte Naturelle","Cascade","Doesn't matter"],
            Periode_items: ["Moin de cinquante ans","Plus de cinquante ans","Doesn't matter"],
            Endroit_pour_se_detendre_items: ["True","False","Doesn't matter"],
            places: {
                Type: "",
                Localisation: "",
                Prix: "",
                Climat: "",
                Type_lieu: "",
                Periode: "",
                Endroit_pour_se_detendre: ""
            },
        };
    },
    methods: {
        // fetching places
        async getData() {
            try {
                const response = await axios.post(
                    "http://localhost:5000/api/tourism",
                    {
                        Type: this.places.Type,
                        Localisation: this.places.Localisation,
                        Prix: this.places.Prix,
                        Climat: this.places.Climat,
                        Type_lieu: this.places.Type_lieu,
                        Periode: this.places.Periode,
                        Endroit_pour_se_detendre: this.places.Endroit_pour_se_detendre
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
