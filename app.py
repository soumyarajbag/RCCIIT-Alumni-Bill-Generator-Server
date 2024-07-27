from flask import Flask, request, jsonify
from email.mime.text import MIMEText
from flask_cors import CORS
from email.mime.multipart import MIMEMultipart
import smtplib
from dotenv import load_dotenv
import os
from bill_gen import bill_gen

app = Flask(__name__)
CORS(app)
load_dotenv()

sender = "alumniassociationrcciit@gmail.com"
subject = "RCCIIT Alumni - Bill Details"

app_password = os.getenv("APP_PASSWORD")
sender_email = os.getenv("SENDER_EMAIL")
cc_email = "alma.connect@rcciit.org.in"  

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Alumni Bill Generator"}), 200

@app.route('/generate-bill', methods=['POST'])
def generate_pass():
    try:
        data = request.json
        bill_no = data.get('bill_no')
        name = data.get('name')
        stream = data.get('stream')
        college_id = data.get('college_id')
        email = data.get('email')
        phone = data.get('phone')
        mode = data.get('payment_mode')
        status = 'PAID'
        transaction_id = data.get('transaction_id')
        note = data.get('note')
        receiver = data.get('receiver')
        date = data.get('date')


        html_content = bill_gen(bill_no, name, stream, college_id, email, phone, mode, status, transaction_id, note, receiver, date)


        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = email
        msg["Cc"] = cc_email
        msg["Subject"] = f"{name.upper()} - {subject}"


        msg.attach(MIMEText(html_content, "html"))


        to_addresses = [email] + [cc_email]


        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, app_password)
            server.sendmail(sender, to_addresses, msg.as_string())

        return jsonify({
            "message": "Bill generated and email sent successfully",
            "status_code": 200
        }), 200

    except Exception as e:
        return jsonify({"message": "Failed to generate pass or send email", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
