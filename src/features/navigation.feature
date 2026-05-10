# User story 7
# Som systemägare vill jag att knapparna ska synas när man kommer in på sidan
# så att användare kan byta sida

Feature: Navigera i Läslistan

  Scenario: Knapparna i menyn ska vara synliga
    Given att användaren är på webbsidan
    Then ska alla knapparna vara synliga

  Scenario Outline: Klick på menyknapp ändrar undersida
    Given att användaren är på webbsidan
    When användaren klickar på knappen "<knapp>"
    Then ska användaren hamna på undersidan "<sida>"

    Examples:

    | knapp         |sida       |
    | Lägg till bok |add-book    |
    | Mina böcker   |favorites  |
    | Statistik     |statistics |

  Scenario: Klicka på startsida katalog från annan undersida
    Given att användaren är på webbsidan
    And användaren klickar på knappen "Lägg till bok"
    When användaren klickar på knappen "Katalog"
    Then ska användaren hamna på undersidan "catalog"
