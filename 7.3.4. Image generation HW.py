# 7.3.1. Асинхронное программирование
# 7.3.2. Библиотека g4f
# 7.3.3. Потоковый вывод данных
# 7.3.4. Генерация изображений

import asyncio
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from g4f.client import AsyncClient

class ImageGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Image Generator")
        self.root.geometry("600x700")
        
        # Поле ввода промпта
        ttk.Label(root, text="Prompt:").pack(pady=5)
        self.prompt_entry = ttk.Entry(root, width=50)
        self.prompt_entry.pack(pady=5)
        self.prompt_entry.insert(0, "a white siamese cat")
        
        # Кнопка генерации
        self.generate_btn = ttk.Button(root, text="Generate Image", command=self.generate_image)
        self.generate_btn.pack(pady=10)
        
        # Лейбл для изображения
        self.image_label = ttk.Label(root)
        self.image_label.pack(pady=10)
        
        # Статус
        self.status_label = ttk.Label(root, text="Ready")
        self.status_label.pack(pady=5)
    
    def generate_image(self):
        self.status_label.config(text="Generating image...")
        self.generate_btn.config(state="disabled")
        self.root.update()
        
        # Запуск асинхронной функции
        asyncio.run(self.async_generate())
    
    async def async_generate(self):
        try:
            client = AsyncClient()
            
            response = await client.images.generate(
                prompt=self.prompt_entry.get(),
                model="flux",
                response_format="url"
            )
            
            image_url = response.data[0].url
            
            # Загрузка и отображение изображения
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            
            # Изменение размера для окна
            image.thumbnail((500, 500))
            photo = ImageTk.PhotoImage(image)
            
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Сохранение ссылки
            
            self.status_label.config(text="Image generated successfully!")
            
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")
        
        finally:
            self.generate_btn.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGeneratorApp(root)
    root.mainloop()
