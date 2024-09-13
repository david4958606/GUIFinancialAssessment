import os


class FileUtils:
    @staticmethod
    def check_result_file():
        # Check if the "result.txt" file exists in the root directory
        if not os.path.exists("result.txt"):
            return False

    @staticmethod
    def new_result_file():
        # Create a new empty "result.txt" file if not already present
        # Or clean the existing file
        with open("result.txt", "w") as file:
            file.write("")

    @staticmethod
    def amend_result_file(data):
        # Append data to the "result.txt" file
        with open("result.txt", "a") as file:
            file.write(data)
            file.write("\n")

    @staticmethod
    def find_string_in_file(string):
        # Check if the given string is present in the "result.txt" file
        with open("result.txt", "r") as file:
            return string in file.read()

    @staticmethod
    def judge_car():
        str1 = "Question: 1. I have a diploma or higher qualification in finance, business or accounting\nAnswer: Yes"
        str2 = "Question: 2. I have a professional finance qualification\nAnswer: Yes"
        str3 = "Question: 3. In the last 10 years, I have at least 3 years of working experience in finance or accounting\nAnswer: Yes"
        str4 = "Question: 4. I have at least 3 years of working experience in the last 10 years in a finance or accounting role"
        # print("MainUIController: judge_car_cka called")
        # Check if the result file contains "Knowledge and Experience Results"
        if not FileUtils.find_string_in_file("Knowledge and Experience Results:"):
            pass

        if FileUtils.find_string_in_file(str1) or FileUtils.find_string_in_file(str2) or FileUtils.find_string_in_file(
                str3):
            return True
        elif FileUtils.find_string_in_file(str4):
            if not FileUtils.find_string_in_file("None of above"):
                return True
        else:
            return False

    @staticmethod
    def judge_cka():
        str1 = "Question: 1. I have a diploma or higher qualification in finance, business or accounting\nAnswer: Yes"
        str2 = "Question: 2. I have a professional finance qualification\nAnswer: Yes"
        str3 = "Question: 3. In the last 10 years, I have at least 3 years of working experience in finance or accounting\nAnswer: Yes"
        str4 = "Question: 4. I have at least 3 years of working experience in the last 10 years in a finance or accounting role"
        if FileUtils.find_string_in_file(str1) or FileUtils.find_string_in_file(str2) or FileUtils.find_string_in_file(
                str3):
            return True
        elif FileUtils.find_string_in_file(str4):
            if not FileUtils.find_string_in_file("None of above"):
                return True
        else:
            return False

    @staticmethod
    def get_financial_objective():
        # if one line contains "Your Financial Objective: " in the file, return the next line,exclude the first 3 characters
        with open("result.txt", "r") as file:
            for line in file:
                if "Your Financial Objective: " in line:
                    objective = next(file).strip()
                    return objective[3::]
                else:
                    pass
