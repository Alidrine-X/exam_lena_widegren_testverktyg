# User story 2
# Som en användare vill jag kunna se en lista på böcker
# för att kunna markera mina favoriter

  Feature: Visa boklista

    Scenario: Se befintlig lista med böcker
      Given att användaren är på webbsidan
      Then ska boken "The Bugs are Coming" av "George R.R. Martin" finnas med i Läslistan
      And Läslistan innehåller 13 böcker

    Scenario: Markera favoritbok
      Given att användaren är på webbsidan
      And Läslistan innehåller 13 böcker
      When användaren klickar på raden framför boken "Agile Is a Feeling" av "Jeff Sutherland"
      Then ska ett hjärta synas på raden framför boken "Agile Is a Feeling" av "Jeff Sutherland"
