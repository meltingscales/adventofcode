import java.io.File
import kotlin.test.assertFalse
import kotlin.test.assertTrue

fun getData(): List<String> {
    val file = File("input.txt")

    return file.readLines()
}


fun computeOccurrences(list: List<String>): Map<Int, Int> {

    val occurrences = HashMap<Int, Int>()

    list.forEach {
        print("todo :)")
    }

    return occurrences

}

fun containsNLetters(str: String, n: Int): Boolean {

    val seen = HashMap<Char, Int>()

    str.iterator().forEach { character ->

        if (seen.containsKey(character)) {
            seen[character] = seen[character]!! + 1
        } else {
            seen[character] = 1
        }
    }

    seen.iterator().forEach { entry ->
        if (entry.value == n) {
            return true
        }
    }

    return false

}

fun tests() {

    assertTrue { containsNLetters("abcccb", 3) }
    assertFalse { containsNLetters("aaabbcc", 1) }

}

fun main(args: Array<String>) {

    tests()

    //var data = getData()


}

