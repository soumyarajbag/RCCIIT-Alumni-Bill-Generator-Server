def bill_gen(bill_no, name, stream, college_id, email, phone, mode, status, transaction_id, note, receiver, date):
    with open("index.html", "r") as file:
        html = file.read()

    def safe_upper(value):
        return value.upper() if value else ""

    html = html.replace("{{bill_no}}", bill_no if bill_no else "")
    html = html.replace("{{name}}", safe_upper(name))
    html = html.replace("{{stream}}", safe_upper(stream))
    html = html.replace("{{college_id}}", safe_upper(college_id))
    html = html.replace("{{email}}", email.lower() if email else "")
    html = html.replace("{{phone}}", phone if phone else "")
    html = html.replace("{{mode}}", safe_upper(mode))
    html = html.replace("{{status}}", safe_upper(status))
    html = html.replace("{{transaction_id}}", transaction_id if transaction_id else "")
    html = html.replace("{{note}}", note if note else "N/A")
    html = html.replace("{{receiver}}", safe_upper(receiver))
    html = html.replace("{{date}}", date if date else "")

    return html
