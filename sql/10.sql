SELECT City.Name, Country.Name, LiteracyRate.Year, Capital.CityId FROM City
JOIN Country ON City.CountryCode = Country.Code AND 
                            City.Population >= 1000000
JOIN LiteracyRate ON LiteracyRate.CountryCode = Country.Code AND 
                                     LiteracyRate.Year >= 2010
LEFT JOIN Capital ON City.Id = Capital.CityId
ORDER BY  (LiteracyRate.Rate*City.Population) DESC;
