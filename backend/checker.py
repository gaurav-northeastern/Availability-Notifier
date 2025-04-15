# import time
# from .email_sender import EmailSender
# from .Date_checker import DateChecker
# from .get_earliest_date import get_earliest_dates


# class MainClass:
#     def __init__(self, receiver_email, visaType, vac, location):
#         self.sender_email = "gauravxbusiness@gmail.com"
#         self.receiver_email = receiver_email
#         self.subject = "Version 1.0 Minimum viable product"
#         self.body = "Hello, this is a test email sent using Python."
#         self.password = "tfle mlzc nioj zwvk"
#         self.visaType = visaType
#         self.vac = vac
#         self.location = location
#   # Use an env variable in production

#     def send_first_date_email(self):
#         try:
#             print(f"[{self.receiver_email}] Starting checker for {self.visaType} - {self.vac} at {self.location}")

#             # Use visaType as the dynamic table ID
#             dates = get_earliest_dates(self.visaType, self.location)
#             vac_location = f"{self.location} VAC"

#             # CASE 1: Scraper returned nothing
#             if not dates:
#                 print(f"[{self.receiver_email}] No dates returned from scraper.")
#                 subject = "No Dates Available"
#                 body = f"Could not retrieve any appointment dates for {self.location}."
#                 self.send_email(subject, body, "No dates returned.")
#                 return

#             # CASE 2: Check based on appointment type
#             if self.vac.lower() == "vac":
#                 if not dates.get(self.location) and not dates.get(vac_location):
#                     subject = f"No Dates Available for {self.visaType} - {self.vac} at {self.location}"
#                     body = (
#                         f"Hello,\n\n"
#                         f"No appointment dates are currently available for:\n"
#                         f"- Visa Type: {self.visaType}\n"
#                         f"- Appointment Type: {self.vac}\n"
#                         f"- Location: {self.location} and {vac_location}\n\n"
#                         "We will notify you as soon as dates become available.\n\nRegards,\nVisa Notifier"
#                     )
#                     self.send_email(subject, body, "No dates found (VAC + location).")
#                     print(f"[{self.receiver_email}] No VAC or regular dates found for {self.location}.")
#                     return
#             else:
#                 if not dates.get(self.location):
#                     subject = f"No Dates Available for {self.visaType} at {self.location}"
#                     body = (
#                         f"Hello,\n\n"
#                         f"No appointment dates are currently available for:\n"
#                         f"- Visa Type: {self.visaType}\n"
#                         f"- Appointment Type: {self.vac}\n"
#                         f"- Location: {self.location}\n\n"
#                         "We will notify you as soon as dates become available.\n\nRegards,\nVisa Notifier"
#                     )
#                     self.send_email(subject, body, "No dates found (regular only).")
#                     print(f"[{self.receiver_email}] No regular dates found for {self.location}.")
#                     return

#             # ✅ Send Initial Available Dates
#             subject = f"Initial Appointment Dates for {self.visaType} - {self.vac} at {self.location}"
#             body = (
#                 f"Hello,\n\n"
#                 f"Here are the nearest appointment dates available for your selection:\n"
#                 f"- Visa Type: {self.visaType}\n"
#                 f"- Appointment Type: {self.vac}\n"
#                 f"- Location: {self.location}\n\n"
#             )

#             if dates.get(vac_location):
#                 body += f"- {vac_location}: {dates[vac_location]}\n"
#             if dates.get(self.location):
#                 body += f"- {self.location}: {dates[self.location]}\n"

#             body += "\nWe will continue monitoring and notify you of any changes.\n\nRegards,\nVisa Notifier"

#             print(f"[{self.receiver_email}] Initial Dates Found:\n{body}")
#             self.send_email(subject, body, "Initial appointment dates sent to user.")

#             # 🕒 Begin monitoring loop
#             current_dates = dates

#             while True:
#                 time.sleep(300)  # 5 minutes
#                 new_dates = get_earliest_dates(self.visaType)
#                 if not new_dates:
#                     print(f"[{self.receiver_email}] No new dates fetched.")
#                     continue

#                 for loc_key in current_dates:
#                     old_date = current_dates.get(loc_key)
#                     new_date = new_dates.get(loc_key)

#                     if not new_date or new_date == old_date:
#                         continue

#                     checker = DateChecker(old_date, new_date)
#                     if checker.is_new_date_earlier():
#                         subject = f"📅 Date Change Alert: {loc_key}"
#                         body = (
#                             f"Hello,\n\n"
#                             f"The appointment date for {loc_key} has changed:\n"
#                             f"- Old Date: {old_date}\n"
#                             f"- New Date: {new_date}\n\n"
#                             f"Visa Type: {self.visaType}\n"
#                             f"Appointment Type: {self.vac}\n"
#                             f"Location: {self.location}\n\n"
#                             "We’ll continue monitoring and notify you of further changes.\n\nRegards,\nVisa Notifier"
#                         )
#                         self.send_email(subject, body, f"{loc_key} date update sent to user.")
#                         print(f"[{self.receiver_email}] {loc_key} updated: {old_date} → {new_date}")
#                         current_dates[loc_key] = new_date

