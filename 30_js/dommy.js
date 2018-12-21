// team Cassandra Gemini -- Theodore Peters, Jabir Chowdhury
// SoftDev pd7
// K28 -- sequential regression III: Season of the Witch
// 2018-12-21

var thelist = document.getElementById("thelist");
var theelements = thelist.getElementsByTagName("li");
var header = document.getElementById("h");

var removeItem = (e) => {
	e.remove();
}

var eventify = (e) => {
    e.addEventListener('mouseover',()=>{header.innerHTML=e.innerHTML;});
    e.addEventListener('mouseout',()=>{header.innerHTML="Hello, World!";});
    e.addEventListener('click',()=>{removeItem(e);});
}

for (let i = 0; i < theelements.length; i++){
    let e = theelements[i];
    eventify(e);
}

var addItem = () => {
    let e=document.createElement("li");
    e.innerHTML = "wORD";
    thelist.appendChild(e);
    eventify(e);
}

document.getElementById("b").addEventListener('click', addItem);

var fiblist = document.getElementById("fiblist");
var fib = () => {
	let fibelements = fiblist.getElementsByTagName("li");
	console.log(fibelements.length);
	let n = fibelements.length<2 ? fibelements.length : parseInt(fibelements[fibelements.length-1].innerHTML) + parseInt(fibelements[fibelements.length - 2].innerHTML);
	let e = document.createElement("li");
	e.innerHTML = n;
	fiblist.appendChild(e);
}

document.getElementById("fb").addEventListener("click",fib);
