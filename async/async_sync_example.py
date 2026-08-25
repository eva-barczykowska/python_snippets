# import asyncio
#
#
# async def greet(word):
#     for _ in range(5):
#         await asyncio.sleep(0.001)
#         print(word)
#
#
# loop = asyncio.get_event_loop()
#
# loop.create_task(greet('hello'))
# loop.create_task(greet('goodbye'))
#
# tasks = asyncio.all_tasks(loop=loop)
# group = asyncio.gather(*tasks)
# loop.run_until_complete(group)

#
# import warnings
# warnings.filterwarnings("ignore")
#
# import requests
# import time
#
# urls = ['https://nytimes.com',
#         'https://python.org',
#         'https://us.pycon.org']
#
# sizes = {}
#
# start_time = time.time()
#
# for one_url in urls:
#     print(one_url)
#     content = requests.get(one_url).content
#     sizes[one_url] = len(content)
#
# total_time = time.time() - start_time
# print(f'It took {total_time} seconds') # It took 1.6350290775299072 seconds

# same but with asyncio, but this will not work
#!/usr/bin/env python3

import warnings
warnings.filterwarnings("ignore")
import time
import requests
import asyncio


urls = ['https://nytimes.com',
            'https://python.org',
            'https://us.pycon.org']

sizes = {}


async def measure_url_content(one_url):
        print(one_url)
        content = requests.get(one_url).content
        sizes[one_url] = len(content)


loop = asyncio.get_event_loop()

start_time = time.time()
for one_url in urls:
    loop.create_task(measure_url_content(one_url))

tasks = asyncio.all_tasks(loop=loop)
group = asyncio.gather(*tasks)
loop.run_until_complete(group)

total_time = time.time() - start_time
print(f'It took {total_time} seconds') #It took 2.7863478660583496 seconds so it is NOT FASTER AT ALL



