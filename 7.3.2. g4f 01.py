# 7.3.1. Асинхронное программирование
# 7.3.2. Библиотека g4f

# Вывод сразу полностью готового ответа

import asyncio
from g4f.client import AsyncClient

async def main():
    client = AsyncClient()
    
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "Скажи, какое сегодня число?"
            }
        ],
        
        
    )
    
    print(response.choices[0].message.content)

asyncio.run(main())