# User story 1
# Som användare vill jag enkelt kunna navigera bland olika delar av läslistan
# för att snabbt kunna titta på böcker och statistik

Feature: Navigera i Läslistan

  Scenario: Webbsidans titel och startvy
    Given att användaren är på webbsidan
    Then ska fliken ha namnet "Läslistan"
    And rubriken ska vara "Läslistan"

  Scenario: Knapparna i menyn ska vara synliga
    Given att användaren är på webbsidan
    Then ska alla navigeringsknapparna vara synliga

  Scenario: Navigering till "Lägg till bok"
    Given att användaren är på webbsidan
    When användaren klickar på knappen "Lägg till bok"
    Then ska undersidan för "add-book" visas

  Scenario: Navigering till Mina böcker
    Given att användaren är på webbsidan
    When användaren klickar på knappen "Mina böcker"
    Then ska undersidan för "favorites" visas

  Scenario: Navigering till Statistik
    Given att användaren är på webbsidan
    When användaren klickar på knappen "Statistik"
    Then ska undersidan för "statistics" visas

  Scenario: Klicka på startsida Katalog från annan undersida
    Given att användaren är på webbsidan
    And användaren klickat på knappen "Lägg till bok"
    When användaren klickar på knappen "Katalog"
    Then ska undersidan för "catalog" visas
