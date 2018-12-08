from core.Tasks import CommonTasks
from core.Spider import Spider
import asyncio
import json


# if __name__ == '__main__':
#     task_list = []
#     url = [
#         'https://www.freebuf.com/vuls/126499.html',
#         'https://xz.aliyun.com/t/3264',
#         'https://xz.aliyun.com/t/2225',
#         'https://xz.aliyun.com/t/2651',
#     ]
#     # url = [
#     #     'https://xz.aliyun.com/t/2651',
#     # ]
#     for i in url:
#         request = Producer.set_request(i, 'freebuf', 'test')
#         task_list.append(request)
#     asyncio.run(Tasks.create_tasks(task_list))

# if __name__ == '__main__':
#     check = Check()
#     asyncio.run(check.check_authorization_code(), debug=True)

# if __name__ == '__main__':
#     worker = Worker()
#     butter = bytes
#     with open('authorization_code.json', 'r') as f:
#         token = json.load(f)
#     buffer = open('test.pdf', 'rb')
#     tag = '/test/demo1/demo.pdf'
#     print(buffer)
#     print('----------------------')
#     asyncio.run(worker.upload_worker(token['authorization'], buffer, tag))

# if __name__ == '__main__':
#     url = 'https://www.freebuf.com/vuls/126499.html'
#     worker = Worker()
#     asyncio.run(worker.spider_worker(url))

# if __name__ == '__main__':
#     tasks = CommonTasks()
#     url = 'https://www.freebuf.com/vuls/126499.html'
#     asyncio.run(tasks.create_tasks(url, 'sniper/test'))

if __name__ == '__main__':
    spider = Spider()
    url = 'https://www.anquanke.com/post/id/167384'
    asyncio.run(spider.spider(url))

