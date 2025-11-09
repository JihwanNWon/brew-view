================================================================================
                        BREW VIEW - POTION FLOW MONITORING
                              Installation & Usage Guide
================================================================================

TABLE OF CONTENTS
-----------------
1. Overview
2. Prerequisites
3. Installation
4. Starting the Application
5. Usage Guide
6. Features
7. Troubleshooting


1. OVERVIEW
-----------
Brew View is a web-based dashboard for monitoring potion flow and cauldron
management. It provides interactive maps, 3D visualization, ticket logs,
analytics, and route optimization tools.


2. PREREQUISITES
----------------
- Python 3.7 or higher
- pip (Python package installer)
- Internet connection (for API access and map tiles)


3. INSTALLATION
---------------
Step 1: Navigate to the project directory
    cd /home/haker/PycharmProjects/brew-view

Step 2: Create a virtual environment (recommended)
    python3 -m venv .venv

Step 3: Activate the virtual environment
    # On Linux/Mac:
    source .venv/bin/activate

    # On Windows:
    .venv\Scripts\activate

Step 4: Install required dependencies
    pip install -r requirements.txt


4. STARTING THE APPLICATION
----------------------------
Step 1: Ensure you're in the project directory and virtual environment is active

Step 2: Run the Flask application
    python flask_app.py

Step 3: Open your web browser and navigate to:
    http://localhost:5000

Step 4: To stop the application, press Ctrl+C in the terminal


5. USAGE GUIDE
--------------

NAVIGATION:
-----------
The application has multiple tabs accessible from the top navigation bar:

📍 Map Tab (Default)
    - Interactive map showing cauldron locations
    - Color-coded markers indicate capacity levels
    - Timeline controls for historical data viewing
    - Date/time selection with year, month, day, and hour controls
    - Click "Show" button to display selected data on map
    - Wiggle animation on "Show" button prompts you to click it (stops after first click)

🔮 3D Visualization Tab
    - Three-dimensional view of the cauldron network
    - Interactive 3D controls (rotate, zoom, pan)
    - Animated particle effects
    - Timeline controls for temporal data

🎫 Ticket Logs Tab
    - View all collection tickets
    - Filter by:
        * Date range
        * Cauldron ID
        * Courier ID
        * Status (Normal/Suspicious)
    - Sort by various columns
    - Displays ticket statistics
    - Suspicious tickets highlighted in red
    - Light mode: Text displays in black for readability

📈 Cauldron Trends Tab
    - Historical trend charts for individual cauldrons
    - Multi-cauldron comparison
    - Capacity over time visualization
    - Filtering options by date and cauldron

📊 Analytics Dashboard Tab
    - Comprehensive system statistics
    - Collection efficiency metrics
    - Courier performance data
    - System health indicators

🗺️ Route Optimization Tab
    - Optimize collection routes
    - Calculate efficient paths between cauldrons
    - Distance and time estimates
    - Visual route display on map


LIGHT MODE TOGGLE:
------------------
- Click the theme toggle button (☀️/🌙) in the top-right corner
- Switches between dark and light themes
- Setting persists across sessions


TIMELINE CONTROLS:
------------------
1. Select Year from dropdown
2. Select Month from dropdown
3. Select Day from dropdown
4. Use time slider to select specific hour
5. Click the "Show" button to load and display data


FILTERING DATA:
---------------
In Ticket Logs and Trends tabs:
- Use dropdown filters to select specific cauldrons, couriers, or date ranges
- Multiple selections allowed in dropdowns
- Changes apply automatically or on clicking "Apply"


6. FEATURES
-----------
✓ Real-time cauldron monitoring
✓ Interactive Leaflet/OpenStreetMap integration
✓ 3D visualization with Three.js
✓ Historical data timeline
✓ Ticket logging and filtering
✓ Suspicious activity detection
✓ Route optimization algorithms
✓ Analytics and trend analysis
✓ Light/Dark mode themes
✓ Responsive design
✓ Animated UI elements


7. TROUBLESHOOTING
------------------

Problem: Application won't start
Solution:
    - Ensure all dependencies are installed: pip install -r requirements.txt
    - Check Python version: python --version (must be 3.7+)
    - Verify port 5000 is not in use by another application

Problem: Map tiles not loading
Solution:
    - Check internet connection
    - Verify firewall settings allow outbound connections

Problem: API data not loading
Solution:
    - Check internet connection
    - Verify API endpoint is accessible: https://hackutd2025.eog.systems
    - Check browser console for errors (F12)

Problem: Light mode text not visible
Solution:
    - This has been fixed in the latest version
    - Ensure you're using the updated index.html file

Problem: Show button animation not stopping
Solution:
    - Click the "Show" button to stop the wiggle animation
    - Refresh the page if animation persists


SUPPORT & FEEDBACK
------------------
For issues, bugs, or feature requests, please open an issue on the
project's GitHub repository.


================================================================================
                              Happy Brewing! 🧪✨
================================================================================
