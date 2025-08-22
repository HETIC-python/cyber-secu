# Configuration Template for Ransomware Simulation
# Copy this file to config.py and fill in your own values

# SMTP Configuration for sending emails
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USERNAME = "your_email@example.com"
EMAIL_PASSWORD = "your_app_password_here"

# Test Email Addresses (use your own test emails)
TARGET_EMAIL = "target@example.com"
SENDER_EMAIL = "sender@example.com"

# Server Configuration (for hosting malware files)
SERVER_URL = "https://your-server.example.com"
MALWARE_FILE_NAME = "bienveillance.exe"

# Security Notes:
# 1. Never use real production email accounts
# 2. Only use test email addresses you own
# 3. Use Gmail App Passwords, not regular passwords
# 4. This is for educational purposes only
# 5. Always inform participants this is a simulation