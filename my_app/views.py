from django.shortcuts import render
from django.http import HttpResponse

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import datetime

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')

def accpet(request):
    try:
        # Replace with the ID of your Google Sheets document
        SPREADSHEET_ID = '1vdOK4B4AYSm_ZJd-hTXYwuCisbMl0hhxJStLE70mh2E'

        # Replace with the range of cells where you want to store the data
        RANGE_NAME = 'Sheet1!A2:C'

        # Replace with the path to your credentials file
        CREDENTIALS_FILE = 'C:/Users/adityamishra/local_personal/ExcelAssignment/my_app/rupicarddatabase.json'

        # Load the credentials from the file
        creds = Credentials.from_service_account_file(CREDENTIALS_FILE)

        # Create a new service object for the Google Sheets API
        service = build('sheets', 'v4', credentials=creds)          
    
        name  = request.POST['name']
        mobile  = request.POST['mobile']
        print(name, mobile)
        ## call update function to add this to DataBase

        # Get the current date and time
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    
        # Create a new row in the Google Sheets document with the user data
        values = [[timestamp, name, mobile]]
        body = {'values': values}
        result = service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
            valueInputOption='USER_ENTERED', body=body).execute()

    except:
        return HttpResponse("Issue is parsing form Data, Try again :)")
    return HttpResponse("Request has been updated in the Data-Base")
    #return render(request, 'my_app/result.html',)