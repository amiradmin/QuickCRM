

var cursorFocus = function(elem) {
  var x = window.scrollX, y = window.scrollY;
  elem.focus();
  window.scrollTo(x, y);
}

function topFormValidate(){

    canID = document.getElementById("canID");
    eventID = document.getElementById("eventID");
    mainCanIDError = document.getElementById("mainCanIDError");

    if(canID.value == "" || canID.value == null  ){
          msg = "Please choose candidate first!";
          mainCanIDError.style.visibility = "visible";
          mainCanIDError.innerHTML = msg;
          canID.focus();
          canID.style.backgroundColor = "#ffabab";
          window.scrollTo(100,canID.offsetTop);
          return false;
        }

//    if(eventID.value == "" || eventID.value == null  ){
//          msg = "Please choose event!";
//          eventIDError.style.visibility = "visible";
//          eventIDError.innerHTML = msg;
//          eventID.focus();
//          eventID.style.backgroundColor = "#ffabab";
//          window.scrollTo(100,eventID.offsetTop);
//          return false;
//        }

}
function controllerMani(id,msg) {
        element = document.getElementById(id);
        if(element.value == "" || element.value == null ){
            element.placeholder = msg;
            element.focus();
            element.style.backgroundColor = "#ffabab";
            window.scrollTo(100,element.offsetTop);
            return false;
          }
}

function checkboxChange(obj,inputClass) {
    var cbs = document.getElementsByClassName(inputClass);
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}
function abilityChange(obj) {
    var cbs = document.getElementsByClassName("ability");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}

