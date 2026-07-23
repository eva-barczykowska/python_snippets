import asyncio

from sqlalchemy.util import await_only


class MySingleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MySingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.var = 0
        self.var2 = 0

    async def increment(self):
        self.var = self.var + 1



async def my_task():
    #print("my_task")
    a = MySingleton()
    await a.increment()
    print(id(a), a.var)


async def main_sync():

    task = [my_task() for i in range(5)]
    await asyncio.gather(*task)


def main():
    a = MySingleton()
    b = MySingleton()
    print(a.var2)
    a.var2 = 100
    print(b.var2)


if __name__ == '__main__':
    loop = asyncio.run(main_sync())
    main()

# result:
# 4351323104 1
# 4351323104 1
# 4351323104 1
# 4351323104 1
# 4351323104 1

# In the my_task function, each instance of MySingleton is
# created independently. When the increment method is called asynchronously,
# it only modifies the var attribute of the instance it belongs to.
# To make the class behave as a singleton and increase the var attribute
# correctly, you can modify the increment method to use the class instance instead of creating a new one. Here's an updated version of the code:
### Question:
# WHy does this calss not behave as singleton, the value or a is not increased... How to increase it coz it's a singleton... even though we call asynchronously but we call the same instance so the value or a should be increased, right?
#
# ### Answer:
# The class `MySingleton` is indeed a singleton, but the asynchronous nature of the code is causing some unexpected behavior.
#
# In the `my_task` function, each instance of `MySingleton` is created independently. When the `increment` method is called asynchronously, it only modifies the `var` attribute of the instance it belongs to.
#
# To make the class behave as a singleton and increase the `var` attribute correctly, you can modify the `increment` method to use the class instance instead of creating a new one. Here's an updated version of the code:

print('---------------')
import asyncio

from sqlalchemy.util import await_only


class MySingleton:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MySingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.var = 0
            self.var2 = 0
            MySingleton._initialized = True  # use class var, not self

    async def increment(self):
        self.var = self.var + 1



async def my_task():
    a = MySingleton()
    await a.increment()
    print(id(a), a.var)


async def main_sync():

    task = [my_task() for i in range(5)]
    await asyncio.gather(*task)


def main():
    a = MySingleton()
    b = MySingleton()
    print(a.var2)
    a.var2 = 100
    print(b.var2)


if __name__ == '__main__':
    loop = asyncio.run(main_sync())
    main()
