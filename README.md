# 🔍 Nmap Python Scanner

A lightweight Python script that wraps Nmap to perform fast and customizable network scans from the terminal. Ideal for ethical hacking, network diagnostics, and pentesting labs.

## ⚙️ Features

- Fast port scanning using Nmap (`-T4`, `-F`)
- Single IP or domain scanning
- Custom port ranges (default: 1-1024)
- Clean terminal output
- Easily extendable for banner grabbing or OS detection

## 📦 Requirements

- Python 3.x
- Nmap (must be installed and accessible via CLI)
- [`python-nmap`](https://pypi.org/project/python-nmap/) (`pip install python-nmap`)

## 🧪 Installation

Linux User
git clone https://github.com/b4dcyber/NetworkScanner.git
cd NetworkScanner
python3 -m venv .venv
source .venv/bin/activate
pip install nmap
python scanner.py



Windows User
.venv\Scripts\activate
pip install python-nmap
python scanner.py





# NetworkScanner
# 🔍 Nmap Python Scanner  A basic Python tool that wraps Nmap for quick host and port scans.  ## Features - Port scanning with Nmap - Fast scanning with `-T4` and `-F` - Easy-to-use interface  ## Usage  ```bash python scanner.py
Python 3.x
must install in your pc 
Nmap installed

python-nmap module: pip install python-nmap
