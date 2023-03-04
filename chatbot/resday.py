import functions_framework
import datetime
 
def res_day(request):
        # build a request object
        req = request.get_json()
        daylist = []
        DIFF_JST_FROM_UTC = 9
        day = (datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)).date()
                
        for i in range(5):
            day1 = day + datetime.timedelta(days = i)
            daylist.append(day1.strftime('%Y年%m月%d日'))
              
        res = { "fulfillment_response": {
                "messages": [
                    {
                        "payload": {
                            "richContent": [
                                [
                                {
                                    "type": "chips",
                                    "options": [
                                    {
                                        "text": f"{daylist[0]}",
                                    },
                                    {
                                        "text": f"{daylist[1]}",
                                    },
                                    {
                                        "text": f"{daylist[2]}",
                                    },
                                    {
                                        "text": f"{daylist[3]}",
                                    },
                                    {
                                        "text": f"{daylist[4]}",
                                    }
                                    ]
                                }
                                ]
                            ]
                        }
                    }
                ]
            }
        }

        return res
