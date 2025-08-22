# 7.3.1. Асинхронное программирование
# 7.3.2. Библиотека g4f
# 7.3.3. Потоковый вывод данных

# Вывод потоковый 

import asyncio
from g4f.client import AsyncClient

async def main():
    client = AsyncClient()

    stream = client.chat.completions.stream(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Ты преподаватель Python в первом классе"
            },
            {
                "role": "user",
                "content": "Что такое библиотека g4f?"
            }
        ],
        web_search = False
    )

    async for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
            
asyncio.run(main())
