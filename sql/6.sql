SELECT City.Name, (100*City.Population / Country.Population) AS PrPop FROM City
JOIN Country ON Country.Code = City.CountryCode
GROUP BY Code
ORDER BY PrPop DESC, City.Name DESC LIMIT 20;