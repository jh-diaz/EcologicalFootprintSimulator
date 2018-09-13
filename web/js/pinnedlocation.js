var marker = L.marker([51.5, -0.09]).addTo(mymap);
marker.bindPopup("<b>Selected Country</b><br>Data").openPopup();

function onMapClick(e) {
    alert("You clicked the map at " + e.latlng);
    var marker = L.marker(e.latlng).addTo(mymap);
    marker.bindPopup("<b>Selected Country</b><br>Data").openPopup();
}
mymap.on('click', onMapClick);