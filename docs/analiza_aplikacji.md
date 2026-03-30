# Analiza i projekt aplikacji do zarządzania przepisami kuchennymi

**Data:** 13 czerwca 2025

## Spis treści
1. Analiza podobnych aplikacji
2. Proponowane biblioteki i modele językowe
3. Schemat aplikacji
4. Plan rozwoju wersji
5. Szczegółowy opis funkcjonalności

## Analiza podobnych aplikacji

Na rynku istnieje kilka aplikacji do zarządzania przepisami kuchennymi, ale niewiele z nich wykorzystuje zaawansowane możliwości AI do rozpoznawania tekstu z obrazów i wyszukiwania semantycznego. Oto najważniejsze istniejące rozwiązania:

1. **Paprika Recipe Manager**
   - Pozwala na zapisywanie przepisów z internetu
   - Brak wbudowanego OCR
   - Brak wyszukiwania semantycznego
   - Dobre zarządzanie kategoriami i tagami

2. **Evernote Food** (już nierozwijana)
   - Zapisywanie notatek dotyczących jedzenia
   - Podstawowe OCR
   - Brak zaawansowanego wyszukiwania semantycznego

3. **ChefTap**
   - Automatyczne importowanie przepisów ze stron internetowych
   - Brak wbudowanego OCR
   - Ograniczone możliwości wyszukiwania

4. **Mela**
   - Nowoczesny interfejs
   - Ograniczone możliwości wyszukiwania i kategoryzacji
   - Brak zaawansowanych funkcji AI

5. **Notion + szablony przepisów**
   - Elastyczność w organizacji przepisów
   - Brak dedykowanego OCR dla przepisów
   - Bez dedykowanego wyszukiwania semantycznego dla przepisów

**Nisza rynkowa:** Brakuje rozwiązania, które łączyłoby zaawansowane rozpoznawanie tekstu z obrazów (OCR) specjalizowane pod kątem przepisów kuchennych z wyszukiwaniem semantycznym opartym o najnowsze modele językowe. Proponowana aplikacja wypełni tę lukę.

## Proponowane biblioteki i modele językowe

### OCR (Optical Character Recognition)
1. **Tesseract OCR** - sprawdzona biblioteka open-source do rozpoznawania tekstu
2. **EasyOCR** - wielojęzyczna biblioteka OCR oparta na PyTorch, dobra obsługa języków europejskich
3. **Microsoft Azure Computer Vision** / **Google Cloud Vision API** - dla lepszej jakości OCR, ale wiąże się z kosztami
4. **PaddleOCR** - wysoka dokładność, obsługa wielu języków, dobre rozpoznawanie tekstu w różnych układach

### Przetwarzanie języka naturalnego
1. **Sentence Transformers** - do generowania embeddingów do wyszukiwania semantycznego
2. **BERT** / **RoBERTa** - dla zrozumienia kontekstu przepisów
3. **GPT-4** / **Claude 3** - dla zaawansowanej analizy i poprawiania przepisów
4. **LLaMA 3** / **Mistral AI** - lokalne modele do uruchamiania na komputerze użytkownika

### Bazy danych i wektorowe
1. **Qdrant** - do przechowywania i wyszukiwania embeddingów (zgodnie z wymogami)
2. **SQLite** / **PostgreSQL** - do przechowywania metadanych przepisów
3. **Chroma** / **Milvus** - alternatywne bazy wektorowe (jeśli Qdrant okaże się niewystarczający)

### Frontend
1. **Streamlit** - szybki prototyp i rozwój aplikacji
2. **Flask** / **FastAPI** + **React** - bardziej zaawansowany interfejs
3. **PyQt** / **Tkinter** - dla aplikacji desktopowej
4. **Electron** - wieloplatformowa aplikacja desktopowa z UI webowym

### Przechowywanie plików
1. **System plików lokalny** - podstawowe przechowywanie obrazów i tekstów
2. **MinIO** - obiektowe przechowywanie plików (jeśli potrzebne bardziej zaawansowane rozwiązanie)

### RAG (Retrieval Augmented Generation)
1. **LangChain** / **LlamaIndex** - frameworki do budowania systemów RAG
2. **HuggingFace Transformers** - do dostępu do różnych modeli językowych

## Schemat aplikacji

*Schemat zostanie przygotowany w Excalidraw i załączony jako oddzielny plik.*

