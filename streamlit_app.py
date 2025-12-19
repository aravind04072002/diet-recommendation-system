"""
Streamlit Cloud Entry Point
This file redirects to the main application in Streamlit_Frontend/Hello.py
"""

import sys
import os

# Add Streamlit_Frontend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Streamlit_Frontend'))

# Change to Streamlit_Frontend directory
os.chdir(os.path.join(os.path.dirname(__file__), 'Streamlit_Frontend'))

# Import and run the main app
exec(open('Hello.py').read())
