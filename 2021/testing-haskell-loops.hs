import System.IO
import Control.Monad
import Text.Printf


main :: IO ()
main = do


    let list = [1, 2, 2, 2, 7, 7, 7, 8, 9]
    let listlen = (length list)

    putStrLn "testing loops"

    forM_ [0..(listlen-1)] $ \i -> do
        putStr $ "i="++ show i ++ ", val=" ++ (show $ list !! i) ++ " "
        when (0 == i `mod` 3) $
            putStr "Fizz"
        when (0 == i `mod` 5) $
            putStr "Buzz"
        putStrLn ""


    putStrLn "Goodbye!"