function venueChange(obj) {
    var cbs = document.getElementsByClassName("venueCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}

function examTypeChange(obj) {
    var cbs = document.getElementsByClassName("examTypeCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}
function examBodyChange(obj) {
    var cbs = document.getElementsByClassName("examBodyCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}

function weldingInspChange(obj) {
    var cbs = document.getElementsByClassName("weldInspCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}
function wIChange(obj) {
    var cbs = document.getElementsByClassName("wICh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}
function swIChange(obj) {
    var cbs = document.getElementsByClassName("swICh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}

function weldingQcChange(obj) {
    var cbs = document.getElementsByClassName("weldingQcCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}

function asmeChange(obj) {
    var cbs = document.getElementsByClassName("asmeCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}


function underWaterChange(obj) {
    var cbs = document.getElementsByClassName("underWaterCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}


function ndtExamChange(obj) {
    var cbs = document.getElementsByClassName("ndtExamCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}

function ndtLevelChange(obj) {
    var cbs = document.getElementsByClassName("ndtLevelCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}

function inductorySectorChange(obj) {
    var cbs = document.getElementsByClassName("inductorySectorCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}

function utCatChange(obj) {
    var cbs = document.getElementsByClassName("utCatCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}

function plantInspectionChange(obj) {
    var cbs = document.getElementsByClassName("plantInspectionCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}
function plantInspectionLevelChange(obj) {
    var cbs = document.getElementsByClassName("plantInspectionLevelCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}
function plantInspectionLevel2Change(obj) {
    var cbs = document.getElementsByClassName("plantInspectionLevel2Ch");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}
function examTitleChange(obj) {
    var cbs = document.getElementsByClassName("examTitleCh");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}

function isValidDate(input) {
     var inputEelemnt = document.getElementById(input);

    if(inputEelemnt.value == "" || inputEelemnt.value == null ){
        inputEelemnt.placeholder = "Insert date!";
        inputEelemnt.focus();
        inputEelemnt.style.backgroundColor = "#ffabab";
        window.scrollTo(100,inputEelemnt.offsetTop);
        return false;
      }
    var temp = inputEelemnt.value.split('/');
    var d = new Date(temp[2] + '/' + temp[0] + '/' + temp[1]);
    var result = (d && (d.getMonth() + 1) == temp[0] && d.getDate() == Number(temp[1]) && d.getFullYear() == Number(temp[2]));
    if (result !== true){
            inputEelemnt.style.backgroundColor = "#ffabab";
            inputEelemnt.value = "";
            inputEelemnt.placeholder = "Wrong format";
    }
    return result
}
function selectCheck(className,indicator){

    var checkboxs=document.getElementsByClassName(className);
    var indicatorElement = document.getElementById(indicator);
    var okay=false;
    for(var i=0,l=checkboxs.length;i<l;i++)
    {
        if(checkboxs[i].checked)
        {
            okay=true;
            break;
        }
    }
    if(!okay){
    indicatorElement.style.color = "#FF0000";
    indicatorElement.focus();
    window.scrollTo(100,indicatorElement.offsetTop);
    }else{
    indicatorElement.style.color = "#000000";
    }

}


function sponsorChange(obj) {
    var cbs = document.getElementsByClassName("sponsorCh");
    var form40_1 = document.getElementById("form40_1");
    var form43_1 = document.getElementById("form43_1");
    var form44_1 = document.getElementById("form44_1");
    var form45_1 = document.getElementById("form45_1");
    var form47_1 = document.getElementById("form47_1");

    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
    if(cbs[1].checked==true){
         form40_1.style.backgroundColor = "yellow";
         form43_1.style.backgroundColor = "yellow";
         form44_1.style.backgroundColor = "yellow";
         form45_1.style.backgroundColor = "yellow";
         form47_1.style.backgroundColor = "yellow";


    }else if(cbs[0].checked==true){
         form40_1.style.backgroundColor = "white";
         form43_1.style.backgroundColor = "white";
         form44_1.style.backgroundColor = "white";
         form45_1.style.backgroundColor = "white";
         form47_1.style.backgroundColor = "white";
    }


}

function validate() {

    mainCanID = document.getElementById("mainCanID");
    mainEventID = document.getElementById("mainEventID");



    if(mainCanID.value == "" || mainCanID.value == null  ){
          msg = "Please choose this section first!";
          topFormError.style.visibility = "visible";
          topFormError.innerHTML = msg;
          mainCanID.focus();
          mainCanID.style.backgroundColor = "#ffabab";
          window.scrollTo(100,mainCanID.offsetTop);
          return false;
        }
//    controllerMani("birthday","Please insert birth of date!");
//     controllerMani("date","Please insert date!");
      isValidDate("birthDay");


      selectCheck("near","nearTitle");
      selectCheck("color","colorTitle");
      selectCheck("shadeClass","shadeTitle");
      return isValidDate("recognisedDate");
//        selectCheck("level","levelTitle");
//        checkboxChange("ndtMethod");


//     controllerMani("verDate","Please insert date!");
//     return isValidDate("issueExpiryDates");




}

// Format the phone number as the user types it
document.getElementById('phone').addEventListener('keyup',function(evt){
        var phoneNumber = document.getElementById('phone');
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        phoneNumber.value = phoneFormat(phoneNumber.value);
});

// We need to manually format the phone number on page load
document.getElementById('phone').value = phoneFormat(document.getElementById('phone').value);

// A function to determine if the pressed key is an integer
function numberPressed(evt){
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        if(charCode > 31 && (charCode < 48 || charCode > 57) && (charCode < 36 || charCode > 40)){
                return false;
        }
        return true;
}


// Format the phone number as the user types it
document.getElementById('recognisedPhone').addEventListener('keyup',function(evt){
        var phoneNumber = document.getElementById('recognisedPhone');
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        phoneNumber.value = phoneFormat(phoneNumber.value);
});

// We need to manually format the phone number on page load
document.getElementById('recognisedPhone').value = phoneFormat(document.getElementById('recognisedPhone').value);

// A function to determine if the pressed key is an integer
function numberPressed(evt){
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        if(charCode > 31 && (charCode < 48 || charCode > 57) && (charCode < 36 || charCode > 40)){
                return false;
        }
        return true;

}function regNumberPressed(evt){
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        if(charCode > 31 && (charCode < 48 || charCode > 57) && (charCode < 36 || charCode > 40)){
                return false;
        }
        return true;
}

// A function to format text to look like a phone number
function phoneFormat(input){
        // Strip all characters from the input except digits
        input = input.replace(/\D/g,'');

        // Trim the remaining input to ten characters, to preserve phone number format
        input = input.substring(0,10);

        // Based upon the length of the string, we add formatting as necessary
        var size = input.length;
        if(size == 0){
                input = input;
        }else if(size < 4){
                input = '('+input;
        }else if(size < 7){
                input = '('+input.substring(0,3)+') '+input.substring(3,6);
        }else{
                input = '('+input.substring(0,3)+') '+input.substring(3,6)+' - '+input.substring(6,10);
        }
        return input;
}




// Emergency Tel
document.getElementById('form21_1').addEventListener('keyup',function(evt){
        var phoneNumber = document.getElementById('form21_1');
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        phoneNumber.value = phoneFormat(phoneNumber.value);
});

// We need to manually format the phone number on page load
document.getElementById('form21_1').value = phoneFormat(document.getElementById('form21_1').value);

// A function to determine if the pressed key is an integer
function emrNumberPressed(evt){
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        if(charCode > 31 && (charCode < 48 || charCode > 57) && (charCode < 36 || charCode > 40)){
                return false;
        }
        return true;
}

// Emergency Tel
document.getElementById('form4_4').addEventListener('keyup',function(evt){
        var phoneNumber = document.getElementById('form4_4');
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        phoneNumber.value = phoneFormat(phoneNumber.value);
});

// We need to manually format the phone number on page load
document.getElementById('form4_4').value = phoneFormat(document.getElementById('form4_4').value);

// A function to determine if the pressed key is an integer
function sponsorNumberPressed(evt){
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        if(charCode > 31 && (charCode < 48 || charCode > 57) && (charCode < 36 || charCode > 40)){
                return false;
        }
        return true;
}