#         except Exception as e:
#             print(f"❌ Error in send_first_date_email for {self.receiver_email}: {e}")


#     def send_email(self, subject, body, log_msg):
        
#         email_sender = EmailSender(
#             self.sender_email,
#             self.receiver_email,
#             subject,
#             body,
#             self.password,
#             log_msg
#         )
#         email_sender.send_email()


import time
from .email_sender import EmailSender
from .Date_checker import DateChecker
from .get_earliest_date import get_earliest_dates
from datetime import datetime

# class MainClass:
#     def __init__(self, receiver_email, visaType, vac, location):
#         self.sender_email = "gauravxbusiness@gmail.com"
#         self.receiver_email = receiver_email
#         self.password = "tfle mlzc nioj zwvk"
#         self.visaType = visaType
#         self.vac = vac
#         self.location = location

#     def log(self, message):
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         print(f"[{timestamp}] [{self.receiver_email}] {message}")

#     def send_email(self, subject, body, log_msg):
#         email_sender = EmailSender(
#             self.sender_email,
#             self.receiver_email,
#             subject,
#             body,
#             self.password,
#             log_msg
#         )
#         email_sender.send_email()

#     def send_first_date_email(self):
#         try:
#             self.log(f"Starting checker for {self.visaType} - {self.vac} at {self.location}")

#             dates = get_earliest_dates(self.visaType, self.location)
#             vac_location = f"{self.location} VAC"

#             if not dates:
#                 self.log("No dates returned from scraper.")
#                 subject = "No Dates Available"
#                 body = f"Could not retrieve any appointment dates for {self.location}."
#                 self.send_email(subject, body, "No dates returned.")
#                 return

#             if self.vac:  # true means check both VAC and base location
#                 if not dates.get(self.location) and not dates.get(vac_location):
#                     subject = f"No Dates Available for {self.visaType} - {self.vac} at {self.location}"
#                     body = (
#                         f"Hello,\n\n"
#                         f"No appointment dates are currently available for:\n"
#                         f"- Visa Type: {self.visaType}\n"
#                         f"- Appointment Type: {self.vac}\n"
#                         f"- Location: {self.location} and {vac_location}\n\n"
#                         "We will notify you as soon as dates become available.\n\nRegards,\nVisa Notifier"
#                     )
#                     self.send_email(subject, body, "No dates found (VAC + location).")
#                     self.log(f"No VAC or regular dates found for {self.location}.")
#                     return
#             else:
#                 if not dates.get(self.location):
#                     subject = f"No Dates Available for {self.visaType} at {self.location}"
#                     body = (
#                         f"Hello,\n\n"
#                         f"No appointment dates are currently available for:\n"
#                         f"- Visa Type: {self.visaType}\n"
#                         f"- Appointment Type: Interview\n"
#                         f"- Location: {self.location}\n\n"
#                         "We will notify you as soon as dates become available.\n\nRegards,\nVisa Notifier"
#                     )
#                     self.send_email(subject, body, "No dates found (regular only).")
#                     self.log(f"No regular dates found for {self.location}.")
#                     return

#             subject = f"Initial Appointment Dates for {self.visaType} - {self.vac} at {self.location}"
#             body = (
#                 f"Hello,\n\n"
#                 f"Here are the nearest appointment dates available for your selection:\n"
#                 f"- Visa Type: {self.visaType}\n"
#                 f"- Appointment Type: {self.vac}\n"
#                 f"- Location: {self.location}\n\n"
#             )
#             if dates.get(vac_location):
#                 body += f"- {vac_location}: {dates[vac_location]}\n"
#             if dates.get(self.location):
#                 body += f"- {self.location}: {dates[self.location]}\n"

#             body += "\nWe will continue monitoring and notify you of any changes.\n\nRegards,\nVisa Notifier"
#             self.log(f"Initial Dates Found:\n{body}")
#             self.send_email(subject, body, "Initial appointment dates sent to user.")

#             current_dates = dates

#             while True:
#                 time.sleep(300)  # 5 minutes
#                 new_dates = get_earliest_dates(self.visaType, self.location)
#                 if not new_dates:
#                     self.log("No new dates fetched.")
#                     continue

#                 for loc_key in current_dates:
#                     old_date = current_dates.get(loc_key)
#                     new_date = new_dates.get(loc_key)

#                     if not new_date or new_date == old_date:
#                         continue

#                     checker = DateChecker(old_date, new_date)
#                     if checker.is_new_date_earlier():
#                         subject = f"\U0001F4C5 Date Change Alert: {loc_key}"
#                         body = (
#                             f"Hello,\n\n"
#                             f"The appointment date for {loc_key} has changed:\n"
#                             f"- Old Date: {old_date}\n"
#                             f"- New Date: {new_date}\n\n"
#                             f"Visa Type: {self.visaType}\n"
#                             f"Appointment Type: {self.vac}\n"
#                             f"Location: {self.location}\n\n"
#                             "We’ll continue monitoring and notify you of further changes.\n\nRegards,\nVisa Notifier"
#                         )
#                         self.send_email(subject, body, f"{loc_key} date update sent to user.")
#                         self.log(f"{loc_key} updated: {old_date} → {new_date}")
#                         current_dates[loc_key] = new_date

