from django.shortcuts import render
import requests
import json

def get_job_listings():
    url = "http://api.adzuna.com/v1/api/jobs/gb/search/1"
    params = {
        "app_id": "22ad7033",
        "app_key": "09ba450914232d9866bb2eabb94c101e",
        "results_per_page": 200,
        "what": "Software developer",
        "where": "london",
        "content-type": "application/json"
    }

    response = requests.get(url, params=params)
    data = json.loads(response.text)

    job_listings = []

    if "results" in data:
        job_listings = data["results"]

    return job_listings



def index(request):
    job_listings = get_job_listings()
    return render(request, "index.html", {"job_listings": job_listings})
