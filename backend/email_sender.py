import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, sender_email, receiver_email, subject, body, password, status):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.subject = subject
        self.body = body
        self.password = password
        self.status = status
        

    def create_message(self):
        """Create and return the MIME message."""
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.receiver_email
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body, 'plain'))
        return msg

    def send_email(self):
        """Send the email."""
        msg = self.create_message()
        server = None  # Initialize server variable
        

        try:
            # Connect to Gmail's SMTP server and send the email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()  # Secure the connection
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, msg.as_string())
            print(self.status)
        except Exception as e:
            print(f"Failed to send email: {e}")
        finally:
            if server:
                server.quit()
