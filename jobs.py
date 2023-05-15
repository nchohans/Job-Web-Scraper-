
import requests
import csv

# Set the URL of the LinkedIn jobs page
url = "https://www.linkedin.com/jobs/"

# Get the response from the URL
response = requests.get(url)

# Check if the response was successful
if response.status_code == 200:

    # Parse the response into a HTML object
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the job postings on the page
    jobs = soup.find_all("div", class_="jobs-card__content")

    # Create a list to store the job data
    job_data = []

    # Loop through the job postings
    for job in jobs:

        # Get the title of the job
        title = job.find("h3", class_="jobs-card__title").text

        # Get the company name
        company = job.find("a", class_="jobs-card__company").text

        # Get the location of the job
        location = job.find("span", class_="jobs-card__location").text

        # Get the link to the job posting
        link = job.find("a", class_="jobs-card__link").get("href")

        # Add the job data to the list
        job_data.append({
            "title": title,
            "company": company,
            "location": location,
            "link": link,
        })

    # Create a CSV file to store the job data
    with open("content_creator_jobs.csv", "w", newline="") as csvfile:

        # Create a CSV writer object
        writer = csv.writer(csvfile)

        # Write the header row to the CSV file
        writer.writerow(["Title", "Company", "Location", "Link"])

        # Write the job data to the CSV file
        for job in job_data:
            writer.writerow(job.values())

else:
    print("Error: The request failed with status code {}.".format(response.status_code))
