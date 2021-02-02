## Instructions for deployment

1. you will need to install python 3.x and pip
2. on a linux/powershell run 'pip install flask'
3. on linux/powershell run 'python src/SingleSprout.py'
4. to test you will need to send a 'POST' request with 'application/json' headers to 'http://127.0.0.0:5000/api/v1/resources/client (REQUEST MUST BE VALID JSON SHOWN IN THE FORMAT BELOW)

Test Input

[
  {
    "full_name": "Omar Becerra",
    "phone": "(111) 555-5555",
    "email_address": "omar@test.com",
    "linkedin_username": "omarbecerra",
    "employments": [{
      "company_name": "Company 1",
      "job_title": "Best Engineer",
      "start_date": "2018-12-24",
      "end_date": "2021-11-01"
    }]
  },
  {
    "full_name": "Omar Becerra",
    "phone": "(111) 555-6666",
    "email_address": "omasr@test.com",
    "linkedin_username": "omarbecerra",
    "employments": [{
      "company_name": "Company 1",
      "job_title": "Best Engineer",
      "start_date": "2018-12-25",
      "end_date": "2021-11-02"
    }]
  }
]

Test Output

[
  {
    "emails": [
      "omar@test.com",
      "omasr@test.com"
    ],
    "employments": [
      {
        "company_name": "Company 1",
        "end_date": "2021-11-01",
        "job_title": "Best Engineer",
        "start_date": "2018-12-24"
      },
      {
        "company_name": "Company 1",
        "end_date": "2021-11-02",
        "job_title": "Best Engineer",
        "start_date": "2018-12-25"
      }
    ],
    "first_name": "Omar",
    "last_name": "Becerra",
    "linkedin_username": "omarbecerra",
    "phone_numbers": [
      "(111) 555-5555",
      "(111) 555-6666"
    ]
  }
]