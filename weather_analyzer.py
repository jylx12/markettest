# weather_analyzer.py

import random
from statistics import mean


class WeatherDay:
    def __init__(self, day, temperature, humidity):
        self.day = day
        self.temperature = temperature
        self.humidity = humidity

    def comfort_score(self):
        score = 100
        score -= abs(22 - self.temperature) * 2
        score -= abs(50 - self.humidity) * 0.5
        return max(0, round(score, 1))


def generate_week():
    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    forecast = []

    for day in days:
        forecast.append(
            WeatherDay(
                day,
                random.randint(15, 35),
                random.randint(30, 90)
            )
        )

    return forecast


def hottest_day(forecast):
    return max(forecast, key=lambda d: d.temperature)


def average_temperature(forecast):
    return mean(day.temperature for day in forecast)


def print_report(forecast):
    print("=== Weekly Weather Report ===\n")

    for day in forecast:
        print(
            f"{day.day:<10} "
            f"{day.temperature:>2}°C  "
            f"{day.humidity:>2}% humidity  "
            f"Comfort: {day.comfort_score()}"
        )

    print("\nStatistics")
    print("-" * 30)

    hottest = hottest_day(forecast)

    print(f"Average Temperature: {average_temperature(forecast):.1f}°C")
    print(f"Hottest Day: {hottest.day} ({hottest.temperature}°C)")


def main():
    weekly_forecast = generate_week()
    print_report(weekly_forecast)


if __name__ == "__main__":
    main()
