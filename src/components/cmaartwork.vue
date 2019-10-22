<template>
  <div class="cartwork">
    <img v-bind:src="imgsrc()"
         v-bind:alt="artwork.accession_number + '_reduced.jpg'"
         v-bind:title="artwork.title"
         v-on:click="$emit('artwork-clicked', this)">
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
    }
  },
  methods: {
    imgsrc: function() {
      return '../images/small/' + this.artwork.accession_number + '_reduced.jpg';
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .cartwork {
    margin: 15px;
  }
  img {
    border: 2px solid #fff;
    border-radius: 5px;
    opacity: 0.9;
    color: white;

    transition: all 500ms;
    z-index: 1;
    position: relative;
  }

  img:hover {
    background-color: blue;
    border-color: yellow;
    opacity: 1.0;
    transform: scale(1.5);
    cursor: pointer;
    z-index: 10;
  }
</style>