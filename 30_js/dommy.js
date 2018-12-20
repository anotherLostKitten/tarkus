// team Cassandra Gemini -- Theodore Peters, Jabir Chowdhury
// SoftDev pd7
// K28 -- sequential regression III: Season of the Witch
// 2018-12-21

var thelist = Document.getElementById("thelist");
var theelements = thelist.getElementsByTagName("li");
var header = Document.getElementById("h");

var removeItem = (e) => {
    
}

for (var e in theelements){
    e.addEventListener('mouseover',()=>{header.innerHTML=e.innerHTML;});
    e.addEventListener('mouseout',()=>{header.innerHTML="Hello, World!";});
    e.addEventListener('click',()=>{removeItem(e);});
}

var addItem = () => {
    var e=document.createElement("li");
    e.innerHTML = "wORD";
    thelist.appendChild(e);
}

document.getLementById("b").addEventListener('click', addItem);
