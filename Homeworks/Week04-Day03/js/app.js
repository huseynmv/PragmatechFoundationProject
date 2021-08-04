let box=document.querySelector('.box')
let up=document.querySelector('#up')
let down=document.querySelector('#down')
let right=document.querySelector('#right')
let left=document.querySelector('#left')


up.addEventListener('click', function(){
    box.style.marginBottom='20px'
})

down.addEventListener('click', function(){
    box.style.marginTop='20px'
})

right.addEventListener('click', function(){
    box.style.marginLeft='20px'
})

left.addEventListener('click', function test(){
    box.style.marginRight='20px'
})

