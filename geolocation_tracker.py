import geocoder
import folium

# Get current location using IP
g = geocoder.ip('me')
lat, lng = g.latlng

print(f"Your location: Latitude = {lat}, Longitude = {lng}")

# Create a map centered at the location
map = folium.Map(location=[lat, lng], zoom_start=15)
folium.Marker([lat, lng], popup="You are here!").add_to(map)

# Save the map to an HTML file
map.save("geolocation_tracker.html")
print("Map saved as geolocation_tracker.html")
