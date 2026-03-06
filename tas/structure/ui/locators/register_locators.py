CONTENT_CONTAINER = "#content"
REGISTER_HEADER = "xpath=//h1[normalize-space()='Register Account']"
REGISTER_FORM = "#form-register"
PERSONAL_DETAILS_LEGEND = "xpath=//legend[normalize-space()='Your Personal Details']"

FIRSTNAME_INPUT = "#input-firstname"
FIRSTNAME_ERROR = "#error-firstname"

LASTNAME_INPUT = "#input-lastname"
LASTNAME_ERROR = "#error-lastname"

EMAIL_INPUT = "#input-email"
EMAIL_ERROR = "#error-email"

PASSWORD_LEGEND = "xpath=//legend[normalize-space()='Your Password']"
PASSWORD_INPUT = "#input-password"
PASSWORD_ERROR = "#error-password"

NEWSLETTER_LEGEND = "xpath=//legend[normalize-space()='Newsletter']"
NEWSLETTER_CHECKBOX = "#input-newsletter"

PRIVACY_POLICY_CHECKBOX = "xpath=//input[@name='agree' and @type='checkbox']"
PRIVACY_POLICY_LINK = "xpath=//a[contains(@href,'privacy') and contains(text(),'Privacy Policy')]"

CONTINUE_BUTTON = "xpath=//form[@id='form-register']//button[@type='submit' and normalize-space()='Continue']"
LOGIN_PAGE_LINK = "xpath=//p//a[contains(@href,'account/login')]"
