function gosite(e){
    var username = document.getElementById("username").value;
    var table_no = document.getElementById("table_no").value;

    console.log(username, table_no)

    if(username===''){
        alert(" กรุณาใส่ชื่อ");
        e.preventDefault();
        e.stopPropagation();
        // window.location.href = "/";
    }
    else if(table_no===''){
        alert("กรุณาใส่หมายเลขโต๊ะให้ถูกต้อง");
        e.preventDefault();
        e.stopPropagation();
        // window.location.href = "/";
    }
    if (username!=='' && table_no!==''){
        alert("welcome: "+username+table_no);
        window.location.href = "/inmain/"+username+"/"+String(table_no);
    }
}

