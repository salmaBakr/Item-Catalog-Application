import sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(String(250), primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	picture = Column(String(250))

class Category(Base):
	__tablename__ ='category'
	name = Column(String(250)) 
	id = Column(Integer, primary_key = True)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'name': self.name,
			'id': self.id,
		}


class Item(Base):
	__tablename__ = 'item'
	id = Column(Integer, primary_key = True) 
	title = Column(String(250)) 
	description = Column(String(250)) 
	category_id = Column(Integer, ForeignKey(Category.id))
	category = relationship(Category)
	user_id = Column(String(250), ForeignKey('user.id'))
	user = relationship(User)

# We added this serialize function to be able to send JSON objects in a
# serializable format
	@property
	def serialize(self):
		return {
			'title': self.title,
			'description': self.description,
			'id': self.id,
		}

engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)


		