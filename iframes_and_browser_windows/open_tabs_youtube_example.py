from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the YouTube creator's page
    driver.get("https://www.youtube.com/@Micha.Stocks/videos")
    time.sleep(0.5)  # Wait for the page to load

    # Find all video elements with id="content"
    video_elements = driver.find_elements(By.ID, "content")

    print(video_elements)

    # Limit to the first 3 elements
    videos_to_open = video_elements[:4]
    videos_to_open = videos_to_open[::-1]

    # Open each video in a new tab
    for video in videos_to_open:
        # Right-click + Open in new tab (simulate CTRL + click for a new tab)
        action = webdriver.ActionChains(driver)
        action.key_down(Keys.CONTROL).click(video).key_up(Keys.CONTROL).perform()
        time.sleep(1)  # Small delay between actions for reliability

    # Optional: Switch between tabs or interact with them
    driver.switch_to.window(driver.window_handles[1])  # Switch to the second tab

    # Clean up
    time.sleep(10)  # Keep tabs open for observation
    driver.quit()
