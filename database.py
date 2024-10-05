from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Вкажіть URL до вашої бази даних
DATABASE_URL = "sqlite:///database.db"  # Тут може бути ваш URL, якщо використовується інший тип бази даних

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
