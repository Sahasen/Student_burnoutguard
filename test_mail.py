"""Run:  python test_mail.py your_email@gmail.com
Sends ONE test email and prints exactly what is wrong. Safe: never prints your password."""
import os, sys
from dotenv import load_dotenv
load_dotenv()

to = sys.argv[1] if len(sys.argv) > 1 else input('Send test email to: ').strip()

sender = os.environ.get('BURNOUT_MAIL_SENDER', '')
pw     = os.environ.get('BURNOUT_MAIL_PASSWORD', '')
brevo  = os.environ.get('BREVO_API_KEY', '')

print('\n--- CONFIG CHECK ---')
print('.env found in this folder :', os.path.exists('.env'))
print('BURNOUT_MAIL_SENDER       :', sender or 'NOT SET')
print('BURNOUT_MAIL_PASSWORD     :', f'set ({len(pw)} characters, should be 16 with no spaces)' if pw else 'NOT SET')
print('BREVO_API_KEY             :', 'set' if brevo else 'NOT SET')
print('Mode that will be used    :', 'Brevo API' if brevo else ('Gmail SMTP' if pw else 'NONE - emails disabled'))
print('\n--- SENDING ---')

import email_service as es
ok = es.send_email(to, 'BurnoutGuard test email', '<h2>It works!</h2><p>Test from BurnoutGuard.</p>')
print('\nRESULT:', 'SUCCESS - check your inbox and spam folder' if ok else 'FAILED - read the [EMAIL ERROR ...] line above')