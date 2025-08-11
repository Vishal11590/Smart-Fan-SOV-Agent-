# Share-of-Voice (SoV) Agent for 'Smart Fan'

This repository contains a minimal AI-agent to compute Share-of-Voice (SoV)
for brands (e.g., Atomberg) for keywords like 'smart fan'.

## What it does
- Searches Google (via SerpAPI) and YouTube (via YouTube Data API) for top N results.
- Normalizes results and computes a simple SoV metric combining mentions, engagement, and sentiment.
- Dumps `results.csv` and prints SoV percentages.

## Files
- `config_example.py`: Copy to `config.py` and add your API keys.
- `search_serpapi.py`: Fetch Google organic results using SerpAPI.
- `search_youtube.py`: Fetch YouTube search results and video stats.
- `analysis.py`: Brand detection, engagement computation, and sentiment scoring.
- `main.py`: Orchestrator - runs searches, computes SoV, saves `results.csv`.
- `requirements.txt`: Python dependencies.

## Setup
1. Copy `config_example.py` → `config.py` and put your API keys.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
3. Run:
   ```
   python main.py
   ```
4. Outputs: `results.csv` and console SoV summary.

## Notes & Ethics
- Do NOT commit actual API keys to public repos. Use environment variables or GitHub Secrets.
- Respect platform Terms of Service and rate limits.

## Sample Output
See `results_sample.csv` for an example output file you can include in your repo.

## Extensions
- Add more platforms (X/Twitter, Instagram) using their APIs.
- Build a Streamlit dashboard to visualize SoV over time.
