## Teorifrågor

**1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?**
   * Enhetstest testar en liten specifik del av systemet, tex metod eller funktion.
   * Integrationstest testar att kommunikationen mellan två eller flera delar av systemet fungerar. Tex mellan frontend och databas.
   * Regressionstest säkerställer att befintlig kod fortsätter att fungera när ny kod lagts till.
   * Prestandatest mäter hur ett system presterar vad gäller stabilitet, kapacitet, svarstider under olika hög belastning.  


**2. Beskriv hur det går till när man arbetar med TDD.** 
   * Välj user story, skriv testfall, skriv kod som uppfyller testfall; Red - Green - Refactor. Red - skriv ett test som misslyckas då koden inte finns än. Green - skriv minsta mängden kod för att få testet att lyckas. Refactor - förbättra gör koden bättre (bättre namn, bättre struktur)  


**3. Beskriv hur BDD skiljer sig från TDD.**
   * TDD fokuserar på att koden fungerar rent tekniskt och är mer för utvecklare. BDD fokuserar mer på systembeteende och är mer förståeligt iom att Gherkin/Given-When-Then används som ett gemensamt språk mellan tekniker och verksamhet.  


**4. Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.**
   * Jag skulle arbeta med BDD både för backend och frontend. Dels för att få det enhetligt och dels för att få både backend och frontend att vara mer förståeligt för både utvecklare, testare och användare. Jag skulle kombinera detta med enhetstester för att snabbt hitta småfel i logiken, vilket ger ett stabilt och lättförståeligt system.
