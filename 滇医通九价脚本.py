# by Cat00011cat
# 本测试仅供学习研究，请勿用于非法用途。
# 侵权邮件联系 990667303@qq.com 立即删除

import requests
import json

'''
昆明医科大学第一附属医院一般是周二、周三、周四早上6：30放苗；

昆明市第一人民医院北院（甘美医院）一般是周二、周三、周四、周五早上8：00放苗；

昆明市妇幼保健院（丹霞路院区）一般为周二、周三、周六、周日早上8：00放苗；

昆明市妇幼保健院（华山院区）一般为：周二、周六、周日早上8：00放苗；

关上街道社区卫生服务中心一般在每天早上8：30分放苗
'''

# 基本信息  必要参数 防止被检测出刷
hos_code = "";     # 医院id   昆明第一人民医院 甘美医院
dep_id = "";          # 医院的总疫苗选择页id
doc_id = "";         # 医院的预约疫苗类型的id

pat_id = "";       # 就诊人信息id
user_id = "";       # 滇医通登录用户id

# 凭证会过期  。。。 所以在有开放预约前一分钟进行探测
Authorization = "DYT eyJhbGciOiJI456456445646UzI1NiJ9.eyJ3ZWNoYXRfaWQiOjE1NzAzNzcsInN1YnNjcmliZSI6MCwiZHpqX3N1YnNjcmliZSI6MCwib3BlbmlkIjoib19VMzZzejhMOEZXZVRsR0NMU01mSlZTdUE0TSIsInRoaXJkX3VzZXJfaWQiOiIiLCJpc3MiOiJkeXQiLCJuZXdfc3Vic2NyaWJlIjoxLCJuZXdfb3BlbmlkIjoibzdMQ1g2RGljVDRVcG1XbkswNEdfZ0ZDYWhfcyIsInVzZXJfaWQiOjI3ODMwNDUsIndlY2hhdF9vcGVuX2lkIjoib19VMzZzejhMOEZXZVRsR0NMU01mSlZTdUE0TSIsInVuaW9uX2lkIjoib05RejQwYl85a2t4VnpxVmI5blZHTFlIenFaayIsIm1vY2tfb3BlbmlkIjpmYWxzZSwibWluaV9vcGVuaWQiOiJvaUE0UDVQYlRDdXpMWlBIVWlBUDFjMFYxbTdnIiwiZXhwIjoxNjgzOTAzNDQ3LCJpYXQiOjE2ODM4OTc4NDd9.LpD3g-xJ1D6klhEmHCS28Ke1TQjOR_QLAwvp56t5Kvk";      # 滇医通的登录凭证
x_uuid = "34BB6F3116458FCA769B2B3B15040C28";      # 滇医通的登录认证

acw_tc = "acw_tc=2760824516838778689681158ee656344382b393fc17a42773f0a60fd19b1f";      # 浏览器Cookie
UserAgent = 'Mozilla/5.0 (Linux; U; Android 10; zh-cn; Redmi Note 8 Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.8.14'

# 提交九价疫苗订单信息
'''
schedule_id     # 医生的排班表 ID
sch_date        # 排班日期
time_type       # 时段 "1", "早上" 或 "2", "下午"
'''
def sub(schedule_id, sch_date, time_type):
        appointUrl = "https://dytapi.ynhdkc.com/v1/appoint?hos_code={}&dep_id={}&doc_id={}&pat_id={}&user_id={}&schedule_id={}&cate_name=".format(hos_code,dep_id,doc_id,pat_id,user_id,schedule_id)

        headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'Authorization': Authorization,
        'User-Agent': UserAgent,
        'x-uuid': x_uuid,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://appv2.ynhdkc.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh',
        'Cookie': '_ga=GA1.2.1272911943.1683888038; _gid=GA1.2.274727360.1683888038; acw_tc=2760776d16838886437011939e0f98d71184500b0aa4c4b2c947be650f84fb'
        }

        data = {
        "doc_name": "进口九价宫颈癌疫苗",           # 标题
        "hos_name": "昆明市第一人民医院北院(甘美医院)-疫苗",      # 医院名称
        "hos_code": hos_code,                                 # 医院id
        "dep_name": "成人疫苗预约", 
        "level_name": "疫苗", 
        "dep_id": dep_id,                                      # 医院的总疫苗选择页id
        "doc_id": doc_id,                                     # 医院的预约疫苗类型的id
        "pat_id": pat_id,                                   # 就诊人信息id 
        "schedule_id": schedule_id,                               # 排班id
        "jz_card": "", 
        "sch_date": sch_date ,                             # 排班时间 "2023-05-13"
        "time_type": time_type,                                     # 时段 1为早上，2为下午
        "info": "", 
        "ghf": 0, 
        "zlf": 0, 
        "zjf": 0, 
        "jz_start_time": 0, 
        "amt": 0, 
        "jz_card_type": 0, 
        "queue_sn_id": "", 
        "wechat_login": "dytminiapp"
        }

        response = requests.request("POST", appointUrl, headers=headers, data=data)
        resp = json.loads(response.text)
        # print(resp)   # 打印响应信息
        msg = resp['msg']
        # 判断是否预约成功，并且发送通知
        if msg.find("预约成功") != -1:
            print("预约成功！")
        else:
            print(msg)


def push():
    url = "http://www.pushplus.plus/send/8d90abe455fe48e880028871c76ecea2"

    payload = 'token=8d90abe455fe48e880028871c76ecea2&title=甘美医院放苗了！！！1&content={}E&channel=mail'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


# 获取挂号（号源）列表  使用while暴力循环探测疫苗号源，程序请在疫苗开枪前30s内开启，请勿长时间使用程序探测号源，避免后台把该接口封死。
def check():
    url = "https://newdytapi.ynhdkc.com/index/schedule?hos_code={}&dep_id={}&doc_id={}".format(hos_code,dep_id,doc_id)
    payload = {}
    headers = {
    'Cookie': acw_tc,
    'User-Agent': UserAgent
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    haoyuanList = json.loads(response.text)
    print('昆明市第一人民医院北院（甘美医院）-疫苗- 九价号源探测')
    print('===========================================================================================================================','\n')
    hLen = len(haoyuanList['data'])
    print('探测到', hLen, '条挂号信息列表')
    # 显示打印+疫苗号源列表遍历,从后往前遍历（抢），增加抢到概率。
    for i in range(hLen):
        print('排班编号：',haoyuanList["data"][i]["schedule_id"], '排班日期：',haoyuanList["data"][i]["sch_date"], '时段：',haoyuanList["data"][i]["time_type"], '日期：',haoyuanList["data"][i]["sch_date"], '时间：',haoyuanList["data"][i]["cate_name"], '时段：',haoyuanList["data"][i]["time_type"], '总号源：',haoyuanList["data"][i]["src_max"], '剩余号源：',haoyuanList["data"][i]["src_num"])
        
        # 判断列表是否存在剩余号源
        if haoyuanList['data'][i]['src_num'] != 0:
            # 尝试挂号预约，如果提交成功，退出while，程序结束！
            if sub():
                    push() # 发送通知提醒抢号成功
                    break # 退出探测 程序结束 
        else:
            print('当前没有探测到号源可以预约','\n')
    print('===========================================================================================================================','\n')

if __name__ == '__main__':
    while True:
        check()
#sub(1,1,1)
