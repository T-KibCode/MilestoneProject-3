#import os
#import pandas as pd
#from google.oauth2 import service_account
#from googleapiclient.discovery import build
#from googleapiclient.errors import HttpError
#from sqlalchemy import create_engine

# Set up credentials for accessing the Google Sheets API
#SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
#SERVICE_ACCOUNT_FILE = 'path/to/service/account/key.json'
#creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Extract the sheet ID from the Google Sheet URL
#sheet_url = 'https://docs.google.com/spreadsheets/d/1HTzUEipK0ITfIWwiIkrF9J_BTICrs_ya8pUC9MdYqY8/edit#gid=180562119'
#sheet_id = sheet_url.split('/')[-2]

# Connect to the Google Sheets API and retrieve data from the sheet
#sheet_range = 'movie_id!A1:D'
#sheets = build('sheets', 'v4', credentials=creds)
#result = sheets.spreadsheets().values().get(spreadsheetId=sheet_id, range=sheet_range).execute()

# Convert the retrieved data to a pandas dataframe
#data = result.get('values', [])
#headers = data.pop(0)
#df = pd.DataFrame(data, columns=headers)

# Set up a connection to your SQL database
#DATABASE_TYPE = 'postgresql'
#DATABASE_USER = 'your-database-username'
#DATABASE_PASSWORD = 'your-database-password'
#DATABASE_HOST = 'your-database-host'
#DATABASE_NAME = 'your-database-name'
#DATABASE_PORT = 'your-database-port'
#DATABASE_URL = f'{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
#engine = create_engine(DATABASE_URL)

# Create a new SQL table using the data from the Google Sheet
#table_name = 'movie_credits'
#df.to_sql(table_name, engine, if_exists='replace', index=False)

#print(f"Data from {sheet_range} has been successfully written to {table_name} table in the database.")
