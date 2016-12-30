SELECT City.Name, Country.Name, LiteracyRate.Year FROM City
JOIN Country ON City.CountryCode = Country.Code AND 
                            City.Population >= 1000000
JOIN LiteracyRate ON LiteracyRate.CountryCode = Country.Code AND 
                                     LiteracyRate.Year >= 2010
ORDER BY  (LiteracyRate.Rate*City.Population) DESC;