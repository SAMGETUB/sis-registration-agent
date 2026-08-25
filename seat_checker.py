from config import wishlist
from enroller import enroll

def check_seats(page):
    for course in wishlist:
        subject = course["subject"]
        class_number = course["class_number"]
        catalog_number = course["catalog_number"]
        url = f"https://uml.edu/student-dashboard#class-search/search?term=3610&subjects={subject}&partialCatalogNumber={catalog_number}&classNumber={class_number}"
        page.goto(url)
        status_div= page.locator("div.text.enrollment-status")
        status_div.first.wait_for(timeout=10000)

        icon_class= status_div.first.locator("i.enrollment-status-icon").get_attribute("class") or " "
        print(f"{course['name']} : icon_class=[ {icon_class}]")



      
        if "enrollment-status-open" in icon_class:
            result= enroll(page,course)
            print(f"{course['name']} : {result[0]} - {result[1]}")
        elif "enrollment-status-waitlist" in icon_class:
            print(f"{course['name']} is Wait Listed - can't enroll")
        elif "enrollment-status-closed" in icon_class:
            print(f"{course['name']} is Closed - can't enroll")
        else:
            print(f"{course['name']} : UNKNOWN [ {icon_class} ]")    