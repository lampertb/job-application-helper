import requests
from bs4 import BeautifulSoup
import argparse
from openai import OpenAI
import os

# Set your OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def fetch_job_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def parse_job_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the job title
    title_tag = soup.find('h1', {'class': 'app-title'})
    title = title_tag.get_text().strip() if title_tag else "No title found"

    # Extract the company name
    company_tag = soup.find('span', {'class': 'company-name'})
    company = company_tag.get_text().strip() if company_tag else "No company found"

    # Extract the job description
    description_tag = soup.find('div', {'id': 'content'})
    description = description_tag.get_text(separator="\n").strip() if description_tag else "No description found"

    return title, company, description

def generate_cover_letter(title, company, description):
    prompt = f"Please write a cover letter for this role: {title} at {company}. Job description: {description}"

    #gpt-3.5-turbo-instruct
    #gpt-4o
    try:
        response = client.completions.create(model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=500)
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating cover letter: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Parse job details from a Greenhouse job application page and generate a cover letter using OpenAI.")
    parser.add_argument('url', type=str, help='URL of the job application page')

    args = parser.parse_args()
    url = args.url

    html_content = fetch_job_page(url)
    if html_content:
        title, company, description = parse_job_page(html_content)

        print("Job Title:")
        print(title)
        print("\nCompany:")
        print(company)
        #print("\nJob Description:")
        #print(description)

        cover_letter = generate_cover_letter(title, company, description)
        if cover_letter:
            print("\nGenerated Cover Letter: \n")
            print(cover_letter)

if __name__ == "__main__":
    main()
