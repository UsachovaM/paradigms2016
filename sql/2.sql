SELECT Name, Rate FROM Country, LiteracyRate
WHERE Country.Code  = LiteracyRate.CountryCode
GROUP BY Name HAVING MAX(Year)=Year
ORDER BY Rate DESC LIMIT 1;
