# Python-Developer-Sample-Case-Study
### Question 1

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase. In other words, both strings must contain the same exact letters in the same exact frequency.

##### Write a python script that reads 2 strings from command line and finds out whether they are anagrams or not. If they are not anagrams, then the script should find and print the minimum number of character deletions required to make the two strings anagrams. Otherwise, just print that they are anagrams.

Input Format

The first line contains a single string, a.
The second line contains a single string, b.
Expected input and output: ``` $ python3 solution.py a: Tom Marvolo Riddle b: I Am Lord Voldemort remove 7 characters from 'Tom Marvolo Riddle' and 8 characters from 'I Am Lord Voldemort'

$ python3 solution.py a: tom marvolo riddle b: i am lord voldemort remove 0 characters from 'tom marvolo riddle' and 1 characters from 'i am lord voldemort'

$ python3 solution.py a: tom marvolo riddle b: i am lordvoldemort they are anagrams

$ python3 solution.py a: tom riddle b: voldemort remove 3 characters from 'tom riddle' and 2 characters from 'voldemort' ```

### Question 2

##### Write a python script using pandas that finds and prints: - top seller n products in given date range (product name & quantity) - top seller n stores in given date range (store name & quantity) - top seller n brands in given date range (brand & quantity) - top seller n cities in given date range (city & quantity)

On equality, print all of the rows.

Input Data Format

product.csv - id: identifier of the product - name: name of the product - brand: brand of the product

store.csv - id: identifier of the store - name: name of the store - city: city that the store is located in

sales.csv - product: identifier of the product (id column in product.csv) - store: identifier of the product (id column in product.csv) - date: date of sale - quantity: sales quantity of the specified product in the specified store

Arguments

Your script should take following arguments from command line: - "--min-date": start of the date range. type:str, format:"YYYY-MM-DD", default:"2020-01-01" - "--max-date": end of the date range. type:str, format:"YYYY-MM-DD", default:"2020-06-30" - "--top": number of rows in the output. type:int, default:3

Expected command and output: $ python3 solution.py --min-date 2020-02-01 --max-date 2020-06-30 --top 2 -- top seller product -- name quantity p-103 33 p-102 24 p-110 24 -- top seller store -- name quantity s-3 42 s-2 36 s-7 36 -- top seller brand -- brand quantity yoyodyne 100 acme 65 -- top seller city -- city quantity gotham 108 coruscant 78
