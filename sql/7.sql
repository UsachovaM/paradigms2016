SELECT Country.Name FROM Country
LEFT JOIN City ON Country.Code = City.CountryCode 
GROUP BY Country.Code
HAVING  (COUNT(City.Name) = 0 AND Country.Population > 0) OR (Country.Population > 2 * SUM(City.Population))
ORDER BY Country.Name;
