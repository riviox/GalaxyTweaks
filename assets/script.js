fetch('https://raw.githubusercontent.com/RivioxGaming/GalaxyTweaks/main/version')
    .then(response => response.text())
    .then(ver => {
        document.getElementById('version').innerText = ver;
    })
    .catch(error => {
        console.log('Version Error: ', error);
});

fetch('https://raw.githubusercontent.com/RivioxGaming/GalaxyTweaks/main/changelog')
    .then(response => response.text())
    .then(clog => {
        document.getElementById('clog').innerHTML = clog;
    })
    .catch(error => {
        console.log('Changelog Error: ', error);
});

$(document).ready(function() {
    $('a[href^="#"]').on('click', function(event) {
        var target = $(this.getAttribute('href'));
        if (target.length) {
            event.preventDefault();
            $('html, body').animate({
                scrollTop: target.offset().top
            }, 1000);
        }
    });

    function updateVisibility() {
        var scrollPosition = $(window).scrollTop();
        $('section').each(function() {
            var sectionPosition = $(this).offset().top;
            if (sectionPosition < (scrollPosition + $(window).height())) {
                $(this).addClass('visible');
            } else {
                $(this).removeClass('visible');
            }
        });

        var headerPosition = $('header').offset().top;
        if (headerPosition < (scrollPosition + $(window).height())) {
            $('header').addClass('visible');
        } else {
            $('header').removeClass('visible');
        }
    }

    $(window).scroll(updateVisibility);

    // Inicjalizacja animacji po załadowaniu strony
    $(window).scroll();
});