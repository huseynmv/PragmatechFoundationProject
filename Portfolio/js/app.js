window.addEventListener('scroll', ()=>{
    let navbar = document.getElementById("navbarr")
    navbar.classList.toggle("sticky", window.scrollY>0)
})