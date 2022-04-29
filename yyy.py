import asyncio


async def generator(n):
    i = 0
    while i < n:
        yield 2 ** i
        i += 1
        await asyncio.sleep(1)

async def main(n):
    gen = [i async for i in generator(n)]
    return gen

print(asyncio.run(main(10)))