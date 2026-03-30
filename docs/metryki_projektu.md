# Kluczowe Metryki Projektu "Przepisy"

**Data:** 13 czerwca 2025

## 1. Dokładność Rozpoznawania Tekstu (OCR Accuracy)

**Definicja:** Procentowy wskaźnik poprawnie rozpoznanych słów i znaków z zeskanowanych lub sfotografowanych przepisów kulinarnych.

**Sposób pomiaru:**
- Porównanie oryginalnego tekstu z tekstem rozpoznanym przez system OCR
- Obliczenie współczynnika: (liczba poprawnie rozpoznanych słów / całkowita liczba słów) × 100%

**Cele:**
- Minimum akceptowalne: ≥ 85% dokładności
- Cel docelowy: ≥ 95% dokładności
- Cel ambitny: ≥ 98% dokładności

**Znaczenie biznesowe:** Wysoka dokładność OCR bezpośrednio przekłada się na zadowolenie użytkownika, ponieważ minimalizuje konieczność ręcznej korekty rozpoznanego tekstu. Poprawa tej metryki o każdy punkt procentowy znacząco zmniejsza czas potrzebny na dodanie nowego przepisu do kolekcji.

## 2. Trafność Wyszukiwania Semantycznego (Semantic Search Precision)

**Definicja:** Miara określająca, jak dobrze system zwraca przepisy odpowiadające semantycznemu znaczeniu zapytania użytkownika, a nie tylko dopasowaniu słów kluczowych.

**Sposób pomiaru:**
- Mean Average Precision (MAP) w zbiorze testowym zapytań semantycznych
- Ocena trafności wyników przez użytkowników w skali 1-5
- A/B testing dla różnych algorytmów wyszukiwania

**Cele:**
- Minimum akceptowalne: ≥ 70% trafności dla pierwszych 5 wyników
- Cel docelowy: ≥ 85% trafności dla pierwszych 5 wyników
- Cel ambitny: ≥ 92% trafności dla pierwszych 5 wyników

**Znaczenie biznesowe:** Ta metryka jest kluczowa dla głównej funkcjonalności aplikacji - szybkiego i intuicyjnego wyszukiwania przepisów. Wysoka trafność wyszukiwania semantycznego oznacza, że użytkownicy mogą znaleźć potrzebne przepisy nawet przy użyciu nieprecyzyjnych zapytań (np. "coś szybkiego z kurczakiem" zamiast dokładnych nazw potraw).

## 3. Czas Do Wartości (Time-to-Value)

**Definicja:** Czas potrzebny nowemu użytkownikowi na dodanie pierwszego przepisu i pomyślne wyszukanie go później przy użyciu zapytania semantycznego.

**Sposób pomiaru:**
- Chronometraż procesu od pierwszego uruchomienia aplikacji do pomyślnego wyszukania dodanego przepisu
- Analiza logów użytkownika: czas między rejestracją a pierwszym pomyślnym wyszukaniem
- Badania UX z użytkownikami testowymi

**Cele:**
- Minimum akceptowalne: ≤ 10 minut
- Cel docelowy: ≤ 5 minut
- Cel ambitny: ≤ 3 minuty

**Znaczenie biznesowe:** Ta metryka łączy użyteczność interfejsu, wydajność OCR i skuteczność wyszukiwania w jeden praktyczny wskaźnik. Określa ona, jak szybko użytkownik może doświadczyć głównej wartości aplikacji. Krótszy czas do wartości zwiększa szanse na utrzymanie użytkownika i jego dalsze zaangażowanie.

---

Te trzy metryki wspólnie pokrywają najważniejsze aspekty aplikacji "Przepisy":
1. **Jakość wprowadzania danych** (dokładność OCR)
2. **Skuteczność odzyskiwania informacji** (trafność wyszukiwania)
3. **Ogólna użyteczność i doświadczenie użytkownika** (czas do wartości)

Systematyczne monitorowanie i optymalizacja tych metryk pozwoli na ciągłe ulepszanie aplikacji w obszarach najważniejszych dla użytkowników końcowych.
