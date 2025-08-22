# 7.3.1. Асинхронное программирование
# 7.3.2. Библиотека g4f
# 7.3.3. Потоковый вывод данных
# 7.3.4. Генерация изображений

import asyncio
from g4f.client import AsyncClient

async def main():
    client = AsyncClient()
    
    response = await client.images.generate(
        prompt="a white siamese cat",
        model="flux",
        response_format="url"
        # Add any other necessary parameters
    )
    
    image_url = response.data[0].url
    print(f"Generated image URL: {image_url}")

asyncio.run(main())
