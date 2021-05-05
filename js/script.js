function find(){
    var ajax = new XMLHttpRequest();
    var zn = document.getElementById('input').value;
    //ajax.open('GET','find?text='+zn);
    ajax.open('GET','find?text='+zn);
    ajax.onreadystatechange=function(){
        if(ajax.readyState == 4){
            //console.log(ajax);
            if(ajax.status == 200){
                console.log(ajax);
                var res1=document.getElementById('file');
                res1.innerHTML=ajax.responseText;
            }
        }
    }
    ajax.send();
}
function download(fileid){
    var ajax = new XMLHttpRequest();
    //var zn = document.getElementById('input').value;
    //ajax.open('GET','find?text='+zn);
    ajax.open('GET','download?id='+fileid);
    ajax.onreadystatechange=function(){
        if(ajax.readyState == 4){
            //console.log(ajax);
            if(ajax.status == 200){
                console.log(ajax);
                //var res1=document.getElementById('file');
                //res1.innerHTML=ajax.responseText;
            }
        }
    }
    ajax.send();
}