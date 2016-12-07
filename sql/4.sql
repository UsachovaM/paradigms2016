SELECT Country.Code, COUNT(City.Name) AS CityCnt FROM Country
LEFT JOIN City ON (Country.Code = City.CountryCode) AND (City.Population >= 1000000)
GROUP BY Country.Code
ORDER BY CityCnt DESC, City.Name;