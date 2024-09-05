from utilities.file_utils import FileUtils

test_text = """Question: 1. I have a diploma or higher qualification in finance, business or accounting\nAnswer: Yes"""

if FileUtils.find_string_in_file(test_text):
    print("String found in file")

print(FileUtils.get_financial_objective())
