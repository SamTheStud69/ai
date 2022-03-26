import sys
import copy
import math
import numpy as np

#Finding postion of element
def find_pos(s, elem):
 for i in range(len(s)):
  for j in range(len(s[0])):
   if s[i][j] == elem:
     return [i, j]

#Function to Calculate Euclidean Distance
def eucledian(s, g):
  res_mat = np.zeros(len(s) * len(s[0]), dtype=float)
  print(res_mat)
  res_mat = res_mat.reshape(len(s), len(s))
  print(res_mat)
  for x1 in range(len(s)):
    for y1 in range(len(s[0])):
      elem = s[x1][y1]
      pos = find_pos(g, elem)
      x2 = pos[0]
      y2 = pos[1]
      res_mat[x1][y1] = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
  summ = 0
  for i in range(len(res_mat)):
    summ += sum(res_mat[i])
  return summ

#Funtion to Calculate Manhattan Distance
def manhattan(s, g):
   res_mat = np.zeros(len(s) * len(s[0]), dtype=float)
   res_mat = res_mat.reshape(len(s), len(s))
   for x1 in range(len(s)):
     for y1 in range(len(s[0])):
       elem = s[x1][y1]
       pos = find_pos(g, elem)
       x2 = pos[0]
       y2 = pos[1]
       res_mat[x1][y1] = abs(x2 - x1) + abs(y2 - y1)
   summ = 0
   for i in range(len(res_mat)):
      summ += sum(res_mat[i])
   return summ

#Function to Calculate Minkowiski Distance
def minkowiski(s, g, p):
   res_mat = np.zeros(len(s) * len(s[0]), dtype=float)
   res_mat = res_mat.reshape(len(s), len(s))
   for x1 in range(len(s)):
     for y1 in range(len(s[0])):
       elem = s[x1][y1]
       pos = find_pos(g, elem)
       x2 = pos[0]
       y2 = pos[1]
       res_mat[x1][y1] = ((abs(x2 - x1) ** p) + (abs(y2 - y1) ** p)) **(1. / p)
   summ = 0
   for i in range(len(res_mat)):
     summ += sum(res_mat[i])
   return summ

#Driver Function
p_val = 3

s0 = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
print(len(s0))
g = [[1, 2, 3], [8, 4, 0], [7, 6, 5]]
euc_102003060 = eucledian(s0, g)
man = manhattan(s0, g)
mink = minkowiski(s0,g,p_val)
print(euc_102003060,"\n",man,"\n",mink)

