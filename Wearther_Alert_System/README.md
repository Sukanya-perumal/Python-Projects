Rain Alert Email Notification Script

A Python script that checks the weather forecast for the next few hours using the OpenWeatherMap API. If rain is detected in the forecast, it automatically sends an email alert to your inbox reminding you to bring an umbrella.

Features
* Fetches real-time, 3-hourly weather forecasts.
* Parses weather condition codes to detect rain.
* Sends automated email alerts securely using SMTP and TLS encryption.
* Secures private API keys and login credentials using environment variables.
* .env file example:
    My_EMAIL=your_email@gmail.com
    PASSWORD=your_app_password
    API_KEY=your_openweathermap_api_key
    
