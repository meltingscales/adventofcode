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

measureTrajectory :: ([Int]) -> ([Int])
measureTrajectory (integers) = do

    let var = 0

    forM_ [0..(integers-1)] $ \i -> do
        let var = var + i

    return var


main :: IO ()
main = do
    putStrLn "Hello, Haskell!"

    contents :: String <- readFile "./input"

    let list :: [String] = words contents

    printf "first element in list: %s\n" (list !! 0)

    -- putStrLn ("Hello World" !!! (2,7))
    -- printf "Is 1 larger than 2? %s\n" (tupleLarger (1, 2))

    putStrLn "Goodbye!"
