import time
from .email_sender import EmailSender
from .Date_checker import DateChecker
from .get_earliest_date import get_earliest_date


class MainClass:
    def __init__(self):
        # Email and authentication parameters
        self.sender_email = "gauravxbusiness@gmail.com"
        self.receiver_email = "gouravs229@gmail.com"
        self.subject = "Version 1.0 Minimum viable product"
        self.body = "Hello, this is a test email sent using Python."
        self.password = "tfle mlzc nioj zwvk"  # Your Gmail app-specific password

    def send_test_email(self):
        email_sender = EmailSender(
            self.sender_email,
            self.receiver_email,
            self.subject,
            self.body,
            self.password,
            "Register Email sent successfully!"
        )
        email_sender.send_email()

    def send_first_date_email(self):
        current_date = get_earliest_date()
        if current_date is None:
            subject = "No Date Available Currently"
            body = "We will update once the date is available."
            email_sender = EmailSender(
                self.sender_email,
                self.receiver_email,
                subject,
                body,
                self.password,
                "No Date found and updated to user"
            )
            email_sender.send_email()
            print("Couldn't find the required date in the table.")
            return
        else:
            print(f"Initial Earliest Date: {current_date}")
            subject = "Here is the Initial Date"
            body = "This is the nearest date available for an appointment in Delhi: " + current_date
            email_sender = EmailSender(
                self.sender_email,
                self.receiver_email,
                subject,
                body,
                self.password,
                "Date found and sent to User"
            )
            email_sender.send_email()
    
        # Warning: This loop will run indefinitely.
        while True:
            time.sleep(300)  # Sleep for 5 minutes (adjust as needed)
            new_date = get_earliest_date()
            # Check if the new date is earlier than the current date
            date_checker = DateChecker(current_date, new_date)
            if new_date == current_date:
                print(f"Date not changed: {current_date}")
            elif new_date and date_checker.is_new_date_earlier():
                print(f"Date has changed! Old Date: {current_date}, New Date: {new_date}")
                status = f"Old Date: {current_date}, New Date: {new_date}"
                body = f"Date has changed! Old Date: {current_date}, New Date: {new_date}"
                email_sender = EmailSender(
                    self.sender_email,
                    self.receiver_email,
                    subject,
                    body,
                    self.password,
                    status
                )
                email_sender.send_email()
                current_date = new_date
