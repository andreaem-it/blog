#!/usr/bin/env python3
"""
Configuration file for TechJournal.it automation
Modify these settings to customize the automation behavior
"""

# Website settings
WEBSITE_URL = "https://www.techjournal.it"

# Timing settings (in minutes)
MIN_INTERVAL = 15  # Minimum interval between sessions
MAX_INTERVAL = 30  # Maximum interval between sessions

# Session behavior
MAX_BANNER_CLICKS_PER_SESSION = 3  # Maximum banner clicks per session
BANNER_CLICK_PROBABILITY = 0.7  # Probability of clicking a banner (0.0-1.0)
GO_BACK_PROBABILITY = 0.3  # Probability of going back after clicking (0.0-1.0)

# Human-like behavior settings
MIN_DELAY = 1.0  # Minimum delay between actions (seconds)
MAX_DELAY = 3.0  # Maximum delay between actions (seconds)
MIN_SCROLL_DELAY = 0.5  # Minimum delay after scrolling (seconds)
MAX_SCROLL_DELAY = 1.5  # Maximum delay after scrolling (seconds)
MIN_INITIAL_DELAY = 2.0  # Minimum initial delay after page load (seconds)
MAX_INITIAL_DELAY = 5.0  # Maximum initial delay after page load (seconds)

# Scroll behavior
MIN_SCROLL_AMOUNT = 100  # Minimum scroll amount (pixels)
MAX_SCROLL_AMOUNT = 500  # Maximum scroll amount (pixels)
SCROLL_BACK_PROBABILITY = 0.3  # Probability of scrolling back up (0.0-1.0)
HORIZONTAL_SCROLL_PROBABILITY = 0.1  # Probability of horizontal scroll (0.0-1.0)
MIN_SCROLL_SESSIONS = 2  # Minimum number of scroll sessions per page visit
MAX_SCROLL_SESSIONS = 5  # Maximum number of scroll sessions per page visit

# Hover behavior
HOVER_BEFORE_CLICK_PROBABILITY = 0.3  # Probability of hovering before clicking (0.0-1.0)

# Browser settings
HEADLESS_MODE = False  # Set to True to run browser in headless mode
WINDOW_SIZES = [
    (1920, 1080),
    (1366, 768),
    (1440, 900),
    (1536, 864),
    (1280, 720)
]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
]

# Banner detection selectors
BANNER_SELECTORS = [
    "iframe[src*='ads']",
    "iframe[src*='banner']",
    "iframe[src*='ad']",
    "iframe[src*='doubleclick']",
    "iframe[src*='googleadservices']",
    "div[class*='banner']",
    "div[class*='ad']",
    "div[class*='advertisement']",
    "div[id*='banner']",
    "div[id*='ad']",
    "div[id*='advertisement']",
    "a[href*='ads']",
    "a[href*='banner']",
    "a[href*='ad']",
    "img[src*='ads']",
    "img[src*='banner']",
    "img[src*='ad']",
    "img[alt*='banner']",
    "img[alt*='ad']",
    "img[alt*='advertisement']"
]

# Logging settings
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FILE = "techjournal_automation.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# Error handling
RETRY_DELAY = 60  # Seconds to wait before retrying after an error
MAX_RETRIES = 3  # Maximum number of retries before giving up

# Advanced settings
ENABLE_PROXY = False  # Set to True to use proxy
PROXY_SERVER = None  # Proxy server address (e.g., "ip:port")
ENABLE_VPN_ROTATION = False  # Set to True to rotate VPN connections
VPN_ROTATION_INTERVAL = 3600  # VPN rotation interval in seconds