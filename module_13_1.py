import asyncio

async def  start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1,6):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task = asyncio.create_task(start_strongman('Pasha', 3))
    task = asyncio.create_task(start_strongman('Denis', 4))
    task = asyncio.create_task(start_strongman('Apollon', 5))
    await task
asyncio.run(start_tournament())
