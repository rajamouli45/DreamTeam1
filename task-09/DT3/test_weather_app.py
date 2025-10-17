from unittest.mock import patch
from weather_app import get_weather

@patch("weather_app.requests.get")
def test_get_weather_valid_city(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "name": "London",
        "sys": {"country": "GB"},
        "main": {"temp": 20, "humidity": 65},
        "weather": [{"description": "clear sky"}]
    }


    result = get_weather("London")


    assert result["city"] == "London"
    assert result["country"] == "GB"
    assert result["temp"] == 20
    assert result["humidity"] == 65
    assert result["description"] == "clear sky"


@patch("weather_app.requests.get")
def test_get_weather_invalid_city(mock_get):

    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = {
        "message": "city not found"
    }

    result = get_weather("FakeCity123")

    
    assert result is None
