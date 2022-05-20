<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" app>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title>
            Menu
          </v-list-item-title>
          <v-list-item-content-subtitle>
            Navigate where you want 
          </v-list-item-content-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <template>
        <v-card
          class="mx-auto"
          max-width="300"
          tile
        >
          <v-list rounded>
            <v-list-item-group
              color="primary"
            >
              <v-list-item
                v-for="(item, i) in items"
                :key="i" :to="item.link" link
              >
                <v-list-item-icon>
                  <v-icon v-text="item.icon"></v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="item.text"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </template>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Projet Tech Agent</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    data: () => ({ 
      drawer: null,
      items: [
        { text: 'Products', icon: 'mdi-bag-suitcase', link: "/" },
        { text: 'Vehicles', icon: 'mdi-car', link: "/vehicles" },
        { text: 'Facts', icon: 'mdi-file-document', link: "/facts"  },
        { text: 'Rules', icon: 'mdi-library', link: "/rules"  },
        { text: 'About', icon: 'mdi-robot', link: "/about" },
        ], 
      }),
  }
</script>