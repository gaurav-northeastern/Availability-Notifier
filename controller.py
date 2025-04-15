# controller/routes.py
from flask import request, jsonify
from backend.checker import MainClass
import threading

def register_routes(app):

    @app.route("/start", methods=["POST"])
    def start_checker():
        data = request.get_json()
        email = data.get("email")
        visaType = data.get("visaType")
        vac = data.get("vac")
        location = data.get("location")

        if not email:
            return jsonify({"error": "Email is required"}), 400
        if not visaType:
            return jsonify({"error": "Select Visa Type"}), 400
        if  vac is None:
            return jsonify({"error": "Select VAC Appointment or Interview Appointment"}), 400

        if not location:
            return jsonify({"error": "Location is Required"}), 400
        
        print(f"Starting checker for {email}...")

        # Start the checker with custom email
        main_class = MainClass(
    receiver_email=email,
    visaType=visaType,
    vac=vac,
    location=location
)

        thread = threading.Thread(target=main_class.send_first_date_email, daemon=True)
        thread.start()

        return jsonify({"message": f"Checker started for {email}."}), 200

