SELECT Country.Name, COUNT(City.Name) AS CityCnt FROM Country
JOIN LiteracyRate, City ON (Country.Code = LiteracyRate.CountryCode) AND 
                                               (City.CountryCode = Country.Code) AND
                                               (LiteracyRate.Rate*City.Population >= 100000000)
GROUP BY Country.Code
ORDER BY CityCnt DESC, Country.Name;