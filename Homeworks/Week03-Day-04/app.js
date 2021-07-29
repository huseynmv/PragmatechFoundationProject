// numeric string used with + gives string type
let result;

result = '3' + 2; 
console.log(result) // "32"

result = '3' + true; 
console.log(result); // "3true"

result = '3' + undefined; 
console.log(result); // "3undefined"

result = '3' + null; 
console.log(result); // "3null"


let result;

// string to number
result = Number('324');
console.log(result); // 324

// boolean to number
result = Number(true);
console.log(result); // 1

result = Number(false);
console.log(result); // 0