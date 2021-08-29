

var cursorFocus = function(elem) {
  var x = window.scrollX, y = window.scrollY;
  elem.focus();
  window.scrollTo(x, y);
}


function validate() {

    form7_1 = document.getElementById("form7_1");
    form7_1Error = document.getElementById("form7_1Error");
    form7_1Error.style.visibility = "hidden";

    if(form7_1.value == "" || form7_1.value == null || form7_1.value > 31 || form7_1.value < 1  ){

          msg = "Please insert correct day format!";
          form7_1Error.style.visibility = "visible";
          form7_1Error.innerHTML = msg;
          form7_1.focus();
          form7_1.style.backgroundColor = "#ffabab";
          window.scrollTo(100,form7_1.offsetTop);

          return false;
        }

}

