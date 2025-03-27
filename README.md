# NTS-NAT-Application-Monitor: Automated Portal Checker & Email Alert System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A Python script that automates checking the **NTS Portal** for the availability of the **National Aptitude Test (NAT 2025-IV)** application. Sends an email alert when the application opens.

---

## 🚀 Features
- **Automated Login**: Logs into the NTS portal using your CNIC and password.
- **Real-Time Monitoring**: Scrapes the portal to check for the NAT 2025-IV application status.
- **Email Notifications**: Sends an email via Gmail when the application becomes available.
- **Headless Mode Support**: Optional configuration for running in the background.
- **Robust Waits**: Uses `WebDriverWait` to handle dynamic page elements.

---

## ⚙️ Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/NTS-NAT-Application-Monitor.git
   cd NTS-NAT-Application-Monitor
