import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

clients = gspread.authorize(creds)

sheet = clients.open("tutorial").sheet1 # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

row = sheet.row_values(3)  # Get a specific row
col = sheet.col_values(3)  # Get a specific column
cell = sheet.cell(1,2).value  # Get the value of a specific cell
sheet.update_cell(2,2, "Umair") # updated sheet cell through index

insertRow = ["Zubair", " 25", "MALE", "LAHORE", "PAK"]
sheet.insert_row(insertRow, 5)  # Insert the list as a row at index 5
#sheet.delete_row(insertRow, 5) # delete the row as a row at index 5
