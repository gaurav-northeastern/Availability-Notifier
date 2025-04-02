# controller/routes.py

from backend.checker import MainClass
import threading

def register_routes(app):
    @app.route("/start")
    def start_checker():
        main_class = MainClass()
        main_class.send_test_email()

        # Start date checker in background thread
        thread = threading.Thread(target=main_class.send_first_date_email, daemon=True)
        thread.start()

        return "Checker started and test email sent!"

    @app.route("/home")
    def home():
        return "Welcome home! currently under building"
