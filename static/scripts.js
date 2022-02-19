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