from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("SIS_PASSWORD")
webhook_url = os.getenv("N8N_WEBHOOK_URL")

wishlist = [

            {
             "name": " Introduction to Ethics",
             "subject": "PHIL",
             "catalog_number": "1030",
             "class_number": "6031",
            },

            {
             "name": " Introduction to Sociology",
             "subject": "SOCI",
             "catalog_number": "1010",
             "class_number": "7613",
            },

             {
             "name": "French 1",
             "subject": "WLFR",
             "catalog_number": "1010",
             "class_number": "6006",
            }

]

poll_interval= 1800
