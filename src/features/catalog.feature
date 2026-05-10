# User story 1
# Som en användare vill jag kunna se en lista på böcker
# för att kunna hitta bra böcker att läsa

  Feature: Visa boklista

    Scenario: Se befintlig lista med böcker
      Given att användaren är på webbsidan
      Then ska boken "Ormar på ett plan: En Python-berättelse" finnas med i Läslistan
      And Läslistan ska innehålla minst 13 böcker

