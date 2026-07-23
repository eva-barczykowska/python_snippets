import asyncio
import datetime

# Define an asynchronous function using 'async def'
async def greet_after_delay(name, delay):
    print(f"{datetime.datetime.now()} - Started greeting {name}")
    await asyncio.sleep(delay)  # Simulate a non-blocking delay - what does this mean?
    print(f"{datetime.datetime.now()} - Hello, {name}!")

# Main function to run the asynchronous code
async def main():
    # Schedule two asynchronous tasks concurrently
    task1 = asyncio.create_task(greet_after_delay("Alice", 20))
    task2 = asyncio.create_task(greet_after_delay("Bob", 10)) # how much time are we waiting here?

    # Both tasks will be executed concurrently
    await task1  # Wait for task1 to finish
    await task2  # Wait for task2 to finish

# Run the main event loop
asyncio.run(main())
print(f"{datetime.datetime.now()} - After")
