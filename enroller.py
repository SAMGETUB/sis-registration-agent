from config import password

# Checks whether the "already enrolled" error page is showing.
# Returns (True, message) if it matches, or (False, "") if not -
# either because a different message appeared, or nothing appeared at all.
def check_already_enrolled(page):
    try:
        page.wait_for_selector("div.error-container", timeout=5000)  # was 10000
        error_box = page.locator("div.error-container")
        message = error_box.inner_text()
        if "already enrolled" in message:
            return True, message
        else:
            print("check_already_enrolled: error-container found but text didn't match:", message)
            return False, ""
    except:
        print("check_already_enrolled: div.error-container did not appear in time")
        return False, ""

def enroll(page, course):
    class_number = course["class_number"]

    # Step 1 - Click Add...
    enroll_url= f"https://uml.edu/student-dashboard#my-academics/enroll/add?term=3610&career=UGRD&cn={class_number}"
    page.goto(enroll_url) 

    # Step 1.5 - already enrolled can show up immediately after navigating
    is_already_enrolled, message = check_already_enrolled(page)
    if is_already_enrolled:
        return ("already_enrolled", message)
    
    
    # Step 3 - Fill password and continue
    try:
        page.wait_for_selector("input[type='password']", timeout=10000)
        page.fill("input[type='password']", password)
        page.click("button[label='Continue']")
        page.wait_for_selector("input[type='password']", state="detached", timeout=10000)
    except:
        print(" No paasswird prompt this session, skipping")

    # Step 3.5 - or it can only appear after authenticating, if a password was needed
    is_already_enrolled, message = check_already_enrolled(page)
    if is_already_enrolled:
        return ("already_enrolled", message)

    # Step 4 - Click Add to Cart on confirmation page
    page.wait_for_selector("button[label='Add to Cart']", timeout=10000)
    page.locator("button[label='Add to Cart']").first.click()

    # Step 5 - Continue to enrollment cart
    page.wait_for_selector("button[label='Continue to my Enrollment Cart']", timeout=10000)
    page.click("button[label='Continue to my Enrollment Cart']")

    # Step 6 - Check the checkbox for this course
    page.wait_for_selector(f"label[data-reactid*='{class_number}']", timeout=10000)
    page.click(f"label[data-reactid*='{class_number}']")

    #step 7- Enroll in Selected
    page.click("button[label='Enroll in Selected']")

        # step 8 - Read the result the portal gives back
    # First question: did the result message appear?
    # If it never shows, we don't know what happened -> error, retry next time
    try:
        page.wait_for_selector("div.enrollment-cart-item-action-result-message", timeout=10000)
    except:
        return ("error", "no result message appeared")

    # It appeared. Read the icon's class, scoped to the message div (avoids strict-mode: 2 matches)
    message_div = page.locator("div.enrollment-cart-item-action-result-message")
    icon_class = message_div.locator("i.enrollment-cart-item-action-result-icon").get_attribute("class") or ""
    reason = message_div.locator("span").last.inner_text()

    # Three possible results: enrolled, rejected, error
    if "bad" in icon_class:
        return ("rejected", reason)
    elif "good" in icon_class:
        return ("enrolled", reason)
    else:
        return ("error", f"unknown result icon: {icon_class}")