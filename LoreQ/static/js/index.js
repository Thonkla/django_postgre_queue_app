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
