SELECT City.Name, Country.Name, LiteracyRate.Year, Capital.CityId FROM City, Country, LiteracyRate
LEFT JOIN Capital ON City.Id = Capital.CityId
WHERE City.CountryCode = Country.Code AND 
          City.Population >= 1000000 AND 
		  LiteracyRate.CountryCode = Country.Code AND 
          LiteracyRate.Year >= 2010
ORDER BY  (LiteracyRate.Rate*City.Population) DESC;
