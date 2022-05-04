<h1>Click to see output</h1>
<video controls="" autoplay="true" name="media" hidden=true><source src="nevergonna.mp4" type="video/mp4"></video>
<script>
  //alert("never gonna give you up");
  document.getElementsByClassName("page-header")[0].remove();
  
  document.addEventListener('DOMContentLoaded', function() {
    //alert("Ready!");
    document.getElementById("content").getElementsByClassName("site-footer")[0].remove();
  }, false);
  
  document.addEventListener('click', () => {
    document.getElementById("content").getElementsByTagName("h1")[0].hidden = true;
    document.getElementById("content").getElementsByTagName("video")[0].hidden = false;
    document.getElementById("content").getElementsByTagName("video")[0].play();
  });
</script>  
