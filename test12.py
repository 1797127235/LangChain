import asyncio

async def boil_water():
    print("开始烧水")
    await asyncio.sleep(5)
    print("水烧开了")

async def send_message():
    print("开始发送消息")
    await asyncio.sleep(2)
    print("消息发送成功")

async def main():
    # asyncio.run(boil_water())
    # asyncio.run(send_message())
    task1 = asyncio.create_task(boil_water())
    task2 = asyncio.create_task(send_message())
    await task1
    await task2

if __name__ == "__main__":
    #run会创建一个事件循环
    asyncio.run(main())
