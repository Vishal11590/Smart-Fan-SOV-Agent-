import os
from serpapi import GoogleSearch

def serp_search(query, serpapi_key, num=30):
    params = {
        "engine": "google",
        "q": query,
        "api_key": serpapi_key,
        "num": num
    }
    search = GoogleSearch(params)
    data = search.get_dict()
    results = []
    for item in data.get("organic_results", [])[:num]:
        results.append({
            "source": "google",
            "title": item.get("title"),
            "snippet": item.get("snippet"),
            "link": item.get("link")
        })
    return results
