

var cursorFocus = function(elem) {
  var x = window.scrollX, y = window.scrollY;
  elem.focus();
  window.scrollTo(x, y);
}

function topFormValidate(){

    canID = document.getElementById("canID");
    eventID = document.getElementById("eventID");

    if(canID.value == "" || canID.value == null  ){
          msg = "Please choose candidate first!";
          mainCanIDError.style.visibility = "visible";
          mainCanIDError.innerHTML = msg;
          canID.focus();
          canID.style.backgroundColor = "#ffabab";
          window.scrollTo(100,canID.offsetTop);
          return false;
        }

    if(eventID.value == "" || eventID.value == null  ){
          msg = "Please choose event!";
          eventIDError.style.visibility = "visible";
          eventIDError.innerHTML = msg;
          eventID.focus();
          eventID.style.backgroundColor = "#ffabab";
          window.scrollTo(100,eventID.offsetTop);
          return false;
        }

}

function validate() {

    mainCanID = document.getElementById("mainCanID");
    mainEventID = document.getElementById("mainEventID");

    form7_1 = document.getElementById("form7_1");
    form8_1 = document.getElementById("form8_1");
    form9_1 = document.getElementById("form9_1");
    form4_1 = document.getElementById("form4_1");
    form6_1 = document.getElementById("form6_1");
    birthDayError = document.getElementById("birthDayError");
    birthDayError.style.visibility = "hidden";


    if(mainCanID.value == "" || mainCanID.value == null  ){
          msg = "Please choose this section first!";
          topFormError.style.visibility = "visible";
          topFormError.innerHTML = msg;
          mainCanID.focus();
          mainCanID.style.backgroundColor = "#ffabab";
          window.scrollTo(100,mainCanID.offsetTop);
          return false;
        }



    if(form4_1.value == "" || form4_1.value == null  ){
          msg = "Please insert family name!";
          familyNameError.style.visibility = "visible";
          familyNameError.innerHTML = msg;
          form4_1.focus();
          form4_1.style.backgroundColor = "#ffabab";
          window.scrollTo(100,form4_1.offsetTop);
          return false;
        }

    if(form6_1.value == "" || form6_1.value == null  ){
          msg = "Please insert first name!";
          form6_1Error.style.visibility = "visible";
          form6_1Error.innerHTML = msg;
          form6_1.focus();
          form6_1.style.backgroundColor = "#ffabab";
          window.scrollTo(100,form6_1.offsetTop);
          return false;
        }

    if(form7_1.value == "" || form7_1.value == null || form7_1.value > 31 || form7_1.value < 1  ){
          msg = "Please insert correct day format!";
          birthDayError.style.visibility = "visible";
          birthDayError.innerHTML = msg;
          form7_1.focus();
          form7_1.style.backgroundColor = "#ffabab";
          window.scrollTo(100,form7_1.offsetTop);
          return false;
        }

    if(form8_1.value == "" || form8_1.value == null || form8_1.value > 12 || form8_1.value < 1  ){
          msg = "Please insert correct month format!";
          birthDayError.style.visibility = "visible";
          birthDayError.innerHTML = msg;
          form8_1.focus();
          form8_1.style.backgroundColor = "#ffabab";
          window.scrollTo(100,form8_1.offsetTop);
          return false;
        }
    if(form9_1.value == "" || form9_1.value == null || form9_1.value > 12 || form9_1.value < 1  ){
          msg = "Please insert correct year format!";
          birthDayError.style.visibility = "visible";
          birthDayError.innerHTML = msg;
          form9_1.focus();
          form9_1.style.backgroundColor = "#ffabab";
          window.scrollTo(100,form9_1.offsetTop);
          return false;
        }


}

