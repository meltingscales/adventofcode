import System.IO
import Control.Monad


main :: IO ()
main = do
    putStrLn "Hello, Haskell!"

    contents <- readFile "./input"
    putStrLn contents

    putStrLn "Goodbye!"