import os


class FileUtils:
    @staticmethod
    def check_result_file():
        # Check if the "result.txt" file exists in the root directory
        if not os.path.exists("result.txt"):
            return False
