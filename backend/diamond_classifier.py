def classify_event(event):
    """
    Classify an incident event into one of the Diamond Model components:
    Adversary, Infrastructure, Capability, or Victim.
    
    Uses simple rule-based keyword matching on the event's description.
    """
    description = event.get('description', '').lower()
    
    if any(keyword in description for keyword in ['apt', 'attacker', 'hacker', 'threat actor', 'malware campaign']):
        return 'Adversary'
    elif any(keyword in description for keyword in ['server', 'domain', 'ip', 'dns', 'infrastructure']):
        return 'Infrastructure'
    elif any(keyword in description for keyword in ['exploit', 'malware', 'attack', 'phishing', 'ransomware']):
        return 'Capability'
    elif any(keyword in description for keyword in ['target', 'victim', 'user', 'customer']):
        return 'Victim'
    else:
        return 'Unknown'

def classify_incidents(incidents):
    """
    Process a list of incident events by adding a 'component' key based on their classification.
    """
    for event in incidents:
        event['component'] = classify_event(event)
    return incidents

if __name__ == '__main__':
    # Sample test
    sample_incidents = [
        {"timestamp": "2025-05-15T08:00:00Z", "description": "Detected APT activity from a known threat actor", "artifact": "APT Group XYZ"},
        {"timestamp": "2025-05-15T09:00:00Z", "description": "Suspicious DNS query from compromised server", "artifact": "malicious.example.com"},
        {"timestamp": "2025-05-15T10:00:00Z", "description": "User reported a phishing email; potential victim identified", "artifact": "employee@company.com"}
    ]
    classified = classify_incidents(sample_incidents)
    import json
    print(json.dumps(classified, indent=2))
