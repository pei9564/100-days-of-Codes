import requests
from bs4 import BeautifulSoup
import time

url = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"

# write the first row in csv
with open("salaries_by_college_major_new.csv", 'w') as file_create:
    file_create.write("Major,Early Career Pay,Mid-Career Pay,High Meaning\n")


def record_data(major_list, salary_list):
    for major_index in range(0, len(major_list)):
        salary_index = major_index * 3
        with open("salaries_by_college_major_new.csv", 'a') as file:
            file.write(f"{major_list[major_index]},"
                       f"{float(salary_list[salary_index].replace(',', '').replace('$', ''))},"
                       f"{float(salary_list[salary_index + 1].replace(',', '').replace('$', ''))},"
                       f"{salary_list[salary_index + 2]}\n")


for page in range(1, 35):  # 35
    web_data = requests.get(f"{url}/page/{page}").text
    soup = BeautifulSoup(web_data, "html.parser")

    majors_html = soup.select(".csr-col--school-name .data-table__value")
    majors = [major.text for major in majors_html]

    salaries_html = soup.select(".csr-col--right .data-table__value")
    salaries = [salary.text for salary in salaries_html]

    record_data(majors, salaries)
    time.sleep(5)
