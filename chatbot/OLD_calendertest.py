import functions_framework
import datetime
 
from flask import abort
 
import google.auth
from googleapiclient.discovery import build

def calender(request):
    # 実行環境のデフォルトクレデンシャル = Cloud Functions にアタッチされているサービスアカウントを取得
    credentials, project = google.auth.default()

    # サービスを生成
    service = build('calendar', 'v3', credentials=credentials, cache_discovery=False) 

    # Google Calendar API 呼び出し
    #result = service.events().list(
    #    calendarId='dokutapakase@gmail.com',
    #    timeMin='2022-01-01T00:00:00.000000Z',
    #    timeMax='2022-12-31T23:59:59.999999Z',
    #    singleEvents=True,
    #    orderBy='startTime'
    #).execute()
    #calender_info = result.get('items', [])

    #return calender_info

    event={
               'summary':'insert test',
               'description':8,
               'start':{
                        'dateTime': '2022-12-25T19:00:00',
                        'timeZone': 'Asia/Tokyo',
                      },
               'end':{
                      'dateTime': '2022-12-25T20:00:00',
                      'timeZone': 'Asia/Tokyo',
                      },
                      }
    service.events().insert(calendarId='dokutapakase@gmail.com', body=event).execute()
    return

