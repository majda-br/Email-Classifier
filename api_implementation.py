# -*- coding: utf-8 -*-


import json
import requests


url = ""

input_data_for_model = {
    "email": "Subject: Invitation to Attend a Job Interview\
Dear [Applicant Name],\
Thank you for applying for the [Job Title] position with our company. We were impressed with your qualifications and experience, and we would like to invite you to attend an interview with our team.\
The interview will take place on [Date] at [Time] at our office located at [Address]. During the interview, we will discuss your qualifications, experience, and your fit with our company culture. You will also have the opportunity to ask any questions you may have about the position and the company.\
Please let us know if this date and time work for you. If not, we are happy to arrange a different time that is convenient for you. Also, please bring a copy of your updated resume and any relevant certifications or documents.\
We would like to remind you that the interview is an important part of our selection process, and we ask that you dress appropriately and arrive on time.\
We look forward to meeting with you and getting to know you better.\
Best regards,"
}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)
