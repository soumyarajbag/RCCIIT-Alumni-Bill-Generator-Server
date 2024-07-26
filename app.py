from flask import Flask, request, jsonify
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from dotenv import load_dotenv
import os
from bill_gen import bill_gen

app = Flask(__name__)
load_dotenv()

# Set up the email parameters
sender = "rcciit.regalia.official@gmail.com"
subject = "RCCIIT Alumni - Bill Details"

app_password = os.getenv("APP_PASSWORD")
sender_email = os.getenv("SENDER_EMAIL")

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Regalia 2024 Pass Generator"}), 200

@app.route('/generate-bill', methods=['POST'])
def generate_pass():
    try:
        data = request.json
        print(data)
        bill_no = data.get('bill_no')
        name = data.get('name')
        stream = data.get('stream')
        college_id = data.get('college_id')
        email = data.get('email')
        phone = data.get('phone')
        mode = data.get('mode')
        status = data.get('status')
        transaction_id = data.get('transaction_id')
        note = data.get('note')
        receiver = data.get('receiver')
        date = data.get('date')
        print(data)

        # Generate HTML content for the bill
        html_content = bill_gen(bill_no, name, stream, college_id, email, phone, mode, status, transaction_id, note, receiver, date)

        # Create email message
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = email
        msg["Subject"] = name.upper() + ' - ' + subject

        # Attach email content
        msg.attach(MIMEText(html_content, "html"))

        # Log in to the SMTP server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, app_password)
        server.sendmail(sender, email, msg.as_string())
        server.quit()

        return jsonify({
            "message": "Bill generated and email sent successfully",
            "status_code": 200
        }), 200

    except Exception as e:
        return jsonify({"message": "Failed to generate pass or send email", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
