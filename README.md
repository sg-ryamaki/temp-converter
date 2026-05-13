# Temperature Converter

A simple Python utility to convert temperatures between Celsius, Fahrenheit, and Kelvin.

## Usage

```python
from converter import celsius_to_fahrenheit

print(celsius_to_fahrenheit(100))  # 212.0
```

## Functions

| Function | Description |
|---|---|
| `celsius_to_fahrenheit(c)` | Celsius → Fahrenheit |
| `fahrenheit_to_celsius(f)` | Fahrenheit → Celsius |
| `celsius_to_kelvin(c)` | Celsius → Kelvin |
| `kelvin_to_celsius(k)` | Kelvin → Celsius |

## Running Tests

```bash
pytest test_converter.py
```
