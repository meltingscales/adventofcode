import java.io.File
import java.lang.Exception


fun firstSolution() {

    val file = File("input.txt")

    var total = 0

    file.readLines().map {
        total += it.toInt()
    }

    print("`$total` is your total.\n")

}

fun secondSolution() {

    val file = File("input.txt")

    val seenFrequencies = HashMap<Int, Int>()

    var total = 0

    file.readLines().map { line ->

        val number = line.toInt()
        total += number

        if (total !in seenFrequencies) {
            seenFrequencies[total] = 0
        }

        seenFrequencies[total] = seenFrequencies[total]!! + 1

        seenFrequencies.entries.forEach {

            if (it.value >= 2) {
                print("We have seen the number ${it.key} twice or more!\n")

                return
            }
        }

    }

    throw Exception("No numbers have occurred more than twice!")
}

fun main() {

    firstSolution()

    secondSolution()
}