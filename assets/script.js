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
