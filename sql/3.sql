SELECT City.Name FROM City
JOIN Capital, Country ON  (City.Id = Capital.CityId) AND (Capital.CountryCode = Country.Code)
WHERE Country.Name = 'Malaysia';
