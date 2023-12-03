function payNow() {
    var ttprice = document.getElementById('ttprice').value;
    var username = document.getElementById('Uname').value;
    var table_no = document.getElementById('Tno').value;
    var paymentMethod = document.getElementById('paymnetmethod').value;

    // Construct the URL using JavaScript
    var url = '../../create_queue/' + ttprice + '/' + username + '/' + table_no + '/' + paymentMethod;

    // Open the URL in a new tab
    
    window.open(url, '_blank');
    window.location.href = "/UserQ/"+username+"/"+String(table_no);
}

function minus(e){
    var number = parseInt(document.getElementById(e).value)
    number -= 1
    if (number==0){
        document.getElementById(e).value = 1
    }else{
        document.getElementById(e).value = number
    }
}

function plus(e){
    var number = parseInt(document.getElementById(e).value)
    number += 1
    if (number<=0){
        document.getElementById(e).value = 1
    }else{
        document.getElementById(e).value = number
    }
}