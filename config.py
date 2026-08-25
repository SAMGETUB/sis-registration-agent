from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("SIS_PASSWORD")

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
notify_email= "coq.erwin.samuel@gmail.com"


# https://www.uml.edu/student-dashboard#class-search/search?term=3610&subjects=SOCI&partialCatalogNumber=1010&classNumber=7613