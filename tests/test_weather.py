"""
Test cases:
1. City found
2. City not found
3. None input
"""

from unittest.mock import Mock, patch
from scripts.weather import get_weather


def test_get_weather(capsys):
    mock_json = {
        "main": {"temp": 22.5},
        "weather": [{"description": "sunny"}],
        "name": "London",
    }
    with patch("requests.get", return_value=Mock(json=lambda: mock_json)):
        get_weather("London")
        captured = capsys.readouterr()

    assert captured.out == "🌤️ London Weather: 22.5°C, sunny\n"


def test_get_weather_city_not_found(capsys):
    """Тест: город не найден — API вернул ошибку."""
    mock_json = {"cod": "404", "message": "City not found"}

    with patch("requests.get", return_value=Mock(json=lambda: mock_json)):
        get_weather("InvalidCity")
        captured = capsys.readouterr()

    assert captured.out == "❌ City not found\n"

    mock_json_none = {"cod": "404", "message": "Please enter a valid city name"}
    with patch("requests.get", return_value=Mock(json=lambda: mock_json_none)):
        get_weather("")
        captured = capsys.readouterr()

    assert captured.out == "❌ City not found\n"
