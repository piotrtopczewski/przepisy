from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Iterator, Literal, Optional

import streamlit as st

from db import Recipe, RecipeFilter, RecipeRepository, create_tables, get_session, DATA_DIR


IMAGE_DIR = DATA_DIR / "images"


@contextmanager
def recipe_repository() -> Iterator[RecipeRepository]:
    for session in get_session():
        repo = RecipeRepository(session)
        try:
            yield repo
        finally:
            # session is closed in get_session
            pass


def initialize() -> None:
    if not st.session_state.get("db_initialized"):
        create_tables()
        IMAGE_DIR.mkdir(parents=True, exist_ok=True)
        st.session_state["db_initialized"] = True


def add_recipe_view() -> None:
    st.header("Dodaj przepis")

    uploaded_file = st.file_uploader(
        "Zdjęcie przepisu", type=["jpg", "jpeg", "png"], accept_multiple_files=False
    )
    title = st.text_input("Tytuł przepisu")
    description = st.text_area("Opis przepisu")

    can_save = bool(uploaded_file and title.strip() and description.strip())

    if st.button("Zapisz przepis", disabled=not can_save):
        if not uploaded_file:
            st.error("Dodaj zdjęcie przepisu.")
            return

        safe_title = title.strip().replace(" ", "_")
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
        extension = Path(uploaded_file.name).suffix.lower() or ".jpg"
        filename = f"{timestamp}_{safe_title}{extension}"
        image_path = IMAGE_DIR / filename

        with image_path.open("wb") as buffer:
            buffer.write(uploaded_file.getbuffer())

        with recipe_repository() as repo:
            recipe = repo.add_recipe(
                title=title,
                description=description,
                image_path=str(image_path),
            )

        st.success(f"Przepis został zapisany (ID: {recipe.id}).")


def list_recipes_view() -> None:
    st.header("Lista przepisów")

    search_query = st.text_input("Szukaj po tytule", "")

    sort_field_label = st.selectbox(
        "Sortuj według",
        options=["Data dodania", "Tytuł"],
        index=0,
    )
    sort_direction_label = st.radio(
        "Kierunek sortowania",
        options=["Malejąco", "Rosnąco"],
        horizontal=True,
        index=0,
    )

    sort_field: Literal["created_at", "title"]
    if sort_field_label == "Tytuł":
        sort_field = "title"
    else:
        sort_field = "created_at"

    sort_direction: Literal["asc", "desc"]
    if sort_direction_label == "Rosnąco":
        sort_direction = "asc"
    else:
        sort_direction = "desc"

    filters = RecipeFilter(
        title_query=search_query or None,
        sort_field=sort_field,
        sort_direction=sort_direction,
    )

    with recipe_repository() as repo:
        recipes = repo.list_recipes(filters)

    if not recipes:
        st.info("Brak przepisów spełniających kryteria wyszukiwania.")
        return

    options = {f"{recipe.id} — {recipe.title}": recipe.id for recipe in recipes}
    selected_label = st.selectbox("Wybierz przepis", list(options.keys()))
    selected_id = options[selected_label]

    selected_recipe: Optional[Recipe]
    selected_recipe = next((r for r in recipes if r.id == selected_id), None)

    if not selected_recipe:
        st.error("Nie udało się odczytać wybranego przepisu.")
        return

    st.subheader(selected_recipe.title)
    st.write(selected_recipe.description)

    image_path = Path(selected_recipe.image_path)
    if image_path.is_file():
        st.image(str(image_path), caption=selected_recipe.title)
    else:
        st.warning("Nie znaleziono pliku ze zdjęciem przepisu.")

        uploaded_file = st.file_uploader(
            "Dodaj brakujące zdjęcie", type=["jpg", "jpeg", "png"], key="add_image_uploader"
        )
        if uploaded_file and st.button("Zapisz zdjęcie"):
            safe_title = selected_recipe.title.strip().replace(" ", "_")
            timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
            extension = Path(uploaded_file.name).suffix.lower() or ".jpg"
            filename = f"{timestamp}_{safe_title}{extension}"
            new_image_path = IMAGE_DIR / filename

            IMAGE_DIR.mkdir(parents=True, exist_ok=True)
            with new_image_path.open("wb") as buffer:
                buffer.write(uploaded_file.getbuffer())

            with recipe_repository() as repo:
                repo.update_image_path(selected_recipe.id, str(new_image_path))

            st.success("Zdjęcie zostało zapisane dla tego przepisu.")
            return

    if st.button("Usuń przepis"):
        if image_path.is_file():
            image_path.unlink()
        with recipe_repository() as repo:
            repo.delete_by_id(selected_recipe.id)
        st.success("Przepis został usunięty.")
        return


def main() -> None:
    st.set_page_config(page_title="Przepisy", layout="wide")
    initialize()

    st.sidebar.title("Nawigacja")
    view = st.sidebar.radio(
        "Wybierz widok",
        options=["Dodaj przepis", "Lista przepisów"],
    )

    if view == "Dodaj przepis":
        add_recipe_view()
    else:
        list_recipes_view()


if __name__ == "__main__":
    main()

