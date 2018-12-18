// team Cassandra Gemini -- Theodore Peters, Jabir Chowdhury
// SoftDev pd7
// K28 -- sequential progression
// 2018-12-19

var fibonacci = (n) => {
    return n < 2 ? n : fibonacci(n-1) + fibonacci(n-2);
}

var gcd = (a,b) => {
    var max = 1;
    for(var i = 1; i <= a && i <= b; i++)
	if(a % i === 0 && b % i === 0)
	    max = i;
    return max;
}

KREWES = [
    ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore (Dont really care)', 'Anton', 'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason'],
    ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason'],
    ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']
]


var randomStudent = () => {
    // come to the computer interaction club
    students = KREWES[Math.floor(Math.random()*KREWES.length)];
    return students[Math.floor(Math.random()*students.length)];
}
