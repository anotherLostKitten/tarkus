// team Cassandra Gemini -- Theodore Peters, Jabir Chowdhury
// SoftDev pd7
// K28 -- sequential progression
// 2018-12-19

var fibonacci = (n) => {
    return n < 2 ? n : fibonacci(n-1) + fibonacci(n-2);
}

var gcd = (a,b) => {
    var max = 1;
    for(var i = 1; i <= a && i <= b; i++){
	if(a % i === 0 && b % i === 0){
	    max = i;
	}
    }
    return max;
}

var students = ["theodore 'big T' peters", "jabir 'computer interaction club 1st president' Chowdhury", "topher 'big bazinga' brown mykolyk"]

var randomStudent = () => {
    // come to the computer interaction club
    return students[Math.floor(Math.random()*students.length)];
}
