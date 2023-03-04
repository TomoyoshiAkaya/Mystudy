import functions_framework
import datetime
import os
import re
import google.auth
import google.cloud.bigquery

slots = [0, 30, 30, 30]
tables = [1, 2, 3, 4] 
# BigQueryのクライアント生成
client = google.cloud.bigquery.Client()


def find_availability(table_no, start_time, end_time):
    st = start_time
    et = end_time
    SQL = f"SELECT COUNT(*) FROM [PJID].izakaya.reserve{table_no} WHERE (start_time < \"{et}\" and \"{et}\" < end_time) or (start_time < \"{st}\" and \"{st}\" < end_time)" 
    query_job = client.query(SQL)
    
    for row in query_job:
        row2 = dict(zip(str(table_no), row))
        if row2[str(table_no)] == 1:
            continue
        else:
            return row2

def find_slots(start_time, end_time):
    st = start_time
    available_slots = []
    for slot in slots:
        st = st + datetime.timedelta(minutes=slot)
        for table_no in tables:
            available = find_availability(table_no, start_time, end_time)
            if available:
                available_slots.append((table_no, st))

    resdict = {}
    for i in available_slots:
        resdict.setdefault(i[1], []).append(i[0])

    return resdict

def rescheck(request):
    # build a request object
    req = request.get_json()
    year = req.get('sessionInfo').get('parameters').get('date-time').get('year')
    year = int(year)
    month = req.get('sessionInfo').get('parameters').get('date-time').get('month')
    month = int(month)
    day = req.get('sessionInfo').get('parameters').get('date-time').get('day')
    day = int(day)
    hour = int(re.split('時', req.get('sessionInfo').get('parameters').get('starttime'))[0])
    duration = int(re.split('分|時間', req.get('sessionInfo').get('parameters').get('duration'))[0])
    number = req.get('sessionInfo').get('parameters').get('number')
    number = int(number)

    start_time = datetime.datetime.strptime(f"{year}-{month}-{day} {hour}:01", '%Y-%m-%d %H:%M')
        
    if duration == 1 or duration ==2:
        end_time = start_time + datetime.timedelta(hours = duration)
    else:
        end_time = start_time + datetime.timedelta(minutes = duration)
        
    dlst = list(find_slots(start_time, end_time).keys())
    datelist = [ (m - datetime.timedelta(minutes=1)).strftime('%Y年%m月%d日%H時%M分') for m in dlst ]
    countlist = list(find_slots(start_time, end_time).values())

    reslist = []
    for n in range(len(slots)):
        if len(countlist[n]) > number:
            m = n + 1
            reslist.append(f"{m}：{datelist[n]}：{number}名様")
        else:
            continue

    if len(reslist) == 0:
        reslist.append("ご予約可能なお席がございません。")
        
    options = [dict(text=x) for x in reslist]
        
    res = {"fulfillment_response": {
            "messages": [
                {
                    "payload": {
                        "richContent": [
                            [
                            {
                                "type": "chips",
                                "options": []
                            }
                            ]
                        ]
                    }
                }
            ]
        },"sessionInfo" : {
                 "parameters" : { 
                          "table1": dlst,
                          "table2": countlist
                          }
                          }
        }
        
    res["fulfillment_response"]["messages"][0]["payload"]["richContent"][0][0]["options"] = options
        
    return res
