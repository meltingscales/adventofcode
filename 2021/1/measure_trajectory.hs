import System.IO
import Control.Monad
import Text.Printf

-- Ex: 
--      "Hello World" !!! (2, 7) 
-- returns
--      "llo W"
(!!!) :: [a] -> (Int, Int) -> [a]
(!!!) array (m, n) = (drop m $ take n array)

tupleLarger :: (Int, Int) -> (String)
tupleLarger (first, second) = 
    if  
        first > second 
    then "True"
    else "False"

main :: IO ()
main = do
    putStrLn "Hello, Haskell!"

    contents :: [Char] <- readFile "./input"

    let list :: [String] = words contents

    printf "first element in list: %s\n" (list !! 0)

    putStrLn ("Hello World" !!! (2,7))

    putStrLn "Goodbye!"

    printf "Is 1 larger than 2? %s" (tupleLarger (1, 2))