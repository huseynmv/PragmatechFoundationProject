let i = 0;
let images = ["img/img1.jpg", "img/img2.jpg", "img/img3.jpg", "img/img4.jpg"]

function slideshow(click){
    if(click === 'next'){
        i++;
        if(i === images.length){ 
            i = images.length - 1;
        };

    }if(click === 'previous'){
        i--;
        if(i < 0){ 
            i = 0;
        }
    }
    
    document.getElementById('change').src = images[i];
}