### Brew View — Potion Flow Monitoring

A web-based dashboard for monitoring potion flow and cauldron management. Brew View provides an interactive map, 3D visualization, ticket logs, analytics, and route optimization tools to monitor cauldron capacity, detect suspicious activity, and optimize collection routes.

---

### Table of Contents
- Overview
- Prerequisites
- Installation
- Start the Application
- Usage Guide
  - Navigation
  - Timeline Controls
  - Filtering Data
  - Light Mode Toggle
- Features
- Troubleshooting
- Support and Feedback

---

### Overview
Brew View is a Flask-based dashboard for real-time and historical monitoring of cauldron networks. Key capabilities include map-based monitoring, Three.js 3D visualizations, ticket logging and filtering, suspicious activity highlighting, analytics, and route optimization.

---

### Prerequisites
- **Python** 3.7 or higher  
- **pip3** (Python package installer)  
- **Internet connection** for API access and map tiles

---

### Installation
1. Open a terminal and navigate to the project directory  
   ```
   cd /path/to/PycharmProjects/brew-view
   ```
2. Create a virtual environment (recommended)  
   ```
   python3 -m venv .venv
   ```
3. Activate the virtual environment  
   - On Linux / macOS:  
     ```
     source .venv/bin/activate
     ```
   - On Windows:  
     ```
     .venv\Scripts\activate
     ```
4. Install required dependencies  
   ```
   pip3 install -r requirements.txt
   ```

---

### Start the Application
1. Ensure you are in the project directory and the virtual environment is active  
2. Run the Flask app  
   ```
   python3 flask_app.py
   ```
3. Open your browser and navigate to:  
   ```
   http://localhost:5000
   ```
4. To stop the server press **Ctrl+C** in the terminal

---

### Usage Guide

#### Navigation
- **Map Tab (Default)**  
  - Interactive map showing cauldron locations  
  - Color-coded markers for capacity levels  
  - Timeline controls for historical playback  
  - Date/time selection (year, month, day, hour)  
  - Click **Show** to display selected data on the map  
  - The **Show** button has a wiggle animation until first click

- **3D Visualization Tab**  
  - Three-dimensional view of the cauldron network  
  - Rotate, zoom, and pan controls  
  - Animated particle effects  
  - Timeline controls for temporal data

- **Ticket Logs Tab**  
  - View collection tickets with filters for date range, cauldron ID, courier ID, and status (Normal/Suspicious)  
  - Sortable columns and ticket statistics  
  - Suspicious tickets highlighted in red  
  - Light mode ensures text remains readable

- **Cauldron Trends Tab**  
  - Historical trend charts per cauldron  
  - Multi-cauldron comparison and capacity-over-time visualizations  
  - Date and cauldron filters

- **Analytics Dashboard Tab**  
  - System statistics, collection efficiency, courier performance, and health indicators

- **Route Optimization Tab**  
  - Generate optimized collection routes between cauldrons  
  - Distance and time estimates with visual route display on the map

#### Timeline Controls
1. Select **Year** from the dropdown  
2. Select **Month** from the dropdown  
3. Select **Day** from the dropdown  
4. Use the **time slider** to select a specific hour  
5. Click **Show** to load and display the data

#### Filtering Data
- Use dropdown filters in Ticket Logs and Trends to select cauldrons, couriers, and date ranges  
- Multiple selections are supported  
- Filters apply either automatically or when you click **Apply**, depending on the UI context

#### Light Mode Toggle
- Click the theme toggle button in the top-right corner to switch between **Dark** and **Light** themes  
- Theme selection persists across sessions

---

### Features
- **Real-time cauldron monitoring**  
- **Interactive Leaflet/OpenStreetMap** integration  
- **3D visualization** using Three.js  
- **Historical data timeline** and playback  
- **Ticket logging and advanced filtering**  
- **Suspicious activity detection** with highlighted tickets  
- **Route optimization algorithms** and visual routes  
- **Analytics and trend analysis**  
- **Light/Dark themes** with persistent setting  
- **Responsive design** for desktop and mobile  
- **Animated UI elements** for better discoverability

---

### Troubleshooting

- Problem: **Application won't start**  
  - Ensure dependencies are installed: `pip install -r requirements.txt`  
  - Check Python version: `python --version` (must be 3.7+)  
  - Verify port 5000 is free

- Problem: **Map tiles not loading**  
  - Check internet connection  
  - Verify firewall or outbound rules allow map tile requests

- Problem: **API data not loading**  
  - Check internet connection  
  - Verify API endpoint accessibility (example endpoint used by the project)  
  - Open the browser console (F12) and inspect network or JS errors

- Problem: **Light mode text not visible**  
  - Update to the latest `index.html` provided in the repository

- Problem: **Show button animation not stopping**  
  - Click the **Show** button once to stop the wiggle; refresh the page if it persists

---

### Support and Feedback
For issues, bugs, or feature requests please open an issue in the project GitHub repository.

---

Happy Brewing and safe cauldron handling!
