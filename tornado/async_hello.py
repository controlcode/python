import asyncio
loop = asyncio.get_event_loop()

@asyncio.coroutine
def hello():
  print('Hello')
  yield from asyncio.sleep(10)
  print('World!')

if __name__ == '__main__':
  tasks = [hello(), hello(), hello()]
  loop.run_until_complete(asyncio.wait(tasks))
  #loop.run_until_complete(hello())
