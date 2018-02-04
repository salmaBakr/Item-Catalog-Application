from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

category_1 = Category(id=1, user_id = 1, name = "cat_1")
session.add(category_1)
item_1 = Item(title = "item1",user_id = 1, id=1, description = "d1", category_id = 1)
session.add(item_1)

category_2 = Category(id=2, user_id = 1, name = "c2")
session.add(category_1)
item_2 = Item(title = "item2", user_id = 1, description = "d2", id=4, category_id=2)
session.add(item_1)

category_3 = Category(id=3, user_id = 1, name = "c3")
session.add(category_1)
item_3 = Item(title = "item3", user_id = 1, description="d3", id=3, category_id=2)
session.add(item_1)

session.commit()