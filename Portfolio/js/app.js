window.addEventListener('scroll', ()=>{
    let navbar = document.getElementById("navbarr")
    navbar.classList.toggle("sticky", window.scrollY>0)
})

let ui = document.querySelector('.ui-container')
let marketing = document.querySelector('.marketing-container')
let ecommerce = document.querySelector('.ecommerce-container')
let copyright = document.querySelector('.copyright-container')
let heci = document.querySelector('.heci')
window.addEventListener('scroll', ()=>{
    ui.classList.toggle('animation', window.scrollY>100)
    marketing.classList.toggle('animation', window.scrollY>100)
    ecommerce.classList.toggle('animation', window.scrollY>100)
    copyright.classList.toggle('animation', window.scrollY>100)
})

// window.addEventListener('scroll', ()=>{
//     heci.classList.toggle('animation1', window.scrollY>800)
// })
