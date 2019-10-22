<template>
  <div class="bartwork">
    <div id="bawcontainer" class="textcontainer">
      <p><strong>Artwork ID: </strong><span id=bawtextid></span></p>
      <p><strong>Accession Number: </strong><span id=bawtextacnum></span> </p>
      <p><strong>Title: </strong><span id=bawtexttitle></span> </p>
      <p><strong>Tombstone: </strong><span id=bawtexttomb></span> </p>
    </div>
    <div id="rightcontainer">
      <div id="bcrtext" class="textcontainer">
        <p><strong>Creator ID: </strong><span id=bcrtextid></span></p>
        <p><strong>Role: </strong><span id=bcrtextrole></span> </p>
        <p><strong>Description: </strong><span id=bcrtextdesc></span> </p>
      </div>
      <div id="bdptext" class="textcontainer">
        <p><strong>Department ID: </strong><span id=bdptextid></span></p>
        <p><strong>Name: </strong><span id=bdptextname></span> </p>
      </div>
    </div>
    <img id="bawimg">
  </div>
</template>

<script>
export default {
  name: 'bigartwork',
  props: {
    bartwork: {
      id: String,
      accession_number: String,
      title: String,
      tombstone: String
    },
    bcreator: {
      id: String,
      role: String,
      description: String
    },
    bdepartment: {
      id: String,
      name: String
    }
  },
  watch: {
    bartwork: function(val) {
      var elem = document.getElementById("bawimg");
      var fname = val.accession_number + '_reduced.jpg';
      elem.src = '../images/' + fname;
      elem.alt = fname;
      elem.title = val.title;
      document.getElementById("bawtextid").innerHTML = val.id;
      document.getElementById("bawtextacnum").innerHTML = val.accession_number;
      document.getElementById("bawtexttitle").innerHTML = val.title;
      document.getElementById("bawtexttomb").innerHTML = val.tombstone;
      this.$emit('pass-title', val.title);
    },
    bcreator: function(val) {
      document.getElementById("bcrtextid").innerHTML = val.id;
      document.getElementById("bcrtextrole").innerHTML = val.role;
      document.getElementById("bcrtextdesc").innerHTML = val.description;
    },
    bdepartment: function(val) {
      document.getElementById("bdptextid").innerHTML = val.id;
      document.getElementById("bdptextname").innerHTML = val.name;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .bartwork {
    color: white;
    position: relative;
    left: 0;
    top: 0;
    width: 100%;
    height: 70%;
    z-index: 100;
  }
  .textcontainer {
    text-align: left;
    margin: 20px;
    width: 20%;
    padding: 0 15px 0 20px;
    transition: all 500ms;
    border: 4px solid white;
    border-radius: 5px;
    background-color: black;
  }
  #bawcontainer {
    top: 0;
    left: 0;
  }
  #bawcontainer p:nth-child(4) {
    line-height: 2;
  }
  #rightcontainer {
    position: fixed;
    top: 0;
    left: 72%;
    width: 100%;
  }
  #bcrtext {
    top: 0;
    left: 0;
  }
  #bcrtext p:nth-child(3) {
    line-height: 2;
  }
  #bdptext {
    left: 0;
  }
  #bdptext p:nth-child(2) {
    line-height: 2;
  }
 .bartwork img {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: auto;
    height: auto;
    margin: auto;
    border: 4px solid white;
    border-radius: 5px;
    transition: all 500ms;
  }

</style>