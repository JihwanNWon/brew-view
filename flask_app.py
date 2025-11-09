"""
Brew View - Potion Flow Monitoring Dashboard
Flask application with Leaflet/OSM map visualization
"""

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# API Configuration
API_BASE = "https://hackutd2025.eog.systems"

def fetch_api(endpoint, timeout=10):
    """Fetch data from API."""
    try:
        response = requests.get(endpoint, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"API Error ({endpoint}): {e}")
        return None

@app.route('/')
def index():
    """Main dashboard page with Leaflet map."""
    return render_template('index.html')

@app.route('/api/cauldrons')
def get_cauldrons():
    """Get all cauldron data."""
    data = fetch_api(f"{API_BASE}/api/Information/cauldrons")
    if data:
        return jsonify(data)
    return jsonify({"error": "Failed to fetch cauldrons"}), 500

@app.route('/api/market')
def get_market():
    """Get market location."""
    data = fetch_api(f"{API_BASE}/api/Information/market")
    if data:
        return jsonify(data)
    return jsonify({"error": "Failed to fetch market"}), 500

@app.route('/api/network')
def get_network():
    """Get network connections."""
    data = fetch_api(f"{API_BASE}/api/Information/network")
    if data:
        return jsonify(data)
    return jsonify({"error": "Failed to fetch network"}), 500

@app.route('/api/tickets')
def get_tickets():
    """Get transport tickets."""
    data = fetch_api(f"{API_BASE}/api/Tickets")
    if data:
        return jsonify(data)
    return jsonify({"error": "Failed to fetch tickets"}), 500

@app.route('/api/data')
def get_historical_data():
    """Get historical cauldron level data."""
    data = fetch_api(f"{API_BASE}/api/Data", timeout=30)
    if data:
        return jsonify(data)
    return jsonify({"error": "Failed to fetch historical data"}), 500

@app.route('/api/data-full')
def get_full_historical_data():
    """Get complete historical data with all timestamps and levels."""
    try:
        data = fetch_api(f"{API_BASE}/api/Data", timeout=30)
        if not data or not isinstance(data, list):
            return jsonify({"error": "No data available"}), 500
        
        # Return full dataset for client-side caching
        return jsonify({
            "total_records": len(data),
            "data": data
        })
    except Exception as e:
        print(f"Error getting full data: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/current-levels')
def get_current_levels():
    """Get current potion levels for all cauldrons."""
    try:
        # Fetch historical data
        data = fetch_api(f"{API_BASE}/api/Data", timeout=30)
        if not data or not isinstance(data, list) or len(data) == 0:
            return jsonify({"error": "No data available"}), 500
        
        # Get the most recent timestamp
        latest = data[-1]
        current_levels = latest.get('cauldron_levels', {})
        
        return jsonify({
            "timestamp": latest.get('timestamp'),
            "levels": current_levels
        })
    except Exception as e:
        print(f"Error getting current levels: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/timestamps')
def get_timestamps():
    """Get all available timestamps from historical data."""
    try:
        data = fetch_api(f"{API_BASE}/api/Data", timeout=30)
        if not data or not isinstance(data, list):
            return jsonify({"error": "No data available"}), 500
        
        # Extract just the timestamps
        timestamps = [record.get('timestamp') for record in data if 'timestamp' in record]
        
        return jsonify({
            "timestamps": timestamps,
            "count": len(timestamps)
        })
    except Exception as e:
        print(f"Error getting timestamps: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/levels-at-index/<int:index>')
def get_levels_at_index(index):
    """Get cauldron levels at a specific timestamp index."""
    try:
        data = fetch_api(f"{API_BASE}/api/Data", timeout=30)
        if not data or not isinstance(data, list):
            return jsonify({"error": "No data available"}), 500
        
        if index < 0 or index >= len(data):
            return jsonify({"error": "Index out of range"}), 400
        
        record = data[index]
        
        return jsonify({
            "timestamp": record.get('timestamp'),
            "levels": record.get('cauldron_levels', {}),
            "index": index,
            "total_records": len(data)
        })
    except Exception as e:
        print(f"Error getting levels at index {index}: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/health')
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok", "message": "Brew View is running"})

if __name__ == '__main__':
    print("🔮 Starting Brew View - Potion Flow Monitoring Dashboard")
    print("🌐 Server: http://127.0.0.1:5000/")
    print("-" * 60)
    app.run(debug=True, host='127.0.0.1', port=5000)
