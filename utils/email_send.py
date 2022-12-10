from users.models import EmailVerifyRecord
from django.core.mail import send_mail
import random
import string


def random_str(random_length=8):

    chars = string.ascii_letters + string.digits
    str_code = ''.join(random.sample(chars, random_length))
    return str_code


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_title = 'Account email verification needed'
        email_content = 'Verify now: http://127.0.0.1:8000/users/active/{0}'.format(code)

        send_status = send_mail(email_title, email_content, 'a1728644084@gmail.com', [email])
        if send_status:
            pass
