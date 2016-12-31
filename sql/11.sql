SELECT Country.Name, COUNT(DISTINCT City.Name) AS CityCnt FROM Country
JOIN LiteracyRate, City ON (LiteracyRate.Rate*City.Population >= 100000000)
WHERE (Country.Code = LiteracyRate.CountryCode) AND 
           (City.CountryCode = Country.Code)
GROUP BY Country.Code
ORDER BY CityCnt DESC, Country.Name;
