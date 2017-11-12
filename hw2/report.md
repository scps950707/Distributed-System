# Report

## Question (a)
Modify HW1b to generate random initial value for each node (M1 without M2). Call the new program
HW2a. Note that different initial values MAY lead to different results. To find out, HW2a performs
1,000 tests to see if all test results are identical. Did these tests produce the same result?

```sh
$ for i in {1..1000}; do ./HW2a.py < test1.txt; done | uniq -c
1000 [1, 4, 5, 7, 8, 9]
$ for i in {1..1000}; do ./HW2a.py < test2.txt; done | uniq -c
1000 [4, 5, 6, 8]
```
According to the test, all tests result for identical

## Question (b)
Modify HW1b to be an anonymous algorithm with arbitrary initial values (M1 plus M2). In the new
program called HW2b, a node can be in the set if all of its neighboring nodes with larger or equal W(v)
/ (deg(v) + 1) values are all out of the set, and it must be out of the set otherwise. HW2b performs
1,000 tests on the same input data file, each with different randomized initial values. Is it possible
that HW2b does not stop for some input? Why? If HW2b does stop for some input file, please list
all possible results (one line for each set of duplicated results) with respective percentages. Are all
these results correct (independent sets)?

```sh
$ ./HW2b.py < test1.txt | sort | uniq -c
256 [0, 3, 4, 5, 7, 8]
256 [1, 4, 5, 7, 8, 9]
512 not stop
$ ./HW2b.py < test2.txt | sort | uniq -c
1024 [4, 5, 6, 8]
```
Yes, it is possible that HW2 does not stop for some input. I test HW2b with all posssible
permutations (1024 times) with the result above, it shows that test1.txt has 50% not stop
and two MWIS results 25% for each. The reason is that in test1.txt's graph there are two neighbor nodoes:
1 and 3 have equal W(v) / (deg(v) + 1) value so that they will keep make same decision in next round.




## Question (c)
Modify HW1b to be an anonymous algorithm that allows arbitrary initial values (M1 plus M2). In the
new program called HW2c, a node can be in the set if all of its neighboring nodes with larger W(v) /
(deg(v) + 1) values are all out of the set, and it must be out of the set otherwise. HW2b performs 1,000
tests on the same input data file, each with different randomized initial values. Is it possible that
HW2c does not stop for some input? Why? If HW2c does stop for some input file, please list all
possible results (one line for each set of duplicated results) with respective percentages. Are all these
results correct (independent sets)?
```sh
$ ./HW2c.py < test1.txt | sort | uniq -c
1024 [1, 3, 4, 5, 7, 8]
$ ./HW2c.py < test2.txt | sort | uniq -c
1024 [4, 5, 6, 8]
```

No, it doesn't stop, for test1.txt and test2.txt tested with HW2c using all possible permutations results
in identical output.

## Question (d)
Could you suggest a way to correct HW2b? HW2c is certainly not an answer. Hint: Exploit what you
have learnt from HW2a. This part is optional. Those who have a correct answer to this question will
receive a bonus score.
