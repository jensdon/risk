import os


class FileHelper:

    def read_data_from_file(input_file):

        current_dir = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        file_full_path = current_dir+'/'+input_file
        with open(file_full_path, 'r') as f:
            data = f.read()
        return data