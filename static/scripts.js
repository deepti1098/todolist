function handlerShow() {
  $("#addbox").show();
}

function handlerHide() {
  $("#addbox").hide();
}

function matchPassword() {
  var pw1 = document.getElementById("pass1");
  var pw2 = document.getElementById("cpass2");
  if (pw1.value != pw2.value) {
    $("#signupcpasserr").removeClass("removeele");
    return false;
  } else {
    $("#signupcpasserr").addClass("removeele");
    return true;
  }
}  
function editClickHandle(id){
  $("#"+id+"-icons").hide();
  $("#"+id+"-update").show();
  $("#"+id+"-title").removeAttr('disabled');
  $("#"+id+"-desc").removeAttr('disabled');
  $("#"+id+"-date").removeAttr('disabled');
}
function cancelClickHandle(id){
  $("#"+id+"-icons").show();
  $("#"+id+"-update").hide();
  $("#"+id+"-title").attr('disabled',true);
  $("#"+id+"-desc").attr('disabled',true);
  $("#"+id+"-date").attr('disabled',true);
}
function updateClickHandle(id){
  console.log($("#"+id+"-title").value)
  jdata={
    title:$("#"+id+"-title")[0].value,
    desc:$("#"+id+"-desc")[0].value,
    date:$("#"+id+"-date")[0].value,
  };
  $.ajax(
    {
      type:"post",
      url:"/edittask/"+id,
      headers: {
        "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
      },
      data:jdata,
      datatype: "json",
      success: function(data){
        console.log(data);
        cancelClickHandle(id);
      }
    })
}