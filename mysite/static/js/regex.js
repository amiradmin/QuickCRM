
function abilityChange(obj) {
    alert("Here");
    var cbs = document.getElementsByClassName("ability");

    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}

var cursorFocus = function(elem) {
  var x = window.scrollX, y = window.scrollY;
  elem.focus();
  window.scrollTo(x, y);
}

function topFormFirstValidate(){

    canID = document.getElementById("canID");
    eventID = document.getElementById("eventID");

//    if(canID.value == "" || canID.value == null  ){
//          msg = "Please choose candidate first!";
//          topFormError.style.visibility = "visible";
//          topFormError.innerHTML = msg;
//          canID.focus();
//          canID.style.backgroundColor = "#ffabab";
//          window.scrollTo(100,canID.offsetTop);
//          return false;
//        }

    if(eventID.value == "" || eventID.value == null  ){
          msg = "Please fill this section first!";
          topFormError.style.visibility = "visible";
          topFormError.innerHTML = msg;
          topFormError.focus();
          window.scrollTo(100,eventID.offsetTop);
          return false;
        }

}



function topFormValidate(){

    canID = document.getElementById("canID");
    eventID = document.getElementById("eventID");
    categoryID = document.getElementById("categoryID");

//    if(canID.value == "" || canID.value == null  ){
//          canID.style.backgroundColor = "#ffabab";
////          window.scrollTo(100,canID.offsetTop);
//          return false;
//        }
//
    else if(eventID.value == "" || eventID.value == null  ){
          eventID.style.backgroundColor = "#ffabab";
//          window.scrollTo(100,eventID.offsetTop);
          return false;
        }

    else if(categoryID.value == "" || categoryID.value == null  ){
          categoryID.style.backgroundColor = "#ffabab";
//          window.scrollTo(100,categoryID.offsetTop);
          return false;
        }

}






//==============
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
    var temp = inputEelemnt.value.split('/');
    var d = new Date(temp[2] + '/' + temp[0] + '/' + temp[1]);
    var result = (d && (d.getMonth() + 1) == temp[0] && d.getDate() == Number(temp[1]) && d.getFullYear() == Number(temp[2]));
    if (result !== true){
            inputEelemnt.style.backgroundColor = "#ffabab";
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

    form7_1 = document.getElementById("form7_1");
    form8_1 = document.getElementById("form8_1");
    form9_1 = document.getElementById("form9_1");
    form20_1 = document.getElementById("form20_1");
    birthDayError = document.getElementById("birthDayError");
    birthDayError.style.visibility = "hidden";

//    controllerMani("form7_1","Please choose this section first!");



    if(mainCanID.value == "" || mainCanID.value == null  ){
          msg = "Please choose this section first!";
          topFormError.style.visibility = "visible";
          topFormError.innerHTML = msg;
          mainCanID.focus();
          mainCanID.style.backgroundColor = "#ffabab";
          window.scrollTo(100,mainCanID.offsetTop);
          return false;
        }


    controllerMani("form4_1","Please insert family name!");
    controllerMani("form6_1","Please insert first name!");

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
    if(form9_1.value == "" || form9_1.value == null || form9_1.value > 2002 || form9_1.value < 1940  ){
          msg = "Please insert correct year format!";
          birthDayError.style.visibility = "visible";
          birthDayError.innerHTML = msg;
          form9_1.focus();
          form9_1.style.backgroundColor = "#ffabab";
          window.scrollTo(100,form9_1.offsetTop);
          return false;
        }
        selectCheck("sponsorCh","t1k_1");
        selectCheck("venueCh","t1x_1");
        selectCheck("agreement","t2z_1");
        controllerMani("form21_1","Please insert emergency tel!");
//        controllerMani("form11_2","Please insert approval number!");
//        controllerMani("form12_2","Please insert qualifications held!");
//        controllerMani("form34_2","Please insert under water inspection!");
//        controllerMani("form47_3","Please insert requirements!");
//        controllerMani("form51_3","Please insert examination title!");
//
        controllerMani("form1_4","Please insert insert name!");
        controllerMani("form2_4","Please insert company & position!");
        controllerMani("form3_4","Please insert relation!");
        controllerMani("form4_4","Please insert tel!");
        controllerMani("form5_4","Please insert email address!");
        return isValidDate("form6_4");
        return controllerMani("form6_4","Please insert date!");




}

// Format the phone number as the user types it
document.getElementById('privateTel').addEventListener('keyup',function(evt){
        var phoneNumber = document.getElementById('privateTel');
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        phoneNumber.value = phoneFormat(phoneNumber.value);
});

// We need to manually format the phone number on page load
document.getElementById('privateTel').value = phoneFormat(document.getElementById('privateTel').value);


document.getElementById('form45_1').addEventListener('keyup',function(evt){
        var phoneNumber = document.getElementById('form45_1');
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        phoneNumber.value = phoneFormat(phoneNumber.value);
});

// We need to manually format the phone number on page load
document.getElementById('form45_1').value = phoneFormat(document.getElementById('form45_1').value);

document.getElementById('privateTel').addEventListener('keyup',function(evt){
        var phoneNumber = document.getElementById('privateTel');
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        phoneNumber.value = phoneFormat(phoneNumber.value);
});

// We need to manually format the phone number on page load
document.getElementById('privateTel').value = phoneFormat(document.getElementById('privateTel').value);

// A function to determine if the pressed key is an integer
function numberPressed(evt){
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



