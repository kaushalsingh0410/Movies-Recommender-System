$(document).ready(function () {

    $('.link-backdrops, .link-posters').hide()

    const $tooltip = $('<div id="movie-tooltip"></div>').css({
        position: 'fixed',
        padding: '6px 10px',
        background: 'rgba(0, 0, 0, 0.85)',
        color: '#fff',
        fontSize: '0.75rem',
        borderRadius: '4px',
        whiteSpace: 'nowrap',
        zIndex: 9999,
        pointerEvents: 'none',
        opacity: 0,
        transition: 'opacity 0.2s ease'
    }).appendTo('body');



    $(document).on('mouseenter','.actor-title', function (e) {
        const title = $(this).data('title');
        $(this).css({
            color: '#10B981',
        });
        $tooltip.text(title).css({ opacity: 1 });
    }).on('mousemove','.actor-title', function (e) {
        $tooltip.css({
            top: e.clientY - 40,
            left: e.clientX + 10
        });
    }).on('mouseleave','.actor-title', function () {
        $tooltip.css({ opacity: 0 });
    }).on('mouseleave', '.actor-title',function (e) {
        $(this).css({
            color: 'rgba(0, 0, 0, 0.85)',
        });
    })

    $(document).on('click','.tab',function (){
        const linkClass = $(this).data('link');
        $('[class*="link-"]').hide();
        $('.'+linkClass).show()
    });



  




})

document.addEventListener('DOMContentLoaded', function() {
    const videoWrappers = document.querySelectorAll('.video-wrapper');
    
    videoWrappers.forEach(wrapper => {
        const iframe = wrapper.querySelector('iframe');
        const playButton = wrapper.querySelector('.custom-play-button');
        
        playButton.addEventListener('click', function() {
            // Add autoplay and controls to iframe src
            const currentSrc = iframe.src;
            const newSrc = currentSrc + '&autoplay=1&controls=1';
            iframe.src = newSrc;
            
            // Hide custom play button
            wrapper.classList.add('playing');
        });
    });
});


    const tabs = document.querySelectorAll(".tab");
    const sections = document.querySelectorAll(".media-section");

    tabs.forEach(tab => {
      tab.addEventListener("click", () => {
        // Remove active class from all tabs and sections
        tabs.forEach(t => t.classList.remove("active"));
        sections.forEach(s => s.classList.remove("active"));

        // Add active class to selected tab and section
        tab.classList.add("active");
        document.getElementById(tab.dataset.tab).classList.add("active");
      });
    });