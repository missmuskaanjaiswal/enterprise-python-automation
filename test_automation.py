
import unittest

from enterprise_automation.data_processor import process_data


class TestDataProcessor(unittest.TestCase):

    def test_list_data(self):
        result = process_data([1, 2, 3])
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["total_records"], 3)

    def test_dictionary_data(self):
        result = process_data({"name": "Student"})
        self.assertEqual(result["status"], "success")

    def test_invalid_json(self):
        result = process_data("{invalid json}")
        self.assertEqual(result["status"], "error")


if __name__ == "__main__":
    unittest.main()
  
