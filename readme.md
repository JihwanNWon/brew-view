BREW VIEW - POTION FLOW MONITORING Installation & Usage Guide (Plain Text Version)


## TABLE OF CONTENTS 

Overview

Prerequisites

Installation

Starting the Application

Usage Guide

Features

Troubleshooting

Support & Feedback

========================================

OVERVIEW ======================================== Brew View is a web-based dashboard for monitoring potion flow and cauldron management. It includes interactive maps, 3D visualization, ticket logs, analytics, and route optimization tools.

========================================

PREREQUISITES ========================================

Python 3.7 or higher

pip (Python package installer)

Internet connection (for API access and map tiles)

========================================

INSTALLATION ======================================== Step 1: Navigate to the project directory cd /home/haker/PycharmProjects/brew-view

Step 2: Create a virtual environment (recommended) python3 -m venv .venv

Step 3: Activate the virtual environment On Linux/Mac: source .venv/bin/activate On Windows: .venv\Scripts\activate

Step 4: Install required dependencies pip install -r requirements.txt

========================================

STARTING THE APPLICATION ======================================== Step 1: Ensure you're in the project directory and virtual environment is active Step 2: Run the Flask application python flask_app.py Step 3: Open your web browser and go to: http://localhost:5000 Step 4: To stop the application, press Ctrl+C in the terminal

========================================

USAGE GUIDE ========================================

NAVIGATION TABS:

Map Tab (📍)

Interactive map with cauldron markers

Color-coded capacity indicators

Timeline controls for historical data

"Show" button animates until clicked

3D Visualization Tab (🔮)

3D cauldron network view

Rotate, zoom, pan controls

Particle effects and timeline slider

Ticket Logs Tab (🎫)

View and filter collection tickets

Filter by date, cauldron ID, courier ID, status

Suspicious tickets highlighted in red

Light mode: black text for readability

Cauldron Trends Tab (📈)

Historical charts for cauldrons

Compare multiple cauldrons

Filter by date and cauldron

Analytics Dashboard Tab (📊)

System statistics and health indicators

Courier performance and efficiency metrics

Route Optimization Tab (🗺️)

Calculate efficient collection routes

Distance and time estimates

Visual route display on map

LIGHT MODE TOGGLE:

Click ☀️/🌙 icon in top-right corner

Switches between dark and light themes

Setting persists across sessions

TIMELINE CONTROLS:

Select Year

Select Month

Select Day

Use time slider for hour

Click "Show" to load data

FILTERING DATA:

Use dropdowns to filter cauldrons, couriers, or dates

Multiple selections allowed

Filters apply automatically or via "Apply" button

========================================

FEATURES ========================================

Real-time cauldron monitoring

Leaflet/OpenStreetMap integration

3D visualization with Three.js

Historical data timeline

Ticket logging and filtering

Suspicious activity detection

Route optimization algorithms

Analytics and trend analysis

Light/Dark mode themes

Responsive design

Animated UI elements

========================================

TROUBLESHOOTING ========================================

Problem: Application won't start Solution:

Ensure dependencies are installed: pip install -r requirements.txt

Check Python version: python --version (must be 3.7+)

Verify port 5000 is not in use

Problem: Map tiles not loading Solution:

Check internet connection

Verify firewall allows outbound connections

Problem: API data not loading Solution:

Check internet connection

Verify endpoint: https://hackutd2025.eog.systems

Check browser console (F12) for errors

Problem: Light mode text not visible Solution:

Use updated index.html file

Problem: "Show" button animation not stopping Solution:

Click the "Show" button

Refresh the page if needed

========================================

SUPPORT & FEEDBACK ======================================== For issues, bugs, or feature requests, open an issue on the GitHub repository.

======================================== Happy Brewing! 🧪✨ ========================================
