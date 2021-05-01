const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    // event listener for animation
    burger.addEventListener('click', () => {
        // toggle nav
        nav.classList.toggle('nav-active');

        //animate links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ''
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 4 + 0.5}s`
            }
        })

        // burger animation that adds toggle class 
        burger.classList.toggle('toggle');
    });


}

//invoke function 
navSlide();