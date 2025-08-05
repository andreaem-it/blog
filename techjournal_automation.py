#!/usr/bin/env python3
"""
TechJournal.it Automation Script
Navigates to www.techjournal.it every 15-30 minutes and clicks banner advertisements
with human-like random behavior.
"""

import time
import random
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import threading

# Import configuration
try:
    from config import *
except ImportError:
    # Default configuration if config.py is not found
    WEBSITE_URL = "https://www.techjournal.it"
    MIN_INTERVAL = 15
    MAX_INTERVAL = 30
    MAX_BANNER_CLICKS_PER_SESSION = 3
    BANNER_CLICK_PROBABILITY = 0.7
    GO_BACK_PROBABILITY = 0.3
    MIN_DELAY = 1.0
    MAX_DELAY = 3.0
    MIN_SCROLL_DELAY = 0.5
    MAX_SCROLL_DELAY = 1.5
    MIN_INITIAL_DELAY = 2.0
    MAX_INITIAL_DELAY = 5.0
    MIN_SCROLL_AMOUNT = 100
    MAX_SCROLL_AMOUNT = 500
    SCROLL_BACK_PROBABILITY = 0.3
    HORIZONTAL_SCROLL_PROBABILITY = 0.1
    MIN_SCROLL_SESSIONS = 2
    MAX_SCROLL_SESSIONS = 5
    HOVER_BEFORE_CLICK_PROBABILITY = 0.3
    HEADLESS_MODE = False
    WINDOW_SIZES = [(1920, 1080), (1366, 768), (1440, 900), (1536, 864), (1280, 720)]
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ]
    BANNER_SELECTORS = [
        "iframe[src*='ads']", "iframe[src*='banner']", "iframe[src*='ad']",
        "div[class*='banner']", "div[class*='ad']", "div[id*='banner']", "div[id*='ad']",
        "a[href*='ads']", "a[href*='banner']", "img[src*='ads']", "img[src*='banner']"
    ]
    LOG_LEVEL = "INFO"
    LOG_FILE = "techjournal_automation.log"
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    RETRY_DELAY = 60
    MAX_RETRIES = 3

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TechJournalAutomation:
    def __init__(self):
        self.url = WEBSITE_URL
        self.driver = None
        self.running = False
        
    def setup_driver(self):
        """Setup Chrome WebDriver with human-like settings"""
        chrome_options = Options()
        
        # Add human-like browser settings
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Random window size to appear more human
        size = random.choice(WINDOW_SIZES)
        chrome_options.add_argument(f"--window-size={size[0]},{size[1]}")
        
        # Random user agent
        chrome_options.add_argument(f"--user-agent={random.choice(USER_AGENTS)}")
        
        # Headless mode if configured
        if HEADLESS_MODE:
            chrome_options.add_argument("--headless")
        
        try:
            # Use webdriver-manager to automatically download and manage ChromeDriver
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            logger.info("WebDriver initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize WebDriver: {e}")
            return False
        return True
    
    def human_like_delay(self, min_seconds=None, max_seconds=None):
        """Add human-like random delays"""
        if min_seconds is None:
            min_seconds = MIN_DELAY
        if max_seconds is None:
            max_seconds = MAX_DELAY
        delay = random.uniform(min_seconds, max_seconds)
        time.sleep(delay)
    
    def scroll_randomly(self):
        """Perform random scrolling to simulate human behavior"""
        try:
            # Random scroll up and down
            scroll_amount = random.randint(MIN_SCROLL_AMOUNT, MAX_SCROLL_AMOUNT)
            self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            self.human_like_delay(MIN_SCROLL_DELAY, MAX_SCROLL_DELAY)
            
            # Sometimes scroll back up
            if random.random() < SCROLL_BACK_PROBABILITY:
                self.driver.execute_script(f"window.scrollBy(0, -{scroll_amount//2});")
                self.human_like_delay(MIN_SCROLL_DELAY, MAX_SCROLL_DELAY)
                
            # Sometimes scroll horizontally (rare)
            if random.random() < HORIZONTAL_SCROLL_PROBABILITY:
                horizontal_scroll = random.randint(-50, 50)
                self.driver.execute_script(f"window.scrollBy({horizontal_scroll}, 0);")
                self.human_like_delay(0.3, 0.8)
                
        except Exception as e:
            logger.warning(f"Error during scrolling: {e}")
    
    def find_and_click_banners(self):
        """Find and click on banner advertisements"""
        banner_selectors = BANNER_SELECTORS
        
        banners_clicked = 0
        
        for selector in banner_selectors:
            try:
                # Wait for elements to be present
                elements = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
                )
                
                for element in elements:
                    if not self.running:
                        break
                        
                    try:
                        # Check if element is visible and clickable
                        if element.is_displayed() and element.is_enabled():
                            # Scroll to element with random offset
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                            self.human_like_delay(0.5, 1.0)
                            
                            # Random decision to click
                            if random.random() < BANNER_CLICK_PROBABILITY:
                                # Sometimes hover before clicking
                                if random.random() < HOVER_BEFORE_CLICK_PROBABILITY:
                                    from selenium.webdriver.common.action_chains import ActionChains
                                    actions = ActionChains(self.driver)
                                    actions.move_to_element(element).perform()
                                    self.human_like_delay(0.5, 1.0)
                                
                                element.click()
                                banners_clicked += 1
                                logger.info(f"Clicked banner: {selector}")
                                
                                # Wait a bit after clicking
                                self.human_like_delay(2, 4)
                                
                                # Sometimes go back
                                if random.random() < GO_BACK_PROBABILITY:
                                    self.driver.back()
                                    self.human_like_delay(1, 2)
                                
                                # Limit clicks per session
                                if banners_clicked >= MAX_BANNER_CLICKS_PER_SESSION:
                                    return banners_clicked
                                    
                    except Exception as e:
                        logger.warning(f"Error clicking banner {selector}: {e}")
                        continue
                        
            except TimeoutException:
                continue
            except Exception as e:
                logger.warning(f"Error finding banners with selector {selector}: {e}")
                continue
        
        return banners_clicked
    
    def browse_page(self):
        """Browse the page with human-like behavior"""
        try:
            logger.info(f"Navigating to {self.url}")
            self.driver.get(self.url)
            
            # Wait for page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Random initial delay
            self.human_like_delay(MIN_INITIAL_DELAY, MAX_INITIAL_DELAY)
            
            # Scroll randomly
            for _ in range(random.randint(MIN_SCROLL_SESSIONS, MAX_SCROLL_SESSIONS)):
                if not self.running:
                    break
                self.scroll_randomly()
            
            # Find and click banners
            banners_clicked = self.find_and_click_banners()
            logger.info(f"Clicked {banners_clicked} banners in this session")
            
            # Random final delay
            self.human_like_delay(1, 3)
            
        except Exception as e:
            logger.error(f"Error during browsing: {e}")
    
    def run_automation(self):
        """Main automation loop"""
        if not self.setup_driver():
            return
        
        logger.info("Starting TechJournal.it automation")
        
        while self.running:
            try:
                self.browse_page()
                
                # Calculate next interval
                next_interval = random.randint(MIN_INTERVAL, MAX_INTERVAL) * 60  # Convert to seconds
                logger.info(f"Next session in {next_interval//60} minutes")
                
                # Wait for next session
                for _ in range(next_interval):
                    if not self.running:
                        break
                    time.sleep(1)
                    
            except Exception as e:
                logger.error(f"Error in automation loop: {e}")
                time.sleep(RETRY_DELAY)  # Wait before retrying
        
        if self.driver:
            self.driver.quit()
            logger.info("WebDriver closed")
    
    def start(self):
        """Start the automation"""
        self.running = True
        self.run_automation()
    
    def stop(self):
        """Stop the automation"""
        self.running = False
        logger.info("Stopping automation...")

def main():
    """Main function"""
    automation = TechJournalAutomation()
    
    try:
        automation.start()
    except KeyboardInterrupt:
        logger.info("Received interrupt signal")
        automation.stop()
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        automation.stop()

if __name__ == "__main__":
    main()