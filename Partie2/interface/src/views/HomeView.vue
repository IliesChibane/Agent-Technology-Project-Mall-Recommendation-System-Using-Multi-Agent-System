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
                v-model="product.Type"
            ></v-combobox>
        </v-col>
        <v-col cols="6">
            <v-combobox 
                label="Quantity" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Quantity_items"
                :rules="rules"
                v-model="product.Quantity"
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
                v-model="product.Prix"
            ></v-combobox>
        </v-col>
        <v-col cols="6">
            <v-combobox 
                label="Color" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Couleur_items"
                :rules="rules"
                v-model="product.Couleur"
            ></v-combobox>
        </v-col>
    </v-row>

    <v-row class="mt-5">
        <v-col cols="4">
            <v-combobox 
                label="Promotion" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Promotion_items"
                :rules="rules"
                v-model="product.Promotion"
            ></v-combobox>
        </v-col>
        <v-col cols="4">
            <v-combobox 
                label="Brand" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Marque_items"
                :rules="rules"
                v-model="product.Marque"
            ></v-combobox>
        </v-col>
        <v-col cols="4">
            <v-combobox 
                label="State" 
                dense 
                filled 
                outlined 
                small-chips 
                solo
                :items="Etat_items"
                :rules="rules"
                v-model="product.Etat"
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

    <v-row>
        <v-col col = 6 v-if="Object.keys(results).length != 0">
            <h2 style="text-align: center">List of product to buy</h2>
                <div v-for="(value1, key1) in results" :key="key1"> 
                        <h3 style="text-align: center">
                            {{key1}} : 
                         </h3>
                        <v-card v-for="(value2, key2) in value1" :key="key2">
                            <v-card-title>{{key2}}</v-card-title>
                            <v-card-text v-for="(value3, key3) in value2" :key="key3">
                                {{key3}} : {{value3}}
                            </v-card-text>
                            <v-card-actions>
                            <v-btn
                                elevation="5"
                                large
                                outlined
                                rounded
                                small
                                @click="updateData"
                            >Buy</v-btn>
                            </v-card-actions>
                        </v-card>
                        <br>
                </div>
        </v-col>

        <v-col col = 6 v-if="Object.keys(results).length != 0">
            <h2>agents communication history</h2>
                Main agent sent "../Bases/formulaire.json" <br>
                To : Agent 1, Agent 2, Agent 3 <br>
                Agent 1 received the message !!! <br>
                Agent 2 received the message !!! <br>
                Agent 3 received the message !!! <br>
                Agent 1 sent "../Bases/result1.json" <br>
                Agent 2 sent "../Bases/result2.json" <br>
                Agent 3 sent "../Bases/result3.json" <br>
                Main agent received all the messages !!! <br>
                Main agent send the result to the user as json object <br>
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
            Type_items: ["Laptop","desktop computer","Smartphone","Tablet","Headphones","Microphone","Afficheur","Semiconducteur","TV Screen","TV","Oculus","SSD","RAM","Doesn't matter"],
            Quantity_items: ["1","2","3","4","5","6","7","8","9","10","12","15","20","30","Doesn't matter"],
            Prix_items: ["15000","2000","3500","200000","Doesn't matter"],
            Couleur_items: ["Pink","Grey","Green","Black","Blue","Doesn't matter"],
            Promotion_items: ["5%","10%","15%","20%","Doesn't matter"],
            Marque_items: ["Samsung","Apple","Dell","Condor","Hp","Sony","LG","Doesn't matter"],
            Etat_items: ["New","Usagy","Doesn't matter"],
            product: {
                Type: "",
                Quantity: "",
                Prix: "",
                Promotion: "",
                Marque: "",
                Etat: "",
                Couleur: ""
            },
        };
    },
    methods: {
        // fetching product
        async getData() {
            try {
                const response = await axios.post(
                    "http://localhost:5000/api/mas",
                    {
                        Type: this.product.Type,
                        Quantity: this.product.Quantity,
                        Prix: this.product.Prix,
                        Promotion: this.product.Promotion,
                        Marque: this.product.Marque,
                        Etat: this.product.Etat,
                        Couleur: this.product.Couleur
                    }
                );
                this.results = response.data;
                console.log(Object.keys(this.results).length);
            } catch (error) {
                console.log(error);
            }
        },
        async updateData() {
            try {
                const response = await axios.post(
                    "http://localhost:5000/api/au",
                    {
                        NameFile: "../Bases/Agent1Products.json",
                        NameProduct: "Alienware Aurora",
                        NewQuantity: this.product.Quantity,
                    }
                );
            } catch (error) {
                console.log(error);
            }
        },
    }
}
</script>