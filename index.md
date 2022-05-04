<h1>Click to see output</h1>
<p class="out" hidden=true>
  1<br>
  1<br>
  2<br>
  3<br>
  5<br>
  8<br>
  13<br>
  21<br>
  34<br>
  55<br>
  89<br>
  144<br>
  233<br>
  377<br>
  610<br>
  987<br>
  1597<br>
  2584<br>
  4181<br>
  6765<br>
  10946<br>
  17711<br>
  28657<br>
  46368<br>
  75025<br>
  121393<br>
  196418<br>
  317811<br>
  514229<br>
  832040<br>
  1346269<br>
  2178309<br>
  3524578<br>
  5702887<br>
  9227465<br>
  14930352<br>
  24157817<br>
  39088169<br>
  63245986<br>
  102334155<br>
  165580141<br>
  267914296<br>
  433494437<br>
  701408733<br>
  1134903170<br>
  1836311903<br>
  2971215073<br>
  4807526976<br>
  7778742049<br>
  12586269025<br>
  20365011074<br>
  32951280099<br>
  53316291173<br>
  86267571272<br>
  139583862445<br>
  225851433717<br>
  365435296162<br>
  591286729879<br>
  956722026041<br>
  1548008755920<br>
  2504730781961<br>
  4052739537881<br>
  6557470319842<br>
  10610209857723<br>
  17167680177565<br>
  27777890035288<br>
  44945570212853<br>
  72723460248141<br>
  117669030460994<br>
  190392490709135<br>
  308061521170129<br>
  498454011879264<br>
  806515533049393<br>
  1304969544928657<br>
  2111485077978050<br>
  3416454622906707<br>
  5527939700884757<br>
  8944394323791464<br>
  14472334024676221<br>
  23416728348467685<br>
  37889062373143906<br>
  61305790721611591<br>
  99194853094755497<br>
  160500643816367088<br>
  259695496911122585<br>
  420196140727489673<br>
  679891637638612258<br>
  1100087778366101931<br>
  1779979416004714189<br>
  2880067194370816120<br>
  4660046610375530309<br>
  7540113804746346429<br>
  12200160415121876738<br>
  19740274219868223167<br>
  31940434634990099905<br>
  51680708854858323072<br>
  83621143489848422977<br>
  135301852344706746049<br>
  218922995834555169026<br>
  354224848179261915075
</p>
<video controls="" name="media" hidden=true><source src="nevergonna.mp4" type="video/mp4"></video>
<script>
  //alert("never gonna give you up");
  document.getElementsByClassName("page-header")[0].remove();
  
  document.addEventListener('DOMContentLoaded', function() {
    //alert("Ready!");
    document.getElementById("content").getElementsByClassName("site-footer")[0].remove();
    document.getElementById("content").getElementsByTagName("video")[0].load();
  }, false);
  
  document.addEventListener('click', () => {
    document.getElementById("content").getElementsByTagName("h1")[0].hidden = true;
    document.getElementById("content").getElementsByClassName("out")[0].hidden = false;
    //document.getElementById("content").getElementsByTagName("video")[0].hidden = false;
    document.getElementById("content").getElementsByTagName("video")[0].play();
  });
</script>
