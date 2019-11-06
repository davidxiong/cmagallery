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
    <div id="bimgcontainer">
      <img id="bawimg">
    </div>
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
    box-sizing: border-box;
    color: white;
    position: relative;
    left: 0;
    top: 0;
    max-width: 100%;
    height: 80%;
    z-index: 100;
    overflow: auto;
  }
@media screen and (min-width: 951px) {
  #bawcontainer {
    position: fixed;
    top: 20px;
    left: 20px;
    width: 20%;
  }
  #rightcontainer {
    position: fixed;
    top: 20px;
    right: 20px;
    width: 20%;
  }
}
@media screen and (max-width: 950px) {
  .bartwork {
    display: flex;
    flex-direction: column;
  }
  #bawcontainer {
    position: relative;
  }
  #rightcontainer {
    position: relative;
  }
  #bcrtext {
    margin: 20px 0 0 0;
  }
}
  .textcontainer {
    text-align: left;
    padding: 0;
    transition: all 500ms;
    border: 2px solid white;
    border-radius: 5px;
    background-color: black;
  }
  .textcontainer > p {
    margin: 16px 10px 16px 10px;
  }
  #bawcontainer p:nth-child(4) {
    line-height: 2;
  }
  #bcrtext {
    position: relative;
    width: 100%;
  }
  #bcrtext p:nth-child(3) {
    line-height: 2;
  }
  #bdptext {
    position: relative;
    width: 100%;
    margin: 20px 0 0 0;
  }
  #bdptext p:nth-child(2) {
    line-height: 2;
  }
  img {
    width: auto;
    height: auto;
    margin: auto;
    border: 4px solid white;
    border-radius: 5px;
    transition: all 500ms;
  }

</style>