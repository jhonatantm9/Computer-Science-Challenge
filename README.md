# Computer-Science-Challenge

## Description

This is Jhonatan's repository for the solution of the Computer science challenge of Endava's internship 2024-2.
In this repo, you can find my implemented solutions for each of the four problems and a little explanation about them.

You can use the links of the different sections to travel allong the README file esier.

### Index

- [2570. Merge Two 2D Arrays by Summing Values](#merge-two-2d-arrays-by-summing-values)
- [1219. Path with Maximum Gold](#path-with-maximum-gold)
- [847. Shortest Path Visiting All Nodes](#shortest-path-visiting-all-nodes)
- [32. Longest Valid Parentheses](#longest-valid-parentheses)

## Merge Two 2D Arrays by Summing Values

### Aproach

To solve the problem I implemented a solution using a _Two pointer_ technique.

First I created a new and empty array for the solution where each pair `[id, value]` will be stored. Because both of the initial arrays are ordered by `id`, I used two pointers starting from the first element of each array and compared both the `id`s, then added the lower one or the sum of both values if same id. After that, I advanced with the pointer of the array from which an element was added to result or both if the ids where the same and started again the same procedure.

Lastly, if one of the arrays still had elements left to add to the result array, I iterated over them and added the pairs to the result array. At the end this array is returned.

| Time complexity | Space complexity |
| :-------------: | :--------------: |
| O(n + m) | O(n + m) |

[Go to code file.](MergeTwoArrays.py)

[Return to index.](#index)

## Path with Maximum Gold

In this problem, I used a _DFS_ algorithm starting from each cell with gold to search the path with the highest amount of gold and return that value.

First, I created a function based on the DFS algorithm, but modified in order to search the gold collected in every possible path from one node and return the maximum value. Then, I applied the function for each node (or non-zero value of the grid) and compared the results with the purpose of getting the maximum number. The comparission was made in each call, comparing the previous maximum (stored in a variable) with the new one.

| Time complexity | Space complexity |
| :-------------: | :--------------: |
| O(n\*m\*4<sup>m\*n</sup>) | O(n\*m), m\*n <= 25 |

[Go to code file.](PathWithMaximumGold.py)

[Return to index.](#index)

## Shortest Path Visiting All Nodes

The idea for the solution was to make a BFS taking into account not only the nodes that are being visited, but also the other that have been also visited before reaching a specific node. Using this, is possibble to get the minimum path length used to visit all nodes.

> Note: The code implementation was created based in another solution and explanation found about the same problem.

<!-- I like to see this solution as a BFS for levels -->

| Time complexity | Space complexity |
| :-------------: | :--------------: |
| O(V\*2<sup>V</sup>) | O(V\*2<sup>V</sup>) |

[Go to code file.](ShortestPathVisitingAllNodes.py)

[Return to index.](#index)

## Longest Valid Parentheses

For this problem, the main idea was to find the lengths of the valid substrings in the full string and return the longest one.

To find the lengths of the "good" substrings, I used a stack to get the indexes of the parentheses that didn't have a matching pair. In order to achieve this, for each character in the sequence, I used the following logic:

- If the character is `(` then stack the symbol with its position (index in the string).
- If the character is `)` then:
  - If the last character of the stack is a `(`, pop the element.
  - In other case, push the symbol with its position.

At the end the stack only will contain the parenthesis that are invalid and its indexes.

With these numbers then it was possible to get all the sizes of the valid substrings by spliting the full string between different ranges. The size of the ranges was found by getting the number of characters between the start of the string and a bad parenthesis, two invalid parenthesis or an unmatched parenthesis and the end of the string. Finally the only thing left was to return the biggest of these numbers.

| Time complexity | Space complexity |
| :-------------: | :--------------: |
| O(n)            | O(n)             |

[Go to code file.](LongestValidParentheses.cpp)

[Return to index.](#index)
