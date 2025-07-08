# Rain Alert

**Rain Alert** is a smart, time-specific weather alert system that goes beyond generic rainfall warnings. Unlike typical weather notifications that lack context, this tool is built to predict rain **during a specific time window** — like your office hours, commute slot, or outdoor events — and sends an SMS alert **only if it's actually relevant** to you.

Built using OpenWeather’s forecast API and Twilio SMS, it automatically checks weather data every day at a pre-scheduled time (e.g., **7:00 AM**) and alerts you **only if rain is expected during your defined hours**, such as 9 AM to 5 PM. This makes it highly useful for working professionals, travelers, or anyone who needs practical, personalized alerts — not just general warnings.

---

## Table of Contents

- [Motivation](#motivation)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [How It Works](#how-it-works)
- [Location Example Used](#location-example-used)
- [Folder Structure](#folder-structure)
- [Output Example](#output-example)
- [Notes](#notes)

---

## Motivation

This project was born out of a simple but frustrating monsoon-season problem:  
> "If I carry an umbrella, it doesn’t rain. If I don’t, it definitely does. Carrying it every day without knowing the forecast felt unnecessary."

Also, checking weather apps early in the morning isn't always feasible due to a busy routine. This tool solves that — by notifying in advance whether carrying an umbrella is actually necessary.

---

## Features

- Checks weather forecast of your area specifically for your defined time window.
- Sends SMS alert only when rain is predicted **during that window**.
- Automatically runs at a scheduled time (e.g., every day at 7 AM).
- Fast, efficient, and requires minimal configuration.

---

## Tech Stack

- Pandas
- Twilio API  
- OpenWeather API  
- Requests  

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/anurag2118/rain-alert.git
cd rain-alert
```

### 2. Install dependencies

```bash
pip install requests twilio
```

### 3. Set environment variables

Make sure you have your API keys set as environment variables:

```bash
export OWM_API_KEY=your_openweather_api_key
export AUTH_TOKEN=your_twilio_auth_token
```

Alternatively, you can hardcode them in the script for testing (not recommended for production).

### 4. Update phone numbers in the script

In the script, replace:

```python
from_ = "your_twilio_number"
to = "your_verified_phone_number"
```

---

## How It Works

1. Script runs every day at a specific time (e.g., 7:00 AM).
2. It fetches forecast data for the next few hours.
3. It filters the forecast based on a **user-defined time window**, like 9 AM to 5 PM.
4. If any rain is predicted during this window (weather code < 700), it sends an SMS alert.
5. The SMS looks like:

```
It is going to rain today. Remember to bring an ☔
```

---

## Location Example Used

```python
"lat": 25.5356,
"lon": 84.8513,
```

This corresponds to IIT Patna, Bihar. You can change these coordinates to get alerts for your own area.

---

## Folder Structure

```
rain-alert/
├── rain_alert.py
└── README.md
```

---

## Output Example

If rain is expected:

```
queued
```

If not, nothing happens and the script exits silently.

---

## Notes

- Twilio trial accounts can only send messages to verified numbers.
- Ensure your OpenWeather API key is valid and not rate-limited.
- Automate script execution daily using crontab (Linux/macOS) or Task Scheduler (Windows).
