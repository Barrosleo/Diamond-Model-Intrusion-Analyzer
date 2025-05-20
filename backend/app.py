from flask import Flask, jsonify, render_template
from data_parser import parse_incidents
from diamond_classifier import classify_incidents

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Render the dashboard HTML template
    return render_template('dashboard.html')

@app.route('/api/incidents', methods=['GET'])
def get_incidents():
    # Parse and classify the incident logs
    incidents = parse_incidents()
    classified = classify_incidents(incidents)
    return jsonify(classified)

if __name__ == '__main__':
    app.run(debug=True)
