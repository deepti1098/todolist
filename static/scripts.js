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
    alert("Passwords did not match");
    return false;
  } else {
    alert("Password created successfully");
    return true;
  }
}  