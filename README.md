# 📚 Projekt Läslistan
![Webbsidans gränssnitt](screenshot.png)  
"Läslistan" är en webbsida där man kan välja ut sina favoriter från en katalog med böcker, eller lägga till nya. Beställaren är en organisation som vill öka studenters läsande genom att rikta in sig på lättlästa böcker med tekniskt djup. Nuvarande version har begränsad funktionalitet. På sikt vill man utöka webbsidan med funktioner för att dela sina listor, skapa quiz och diskutera böcker med varandra. Därför är det viktigt att det finns tester för all grundläggande funktionalitet. 
---

## 🛠 Testmetodik

Projektet följer en **testpyramid** för att säkerställa hög kvalitet i alla led:

### 🔹 Backend (TDD)
Logiken i `BookStore` och `FavoriteBooks` har utvecklats genom **Test-Driven Development**.
*   **Enhetstester:** Verifierar isolerade metoder och funktioner i klasserna.
*   **Integrationstester:** Säkerställer att böcker kan läggas till, markeras som favoriter och att statistiken räknas rätt i systemet.
*   *Verktyg:* `pytest`

### 🔹 Frontend (BDD)
Webbgränssnittet testas genom användarbeteenden (End-to-End) med designmönstret **Page Object Model**.
*   **Navigering:** Verifierar att menyer och knappar leder till rätt undersida.
*   **Katalog:** Kontrollerar att listan visas och att favoritmarkering fungerar i UI.
*   **Lägg till bok:** Verifierar att nya böcker kan registreras och därefter dyker upp i läslistan.
*   **Mina böcker:** Säkerställer att favoritlistan synkas korrekt och visar rätt innehåll.
*   **Statistik:** Verifierar att siffrorna på sidan uppdateras i realtid vid ändringar.
*   *Verktyg:* `Playwright`, `Behave`

---

## 🚀 Kom igång

### Förutsättningar
*   Python 3.10 eller senare.
*   Ett terminalfönster.

### Installation
Installera nödvändiga bibliotek och webbläsardrivrutiner:
```bash
pip install -r requirements.txt
playwright install chromium
```

### Köra tester
Projektet är konfigurerat för att köra tester smidigt via terminalen.

**Backend-tester (TDD):**
```bash
pytest
```

**Frontend-tester (BDD):**
```bash
behave
```

## ⚙️ Continuous Integration (CI)
Projektet använder **GitHub Actions** för att automatisera kvalitetssäkringen vid varje `push` eller `pull request` till `main`-branchen:

*   **Linting:** Källkoden kontrolleras automatiskt med `flake8` för att säkerställa att den följer korrekta kodstandarder (PEP 8).
*   **Automatiserad testning:** Hela testsviten (Pytest och Behave) körs automatiskt i en isolerad molnmiljö.
*   **Headless Browser:** Playwright-testerna körs i *headless mode* för att möjliggöra snabb testning utan grafiskt gränssnitt.
*   **Stabilitet:** CI-flödet garanterar att ny kod inte introducerar buggar eller bryter mot kodpraxis.

---

## 📁 Struktur
*   **`.github/workflows/`** – Inställningar för den automatiska testningen på GitHub.
*   **`src/bookstore/`** – Källkoden för själva läslistan.
*   **`src/features/`** – Alla Playwright-tester, steg-filer och Page Objects.
*   **`tests/`** – Backend-tester uppdelade i unit och integration.
*   **`requirements.txt`** – Lista på alla bibliotek som behöver installeras.
*   **`behave.ini` & `pytest.ini`** – Inställningar för hur testerna ska köras.
*   **`STORIES.md` & `ANSWERS.md`** – User stories och teorisvar.

---
*Detta projekt är en del av kursen Testautomatisering Python vid NBI / Handelsakademin.*
