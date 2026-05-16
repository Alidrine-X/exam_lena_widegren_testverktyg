# User story 5
# Som en användare vill jag kunna se statistik över listan
# för att kunna veta hur många böcker som finns i Läslistan
# och hur många som är favoritmarkerade

  Feature: Visa statistik

    Background:
      Given att användaren är på webbsidan
      And följande titlar av författare finns i Läslistan

      | title                                    | author                 |
      | Ormar på ett plan: En Python-berättelse  | Guido van Rossum       |
      | The Pragmatic Procrastinator             | Dave Thomasson         |
      | Python för folk som hatar ormar          | Monty Pythonsson       |
      | Why Your Tests Are Lying to You          | Kent Backdoor          |
      | Playwright: Click It Till You Make It    | Microslop Browserdóttir|
      | Git Blame and Other Ways to Lose Friends | Linus Torvalds         |
      | Learn Python in 21 Years                 | Sams Teachyourself     |
      | Agile Is a Feeling                       | Jeff Sutherland        |
      | Playwright: Waiting for Selectors        | Samuel Barclay Beckett |
      | Stack Overflow: A Love Story             | Copy Pasta             |
      | My First Regex (And Last)                | Larry Wallström        |
      | The Developer Who Knew Nothing           | George R.R. Martin     |
      | The Bugs are Coming                      | George R.R. Martin     |

    Scenario: Visa antal böcker och favoriter i listan
      Given att användaren markerat följande böcker som favoriter:

      | title                                    | author                 |
      | The Pragmatic Procrastinator             | Dave Thomasson         |
      | Why Your Tests Are Lying to You          | Kent Backdoor          |
      | Playwright: Waiting for Selectors        | Samuel Barclay Beckett |
      | Stack Overflow: A Love Story             | Copy Pasta             |

      When användaren klickar på knappen "Statistik"
      Then ska texten "Listan har 13 böcker." visas
      And ska texten "Våra användare har hjärtmarkerat 4 böcker." visas

    Scenario: Visa antal böcker och att favoriter saknas
      Given att användaren inte har markerat några favoriter
      When användaren klickar på knappen "Statistik"
      Then ska texten "Listan har 13 böcker." visas
      And ska texten "Våra användare har hjärtmarkerat 0 böcker." visas

    Scenario: Uppdatering av statistik vid ändring
      Given att användaren markerat följande böcker som favoriter:

      | title                                    | author                 |
      | The Pragmatic Procrastinator             | Dave Thomasson         |
      | Why Your Tests Are Lying to You          | Kent Backdoor          |
      | Playwright: Waiting for Selectors        | Samuel Barclay Beckett |
      | Stack Overflow: A Love Story             | Copy Pasta             |

      When användaren klickar på knappen "Statistik"
      Then ska texten "Våra användare har hjärtmarkerat 4 böcker." visas
      When användaren klickar på knappen "Katalog"
      And användaren avmarkerar boken "The Pragmatic Procrastinator" av "Dave Thomasson"
      And användaren klickar på knappen "Statistik"
      Then ska texten "Våra användare har hjärtmarkerat 3 böcker." visas