Główne komponenty aplikacji:
- **Moduł UI** - interfejs użytkownika do interakcji z aplikacją
- **Moduł OCR** - rozpoznawanie tekstu ze zdjęć i dokumentów
- **Moduł przetwarzania tekstu** - analiza, czyszczenie i strukturyzacja tekstu
- **Moduł bazy danych** - zarządzanie przepisami i metadanymi
- **Moduł embeddingów** - generowanie reprezentacji wektorowych przepisów
- **Moduł wyszukiwania** - wyszukiwanie przepisów (tekstowe i semantyczne)
- **System plików** - zarządzanie zapisanymi zdjęciami i dokumentami

## Plan rozwoju wersji

### Wersja 1.0 - Podstawowy system gromadzenia i wyszukiwania
- Interfejs użytkownika (podstawowy)
- Dodawanie przepisów (ręczne wprowadzanie)
- Podstawowy OCR dla zdjęć
- Zapisywanie przepisów na dysku w formacie tekstowym
- Proste wyszukiwanie pełnotekstowe
- Podstawowe zarządzanie atrybutami (tagi)

### Wersja 1.5 - Ulepszony OCR i zarządzanie
- Ulepszony OCR z możliwością rozpoznawania struktury przepisu (składniki, instrukcje)
- Poprawiony interfejs użytkownika
- Zaawansowane zarządzanie atrybutami (10 kategorii)
- Dodanie widoku listy wszystkich przepisów
- Proste edytowanie istniejących przepisów

### Wersja 2.0 - Wprowadzenie wyszukiwania semantycznego
- Integracja z Qdrant
- Generowanie embeddingów dla przepisów
- Implementacja podstawowego RAG
- Wyszukiwanie semantyczne przepisów
- Ulepszony interfejs użytkownika
- Eksport/import przepisów

### Wersja 2.5 - Zaawansowane AI i optymalizacja
- Integracja z zaawansowanymi modelami językowymi
- Automatyczne sugerowanie atrybutów na podstawie treści przepisu
- Automatyczne poprawianie i formatowanie przepisów
- Optymalizacja wydajności dla dużych kolekcji przepisów
- Zaawansowane filtrowanie wyników wyszukiwania

### Wersja 3.0 - Funkcje społecznościowe i integracje
- Synchronizacja z chmurą (opcjonalnie)
- Udostępnianie przepisów
- Integracja z popularnymi serwisami przepisów
- Rozpoznawanie przepisów ze stron internetowych
- Zaawansowana personalizacja interfejsu

## Szczegółowy opis funkcjonalności

### Zarządzanie przepisami
- **Dodawanie przepisów:**
  - Ręczne wprowadzanie
  - Rozpoznawanie z obrazu (OCR)
  - Import z pliku tekstowego
  - Dyktowanie (przetwarzanie mowy na tekst)

- **Edycja przepisów:**
  - Pełna edycja tekstu
  - Zmiana atrybutów
  - Dodawanie/usuwanie zdjęć

- **Usuwanie przepisów:**
  - Z możliwością archiwizacji zamiast trwałego usuwania

### Rozpoznawanie tekstu (OCR)
- Automatyczne rozpoznawanie tekstu ze zdjęć
- Wyodrębnianie struktury przepisu (tytuł, składniki, instrukcje)
- Sugerowanie tytułu przepisu na podstawie rozpoznanego tekstu
- Obsługa wielu formatów zdjęć (JPG, PNG, HEIF)
- Obsługa dokumentów (PDF, DOC)

### Atrybuty i kategoryzacja
- 10 głównych atrybutów do wyboru (np. wielkanoc, obiad, deser, wegetariańskie)
- Możliwość dodawania własnych słów kluczowych
- Automatyczne sugerowanie atrybutów na podstawie treści przepisu
- Filtry łączone przy wyszukiwaniu

### Wyszukiwanie
- **Wyszukiwanie pełnotekstowe:**
  - Przeszukiwanie tytułów i treści przepisów
  - Przeszukiwanie po atrybutach

- **Wyszukiwanie semantyczne:**
  - Wyszukiwanie przepisów podobnych koncepcyjnie
  - Wyszukiwanie za pomocą zapytań w języku naturalnym
  - Rankingowanie wyników według trafności

### Przechowywanie danych
- Zapisywanie przepisów w formacie tekstowym
- Przechowywanie zdjęć w folderze z przepisami
- Baza danych z metadanymi (atrybuty, daty, itp.)
- Baza wektorowa Qdrant dla embeddingów

### Interfejs użytkownika
- Przejrzysty widok listy przepisów
- Szczegółowy widok pojedynczego przepisu
- Przyjazny interfejs wyszukiwania
- Intuicyjny proces dodawania nowego przepisu
- Responsywny design (dla różnych rozmiarów ekranów)
