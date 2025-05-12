from aiogram import Bot, Dispatcher, executor
from app.handlers import user, operator, admin, custom, broadcast
from config import TOKEN

# Создаём экземпляры бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Регистрация обработчиков
user.register_handlers(dp)
operator.register_handlers(dp)
admin.register_handlers(dp)
custom.register_handlers(dp)
broadcast.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)