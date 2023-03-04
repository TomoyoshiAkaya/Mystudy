import functions_framework
import datetime
import google.cloud.bigquery

def insert_table(request):
    # BigQuery Data Transfer Service のクライアント生成
    client = google.cloud.bigquery.Client()

    # build a request object
    req = request.get_json()
    b = req.get('sessionInfo').get('parameters').get('table2')
    c = req.get('text').split('：', 2)
    n = int(c[0]) - 1
    start_time = datetime.datetime.strptime(c[1], "%Y年%m月%d日%H時%M分")
    i = [ int(m) for m in b[n]]
    i = i[:number]
    duration = int(re.split('分|時間', req.get('sessionInfo').get('parameters').get('duration'))[0])
    number = req.get('sessionInfo').get('parameters').get('number')
    number = int(number)
        
    if duration == 1 or duration ==2:
        end_time = start_time + datetime.timedelta(hours = duration)
    else:
        end_time = start_time + datetime.timedelta(minutes = duration)
  
    name = "test"
    telephone = "test"
    
    for n in i:
        # テーブルの定義
        table_id = f"[PJID].izakaya.reserve{n}"

        # テーブルにINSERT
    
        rows_to_insert = [
            {"start_time": f"{start_time}",
            "end_time": f"{end_time}",
            "name": f"{name}",
            "telephone": f"{telephone}" }  
            ]

        errors = client.insert_rows(table_id, rows_to_insert)  # Make an API request.
    
    return 200

