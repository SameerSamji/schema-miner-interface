import json

def read_json_file(filepath: str, encoding: str = 'utf-8'):
    """
    Reads the JSON file and return it's content

    :param str file_path: The path to the JSON file
    :param str encoding: The encoder to use for reading the file
    
    :returns json_dict: The JSON file content
    """
    try:
        with open(filepath, 'r', encoding=encoding) as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError:
        print('Cannot parse JSON file: {}'.format(filepath))
    except FileNotFoundError:
        print('File Not Found: {}'.format(filepath))
    except Exception as e:
        print('Exception Occured: {}'.format(e))