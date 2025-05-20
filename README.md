# Diamond Model Intrusion Analyzer

## Purpose
Develop a tool that ingests cybersecurity incident data (from logs or threat feeds) and automatically maps key event features to the Diamond Model’s components:
- **Adversary:** Identify the threat actor behind the incident.
- **Infrastructure:** Tag the resources used (e.g., servers, domains).
- **Capability:** Determine the techniques and tools applied.
- **Victim:** Recognize the targeted system or organization.

This tool aids SOC analysts in visualizing attack relationships, highlighting detection gaps, and refining mitigation strategies.

## Key Features
- **Data Ingestion & Parsing:**  
  Accept incident log files (JSON, CSV, log formats), extract attributes such as IP addresses, suspicious commands, and contextual data.
- **Automated Diamond Classification:**  
  Use rule-based keyword matching to classify incident details into Adversary, Infrastructure, Capability, or Victim.
- **Correlation & Relationship Mapping:**  
  Build interactive visual graphs to show how adversaries correlate with specific capabilities, infrastructures, and victims.
- **Interactive Visualization Dashboard:**  
  A web interface (implemented in Flask and enhanced with JavaScript/Chart.js) displays a summary of incidents and mapping of incident phases.
- **Reporting & Alerts:**  
  Generate reports summarizing trends (e.g., common adversaries or high-risk infrastructures) and optionally trigger alerts when a phase is overloaded.

## Tech Stack
- **Backend:** Python with Flask for data processing, log ingestion, and phase classification.
- **Frontend:** HTML/CSS/JavaScript with Chart.js (or D3.js) for interactive visualizations.
- **Data Storage:** JSON files (or SQLite for a lightweight database).
- **Optional:** Threat intelligence API integration (using Python's requests library).

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Diamond-Model-Intrusion-Analyzer.git
   cd Diamond-Model-Intrusion-Analyzer
   ```
2. **Setup the Backend:**
  ```
  cd backend
  python -m venv venv
  source venv/bin/activate   # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  python app.py
  ```

3.  **Using the Dashboard:**

- Place or update sample incident logs in the data/ directory.

- The dashboard visualizes how individual incidents are mapped to the Diamond Model components.

## Future Enhancements

-  Advanced machine learning for improved classification.

=  Integration with live SIEM systems for real-time analysis.

=  User authentication and role-based access control.

=  Enhanced reporting and export functionality.

## License

This project is licensed under the MIT License.

