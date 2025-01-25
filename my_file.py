import asyncio
import time

print('This file was cloned from my repository on GitHub!')

# это пример блокирующего кода
async def send_mail(num):
    print(f'Улетело сообщение {num}')
    await asyncio.sleep(1)  # Имитация отправки сообщения по сети
    print(f'Сообщение {num} доставлено')


async def main():
    for i in range(10):
        await send_mail(i)


start_time = time.time()
asyncio.run(main())
print(f'Время выполнения программы: {time.time() - start_time} с.')
