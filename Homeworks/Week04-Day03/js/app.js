let box=document.querySelector('.box')
let up=document.querySelector('#up')
let down=document.querySelector('#down')
let right=document.querySelector('#right')
let left=document.querySelector('#left')
marginAmount=0

up.addEventListener('click', function(){
    box.style.marginBottom=`${marginAmount}px`
    marginAmount+=20
})

down.addEventListener('click', function(){
    box.style.marginTop=`${marginAmount}px`
    marginAmount+=20
})

right.addEventListener('click', function(){
    box.style.marginLeft=`${marginAmount}px`
    marginAmount+=20
})

left.addEventListener('click', function test(){
    box.style.marginRight=`${marginAmount}px`
    marginAmount+=20
})

