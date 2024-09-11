import pandas as pd

def read_excel_data():
    file_path = r'D:\pycharmProject\practice\data\test_data_login.xlsx'  # Using raw string to avoid escaping backslashes
    read = pd.read_excel(file_path)
    return read

# def read_csv_data():
#     file_path = r'D:\pycharmProject\practice\data\login_csv_data.csv'  # Using raw string to avoid escaping backslashes
#     read = pd.read_csv(file_path)
#     return read
#
# print(read_csv_data())

def read_csv_data():
    file_path = r'D:\pycharmProject\practice\data\login_csv_data.csv'
    read = pd.read_csv(file_path)
    print("Columns in CSV file:", read.columns)  # Check the column names
    read.columns = read.columns.str.strip()  # Remove any leading/trailing spaces from column names
    return read

data = read_csv_data()

# Now, you can access the 'username' column safely after stripping spaces
print(data['username'])  # This should work now if 'username' exists

