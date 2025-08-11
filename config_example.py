"""
config_example.py
-----------------
Configuration template for the SoV AI Agent.

Copy this file to config.py and add your API keys:
    SERPAPI_KEY = "YOUR_SERPAPI_KEY"
    YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"

Also configure:
    TOP_N      - number of results to fetch per keyword
    BRANDS     - list of brands to track
    KEYWORDS   - search keywords

IMPORTANT: Never commit config.py with real keys to a public repo.
"""


SERPAPI_KEY = "YOUR_SERPAPI_KEY"
YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"
TOP_N = 30
BRANDS = ["Atomberg", "Crompton", "Havells", "Orient", "Usha"]
KEYWORDS = ["smart fan", "BLDC fan", "energy saving ceiling fan"]