#         except Exception as e:
#             self.log(f"❌ Error in send_first_date_email: {e}")

class MainClass:
    def __init__(self, receiver_email, visaType, vac, location):
        self.sender_email = "gauravxbusiness@gmail.com"
        self.receiver_email = receiver_email
        self.password = "tfle mlzc nioj zwvk"
        self.visaType = visaType
        self.vac = vac
        self.location = location

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{self.receiver_email}] {message}")

    def send_email(self, subject, body, log_msg):
        email_sender = EmailSender(
            self.sender_email,
            self.receiver_email,
            subject,
            body,
            self.password,
            log_msg
        )
        email_sender.send_email()

    def send_first_date_email(self):
        try:
            self.log(f"Starting checker for {self.visaType} - {self.vac} at {self.location}")

            dates = get_earliest_dates(self.visaType, self.location, self.vac)
            vac_location = f"{self.location} VAC"

            if not dates:
                self.log("No dates returned from scraper.")
                subject = "No Dates Available"
                body = f"Could not retrieve any appointment dates for {self.location}."
                self.send_email(subject, body, "No dates returned.")
                return

            if self.vac:
                if not dates.get(self.location) and not dates.get(vac_location):
                    subject = f"No Dates Available for {self.visaType} - {self.vac} at {self.location}"
                    body = (
                        f"Hello,\n\n"
                        f"No appointment dates are currently available for:\n"
                        f"- Visa Type: {self.visaType}\n"
                        f"- Appointment Type: {self.vac}\n"
                        f"- Location: {self.location} and {vac_location}\n\n"
                        "We will notify you as soon as dates become available.\n\nRegards,\nVisa Notifier"
                    )
                    self.send_email(subject, body, "No dates found (VAC + location).")
                    self.log(f"No VAC or regular dates found for {self.location}.")
                    return
            else:
                if not dates.get(self.location):
                    subject = f"No Dates Available for {self.visaType} at {self.location}"
                    body = (
                        f"Hello,\n\n"
                        f"No appointment dates are currently available for:\n"
                        f"- Visa Type: {self.visaType}\n"
                        f"- Appointment Type: Interview\n"
                        f"- Location: {self.location}\n\n"
                        "We will notify you as soon as dates become available.\n\nRegards,\nVisa Notifier"
                    )
                    self.send_email(subject, body, "No dates found (regular only).")
                    self.log(f"No regular dates found for {self.location}.")
                    return

            subject = f"Initial Appointment Dates for {self.visaType} - {self.vac} at {self.location}"
            body = (
                f"Hello,\n\n"
                f"Here are the nearest appointment dates available for your selection:\n"
                f"- Visa Type: {self.visaType}\n"
                f"- Appointment Type: {self.vac}\n"
                f"- Location: {self.location}\n\n"
            )
            if dates.get(vac_location):
                body += f"- {vac_location}: {dates[vac_location]}\n"
            if dates.get(self.location):
                body += f"- {self.location}: {dates[self.location]}\n"

            body += "\nWe will continue monitoring and notify you of any changes.\n\nRegards,\nVisa Notifier"
            self.log(f"Initial Dates Found:\n{body}")
            self.send_email(subject, body, "Initial appointment dates sent to user.")

            current_dates = dates

            while True:
                time.sleep(300)  # 5 minutes
                new_dates = get_earliest_dates(self.visaType, self.location, self.vac)
                if not new_dates:
                    self.log("No new dates fetched.")
                    continue

                for loc_key in current_dates:
                    old_date = current_dates.get(loc_key)
                    new_date = new_dates.get(loc_key)

                    if not new_date or new_date == old_date:
                        continue

                    checker = DateChecker(old_date, new_date)
                    if checker.is_new_date_earlier():
                        subject = f"\U0001F4C5 Date Change Alert: {loc_key}"
                        body = (
                            f"Hello,\n\n"
                            f"The appointment date for {loc_key} has changed:\n"
                            f"- Old Date: {old_date}\n"
                            f"- New Date: {new_date}\n\n"
                            f"Visa Type: {self.visaType}\n"
                            f"Appointment Type: {self.vac}\n"
                            f"Location: {self.location}\n\n"
                            "We’ll continue monitoring and notify you of further changes.\n\nRegards,\nVisa Notifier"
                        )
                        self.send_email(subject, body, f"{loc_key} date update sent to user.")
                        self.log(f"{loc_key} updated: {old_date} → {new_date}")
                        current_dates[loc_key] = new_date

        except Exception as e:
            self.log(f"❌ Error in send_first_date_email: {e}")