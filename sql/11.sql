SELECT Country.Name, COUNT(DISTINCT City.Name) AS CityCnt FROM Country, LiteracyRate, City
WHERE (Country.Code = LiteracyRate.CountryCode) AND 
           (City.CountryCode = Country.Code) AND
           (LiteracyRate.Rate*City.Population >= 100000000)
GROUP BY Country.Code
ORDER BY CityCnt DESC, Country.Name;
