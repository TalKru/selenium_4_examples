Disclaimer

The following code was selected by the [Guará](https://github.com/douglasdcm/guara) team as part of their validation process to assess the capabilities of the framework. The code illustrates the use of Selenium WebDriver to interact with a web page, with a focus on retrieving a temporary email address from a service. It is organized into discrete transactions, validating how the Guará framework could be used to modularize and streamline web automation tasks.


Code Explanation
1. ConfigureDriverTransaction (Class ConfigureDriverTransaction):

    This transaction encapsulates the logic of configuring the Chrome WebDriver.
    The do method:
        Configures the WebDriver with several options like maximized window, incognito mode, and disabled extensions.
        Returns the configured driver, which will be used in subsequent actions.
    Purpose in Guará: This class modularizes the WebDriver setup, making it reusable for any future tests.

2. IsEmailLoadedTransaction (Class IsEmailLoadedTransaction):

    This transaction checks if the email field in the temporary email service contains a valid email address.
    The do method:
        Locates the email input field and retrieves its value.
        Uses a regular expression to check if the value matches the pattern for a typical email address (ending in .com).
    Purpose in Guará: This encapsulation ensures that the email validation logic can be reused and modified independently.

3. WaitForEmailToLoadTransaction (Class WaitForEmailToLoadTransaction):

    This transaction waits for the email field to be populated with a valid email address before proceeding.
    The do method:
        Waits for the IsEmailLoadedTransaction to return True, indicating that the email has been loaded.
        Retrieves the email value after it has been validated.
    Purpose in Guará: This transaction handles waiting and synchronization, allowing it to be reused in any future tests requiring an email field to load.

4. TakeScreenshotTransaction (Class TakeScreenshotTransaction):

    This transaction takes a screenshot of the page, which is useful for debugging and visual validation.
    The do method:
        Saves a screenshot with the provided filename.
        Returns a confirmation message indicating where the screenshot was saved.
    Purpose in Guará: This provides a clear, reusable action for taking screenshots in any web automation tests.

5. Test Flow (Function test_temp_email_task):

    This function demonstrates how the transactions are orchestrated using the Guará framework.
    Flow:
        The ConfigureDriverTransaction is executed first to initialize the browser.
        The WaitForEmailToLoadTransaction is executed to ensure that the temporary email field is populated.
        Finally, the TakeScreenshotTransaction is executed to capture a screenshot and print the generated email address.
    The test is clean, modular, and flexible, with each transaction focused on a single responsibility.

Why This Code Was Selected for Guará Experimentation
1. Modularization and Separation of Concerns:

    The original code was divided into modular functions like configure_driver, is_email_loaded, and wait_for_email_to_load. The Guará framework takes this modularization a step further by treating each of these as transactions.
    Each transaction in this code follows the principle of separation of concerns, where each transaction is responsible for a specific task (e.g., configuring the driver, waiting for the email field, taking a screenshot).

2. Reusability:

    The Guará transactions are highly reusable. For example, the ConfigureDriverTransaction could be used in any test that requires setting up a Selenium WebDriver. Similarly, the email checking logic is encapsulated in the IsEmailLoadedTransaction, allowing it to be reused wherever such validation is needed.

3. Synchronization:

    The WaitForEmailToLoadTransaction transaction showcases how Guará handles waiting for conditions to be met before proceeding. By using explicit waits in combination with Guará’s transaction flow, the test becomes more stable and resistant to race conditions.

4. Simplified Test Management:

    By using Guará, the test case is organized and streamlined. Each transaction is focused on a single action, making it easy to modify and extend. For example, if the temporary email service changes its structure or if a new test requires a different browser configuration, the relevant transaction can be modified or extended without impacting other tests.

5. Clear Test Flow:

    The Guará framework makes it easy to represent complex workflows in a linear and readable manner. The test flow can be understood at a glance, with each transaction clearly named and logically sequenced.

Conclusion

The Guará framework was used to validate how web automation tasks, like configuring a WebDriver, interacting with form fields, and taking screenshots, could be modularized and reused across different tests. The transactions pattern ensures that each test step is encapsulated in its own class, making the tests easier to maintain, extend, and modify. By organizing the code this way, the Guará team has demonstrated that complex tasks can be broken down into manageable, reusable components, simplifying test management and improving stability.