# Github_API_Authentication

A simple Python project that integrates with the GitHub REST API to fetch
public repositories data for a given user and export it as JSON.

## Features
- Fetch repositories using GitHub REST API
- Handle authentication via environment variables
- Export cleaned data to JSON file

## Technologies
- Python
- requests
- python-dotenv
- GitHub REST API

## Lessons Learned
- API endpoints are strict (trailing slash caused 404)
- Importance of correct headers format
- Debugging HTTP status codes properly

## How to Run
1. Create `.env` file
2. Add your GitHub token:
GITHUB_TOKEN=your_token_here
3. Run: python main.py
