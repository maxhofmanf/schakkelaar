var btn = document.createElement('button');
btn.style.margin = '10px';

document.body.appendChild(btn);


// schijf hier tussen je code
btn.innerHTML = 'light switch: on';
var x = true
document.body.style.backgroundColor = "#FFFF00"


btn.onclick =( )=>{
    if(x === true){
        btn.innerHTML = 'light switch: off';
        document.body.style.backgroundColor = "#000000";
        console.log('hallo')
        x = false
    }else{
        btn.innerHTML = 'light switch: on';
        document.body.style.backgroundColor = "#FFFF00";
        console.log(x)
        x = true  
    }
};


// schijf hier tussen je code