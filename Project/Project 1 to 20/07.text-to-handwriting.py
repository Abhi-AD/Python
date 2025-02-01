import requests
from PIL import Image, ImageDraw, ImageFont
import os


# Function to download the Google font
def download_font(url, font_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{font_name}.ttf", "wb") as f:
            f.write(response.content)
        print(f"Font {font_name} downloaded successfully!")
    else:
        print("Failed to download font")


# URL for the Google Font (Roboto in this case)
font_url = "https://fonts.gstatic.com/s/roboto/v27/KFOmCnqEu92Fr1Mu4mxK.woff2"

# Font name for saving the file
font_name = "Roboto"

# Download the font
download_font(font_url, font_name)

# Create an image with a white background
img = Image.new("RGB", (1000, 1000), color="white")
d = ImageDraw.Draw(img)

# Load the downloaded font
font = ImageFont.truetype(f"{font_name}.ttf", 30)

# Text to convert to handwriting
txt = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio.
Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at 
nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec 
tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget 
nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, 
per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim 
lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In 
scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem.
"""

# Add the text to the image
d.text((10, 10), txt, font=font, fill="black")

# Save the image
img.save("text-handwriting.png")

print("Image with handwriting generated!")
