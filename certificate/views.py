import requests
from io import BytesIO
from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont
from django.templatetags.static import static

# Function to fetch, add text, and resize image
def fetch_edit_and_save_image(image_url, text, position, output_path):
    # Fetch image from URL
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))

    # Resize to a 1:1 ratio (e.g., square the smallest dimension)
    width, height = img.size
    new_size = min(width, height)
    img_resized = img.resize((new_size, new_size))

    # Add text to the image at the specified position
    draw = ImageDraw.Draw(img_resized)

    # You can use a basic font or load a custom one. We'll use the default font here.
    font = ImageFont.load_default()

    # Add the text to the image at the specified position
    draw.text(position, text, font=font, fill="white")  # You can change the text color here

    # Save the edited image as a PDF
    img_resized.save(output_path, "PDF")

def certificate_view(request):
    image_url = static('media/HRC_Certificate.jpeg')
    # image_url = "/static/media/HRC_Certificate.jpeg"
    text_to_add = "Some Name"
    text_position = (50, 50)  # Specify the (x, y) coordinates where you want the text to appear
    output_pdf_path = "HRC_Cert.pdf"

    if request.method == "POST":
        fetch_edit_and_save_image(image_url, text_to_add, text_position, output_pdf_path)

    return render(request, 'certificate/gen_cert1.html')