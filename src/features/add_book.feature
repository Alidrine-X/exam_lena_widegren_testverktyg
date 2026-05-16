# User story 3
# Som en användare vill jag kunna lägga till böcker i listan
# för att de ska komma med i läslistan

Feature: Lägga till böcker

  Scenario Outline: Lägga till en ny bok i läslistan
    Given att användaren är på webbsidan
    And användaren klickat på knappen "Lägg till bok"
    When användaren skriver in titeln "<title>"
    And användaren skriver in författaren "<author>"
    And användaren klickar på knappen "Lägg till ny bok"
    And användaren klickar på knappen "Katalog"
    Then ska boken "<title>" av "<author>" finnas med i Läslistan

    Examples:

      | title           | author          |
      | Talismanen      | Stephen King    |
      | En dos stryknin | Agatha Christie |
      | Mannen som log  | Henning Mankell |
