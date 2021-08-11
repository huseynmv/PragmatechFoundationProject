setInterval(()=>{

let currentDate = new Date()
let birthday = new Date(2000, 1, 4, 12)
let currentYear = currentDate.getFullYear()
let birthdayYear = birthday.getFullYear()
let currentMonth = currentDate.getMonth()
let birthdayMonth = birthday.getMonth()
let currentDay = currentDate.getDate()
let birthdayDay = birthday.getDate()

let age = Math.abs(currentYear-birthdayYear)
let month = Math.abs(currentMonth-birthdayMonth)
let day = Math.abs(currentDay-birthdayDay)

let btn=document.querySelector('.btn')

btn.innerHTML=`${age + "Year"} ${month + "Month"}  ${day + "Days" } ${currentDate.getHours() + 'Hours'} : ${currentDate.getMinutes()+'Minutes'}: ${currentDate.getSeconds()+ 'Seconds'}: ${currentDate.getMilliseconds()+'Milliseconds'}`
},1)