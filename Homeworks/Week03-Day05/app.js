let total = 0
for (let i = 0; i <= 100; i++){
    total += i
}
console.log(total) // Sum 1 to 100

let info='Bu sahəyə yeni başlayanlar üçün programlaşdırma həddindən artıq qarışıq və çətin gələ bilər. İnternetdə tonlarla qaynaqları görüb gözünüz qorxa bilər. Düşünə bilərsiniz ki, bu qədər konsepti necə öyrənə bilərəm və yaxud bu mənim nə qədər zamanımı alar. Əfsanələrə görə, əgər riyaziyyatı yaxşı bilmirsinizsə sizin bu sahədə uğurlu ola bilməyiniz mümkün deyil. Və yaxud bu sahədə ali təhsiliniz yoxdursa heç bir yerdə iş tapa bilməyəcəksiniz. Əslində isə bu sahəyə giriş etdikdən sonra heç də elə olmadığını görəcəksiniz.'

function scount(){
    console.log(info.match(/s/g).length)
}
scount() // Number of s in string

console.log(info.length)  // Number of character in string

function herfler(a, b, c){
    a=info.length
    b=info.split(' ').length
    c=a-b-1
    console.log(c)
}
herfler() // Number of letters

console.log(info.split(' ').length) // Number of words


let arr=[1,3,4,6,89,12,67,34,89,123]

console.log(Math.max(...arr)) // Largest number

let cem = 0
for (let i = 0; i < arr.length; i++) {
    cem += arr[i]
    
}
console.log(cem) // Sum of array elements

