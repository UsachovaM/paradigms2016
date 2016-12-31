SELECT City.Name, Country.Name, LiteracyRate.Year, Capital.CityId FROM City
JOIN Country, LiteracyRate ON City.Population >= 1000000 AND LiteracyRate.Year >= 2010
LEFT JOIN Capital ON City.Id = Capital.CityId
WHERE City.CountryCode = Country.Code AND 
		  LiteracyRate.CountryCode = Country.Code
ORDER BY  (LiteracyRate.Rate*City.Population) DESC;
