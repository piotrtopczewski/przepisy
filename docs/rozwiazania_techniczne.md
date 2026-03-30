# Propozycja rozwiązań technicznych dla aplikacji "Przepisy"

**Data:** 13 czerwca 2025

## Spis treści
1. [Architektura aplikacji](#architektura-aplikacji)
2. [Stos technologiczny](#stos-technologiczny)
3. [Przepływ danych](#przepływ-danych)
4. [Implementacja OCR](#implementacja-ocr)
5. [Implementacja RAG](#implementacja-rag)
6. [Bezpieczeństwo danych](#bezpieczeństwo-danych)
7. [Wymagania sprzętowe](#wymagania-sprzętowe)

## Architektura aplikacji

Proponujemy architekturę modułową, która pozwoli na elastyczny rozwój aplikacji oraz umożliwi łatwe dodawanie nowych funkcjonalności w przyszłości. Aplikacja będzie oparta o wzorzec MVC (Model-View-Controller) z elementami wzorca Repository.

### Główne komponenty:

1. **Interfejs użytkownika** - odpowiedzialny za interakcję z użytkownikiem
2. **Kontrolery** - odpowiedzialne za obsługę logiki biznesowej
3. **Serwisy** - dostarczające funkcjonalności biznesowe
4. **Repozytoria** - zapewniające dostęp do danych
5. **Moduł OCR** - odpowiedzialny za rozpoznawanie tekstu z obrazów
6. **Moduł RAG** - obsługujący wyszukiwanie semantyczne
7. **System przechowywania plików** - zarządzający plikami na dysku

## Stos technologiczny

### Propozycja 1: Aplikacja desktopowa

```
Frontend: PyQt lub Tkinter (Python)
Backend: Python
OCR: Tesseract + EasyOCR
Baza danych: SQLite + Qdrant
Embeddings: Sentence Transformers
RAG: LangChain/LlamaIndex
LLM: Locally hosted model (Mistral, LLaMA)
```

### Propozycja 2: Aplikacja webowa

```
Frontend: React + Tailwind CSS
Backend: FastAPI (Python)
OCR: Tesseract + EasyOCR
Baza danych: PostgreSQL + Qdrant
Embeddings: Sentence Transformers
RAG: LangChain/LlamaIndex
LLM: OpenAI API lub Anthropic API
```

### Propozycja 3: Aplikacja hybrydowa (Electron)

```
Frontend: Electron (HTML/CSS/JavaScript)
Backend: Node.js + Python (bridge)
OCR: Tesseract + EasyOCR
Baza danych: SQLite + Qdrant
Embeddings: Sentence Transformers
RAG: LangChain/LlamaIndex
LLM: OpenAI API lub lokalny model
```

## Szczegółowe porównanie technologii OCR

| Technologia | Zalety | Wady | Koszt |
|-------------|--------|------|-------|
| **Tesseract OCR** | Darmowy, open-source, dojrzały | Mniej dokładny dla skomplikowanych layoutów | Bezpłatny |
| **EasyOCR** | Dobra obsługa wielu języków, dokładność | Wolniejszy niż niektóre alternatywy | Bezpłatny |
| **PaddleOCR** | Wysoka dokładność, dobre dla trudnych layoutów | Wymaga więcej zasobów | Bezpłatny |
| **Azure Computer Vision** | Wysoka dokładność, layout analysis | Wymaga połączenia z internetem, płatny | Od $1 za 1000 stron |
| **Google Cloud Vision** | Bardzo wysoka dokładność | Wymaga połączenia z internetem, płatny | Od $1.50 za 1000 stron |

## Szczegółowe porównanie modeli językowych

| Model | Zalety | Wady | Zastosowanie |
|-------|--------|------|--------------|
| **GPT-4** | Najwyższa jakość, zrozumienie kontekstu | Wysoki koszt, wymaga API | Analiza i poprawa przepisów |
| **Claude 3** | Dobra jakość, długi kontekst | Wysoki koszt, wymaga API | Analiza i poprawa przepisów |
| **LLaMA 3** | Lokalnie hostowany, bez kosztów API | Wymaga GPU dla większych modeli | Embeddingi, wyszukiwanie |
| **Mistral** | Dobre wyniki dla mniejszych modeli | Mniej dokładny niż większe modele | Embeddingi, wyszukiwanie |
| **Sentence Transformers** | Specjalizacja w embeddingach | Nie generuje tekstu | Tylko embeddingi |

## Przepływ danych

1. **Pozyskiwanie danych**:
   - Zdjęcia robione przez użytkownika
   - Dokumenty importowane z dysku
   - Ręczne wprowadzanie przepisów
   - Dyktowanie przepisów (konwersja mowy na tekst)

2. **Przetwarzanie danych**:
   - OCR dla obrazów i dokumentów
   - Analiza struktury tekstu (wyodrębnienie tytułu, składników, instrukcji)
   - Normalizacja i czyszczenie tekstu
   - Generowanie embeddingów dla wyszukiwania semantycznego

3. **Przechowywanie danych**:
   - Zdjęcia i pliki zapisywane w systemie plików
   - Metadane (tytuł, data, atrybuty) w bazie SQL
   - Embeddingi w bazie wektorowej Qdrant
   - Pełny tekst przepisu w bazie SQL oraz w systemie plików

4. **Wyszukiwanie danych**:
   - Wyszukiwanie pełnotekstowe w bazie SQL
   - Wyszukiwanie po atrybutach (tagach) w bazie SQL
   - Wyszukiwanie semantyczne w bazie wektorowej Qdrant

## Implementacja OCR

Rekomendujemy hybrydowe podejście do OCR, wykorzystujące zarówno Tesseract OCR, jak i EasyOCR:

1. **Wstępne przetwarzanie obrazu**:
   - Korekta perspektywy
   - Usuwanie szumów
   - Normalizacja kontrastu i jasności
   - Binaryzacja adaptacyjna

2. **Rozpoznawanie tekstu**:
   - Użycie EasyOCR jako głównego silnika OCR
   - Tesseract jako backup dla problematycznych fragmentów
   - Porównanie wyników i wybór lepszego

3. **Post-processing**:
   - Korekta typowych błędów OCR
   - Wykorzystanie modelu językowego do poprawy jakości tekstu
   - Strukturyzacja tekstu (identyfikacja tytułu, składników, kroków)

## Implementacja RAG (Retrieval Augmented Generation)

System RAG będzie wykorzystywał następujące komponenty:

1. **Generowanie embeddingów**:
   - Użycie modelu Sentence Transformers do generowania embeddingów dla przepisów
   - Tworzenie embeddingów dla całego przepisu oraz oddzielnie dla tytułu i składników

2. **Przechowywanie embeddingów**:
   - Wykorzystanie bazy Qdrant do efektywnego przechowywania i wyszukiwania wektorów
   - Indeksowanie dla szybkiego wyszukiwania

3. **Wyszukiwanie semantyczne**:
   - Konwersja zapytania użytkownika na embedding
   - Wyszukiwanie podobnych embeddingów w bazie Qdrant
   - Rankingowanie wyników według podobieństwa kosunusowego

4. **Augmentacja wyników**:
   - Wykorzystanie modelu językowego do wzbogacenia wyników wyszukiwania
   - Generowanie podsumowań lub sugestii na podstawie znalezionych przepisów

## Bezpieczeństwo danych

1. **Prywatność**:
   - Wszystkie dane przechowywane lokalnie
   - Brak przesyłania danych do chmury (opcjonalnie przy korzystaniu z API)
   - Szyfrowanie bazy danych

2. **Kopie zapasowe**:
   - Automatyczne tworzenie kopii zapasowych
   - Możliwość eksportu/importu danych

3. **Integralność danych**:
   - Walidacja danych wejściowych
   - Transakcyjne operacje na bazie danych
   - Obsługa błędów i mechanizmy odzyskiwania

## Wymagania sprzętowe

### Minimalne wymagania:
- Procesor: Intel Core i3 / AMD Ryzen 3 lub nowszy
- RAM: 4 GB (8 GB rekomendowane)
- Dysk: 10 GB wolnego miejsca (SSD rekomendowany)
- System: Windows 10/11, macOS 10.15+, Ubuntu 20.04+

### Rekomendowane wymagania dla lokalnych modeli językowych:
- Procesor: Intel Core i7 / AMD Ryzen 7 lub nowszy
- RAM: 16 GB
- Dysk: 20 GB wolnego miejsca (SSD wymagany)
- GPU: NVIDIA GeForce GTX 1660 lub lepsza (dla szybszego OCR i lokalnych modeli LLM)

## Podsumowanie

Proponujemy implementację aplikacji do zarządzania przepisami kuchennymi w oparciu o nowoczesne technologie przetwarzania języka naturalnego i rozpoznawania tekstu. Wykorzystanie podejścia RAG pozwoli na semantyczne wyszukiwanie przepisów, a zaawansowane mechanizmy OCR umożliwią efektywne przetwarzanie zdjęć i dokumentów.

Aplikacja będzie rozwijana w sposób iteracyjny, z kolejnymi wersjami wprowadzającymi coraz bardziej zaawansowane funkcjonalności, zgodnie z przedstawionym planem rozwoju.
