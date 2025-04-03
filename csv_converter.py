from flask import Flask, render_template, request, redirect, send_file
import csv
import os

app = Flask(__name__)

# CSV File Name
CSV_FILE = "cybercrime_report.csv"

# Ensure the CSV file has headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Victim Name", "Victim Age", "Victim Contact", "Victim Location",
            "Perpetrator Name/Username", "Perpetrator Contact",
            "Incident Date", "Incident Location", "Incident Description",
            "Cyberbullying Type", "Screenshot Filename"
        ])

@app.route('/')
def form():
    return render_template("input.html")  # Renders the input form

@app.route('/submit', methods=['POST'])
def submit():
    # Fetch form data
    victim_name = request.form['victim_name']
    victim_age = request.form['victim_age']
    victim_contact = request.form['victim_contact']
    victim_location = request.form['victim_location']
    
    perpetrator_name = request.form['perpetrator_name']
    perpetrator_contact = request.form['perpetrator_contact']
    
    incident_date = request.form['incident_date']
    incident_location = request.form['incident_location']
    incident_description = request.form['incident_description']
    cyberbullying_type = request.form['cyberbullying_type']
    
    # Handle file upload
    screenshot = request.files['screenshot']
    screenshot_filename = screenshot.filename if screenshot else "No file"

    if screenshot and screenshot_filename:
        screenshot.save(os.path.join("uploads", screenshot_filename))

    # Save to CSV
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            victim_name, victim_age, victim_contact, victim_location,
            perpetrator_name, perpetrator_contact,
            incident_date, incident_location, incident_description,
            cyberbullying_type, screenshot_filename
        ])

    return redirect('/success')

@app.route('/success')
def success():
    return "<h2>✅ Report Submitted Successfully! <a href='/'>Submit Another</a></h2>"

@app.route('/download')
def download_csv():
    return send_file(CSV_FILE, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists("uploads"):
        os.makedirs("uploads")  # Create an uploads folder if not present
    app.run(debug=True)
