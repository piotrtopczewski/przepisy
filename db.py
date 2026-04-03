from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional

from sqlalchemy import Column, DateTime, Integer, String, create_engine, select, func
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


DATA_DIR = Path("data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_SQLITE_PATH = DATA_DIR / "przepisy.db"
DEFAULT_DATABASE_URL = f"sqlite:///{DEFAULT_SQLITE_PATH.as_posix()}"


class Base(DeclarativeBase):
    pass


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
    image_path: Mapped[str] = mapped_column(String(500), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False), nullable=False, default=datetime.utcnow
    )


engine = create_engine(
    DEFAULT_DATABASE_URL,
    echo=False,
    future=True,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)


@dataclass
class RecipeFilter:
    title_query: Optional[str] = None
    sort_field: str = "created_at"  # "created_at" | "title"
    sort_direction: str = "desc"  # "asc" | "desc"


class RecipeRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def add_recipe(self, title: str, description: str, image_path: str) -> Recipe:
        recipe = Recipe(
            title=title.strip(),
            description=description.strip(),
            image_path=image_path,
        )
        self._session.add(recipe)
        self._session.commit()
        self._session.refresh(recipe)
        return recipe

    def list_recipes(self, filters: RecipeFilter) -> List[Recipe]:
        stmt = select(Recipe)

        if filters.title_query:
            query = f"%{filters.title_query.strip().lower()}%"
            stmt = stmt.where(func.lower(Recipe.title).like(query))

        if filters.sort_field == "title":
            order_column = Recipe.title
        else:
            order_column = Recipe.created_at

        if filters.sort_direction == "asc":
            stmt = stmt.order_by(order_column.asc())
        else:
            stmt = stmt.order_by(order_column.desc())

        result = self._session.execute(stmt)
        return list(result.scalars().all())

    def get_by_id(self, recipe_id: int) -> Optional[Recipe]:
        stmt = select(Recipe).where(Recipe.id == recipe_id)
        result = self._session.execute(stmt).scalar_one_or_none()
        return result

    def delete_by_id(self, recipe_id: int) -> None:
        recipe = self.get_by_id(recipe_id)
        if recipe is None:
            return
        self._session.delete(recipe)
        self._session.commit()

    def update_image_path(self, recipe_id: int, image_path: str) -> None:
        recipe = self.get_by_id(recipe_id)
        if recipe is None:
            return
        recipe.image_path = image_path
        self._session.commit()


def get_session() -> Iterable[Session]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

