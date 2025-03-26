
║   CURRENCY CONVERTER APP     ║


✦ Features ✦
• Convert between USD, EUR, GBP, JPY,RUB,AMD
• Real-time exchange rates
• Clean graphical interface
• Input validation
• Error handling

══════════════════════════════════════════════════════════════

✦ Installation ✦

1. REQUIREMENTS:
   - Python 3.7+
   - pip package manager

2. SETUP:
   [1] Create virtual environment:
       python -m venv venv
       venv\Scripts\activate  (Windows)
       source venv/bin/activate  (Mac/Linux)

   [2] Install dependencies:
       pip install PyQt6 requests

   [3] Run application:
       python currency_converter.py

══════════════════════════════════════════════════════════════

✦ How To Use ✦

[1] SELECT CURRENCIES:
    • First dropdown - Convert FROM
    • Second dropdown - Convert TO

[2] ENTER AMOUNT:
    • Type numerical value (e.g. 100)
    • Only positive numbers accepted

[3] CONVERT:
    • Click "Convert!" button
    • View result in format:
      "100 USD = 85 EUR"

══════════════════════════════════════════════════════════════

✦ API Information ✦

• Uses ExchangeRate-API (free tier)
• Default key included (rate-limited)
• For production use:
  - Get free key at: exchangerate-api.com
  - Replace in code:
    .../v6/YOUR_KEY_HERE/latest/...

══════════════════════════════════════════════════════════════

✦ Troubleshooting ✦

⚠ "Failed to fetch data":
   → Check internet connection
   → Verify API key
   → Try again later

⚠ "Invalid amount":
   → Use numbers only
   → No negative values

⚠ App won't start:
   → Check Python version
   → Verify PyQt6 installed

══════════════════════════════════════════════════════════════

✦ About ✦

Developed with PyQt6 and Python
For educational purposes
MIT License.

══════════════════════════════════════════════════════════════
