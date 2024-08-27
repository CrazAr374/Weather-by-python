Weather Information Script
Description
This script fetches and displays the current weather information for a specified city using an API. It shows details such as temperature, weather condition, humidity, wind speed, feels like temperature, and the last updated time.

Prerequisites
Python 3.x
requests library
tabulate library
Installation
Clone the repository or download the script file.

Ensure you have Python installed. You can check this by running python --version in your terminal or command prompt.

Install the required libraries using pip:
pip install requests tabulate
Usage
Obtain an API key from a weather service provider like WeatherAPI or any other provider that gives current weather data.

Replace "YOUR PERSONAL API KEY" in the script with your actual API key and modify the URL accordingly.

Example URL format:

url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_PERSONAL_API_KEY&q={city}"
Run the script:
python weather_script.py
Enter the city name when prompted.

The script will display the weather information in a formatted table.

Example
Enter the city: London
+-------------------+-----------------+
| Attribute         | Value           |
+-------------------+-----------------+
| City              | London          |
| Temperature (°C)  | 15.0            |
| Condition         | Partly cloudy   |
| Humidity (%)      | 72              |
| Wind Speed (km/h) | 13.0            |
| Feels Like (°C)   | 15.0            |
| Last Updated      | 2024-08-27 10:00|
+-------------------+-----------------+
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
WeatherAPI for providing the weather data API.
