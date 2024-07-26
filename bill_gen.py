def bill_gen(bill_no, name, stream, college_id, email, phone, mode, status, transaction_id, note, receiver, date):
    file = open("index.html", "r")
    html = file.read()
    html = html.replace("{{bill_no}}", bill_no)
    html = html.replace("{{name}}", name.upper())
    html = html.replace("{{stream}}", stream.upper())
    html = html.replace("{{college_id}}", college_id.upper())
    html = html.replace("{{email}}", email.lower())
    html = html.replace("{{phone}}", phone)
    html = html.replace("{{mode}}", mode.upper())
    html = html.replace("{{status}}", status.upper())
    html = html.replace("{{transaction_id}}", transaction_id)
    html = html.replace("{{note}}", note)
    html = html.replace("{{receiver}}", receiver.upper())
    html = html.replace("{{date}}", date)

    file.close()

    return html