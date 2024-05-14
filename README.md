# Job Application Helper

This script fetches job details from a Greenhouse job application page and generates a custom cover letter using OpenAI's API.

## Features

- Fetches job title, company name, and description from a Greenhouse job application page.
- Uses OpenAI's API to generate a custom cover letter for the job.

## Requirements

- Python 3.6 or higher
- `requests` library
- `beautifulsoup4` library
- `openai` library
- OpenAI API key

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/job-application-helper.git
    cd job-application-helper
    ```

2. Install the required libraries:
    ```sh
    pip install requests beautifulsoup4 openai
    ```

3. Set your OpenAI API key as an environment variable:
    ```sh
    export OPENAI_API_KEY='your_openai_api_key'
    ```

## Usage

Run the script with the URL of a Greenhouse job application page:
```sh
python main.py https://boards.greenhouse.io/figma/jobs/5136933004?gh_src=f4e571c44us
