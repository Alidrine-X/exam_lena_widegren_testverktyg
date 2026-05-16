# User story 4
# Som en användare vill jag kunna markera favoritböcker
# för att kunna få en lista med bara mina favoriter

  Feature: Visa favoritlista

    Background:
      Given att användaren är på webbsidan
      And följande titlar av författare finns i Läslistan

      | title                          | author             |
      | The Pragmatic Procrastinator   | Dave Thomasson     |
      | Agile Is a Feeling             | Jeff Sutherland    |
      | Learn Python in 21 Years       | Sams Teachyourself |
      | The Developer Who Knew Nothing | George R.R. Martin |
      | The Bugs are Coming            | George R.R. Martin |

    Scenario: Visa lista med favoriter
      Given att användaren markerat följande böcker som favoriter:

      | title               | author             |
      | Agile Is a Feeling  | Jeff Sutherland    |
      | The Bugs are Coming | George R.R. Martin |

      When användaren klickar på knappen "Mina böcker"
      Then ska följande böcker visas:

      | title               | author             |
      | Agile Is a Feeling  | Jeff Sutherland    |
      | The Bugs are Coming | George R.R. Martin |

      And listan ska innehålla 2 böcker

    Scenario: Visa inga böcker när favoriter saknas
      Given att användaren inte har markerat några favoriter
      When användaren klickar på knappen "Mina böcker"
      Then ska texten "När du valt, kommer dina favoritböcker att visas här." visas
      And favoritlistan ska vara tom
