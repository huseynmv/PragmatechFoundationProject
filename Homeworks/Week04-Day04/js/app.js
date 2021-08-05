let hr=document.querySelector('.hour')
let mn=document.querySelector('.minute')
let sc=document.querySelector('.second')


let deg = 6;


interval = setInterval(()=>{
    let d=new Date();
    let h=d.getHours()*30
    let m=d.getMinutes()*deg
    let s=d.getSeconds()*deg

    sc.style.transform=`rotate(${s}deg)`
    mn.style.transform=`rotate(${m}deg)`
    hr.style.transform=`rotate(${(h) + (m/12)}deg)`
})











// setInterval(() => {
//     s+=6
//     sc.style.transform='rotate(' + s + 'deg)'
// }, 1000)

// setInterval(() => {
//     m+=6
//     mn.style.transform='rotate(' + m + 'deg)'
// }, 60000)

// setInterval(() => {
//     h+=6
//     hr.style.transform='rotate(' + h + 'deg)'
// }, 3600000)

