import yaml, os

class YamlLoader:
    @staticmethod
    def read_file(file_path) -> dict:
        with open(file_path,"r") as file:
            file_content = file.read()
            return file_content