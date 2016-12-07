SELECT City.Name, City.Population, Country.Population FROM City
JOIN Country ON City.CountryCode = Country.Code
GROUP BY Code
ORDER BY (100*City.Population / Country.Population) DESC, City.Name DESC LIMIT 20;;
