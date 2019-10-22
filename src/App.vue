<template>
  <div id="app" v-on:click="appClicked">
    <cmaartwork v-for="(aw, idx) in myJson"
                v-bind:key="aw.artwork.accession_number"
                v-bind:artwork="aw.artwork"
                v-bind:creator="aw.creator"
                v-bind:department="aw.department"
                v-on:artwork-clicked="artworkClicked(aw, idx)"
    />
    <div v-show="isbigartwork" class="bawcontainer">
      <bigartwork class="baw"
                  v-bind:bartwork="curArtwork.artwork"
                  v-bind:bcreator="curArtwork.creator"
                  v-bind:bdepartment="curArtwork.department"
                  v-on:pass-title="passTitle"/>
      <div class="bawidx">
        <div id="prevart" v-on:click="prevClicked" class="prevnextctl">&laquo;</div>
        <div id="nextart" v-on:click="nextClicked" class="prevnextctl">&raquo;</div>
        <div class="bawidxtxt"><strong>{{bigAwTitle}}</strong></div>
        <div class="bawidxtxt"><strong>{{curIdx}} of {{myJson.length}}</strong></div>
      </div>
    </div>
  </div>
</template>

<script>
import artworks from './json/artworks.json'
import cmaartwork from './components/cmaartwork.vue'
import bigartwork from './components/bigartwork.vue'


export default {
  name: 'app',
  data: function() {
    return {
      myJson: artworks,
      isbigartwork: false,
      curIdx: 0,
      curArtwork: cmaartwork,
      bigDisplayed: false,
      bigAwTitle: ''
    }
  },
  methods: {
    artworkClicked: function(aw, idx) {
      this.curArtwork = aw;
      this.curIdx = idx + 1;
      this.isbigartwork = true;
    },
    appClicked: function() {
      if (this.bigDisplayed) {
        this.isbigartwork = false;
        this.bigDisplayed = false;
      }
      if (this.isbigartwork) {
        this.bigDisplayed = true;
      }
    },
    passTitle: function(title) {
      this.bigAwTitle = title;
    },
    prevClicked: function() {
      
    },
    nextClicked: function() {

    }
  },
  components: {
    cmaartwork,
    bigartwork
  }
}
</script>

<style>
#app {
  background-color: black;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  display: flex;
  flex-flow: row wrap;
  justify-content: space-around;
  overflow-y: scroll;
  overflow-x: hidden;
}
.bawcontainer {
  color: white;
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color:rgba(0,0,0,0.8);
  z-index: 10;
}
.baw {
  position: relative;
  top: 0;
  left: 0;
  padding: 5px 0px 15px 0px;
}
.bawidx {
  width: 100%;
  height: 50px;
  position: fixed;
  top: 80%;
  left: 0;
  text-align: center;
  z-index: 110;
}
.bawidxtxt {
  vertical-align: bottom;
}
.prevnextctl {
  position: absolute;
  top: 80;
  font-size: 30px;
  min-width: 40px;
  min-height: 40px;
  padding: 5px;
  margin: 0;
  border: 2px solid transparent;
  vertical-align: top;
	border-radius: 100%;
  user-select: none;
	transition: all 500ms;
}
.prevnextctl:hover {
  background: #222;
  border: 2px solid white;
  border-radius: 100%;
  cursor: pointer;
}
#prevart {
  left: 30%;
}
#nextart {
  left: 70%;
}

</style>
