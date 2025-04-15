from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Placeholder data for now
    return render_template('dashboard.html')

# Example: Inventory API endpoint (for AJAX/JS fetch)
@app.route('/api/inventory')
def api_inventory():
    # Replace with DB query in production
    items = [
        {"name": "Surgical Masks", "category": "PPE", "location": "Storage A", "quantity": 1250, "status": "good", "last_updated": "Today, 9:41 AM"},
        {"name": "Nitrile Gloves (M)", "category": "PPE", "location": "Storage B", "quantity": 850, "status": "medium", "last_updated": "Yesterday, 2:30 PM"},
        {"name": "Insulin", "category": "Medication", "location": "Pharmacy", "quantity": 120, "status": "low", "last_updated": "Jun 12, 2023"},
        {"name": "IV Solution (1L)", "category": "Fluids", "location": "Storage C", "quantity": 432, "status": "good", "last_updated": "Jun 10, 2023"},
        {"name": "Syringes (10ml)", "category": "Supplies", "location": "Storage A", "quantity": 75, "status": "low", "last_updated": "Jun 9, 2023"},
        {"name": "Gauze Pads", "category": "Supplies", "location": "Storage B", "quantity": 620, "status": "good", "last_updated": "Jun 8, 2023"},
        {"name": "Ventilator Filters", "category": "Equipment", "location": "ICU Storage", "quantity": 28, "status": "low", "last_updated": "Jun 7, 2023"}
    ]
    return jsonify(items)

# Example: RAG estimation endpoint (Ollama via LangChain)
@app.route('/api/estimate', methods=['POST'])
def api_estimate():
    data = request.json
    patient_info = data.get('patient_info', {})
    # TODO: Replace with real RAG call
    # For now, return a mock estimation
    return jsonify({
        "estimated_time": f"{random.randint(1, 8)} hours",
        "resources": [
            {"name": "IV Solution (1L)", "amount": random.randint(1, 3)},
            {"name": "Surgical Masks", "amount": random.randint(2, 10)}
        ],
        "explanation": "This is a mock estimation. Integrate with Ollama RAG for real results."
    })

if __name__ == '__main__':
    app.run(debug=True)
