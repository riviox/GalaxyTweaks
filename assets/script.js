fetch('https://raw.githubusercontent.com/RivioxGaming/GalaxyFPS/main/version')
          .then(response => response.text())
          .then(ver => {
              document.getElementById('version').innerText = ver;
          })
          .catch(error => {
              console.log('Error: ', error);
          });