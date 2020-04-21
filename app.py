import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    """Render website's home page."""
    return 'Hello World!'
if __name__ == '__main__':
    app.run(debug="True")
    
#import streamlit as st
#st.write('Hello, world!!')
