API_KEY = "8ae6fe4fcfe30feea584b5a8fbd3ac3e"
CITY_CHECK_BY_IP_URL = "http://ipgeobase.ru/"
GENERAL_URL = "https://api.openweathermap.org/data/2.5/weather?q="
WEATHER_CHECK_URL = "https://api.openweathermap.org/data/2.5/onecall?lat="
GET_COORDINATES_FOR_CITY_URL = "https://nominatim.openstreetmap.org/search?city="
HEADER = "'User-Agent1': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'"
city_data = {
    "city": None,
    "lat": 0,
    "lon": 0
}
weather_data = {
    "lat": 0,
    "lon": 0,
    "timezone": None,
    "timezone_offset": 0,
    "current": {
        "dt": 0,
        "sunrise": 0,
        "sunset": 0,
        "temp": 0,
        "feels_like": 0,
        "pressure": 0,
        "humidity": 0,
        "dew_point": 0,
        "uvi": 0,
        "clouds": 0,
        "visibility": 0,
        "wind_speed": 0,
        "wind_deg": 0,
        "weather": [
            {
                "id": 0,
                "main": None,
                "description": None,
                "icon": "02d"
            }
        ]
    },
    "minutely": [
        {
            "dt": 1598719620,
            "precipitation": 0
        },
        {
            "dt": 1598719680,
            "precipitation": 0
        },
        {
            "dt": 1598719740,
            "precipitation": 0
        },
        {
            "dt": 1598719800,
            "precipitation": 0
        },
        {
            "dt": 1598719860,
            "precipitation": 0
        },
        {
            "dt": 1598719920,
            "precipitation": 0
        },
        {
            "dt": 1598719980,
            "precipitation": 0
        },
        {
            "dt": 1598720040,
            "precipitation": 0
        },
        {
            "dt": 1598720100,
            "precipitation": 0
        },
        {
            "dt": 1598720160,
            "precipitation": 0
        },
        {
            "dt": 1598720220,
            "precipitation": 0
        },
        {
            "dt": 1598720280,
            "precipitation": 0
        },
        {
            "dt": 1598720340,
            "precipitation": 0
        },
        {
            "dt": 1598720400,
            "precipitation": 0
        },
        {
            "dt": 1598720460,
            "precipitation": 0
        },
        {
            "dt": 1598720520,
            "precipitation": 0
        },
        {
            "dt": 1598720580,
            "precipitation": 0
        },
        {
            "dt": 1598720640,
            "precipitation": 0
        },
        {
            "dt": 1598720700,
            "precipitation": 0
        },
        {
            "dt": 1598720760,
            "precipitation": 0
        },
        {
            "dt": 1598720820,
            "precipitation": 0
        },
        {
            "dt": 1598720880,
            "precipitation": 0
        },
        {
            "dt": 1598720940,
            "precipitation": 0
        },
        {
            "dt": 1598721000,
            "precipitation": 0
        },
        {
            "dt": 1598721060,
            "precipitation": 0
        },
        {
            "dt": 1598721120,
            "precipitation": 0
        },
        {
            "dt": 1598721180,
            "precipitation": 0
        },
        {
            "dt": 1598721240,
            "precipitation": 0
        },
        {
            "dt": 1598721300,
            "precipitation": 0
        },
        {
            "dt": 1598721360,
            "precipitation": 0
        },
        {
            "dt": 1598721420,
            "precipitation": 0
        },
        {
            "dt": 1598721480,
            "precipitation": 0
        },
        {
            "dt": 1598721540,
            "precipitation": 0
        },
        {
            "dt": 1598721600,
            "precipitation": 0
        },
        {
            "dt": 1598721660,
            "precipitation": 0
        },
        {
            "dt": 1598721720,
            "precipitation": 0
        },
        {
            "dt": 1598721780,
            "precipitation": 0
        },
        {
            "dt": 1598721840,
            "precipitation": 0
        },
        {
            "dt": 1598721900,
            "precipitation": 0
        },
        {
            "dt": 1598721960,
            "precipitation": 0
        },
        {
            "dt": 1598722020,
            "precipitation": 0
        },
        {
            "dt": 1598722080,
            "precipitation": 0
        },
        {
            "dt": 1598722140,
            "precipitation": 0
        },
        {
            "dt": 1598722200,
            "precipitation": 0
        },
        {
            "dt": 1598722260,
            "precipitation": 0
        },
        {
            "dt": 1598722320,
            "precipitation": 0
        },
        {
            "dt": 1598722380,
            "precipitation": 0
        },
        {
            "dt": 1598722440,
            "precipitation": 0
        },
        {
            "dt": 1598722500,
            "precipitation": 0
        },
        {
            "dt": 1598722560,
            "precipitation": 0
        },
        {
            "dt": 1598722620,
            "precipitation": 0
        },
        {
            "dt": 1598722680,
            "precipitation": 0
        },
        {
            "dt": 1598722740,
            "precipitation": 0
        },
        {
            "dt": 1598722800,
            "precipitation": 0
        },
        {
            "dt": 1598722860,
            "precipitation": 0
        },
        {
            "dt": 1598722920,
            "precipitation": 0
        },
        {
            "dt": 1598722980,
            "precipitation": 0
        },
        {
            "dt": 1598723040,
            "precipitation": 0
        },
        {
            "dt": 1598723100,
            "precipitation": 0
        },
        {
            "dt": 1598723160,
            "precipitation": 0
        },
        {
            "dt": 1598723220,
            "precipitation": 0
        }
    ],
    "hourly": [
        {
            "dt": 1598716800,
            "temp": 25.92,
            "feels_like": 23.82,
            "pressure": 1013,
            "humidity": 36,
            "dew_point": 9.72,
            "clouds": 21,
            "visibility": 10000,
            "wind_speed": 2.95,
            "wind_deg": 162,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "небольшая облачность",
                    "icon": "02d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598720400,
            "temp": 24.59,
            "feels_like": 22.71,
            "pressure": 1013,
            "humidity": 42,
            "dew_point": 10.84,
            "clouds": 19,
            "visibility": 10000,
            "wind_speed": 3.07,
            "wind_deg": 159,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "небольшая облачность",
                    "icon": "02n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598724000,
            "temp": 23.33,
            "feels_like": 21.49,
            "pressure": 1014,
            "humidity": 47,
            "dew_point": 11.39,
            "clouds": 27,
            "visibility": 10000,
            "wind_speed": 3.25,
            "wind_deg": 158,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "переменная облачность",
                    "icon": "03n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598727600,
            "temp": 22.2,
            "feels_like": 20.23,
            "pressure": 1014,
            "humidity": 51,
            "dew_point": 11.59,
            "clouds": 95,
            "visibility": 10000,
            "wind_speed": 3.51,
            "wind_deg": 157,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598731200,
            "temp": 21.4,
            "feels_like": 19.3,
            "pressure": 1014,
            "humidity": 53,
            "dew_point": 11.44,
            "clouds": 53,
            "visibility": 10000,
            "wind_speed": 3.63,
            "wind_deg": 160,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "облачно с прояснениями",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598734800,
            "temp": 21.25,
            "feels_like": 18.41,
            "pressure": 1014,
            "humidity": 53,
            "dew_point": 11.4,
            "clouds": 35,
            "visibility": 10000,
            "wind_speed": 4.63,
            "wind_deg": 172,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "переменная облачность",
                    "icon": "03n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598738400,
            "temp": 21.59,
            "feels_like": 17.95,
            "pressure": 1014,
            "humidity": 49,
            "dew_point": 10.57,
            "clouds": 27,
            "visibility": 10000,
            "wind_speed": 5.42,
            "wind_deg": 195,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "переменная облачность",
                    "icon": "03n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598742000,
            "temp": 21.3,
            "feels_like": 17.51,
            "pressure": 1015,
            "humidity": 48,
            "dew_point": 9.93,
            "clouds": 22,
            "visibility": 10000,
            "wind_speed": 5.42,
            "wind_deg": 204,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "небольшая облачность",
                    "icon": "02n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598745600,
            "temp": 20.82,
            "feels_like": 16.96,
            "pressure": 1015,
            "humidity": 47,
            "dew_point": 9.33,
            "clouds": 18,
            "visibility": 10000,
            "wind_speed": 5.23,
            "wind_deg": 208,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "небольшая облачность",
                    "icon": "02n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598749200,
            "temp": 20.4,
            "feels_like": 16.73,
            "pressure": 1015,
            "humidity": 47,
            "dew_point": 8.95,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.82,
            "wind_deg": 208,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598752800,
            "temp": 19.89,
            "feels_like": 16.43,
            "pressure": 1015,
            "humidity": 48,
            "dew_point": 8.86,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.47,
            "wind_deg": 208,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598756400,
            "temp": 19.56,
            "feels_like": 16.08,
            "pressure": 1015,
            "humidity": 48,
            "dew_point": 8.46,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.39,
            "wind_deg": 203,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598760000,
            "temp": 19.35,
            "feels_like": 15.94,
            "pressure": 1015,
            "humidity": 49,
            "dew_point": 8.51,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.33,
            "wind_deg": 200,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598763600,
            "temp": 20.38,
            "feels_like": 16.98,
            "pressure": 1015,
            "humidity": 48,
            "dew_point": 9.19,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.55,
            "wind_deg": 198,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598767200,
            "temp": 21.92,
            "feels_like": 18.62,
            "pressure": 1015,
            "humidity": 46,
            "dew_point": 10.1,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.69,
            "wind_deg": 196,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598770800,
            "temp": 23.9,
            "feels_like": 20.89,
            "pressure": 1016,
            "humidity": 44,
            "dew_point": 10.98,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.72,
            "wind_deg": 193,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598774400,
            "temp": 25.91,
            "feels_like": 22.86,
            "pressure": 1015,
            "humidity": 40,
            "dew_point": 11.53,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.93,
            "wind_deg": 189,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598778000,
            "temp": 27.76,
            "feels_like": 24.59,
            "pressure": 1015,
            "humidity": 37,
            "dew_point": 11.77,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 5.29,
            "wind_deg": 188,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598781600,
            "temp": 29.21,
            "feels_like": 25.66,
            "pressure": 1015,
            "humidity": 33,
            "dew_point": 11.73,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 5.64,
            "wind_deg": 189,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598785200,
            "temp": 30.13,
            "feels_like": 26.48,
            "pressure": 1015,
            "humidity": 31,
            "dew_point": 11.63,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 5.72,
            "wind_deg": 190,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598788800,
            "temp": 30.6,
            "feels_like": 27.07,
            "pressure": 1015,
            "humidity": 31,
            "dew_point": 11.59,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 5.72,
            "wind_deg": 188,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598792400,
            "temp": 30.76,
            "feels_like": 27.41,
            "pressure": 1015,
            "humidity": 31,
            "dew_point": 11.72,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 5.52,
            "wind_deg": 187,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598796000,
            "temp": 30.42,
            "feels_like": 27.49,
            "pressure": 1014,
            "humidity": 32,
            "dew_point": 12.33,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 5,
            "wind_deg": 184,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598799600,
            "temp": 29.46,
            "feels_like": 27.12,
            "pressure": 1014,
            "humidity": 35,
            "dew_point": 12.66,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.4,
            "wind_deg": 182,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598803200,
            "temp": 27.74,
            "feels_like": 25.78,
            "pressure": 1014,
            "humidity": 38,
            "dew_point": 12.44,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 3.74,
            "wind_deg": 178,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598806800,
            "temp": 26.15,
            "feels_like": 24.01,
            "pressure": 1014,
            "humidity": 39,
            "dew_point": 11.49,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 3.56,
            "wind_deg": 176,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598810400,
            "temp": 25.45,
            "feels_like": 22.96,
            "pressure": 1014,
            "humidity": 38,
            "dew_point": 10.44,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 3.65,
            "wind_deg": 175,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598814000,
            "temp": 24.93,
            "feels_like": 22.16,
            "pressure": 1014,
            "humidity": 37,
            "dew_point": 9.52,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 3.73,
            "wind_deg": 176,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598817600,
            "temp": 24.36,
            "feels_like": 21.45,
            "pressure": 1015,
            "humidity": 37,
            "dew_point": 8.78,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 3.74,
            "wind_deg": 173,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598821200,
            "temp": 23.74,
            "feels_like": 20.45,
            "pressure": 1015,
            "humidity": 36,
            "dew_point": 8.08,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 3.95,
            "wind_deg": 174,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598824800,
            "temp": 23.4,
            "feels_like": 19.75,
            "pressure": 1015,
            "humidity": 36,
            "dew_point": 7.79,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.37,
            "wind_deg": 187,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598828400,
            "temp": 23.05,
            "feels_like": 19.65,
            "pressure": 1014,
            "humidity": 38,
            "dew_point": 8.31,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.17,
            "wind_deg": 197,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598832000,
            "temp": 22.62,
            "feels_like": 19.18,
            "pressure": 1014,
            "humidity": 39,
            "dew_point": 8.28,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.24,
            "wind_deg": 189,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598835600,
            "temp": 22.01,
            "feels_like": 18.66,
            "pressure": 1014,
            "humidity": 41,
            "dew_point": 8.19,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.17,
            "wind_deg": 192,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598839200,
            "temp": 21.57,
            "feels_like": 18.13,
            "pressure": 1013,
            "humidity": 41,
            "dew_point": 8,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.17,
            "wind_deg": 193,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598842800,
            "temp": 21.11,
            "feels_like": 17.64,
            "pressure": 1013,
            "humidity": 42,
            "dew_point": 7.82,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.19,
            "wind_deg": 189,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598846400,
            "temp": 20.9,
            "feels_like": 17.42,
            "pressure": 1013,
            "humidity": 43,
            "dew_point": 7.88,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.25,
            "wind_deg": 190,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598850000,
            "temp": 21.97,
            "feels_like": 18.3,
            "pressure": 1013,
            "humidity": 41,
            "dew_point": 8.14,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.62,
            "wind_deg": 193,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598853600,
            "temp": 23.88,
            "feels_like": 19.92,
            "pressure": 1013,
            "humidity": 36,
            "dew_point": 8.07,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.96,
            "wind_deg": 196,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598857200,
            "temp": 25.95,
            "feels_like": 21.57,
            "pressure": 1013,
            "humidity": 31,
            "dew_point": 7.95,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 5.42,
            "wind_deg": 192,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598860800,
            "temp": 28.06,
            "feels_like": 23.28,
            "pressure": 1013,
            "humidity": 27,
            "dew_point": 7.59,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 5.92,
            "wind_deg": 191,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598864400,
            "temp": 29.61,
            "feels_like": 24.55,
            "pressure": 1013,
            "humidity": 24,
            "dew_point": 7.49,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 6.19,
            "wind_deg": 195,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598868000,
            "temp": 30.61,
            "feels_like": 25.87,
            "pressure": 1012,
            "humidity": 24,
            "dew_point": 7.87,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 6.01,
            "wind_deg": 199,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598871600,
            "temp": 31.35,
            "feels_like": 26.77,
            "pressure": 1012,
            "humidity": 23,
            "dew_point": 8.13,
            "clouds": 1,
            "visibility": 10000,
            "wind_speed": 5.78,
            "wind_deg": 198,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598875200,
            "temp": 31.72,
            "feels_like": 27.23,
            "pressure": 1012,
            "humidity": 23,
            "dew_point": 8.53,
            "clouds": 7,
            "visibility": 10000,
            "wind_speed": 5.76,
            "wind_deg": 192,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598878800,
            "temp": 31.74,
            "feels_like": 27.62,
            "pressure": 1011,
            "humidity": 24,
            "dew_point": 9.1,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 5.46,
            "wind_deg": 195,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598882400,
            "temp": 31.41,
            "feels_like": 28.21,
            "pressure": 1011,
            "humidity": 26,
            "dew_point": 10.06,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 4.47,
            "wind_deg": 198,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1598886000,
            "temp": 30.34,
            "feels_like": 27.69,
            "pressure": 1010,
            "humidity": 29,
            "dew_point": 10.72,
            "clouds": 16,
            "visibility": 10000,
            "wind_speed": 3.96,
            "wind_deg": 199,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "небольшая облачность",
                    "icon": "02d"
                }
            ],
            "pop": 0
        }
    ],
    "daily": [
        {
            "dt": 0,
            "sunrise": 0,
            "sunset": 0,
            "temp": {
                "day": 0,
                "min": 0,
                "max": 0,
                "night": 0,
                "eve": 0,
                "morn": 0
            },
            "feels_like": {
                "day": 0,
                "night": 0,
                "eve": 0,
                "morn": 0
            },
            "pressure": 0,
            "humidity": 0,
            "dew_point": 0,
            "wind_speed": 0,
            "wind_deg": 0,
            "weather": [
                {
                    "id": 0,
                    "main": "Clouds",
                    "description": "небольшая облачность",
                    "icon": "02d"
                }
            ],
            "clouds": 0,
            "pop": 0,
            "uvi": 0
        },
        {
            "dt": 1598778000,
            "sunrise": 1598756987,
            "sunset": 1598806057,
            "temp": {
                "day": 27.76,
                "min": 19.61,
                "max": 30.6,
                "night": 23.74,
                "eve": 29.46,
                "morn": 19.61
            },
            "feels_like": {
                "day": 24.59,
                "night": 20.45,
                "eve": 27.12,
                "morn": 16.14
            },
            "pressure": 1015,
            "humidity": 37,
            "dew_point": 11.77,
            "wind_speed": 5.29,
            "wind_deg": 188,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "clouds": 0,
            "pop": 0,
            "uvi": 5.54
        },
        {
            "dt": 1598864400,
            "sunrise": 1598843478,
            "sunset": 1598892328,
            "temp": {
                "day": 29.61,
                "min": 21.11,
                "max": 31.72,
                "night": 23.54,
                "eve": 30.34,
                "morn": 21.11
            },
            "feels_like": {
                "day": 24.55,
                "night": 22.38,
                "eve": 27.69,
                "morn": 17.64
            },
            "pressure": 1013,
            "humidity": 24,
            "dew_point": 7.49,
            "wind_speed": 6.19,
            "wind_deg": 195,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "clouds": 0,
            "pop": 0.03,
            "uvi": 5.32
        },
        {
            "dt": 1598950800,
            "sunrise": 1598929969,
            "sunset": 1598978599,
            "temp": {
                "day": 24.03,
                "min": 18.09,
                "max": 27.08,
                "night": 18.09,
                "eve": 25.2,
                "morn": 18.85
            },
            "feels_like": {
                "day": 22.46,
                "night": 15.97,
                "eve": 23.2,
                "morn": 17.77
            },
            "pressure": 1012,
            "humidity": 50,
            "dew_point": 13.28,
            "wind_speed": 3.55,
            "wind_deg": 23,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "ясно",
                    "icon": "01d"
                }
            ],
            "clouds": 9,
            "pop": 0,
            "uvi": 4.9
        },
        {
            "dt": 1599037200,
            "sunrise": 1599016460,
            "sunset": 1599064870,
            "temp": {
                "day": 22.23,
                "min": 15.43,
                "max": 24.74,
                "night": 17.15,
                "eve": 22.76,
                "morn": 15.43
            },
            "feels_like": {
                "day": 19.75,
                "night": 13.3,
                "eve": 19.75,
                "morn": 13.05
            },
            "pressure": 1015,
            "humidity": 62,
            "dew_point": 14.72,
            "wind_speed": 5.64,
            "wind_deg": 38,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "облачно с прояснениями",
                    "icon": "04d"
                }
            ],
            "clouds": 78,
            "pop": 0,
            "uvi": 5.08
        },
        {
            "dt": 1599123600,
            "sunrise": 1599102951,
            "sunset": 1599151139,
            "temp": {
                "day": 18.77,
                "min": 13.61,
                "max": 20.86,
                "night": 14.16,
                "eve": 19.43,
                "morn": 13.61
            },
            "feels_like": {
                "day": 14.03,
                "night": 9.99,
                "eve": 15,
                "morn": 9.31
            },
            "pressure": 1024,
            "humidity": 44,
            "dew_point": 6.37,
            "wind_speed": 5.54,
            "wind_deg": 51,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "облачно с прояснениями",
                    "icon": "04d"
                }
            ],
            "clouds": 71,
            "pop": 0,
            "uvi": 5.08
        },
        {
            "dt": 1599210000,
            "sunrise": 1599189442,
            "sunset": 1599237409,
            "temp": {
                "day": 16.83,
                "min": 11.7,
                "max": 19.29,
                "night": 13.97,
                "eve": 18.57,
                "morn": 11.7
            },
            "feels_like": {
                "day": 12.04,
                "night": 10.17,
                "eve": 14.02,
                "morn": 7.32
            },
            "pressure": 1029,
            "humidity": 44,
            "dew_point": 4.55,
            "wind_speed": 5.1,
            "wind_deg": 65,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04d"
                }
            ],
            "clouds": 100,
            "pop": 0,
            "uvi": 5.26
        },
        {
            "dt": 1599296400,
            "sunrise": 1599275932,
            "sunset": 1599323677,
            "temp": {
                "day": 16.86,
                "min": 11.2,
                "max": 18.74,
                "night": 13.34,
                "eve": 18.26,
                "morn": 11.2
            },
            "feels_like": {
                "day": 11.9,
                "night": 9.13,
                "eve": 13.78,
                "morn": 7.64
            },
            "pressure": 1025,
            "humidity": 37,
            "dew_point": 2.36,
            "wind_speed": 4.71,
            "wind_deg": 78,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04d"
                }
            ],
            "clouds": 100,
            "pop": 0,
            "uvi": 5.24
        }
    ]
}
