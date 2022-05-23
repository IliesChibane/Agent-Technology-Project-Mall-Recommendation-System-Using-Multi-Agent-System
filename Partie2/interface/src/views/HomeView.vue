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
                <v-container grid-list-md v-for="(value1, key1) in results" :key="key1"> 
                        <h3 style="text-align: center">
                            {{key1}} : 
                         </h3>
                        <v-card class="mb-5" v-for="(value2, key2) in value1" :key="key2">
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
                                @click="updateData(key1,key2)"
                            >Buy</v-btn>
                            </v-card-actions>
                        </v-card>
                </v-container>
        </v-col>

        <v-col col = 6 v-if="Object.keys(results).length != 0">
            <h2>agents communication history</h2>
                {{historic}}
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
            historic: "",
            Type_items: ["Laptop","desktop computer","Smartphone","Tablet","Headphones","Microphone","Afficheur","Semiconducteur","TV Screen","TV","Oculus","SSD","RAM","Doesn't matter"],
            Quantity_items: ["1","2","3","4","5","6","7","8","9","10","12","15","20","30"],
            Prix_items: ["2000","3500","15000","200000","Doesn't matter"],
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
                this.historic = "Main agent sent '../Bases/formulaire.json'|| To : Agent 1, Agent 2, Agent 3|| Agent 1 received the message !!!|| Agent 2 received the message !!!|| Agent 3 received the message !!!|| Agent 1 sent '../Bases/result1.json'|| Agent 2 sent '../Bases/result2.json'|| Agent 3 sent '../Bases/result3.json' || Main agent received all the messages !!!        Main agent send the result to the user as json object"
           } catch (error) {
                console.log(error);
            }
        },
        async updateData(nf, np) {
            console.log(nf)
            console.log(np)
            var link
            if(nf == "magasin1")
                link = "../Bases/Agent1Products.json"
            else if (nf == "magasin2")
                link = "../Bases/Agent2Products.json"
            else if (nf == "magasin3")
                link = "../Bases/Agent3Products.json"

            try {
                const response = await axios.post(
                    "http://localhost:5000/api/au",
                    {
                        NameFile: link,
                        NameProduct: np,
                        NewQuantity: this.product.Quantity,
                    }
                );
                var number = nf[nf.lenght - 1]
                this.historic = "Main agent sent '../Bases/UpdateInfo.json' à l'agent "+number+"|| Agent "+number+" received the message !!!|| Agent "+number+" sent 'Done' to main agent !!!"
            } catch (error) {
                console.log(error);
            }
        },
    }
}
</script>