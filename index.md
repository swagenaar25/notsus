<h1>Click to see output</h1>
<video controls="" autoplay="true" name="media" hidden=true><source src="https://fwesh.yonle.repl.co/" type="video/mp4"></video>
<script>
  alert("never gonna give you up");
  document.getElementsByClassName("page-header")[0].remove();
  setTimeout(function() { document.getElementById("content").getElementsByClassName("site-footer")[0].remove(); }, 2000);
  
  document.addEventListener('click', () => {
    document.getElementById("content").getElementsByTagName("h1")[0].hidden = true;
    document.getElementById("content").getElementsByTagName("video")[0].hidden = false;
    document.getElementById("content").getElementsByTagName("video")[0].play();
  });
</script>  
