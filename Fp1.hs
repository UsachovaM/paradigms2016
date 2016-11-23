head' :: [a] -> a
head' (x:_) = x

tail' :: [a] -> [a]
tail' (_:xs) = xs
tail' [] = []

take' :: Int -> [a] -> [a]
take' _ [] = []
take' 0 _ = []
take' n (x:xs) = x : take' (n-1) xs

drop' :: Int -> [a] -> [a]
drop' _ [] = []
drop' 0 x = x
drop' n (_:xs) = drop (n-1) xs

filter' :: (a -> Bool) -> [a] -> [a]
filter' _ [] = []
filter' f (x:xs) | f x = x : filter' f xs
                 | otherwise = filter' f xs

foldl' :: (a -> b -> a) -> a -> [b] -> a
foldl' _ z [] = z 
foldl' f z (x:xs) = foldl' f (f z x) xs

concat' :: [a] -> [a] -> [a]
concat' [] y = y
concat' (x:xs) y = x : concat' xs y

quickSort' :: Ord a => [a] -> [a]
quickSort' [] = []
quickSort' (x:xs) = concat' (quickSort' (filter' (< x) xs)) 
                       (x : (quickSort' (filter' (>= x) xs)))
