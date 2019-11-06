<template>
  <div id="app" v-on:click="appClicked">
    <cmaartwork class="cmaaw"
                v-for="(aw, idx) in myJson"
                ref="caws"
                :key="aw.artwork.accession_number"
                :artwork="aw.artwork"
                :creator="aw.creator"
                :department="aw.department"
                @artwork-clicked="artworkClicked(aw, idx)"
                slider="no"
    />
    <div v-show="bigDisplayed" class="bawcontainer">
      <bigartwork class="baw"
                  :bartwork="curArtwork.artwork"
                  :bcreator="curArtwork.creator"
                  :bdepartment="curArtwork.department"
                  @pass-title="passTitle"/>
      <div class="bawidxcontainer">
        <div class="pncontainer">
          <div id="prevart" class="prevnextctl" @click.stop="prevClicked()">&laquo;</div>
          <div id="nextart" class="prevnextctl" @click.stop="nextClicked()">&raquo;</div>
        </div>
        <div class="bawidxtxt">
          <div><strong>{{bigAwTitle}}</strong></div>
        </div>
        <div class="bawidxtxt">
          <div><strong>{{curIdx}} of {{myJson.length}}</strong></div>
        </div>
      </div>
      <div class="slider">
        <cmaartwork v-for="(saw, sidx) in myJson"
                    ref="scaws"
                    :key="saw.artwork.accession_number"
                    :artwork="saw.artwork"
                    :creator="saw.creator"
                    :department="saw.department"
                    @artwork-clicked="artworkClicked(saw, sidx)"
                    slider="yes"
        />
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
      this.bigDisplayed = true;
    },
    appClicked: function() {
      if (this.bigDisplayed) {
        this.bigDisplayed = false;
      }
    },
    passTitle: function(title) {
      this.bigAwTitle = title;
    },
    prevClicked: function() {
      this.curIdx -= 1;
      if (this.curIdx <= 0) {
        this.curIdx = this.myJson.length;
      }
      this.prevNextClicked(this.curIdx - 1);
    },
    nextClicked: function() {
      this.curIdx += 1;
      if (this.curIdx > this.myJson.length) {
        this.curIdx = 1;
      }
      this.prevNextClicked(this.curIdx - 1);
    },
    prevNextClicked: function(idx) {
      var caw = this.$refs.caws[idx];
      this.artworkClicked(caw, idx);
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
  box-sizing: border-box;
  background-color: black;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  display: flex;
  flex-flow: row wrap;
  justify-content: space-around;
  overflow-y: scroll;
  overflow-x: hidden;
}
.cmaaw {
  vertical-align: text-bottom;
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
  padding: 5px 0px 15px 0px;
}
.bawidxcontainer {
  width: 100%;
  height: 50px;
  position: fixed;
  top: 80%;
  left: 0;
  z-index: 110;
}
.bawidxtxt {
  width: 100%;
  margin: 0 10px;
  display: block;
  text-align: center;
}
@media screen and (max-width: 600px) {
  .bawidxtxt div {
    max-width: 200px;
    display: inline-block;
    vertical-align: text-bottom;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
  }
}
@media screen and (min-width: 601px) {
  .bawidxtxt div {
    max-width: 60%;
    display: inline-block;
    vertical-align: text-bottom;
  }
}
.pncontainer {
  position: relative;
}
.prevnextctl {
  position: fixed;
  top: 80%;
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
.slider {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 100px;
  display: flex;
  flex-direction: row;
  overflow-x: hidden;
}

</style>
