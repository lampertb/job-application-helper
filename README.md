# applicationHelper

Job Application Helper
This script fetches job details from a Greenhouse job application page and generates a custom cover letter using OpenAI's API.

# Features
Fetches job title, company name, and description from a Greenhouse job application page.
Uses OpenAI's API to generate a custom cover letter for the job.

# Requirements
Python 3.6 or higher
requests library
beautifulsoup4 library
openai library
OpenAI API key

# Installation
Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/job-application-helper.git
cd job-application-helper
Install the required libraries:

sh
Copy code
pip install requests beautifulsoup4 openai
Set your OpenAI API key as an environment variable:

sh
Copy code
export OPENAI_API_KEY='your_openai_api_key'
Usage
Run the script with the URL of a Greenhouse job application page:

sh
Copy code
python main.py https://boards.greenhouse.io/figma/jobs/5136933004?gh_src=f4e571c44us
Example
sh
Copy code
python main.py https://boards.greenhouse.io/figma/jobs/5136933004?gh_src=f4e571c44us