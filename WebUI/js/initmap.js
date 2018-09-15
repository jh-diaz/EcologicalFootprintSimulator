var mymap = L.map('mapid').setView([0, 0], 2);
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 5,
    minZoom: 2,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1Ijoib2xhb2xzZW4yMiIsImEiOiJjamxxNzVoNngwOW52M3Bxd2g2ZmJ0ZjlwIn0.yYeTTi-TBAXO98wtCudQFQ'
    }).addTo(mymap);
