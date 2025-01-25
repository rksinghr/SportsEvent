import pyotp
from datetime import datetime, timedelta
from azure.communication.email import EmailClient
from .models import otpBank
import pytz

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