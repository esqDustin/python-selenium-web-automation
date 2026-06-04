import csv

def read_csv_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='|')
            return [row for row in reader]

    except FileNotFoundError:
        raise Exception("File cannot be found! Please check the file path.")
    
def read_csv_file_with_lists(file_path, list_column_names=None, list_delimeter=';'):
    try:
        list_column_names = list_column_names or []
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='|')
            for row in reader:
                for column in list_column_names:
                    if column not in row:
                        continue
                    if row[column]:
                        row[column] = [item.strip() for item in row[column].split(list_delimeter)]
                    else:
                        row[column] = []
                data.append(row)    
        return data
        
    except FileNotFoundError:
          raise Exception("File cannot be found! Please check the file path.")
    