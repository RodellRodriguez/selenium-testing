import json, unittest, time

from selenium import webdriver

from pages.schedule_demo_page import ScheduleDemoPage

class ScheduleDemo(unittest.TestCase):
    
    def setUp(self):
        with open('test_data.json') as json_file:  
            self.test_data = json.load(json_file)
        self.browser = webdriver.Firefox()
        self.schedule_demo_page = ScheduleDemoPage(self.browser)
        self.schedule_demo_page.navigate()

    def tearDown(self):
        # Only using the sleep function just to show visually that the 
        # first and last names do fill in the form. Sleep functions
        # would not be used in actual test cases.
        time.sleep(3)
        self.browser.quit()

    def test_first_name_field_checks_if_fields_are_empty(self):
        self.schedule_demo_page.set_first_name(self.test_data['first_name'])
        self.schedule_demo_page.set_last_name(self.test_data['last_name'])
        self.schedule_demo_page.schedule_demo()

        self.assertEqual(
            self.schedule_demo_page.get_complete_all_required_fields_text()
            , "Please complete all required fields."
        )


if __name__ == "__main__":
    unittest.main()