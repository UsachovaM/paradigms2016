import Prelude hiding (lookup)

data BinaryTree k v = Nil | Node k v (BinaryTree k v) (BinaryTree k v) deriving Show

lookup :: Ord k => k -> BinaryTree k v -> Maybe v
lookup _ Nil = Nothing
lookup n (Node key value left right) | n == key = Just value
                                     | n > key = lookup n right
                                     | n < key = lookup n left

insert :: Ord k => k -> v -> BinaryTree k v -> BinaryTree k v
insert n x Nil = Node n x Nil Nil
insert n x (Node key value left right) | n == key = Node n x left right
                                       | n < key = Node key value (insert n x left) right
                                       | n > key = Node key value left (insert n x right)

delete :: Ord k => k -> BinaryTree k v -> BinaryTree k v
delete _ Nil = Nil 
delete n (Node key value left right) | n < key = Node key value (delete n left) right
                                     | n > key = Node key value left (delete n right)
                                     | n == key = merge left right
  where merge Nil r = r
        merge (Node k v left right) r = merge (merge left right) (insert k v r)
