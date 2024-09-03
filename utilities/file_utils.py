import os


class FileUtils:
    @staticmethod
    def check_result_file():
        # Check if the "result.txt" file exists in the root directory
        if not os.path.exists("result.txt"):
            return False
        
    def new_result_file():
        # Create a new empty "result.txt" file if not already present
        # Or clean the existing file
        with open("result.txt", "w") as file:
            file.write("")

    def amend_result_file(data):
        # Append data to the "result.txt" file
        with open("result.txt", "a") as file:
            file.write(data)
            file.write("\n")
