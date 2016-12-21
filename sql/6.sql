SELECT City.Name, City.Population, Country.Population FROM City
JOIN Country ON City.CountryCode = Country.Code
ORDER BY (1000 * City.Population / Country.Population) DESC, City.Name DESC LIMIT 20;
