from epl import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from typing import List

class Club(db.Model):
  __tablename__ = 'club'
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
  stadium: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
  year: Mapped[int] = mapped_column(Integer, nullable=False)
  logo: Mapped[str] = mapped_column(String(255), nullable=False)

  players: Mapped[List['Player']] = relationship(back_populates='club')

  def __repr__(self):
    return f'<Club: {self.name}>'
  
class Player(db.Model):
  __tablename__ = 'player'
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
  position: Mapped[str] = mapped_column(String(20), nullable=False)
  nationality: Mapped[str] = mapped_column(String(30), nullable=False)
  goal: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
  clean_sheets: Mapped[int] = mapped_column(Integer, nullable=True)
  squad_no: Mapped[int] = mapped_column(Integer, nullable=True)
  img: Mapped[str] = mapped_column(String(255), nullable=False)
  club_id: Mapped[int] = mapped_column(Integer, ForeignKey(Club.id))

  club: Mapped[Club] = relationship(back_populates='players')

  def __repr__(self):
    return f'<Player: {self.name}>'