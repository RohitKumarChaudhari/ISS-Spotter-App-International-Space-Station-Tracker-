# 🛰️ ISS Spotter App (International Space Station Tracker)

This simple Python project uses a public API to check when the **International Space Station (ISS)** is passing over your location. It sends a notification or prints a message if the ISS is overhead **and** it's dark outside — the perfect time to spot it in the sky!

---

## 🌐 How It Works

- Uses **Open Notify API** to get the ISS's current position.
- Uses **Sunrise-Sunset API** to determine if it's dark at your location.
- If both conditions are met:
  - The program sends an email.
  - It runs in a loop to keep checking every 60 seconds.

---

## ⚙️ Features

- Real-time ISS tracking.
- Accurate day/night detection based on your location.

---

## 🧪 Technologies Used

- Python
- `requests` module for APIs
- `datetime` module

---

## 📍 Set Your Location

In the code, set your latitude and longitude to your location:

```python
MY_LAT = 26.2  # Example: Siwan, Bihar
MY_LONG = 84.4
```

📦 Requirements
- Python 3.x
- requests library

Install using pip: 
```bash 
pip install requests 
```

🚀 How to Run
```bash
python main.py
```
Make sure you're connected to the internet so the APIs can work properly.

📚 API Sources
- [Open Notify - ISS Location API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)
- [Sunrise-Sunset API](https://sunrise-sunset.org/api)

👨‍💻 Made With Curiosity & Python by Rohit

