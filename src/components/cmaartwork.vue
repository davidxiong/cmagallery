<template>
  <div class="cartwork" :class="{ imgslider: slider == 'yes'}">
    <img v-bind:src="imgsrc()"
         :alt="artwork.accession_number + '_reduced.jpg'"
         :title="artwork.title"
         :class="{ imgslider: slider == 'yes'}"
         @click.stop="imgClicked">
  </div>
</template>

<script>
export default {
  name: 'cmaartwork',
  props: {
    artwork: {
      id: String,
      accession_number: String,
      title: String,
      tombstone: String
    },
    creator: {
      id: String,
      role: String,
      description: String
    },
    department: {
      id: String,
      name: String
    },
    slider: String
  },
  methods: {
    imgsrc: function() {
      return '../images/small/' + this.artwork.accession_number + '_reduced.jpg';
    },
    imgClicked: function() {
      this.$emit('artwork-clicked');
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .cartwork {
    margin: 5px 10px;
    max-width: 100px;
    height: auto;
  }
  .cartwork.imgslider {
    max-width: 75px;
    height: 100%;
    max-height: 75px;
  }
  .cartwork img {
    border: 2px solid #fff;
    border-radius: 5px;
    color: white;
    opacity: 0.9;
    vertical-align: bottom;

    transition: all 500ms;
    z-index: 1;
    position: relative;
  }
  .cartwork img.imgslider {
    opacity: 0.6;
    vertical-align: middle;
  }
  .cartwork img:hover {
    background-color: blue;
    border-color: yellow;
    opacity: 1.0;
    cursor: pointer;
    z-index: 10;
  }
  .cartwork img:hover:not(.imgslider) {
    transform: scale(1.5);
  }
</style>