import streamlit as st
from streamlit_folium import st_folium
import folium

# Example dummy coordinates for donors
donors = [
    {"name": "Alice", "blood": "A+", "lat": 12.9716, "lon": 77.5946, "last_donation": "2024-10-01"},
    {"name": "Bob", "blood": "O-", "lat": 12.9611, "lon": 77.6387, "last_donation": "2024-12-20"},
]

st.title("Find Nearby Blood Donors")

m = folium.Map(location=[12.9716, 77.5946], zoom_start=12)

for donor in donors:
    folium.Marker(
        [donor["lat"], donor["lon"]],
        tooltip=donor["name"],
        popup=f"{donor['name']} - {donor['blood']} - Last Donated: {donor['last_donation']}",
        icon=folium.Icon(color="red" if donor["blood"] == "A+" else "blue"),
    ).add_to(m)

st_folium(m, width=700, height=500)
