from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import re
import sys

EMAIL_PATTERN = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def configure_driver() -> webdriver.Chrome:
    opts = Options()
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--ignore-certificate-errors")
    opts.add_argument("--incognito")
    # opts.add_argument("--headless")
    return webdriver.Chrome(options=opts)


def validate_email(email: str) -> bool:
    """
    Return True if `email` matches the general email pattern,
    otherwise return False.
    """
    match = re.match(EMAIL_PATTERN, email)
    if match is not None:
        return True
    else:
        return False

def wait_for_email(driver, timeout=30) -> str:
    """
    Poll the #mail field until its value matches `validate_email`.
    Returns the email string when ready, or raises TimeoutException.
    """
    def _loaded(driver):
        email_element = driver.find_element(By.ID, "mail")
        val = email_element.get_attribute("value").strip()

        if validate_email(val):
            return email_element
        else:
            return False

    wait = WebDriverWait(
        driver,
        timeout,
        poll_frequency=1,
        ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
    )
    email_el = wait.until(_loaded)  # Block until _loaded returns the element, then grab it
    return email_el.get_attribute("value").strip()

def main():
    driver = configure_driver()
    try:
        driver.get("https://temp-mail.org/en/")
        temp_email = wait_for_email(driver)
        print(f"✓ Temporary email: {temp_email}")
    except Exception as e:
        print(f"Error retrieving email: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

"""
We define an inner function like `_loaded(driver):` for exactly the pattern that `WebDriverWait.until(...)` expects:

1. **Signature**
   `until` takes a callable that receives the driver as its only argument and returns either:

   * A “truthy” value (anything except `False`/`None`), which signals “success, stop waiting,” or
   * `False` (or raises an ignored exception), which tells it “not ready yet, keep polling.”

   By writing:

   ```python
   def _loaded(driver):
       …
       return email_element if validate_email(val) else False
   ```

   we satisfy that interface perfectly.

2. **Closure over locals**
   Because `_loaded` is defined inside `wait_for_email`, it “sees” the surrounding variables (like our `validate_email` function) without having to pass them in explicitly or clutter up its signature.

3. **Encapsulation of waiting logic**
   Pulling the polling logic out into a small helper keeps `wait_for_email`’s outer body clean. All the details of “how do we know the email is loaded?” live in one spot:

   ```python
   wait = WebDriverWait(driver, timeout, …)
   email_el = wait.until(_loaded)
   ```

4. **Returning the element**
   By returning the element object itself when the condition passes, you immediately get a reference to it:

   ```python
   # inside _loaded
   return email_element   # → WebDriverWait.until() hands you this back
   ```

   If you’d returned a boolean instead, you’d have to do another `find_element` afterward.

You could define that function at top‑level instead, but making it inner:

* Keeps it **private** to that one wait routine
* Lets you **capture** any local config (timeouts, locators, regexes) without global variables
* Makes the “shape” of the code match exactly what Selenium’s API expects

In short, the inner function is the natural way to give Selenium a small, self‑contained “is it ready yet?” test.

"""
