## 📝 Opis projektu

Projekt "Przepisy" (aplikacja RecipAI lub SmakoPamieć - do ustalenia) to nowoczesna aplikacja do zarządzania osobistą kolekcją przepisów kulinarnych z wykorzystaniem zaawansowanych technologii AI. Aplikacja umożliwia gromadzenie przepisów z różnych źródeł (zdjęcia, teksty drukowane, nagrania mowy), ich automatyczne rozpoznawanie, kategoryzowanie oraz zaawansowane wyszukiwanie zarówno tradycyjne, jak i semantyczne.

## 🎯 Główne funkcjonalności

- **Wieloźródłowe gromadzenie przepisów**: dodawanie przepisów poprzez zdjęcia, skanowanie tekstów, dyktowanie.
- **Zaawansowane OCR**: automatyczne rozpoznawanie tekstu ze zdjęć i dokumentów.
- **Inteligentne zarządzanie**: automatyczne propozycje tytułów, kategoryzacja przepisów.
- **Wszechstronne wyszukiwanie**: wyszukiwanie pełnotekstowe, po atrybutach oraz semantyczne (RAG).
- **Zarządzanie atrybutami**: elastyczny system słów kluczowych dla łatwej kategoryzacji przepisów.
- **Przyjazny interfejs**: prosty w obsłudze, intuicyjny interfejs użytkownika.

## 📚 Dokumentacja

Dokumentacja projektu składa się z następujących elementów:

1. [Analiza i projekt aplikacji](docs/analiza_aplikacji.md) - Szczegółowa analiza wymagań, podobnych aplikacji oraz plan rozwoju.
2. [Schemat aplikacji](docs/schemat_aplikacji_nowy.excalidraw) - Diagram architektury aplikacji (otworzyć w VS Code z rozszerzeniem Excalidraw).
3. [Propozycje techniczne](docs/rozwiazania_techniczne.md) - Szczegółowe propozycje dotyczące implementacji technicznej.
4. [EasyOCR vs Modele AI](docs/easyocr_vs_modele_ai.md) - Analiza różnic między EasyOCR a ogólnymi modelami AI w kontekście rozpoznawania tekstu.

## 🔄 Plan rozwoju

## Plan / Taski

### Wersja 1.0 - Podstawowy system gromadzenia i wyszukiwania

- wczytanie zdjęcia z przepisem
- zapis głosowy przepisu
- transkrypcja obrazu/dźwięku do tekstu (wyodrębnienie tytułu, składników, instrukcji)
- ew poprawa transkrypcji i zapis do pliku na dysku plus zapis zdjęcia
- przegląd (po tytułach) i odczytanie zapisanych przepisów wraz z widokiem oryginalnego zdjęcia (lub odtworzeniem notatki głosowej)
- proste wyszukanie pełnotekstowe
- obsługa klucza OpenAI

  
  ### Modyfikacja podejścia - v0.1
  
  - interfejs streamlit, streamlit cloud
  - baza sqlite w kontenerze, mozliwośc utraty
  - wczytanie i zapis zdjęcia/skanu z przepisem do bazy wraz z krótkim opisem
  - możliwośc przeglądu zapisanych przepisów 
  


### Wersja 1.5 - Dodatkowe atrybuty i lepsze wyszukiwanie

- import z plików PDF, DOC, txt
- transkrypcja PDF, DOC
- zarządzanie atrybutami (10 kategorii)
- własne słowa kluczowe (np. przepis babci)
- automatyczne sugerowanie atrybutów na podstawie treści przepisu
- uwzględnienie atrybutów w wyszukiwaniu pełnotekstowym

### Wersja 2.0 - Wprowadzenie wyszukiwania semantycznego

- integracja z Qdrant
- generowanie embeddingów dla przepisów (całego przepisu oraz oddzielnie dla tytułu i składników)
- implementacja podstawowego RAG
- wyszukiwanie semantyczne przepisów 
- rankingowanie wyników według trafności
- ulepszony interfejs użytkownika

### Wersja 2.5 - Przejście z zapisu plikowego na bazę danych

- zapis metadanych do bazy SQL (zdjęcia, głos, atrybuty, daty )
- odczyt metadanych z bazy SQL 
- wyszukiwanie pełnotekstowe po SQL
- wyszukiwanie po atrybutach w SQL

### Wersja 3.0 - Obsługa wielu użytkowników

- zakładanie użytkownika 
- logowanie użytkowników
- indywidualne kolekcje w qdrant dla userów
- archiwizacja bazy

### Wersja 4.0 - internet jako dodatkowe źródło przepisów

- możliwość ściągnięcia przepisu ze strony internetowej
- możliwość zaimportowania i przetworzenia filmu np. z youtube

### Wersja 5.0 - lokalny model LLM i OCR - redukcja kosztów

- wykorzystanie np. instalacji lokalnej Mistral/LLaMA 3 zamiast modeli płatnych
- wykorzystanie EasyOCR/TesseractOCR lub inne zamiast modeli płatnych

## 🛠️ Stos technologiczny

Projekt wykorzystuje następujące technologie:

- **Frontend**: PyQt/Tkinter lub React/Electron
- **Backend**: Python/FastAPI
- **OCR**: Tesseract, EasyOCR
- **Bazy danych**: SQLite/PostgreSQL + Qdrant
- **AI/ML**: Sentence Transformers, LangChain, LLaMA/Mistral

## 📊 Status projektu

Projekt jest obecnie w fazie planowania i projektowania. Aktualnie opracowywana jest szczegółowa koncepcja oraz prototyp interfejsu użytkownika.

## 🚀 Jak zacząć pracę z projektem

```bash
# Klonowanie repozytorium (gdy będzie dostępne)
git clone https://github.com/piotrtopczewski/przepisy.git

# Przejście do katalogu projektu
cd przepisy

# Instalacja zależności (gdy będą zdefiniowane)
pip install -r requirements.txt

# Uruchomienie aplikacji (gdy będzie zaimplementowana)
python main.py
```

---

© 2025 Przepisy App. Wszelkie prawa zastrzeżone.