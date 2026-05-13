def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c):
    """Convert Celsius to Kelvin."""
    return c + 273.15


def kelvin_to_celsius(k):
    """Convert Kelvin to Celsius."""
    return k - 273.15


if __name__ == "__main__":
    print("100°C =", celsius_to_fahrenheit(100), "°F")
    print("32°F =", fahrenheit_to_celsius(32), "°C")
    print("0°C =", celsius_to_kelvin(0), "K")
