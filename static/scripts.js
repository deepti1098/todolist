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

function deletemodalshow(id) {
  $("#" + id + "-modal").show();
}

function deletemodalhide(id) {
  $("#" + id + "-modal").hide();

}

function logoutmodalshow() {
  $("#exampleFrameModal2").show();
}

function logoutmodalhide() {
  $("#exampleFrameModal2").hide();

}

function clearallmodalshow() {
  $("#exampleFrameModal3").show();
}

function clearallmodalhide() {
  $("#exampleFrameModal3").hide();

}

//to hide (delete nd edit) icons and display (update nd cancel) buttons and enabling all input fields
function editClickHandle(id) {
  $("#" + id + "-icons").addClass("removeele");
  $("#" + id + "-update").removeClass("removeele");
  $("#" + id + "-title").removeAttr("disabled");
  $("#" + id + "-desc").removeAttr("disabled");
  $("#" + id + "-date").removeAttr("disabled");

}

//to show (delete nd edit) icons and hide (update nd cancel) buttons and disabling all input fields
function altericon(id) {
  $("#" + id + "-icons").removeClass("removeele");
  $("#" + id + "-update").addClass("removeele");
  $("#" + id + "-title").attr("disabled", true);
  $("#" + id + "-desc").attr("disabled", true);
  $("#" + id + "-date").attr("disabled", true);
}
// reset all value to thier initial values
function cancelClickHandle(id) {
  altericon(id);
  $("#" + id + "-title")[0].value = $("#" + id + "-title")[0].defaultValue;
  $("#" + id + "-desc")[0].value = $("#" + id + "-desc")[0].defaultValue;
  $("#" + id + "-date")[0].value = $("#" + id + "-date")[0].defaultValue;
}
// making ajax call to handle update
function updateClickHandle(id) {
  jdata = {
    Title: $("#" + id + "-title")[0].value,
    Desc: $("#" + id + "-desc")[0].value,
    Date: $("#" + id + "-date")[0].value
  }

  $.ajax(
    {
      url: "update/" + id,   //adding id to url
      type: "post",
      headers: { "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val() }, //adding CSRF token for POST request
      data: jdata,
      success: function () {   //if data updated sucessfully change to not editable
        altericon(id)
      }
    }
  )
}