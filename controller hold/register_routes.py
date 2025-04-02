import threading
from backend.checker import MainClass

def register_routes(app):
    @app.route("/start")
    def start_checker():
        main_class = MainClass()
        # Send a test email immediately
        main_class.send_test_email()
        # Start the long-running date checker in a background thread
        thread = threading.Thread(target=main_class.send_first_date_email, daemon=True)
        thread.start()
        return "Checker started and test email sent!"

    @app.route("/home")
    def home():
        return "Welcome home"
