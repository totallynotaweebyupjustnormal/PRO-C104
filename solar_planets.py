import cv2
import numpy as np

# Load the solar system image
solar_system_image = cv2.imread('C:\\Users\\ASUS\\Downloads\\solar-system.jpg\\PRO-104-Project-Image-main')

# Define the names of the planets in the correct order
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Define the coordinates to place the names on the image
name_coordinates = [
    (30, 120),   # Mercury
    (250, 70),   # Venus
    (400, 80),   # Earth
    (550, 140),  # Mars
    (100, 250),  # Jupiter
    (320, 300),  # Saturn
    (520, 350),  # Uranus
    (670, 340)   # Neptune
]

# Define the font and color for the text
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.7
font_color = (255, 255, 255)
font_thickness = 2

# Loop through the planet names and coordinates to add them to the image
for i, name in enumerate(planet_names):
    cv2.putText(solar_system_image, name, name_coordinates[i], font, font_scale, font_color, font_thickness)

# Display the image with names
cv2.imshow('Solar System with Names', solar_system_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image with names
cv2.imwrite('solar_system_with_names.jpg', solar_system_image)