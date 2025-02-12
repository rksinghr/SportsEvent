from django.http import HttpResponse
from django.shortcuts import render
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import io

def generate_certificate(request):
    # Get participant details from form or query parameters
    name = request.GET.get('name', 'Participant')
    position = request.GET.get('position', 'Position')

    # Create an in-memory file-like object for the PDF
    buffer = io.BytesIO()

    # Create the PDF using reportlab
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Draw certificate image (you can adjust this path to the actual image location)
    cert_image = Image.open('path/to/certificate_template.png')
    cert_image_width, cert_image_height = cert_image.size
    p.drawImage('path/to/certificate_template.png', 0, height - cert_image_height, width=cert_image_width, height=cert_image_height)

    # Set font and text size for participant name and position
    p.setFont("Helvetica-Bold", 36)
    p.drawString(100, height - 200, f"Certificate of Completion")
    
    p.setFont("Helvetica", 24)
    p.drawString(100, height - 300, f"This is to certify that")
    p.setFont("Helvetica-Bold", 30)
    p.drawString(100, height - 350, f"{name}")
    
    p.setFont("Helvetica", 24)
    p.drawString(100, height - 450, f"Position: {position}")

    # Save the PDF to the buffer
    p.showPage()
    p.save()

    # Move to the beginning of the StringIO buffer
    buffer.seek(0)

    # Return the PDF as a response
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    return response

def certificate_form(request):
    return render(request, 'certificate/form.html')
