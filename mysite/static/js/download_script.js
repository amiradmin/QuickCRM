var doc = new jsPDF(); 
var specialElementHandlers = { 
    '#editor': function (element, renderer) { 
        return true; 
    } 
};
$('#cmd').click(function () { 
    doc.fromHTML($('#contentContainer').html(), 30, 50, { 
        'width': 900, 
            'elementHandlers': specialElementHandlers 
    }); 
    doc.save('sample-page.pdf'); 
});