import pyotp
from datetime import datetime, timedelta
from azure.communication.email import EmailClient
from .models import otpBank
import pytz
import qrcode
from django.http import HttpResponse
from io import BytesIO

utc = pytz.utc

def email_service(to_add, subject_text, msg_txt):
    try:
        connection_string = "endpoint=https://demo-acs-rit.unitedstates.communication.azure.com/;accesskey=MBkOeR5/rodtitPULt6eYHnf6Z4qjBS8/SmGcdVo+lA1j+EE+hNG7RFQdGDRzLimmfhAsVWXXnwpD+wGPDLu2w=="
        client = EmailClient.from_connection_string(connection_string)

        message = {
            "senderAddress": "DoNotReply@0bd00eea-f8ae-4d6b-93e8-160618cdb67e.azurecomm.net",
            "recipients":  {
                "to": [{"address": to_add }],
            },
            "content": {
                "subject": subject_text,
                "plainText": msg_txt,
            }
        }

        poller = client.begin_send(message)
        result = poller.result()

    except Exception as ex:
        print(ex)

def generate_otp(usr):
    otp_secret_key = pyotp.random_base32()
    hotp = pyotp.HOTP(otp_secret_key)
    otp = hotp.at(1401)
    print(otp)

    valid_date = datetime.now(utc) + timedelta(minutes=1)

    ob = otpBank.objects.create(
        key_user = usr,
        otp_secret_key = otp_secret_key,
        otp_valid_date = valid_date
    )
    
    return otp, valid_date

def generate_qr_code(request, data):
    # Create a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a BytesIO object
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    # Generate a unique CID for embedding the image in the email body
    image_data = img_io.getvalue()

    # Send an email with the QR code embedded
    subject = 'Your QR Code'
    message = 'Here is your QR code:'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = 'recipient@example.com'  # Set the recipient email address

    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=from_email,
        to=[to_email],
    )
    email.content_subtype = "html"

    # Attach the QR code image as an inline image
    email.attach(
        'qrcode.png',
        image_data,
        'image/png',
    )
    email.inline_image_map = {
        'cid:qrcode': 'qrcode.png',
    }

    # HTML body with the image referenced as a Content-ID (cid)
    email.body = f'''
    <p>Here is your QR code:</p>
    <img src="cid:qrcode" alt="QR Code"/>
    '''

    # Send the email
    email.send()


    # Return the image as HTTP response
    return HttpResponse(img_io, content_type="image/png")

