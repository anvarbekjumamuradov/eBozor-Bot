from environs import Env


# environs kutubxonasidan foydalanish
env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
