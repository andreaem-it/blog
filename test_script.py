#!/usr/bin/env python3
"""
Test script to verify TechJournal.it automation setup
"""

import sys
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_setup():
    """Test if all components are working correctly"""
    print("=== TechJournal.it Automation Test ===")
    
    # Test 1: Check Python version
    print(f"✅ Python version: {sys.version}")
    
    # Test 2: Check imports
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        print("✅ All required modules imported successfully")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    
    # Test 3: Test WebDriver setup
    print("🔧 Testing WebDriver setup...")
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode for testing
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("✅ WebDriver initialized successfully")
        
        # Test 4: Test website access
        print("🌐 Testing website access...")
        driver.get("https://www.techjournal.it")
        time.sleep(2)
        
        title = driver.title
        print(f"✅ Website accessed successfully. Title: {title}")
        
        # Test 5: Test banner detection
        print("🔍 Testing banner detection...")
        banner_selectors = [
            "iframe[src*='ads']",
            "iframe[src*='banner']",
            "div[class*='banner']",
            "div[class*='ad']",
            "img[src*='ads']"
        ]
        
        banners_found = 0
        for selector in banner_selectors:
            try:
                elements = driver.find_elements("css selector", selector)
                if elements:
                    banners_found += len(elements)
                    print(f"  Found {len(elements)} elements with selector: {selector}")
            except Exception as e:
                continue
        
        print(f"✅ Banner detection test completed. Found {banners_found} potential banner elements")
        
        # Cleanup
        driver.quit()
        print("✅ WebDriver closed successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ WebDriver test failed: {e}")
        return False

def main():
    """Main test function"""
    success = test_setup()
    
    print("\n" + "="*50)
    if success:
        print("🎉 All tests passed! The automation script is ready to use.")
        print("\nTo start the automation:")
        print("  python3 techjournal_automation.py")
    else:
        print("❌ Some tests failed. Please check the error messages above.")
        print("\nCommon solutions:")
        print("  1. Install Chrome browser")
        print("  2. Run: pip3 install -r requirements.txt")
        print("  3. Check internet connection")
    
    print("="*50)

if __name__ == "__main__":
    main()