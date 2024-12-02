import asyncio


async def main(filenames):
    names = []
    for filename in filenames:
        names.append(await read_file_async(filename))
        await asyncio.sleep(5)
    names_str = " ".join(name for name in names)
    return names_str
