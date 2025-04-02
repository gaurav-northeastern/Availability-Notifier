# Visa Slot Notifier 🛂📬

A simple Python + Flask app that scrapes US visa appointment availability (e.g., Delhi VAC), checks for earlier slots, and sends email alerts when dates change.

---

## 🚀 Features

- ⏱ Scrapes visa slot availability from [checkvisaslots.com](https://checkvisaslots.com/latest-us-visa-availability.html)
- 📬 Sends email alerts via Gmail when a new earlier date is found
- 🛑 Notifies when no dates are available
- 🔁 Checks every 5 minutes (configurable)
- 🧪 Test email functionality included

---

2. Set up a virtual environment
   bash
   Copy
   Edit
   python -m venv venv
   source venv/bin/activate # For macOS/Linux
   venv\Scripts\activate # For Windows
3. Install dependencies
   bash
   Copy
   Edit
   pip install -r requirements.txt
4. Add environment variables
   Create a .env file in the root:

env
Copy
Edit
EMAIL_PASSWORD=your_app_specific_password_here
⚠️ Don't use your regular Gmail password. Use an app password if using Gmail.

🚦 Running the App

1. Start the Flask server
   bash
   Copy
   Edit
   export FLASK_APP=app.py # macOS/Linux
   set FLASK_APP=app.py # Windows
   flask run
   Visit: http://127.0.0.1:5000/start to trigger the notifier.

🧪 Test Email
You can test the email feature by calling:

python
Copy
Edit
MainClass().send_test_email()
