#!/usr/bin/env python

import sys
import copy

def main():
  while 1:
    try:
      line = ""
      while not line or len(line) < 161:
        #print ""
        #print "INPUT:"
        line = sys.stdin.readline()
        line = line.strip()
    except KeyboardInterrupt:
      break

    if not line:
      break

    #print ""
    #print "LINE:"
    #print line

    board_cells = line.split()

    # Sets for rows and columns
    row_set = set()
    col_set = set()
    square_set = set()

    for r in range(0, 9):
      for c in range(0, 9):
        curr_cell = board_cells[r*9 + c]
        if curr_cell != "0":
          row_set.add(str(r) + "_" + curr_cell)
          col_set.add(str(c) + "_" + curr_cell)
          square_set.add(str(r//3) + "_" + str(c//3) + "_" + curr_cell)

    # matrix for board
    while 1:

      made_a_change = False

      for r in range(0, 9):
        for c in range(0, 9):
          curr_cell = board_cells[r*9 + c]

          if curr_cell == "0" or len(curr_cell) > 1:
            options = ""
            if len(curr_cell) > 1:
              for i in curr_cell.split():
                if not (str(r) + "_" + i) in row_set and not (str(c) + "_" + i) in col_set and not (str(r//3) + "_" + str(c//3) + "_" + i) in square_set:
                  options += i + " "
            else:
              for i in range(1, 10):
                if not (str(r) + "_" + str(i)) in row_set and not (str(c) + "_" + str(i)) in col_set and not (str(r//3) + "_" + str(c//3) + "_" + str(i)) in square_set:
                  options += str(i) + " "

            options = options.strip()

            if options != curr_cell:
              made_a_change = True

            if len(options) > 0:
              board_cells[r*9 + c] = options
            else:
              board_cells[r*9 + c] = "0"
              
            if len(options) == 1:
              row_set.add(str(r) + "_" + options)
              col_set.add(str(c) + "_" + options)
              square_set.add(str(r//3) + "_" + str(c//3) + "_" + options)

      if len(row_set) == 81:
        break

      if not made_a_change:
        board_cells = depth_first_search(copy.deepcopy(board_cells), copy.deepcopy(row_set), copy.deepcopy(col_set), copy.deepcopy(square_set))
        break

    #print "\n"
    #print "ANSWER:"
    print " ".join(board_cells)
    sys.stdout.flush()

    #print "\n"
    #print "BOARD:"
    #for r in range(0, 9):
    #  for c in range(0, 9):
    #    print str(board_cells[r*9 + c]),
    #    if (c%3 == 2):
    #      print "",
    #    
    #  if (r%3 == 2):
    #    print "\n"
    #  else:
    #    print ""
    #    
    #print "\n"


def depth_first_search(board_cells_copy, row_set_copy, col_set_copy, square_set_copy):
  return depth_first_search_helper(board_cells_copy, row_set_copy, col_set_copy, square_set_copy, 0, 0)

def depth_first_search_helper(board_cells_copy, row_set_copy, col_set_copy, square_set_copy, r_p, c_p):
  
  curr_cell = board_cells_copy[r_p*9 + c_p]
  baord_cells_cp = []
  r2 = r_p
  c2 = c_p + 1
  if c_p == 8:
    r2 += 1
    c2 = 0
  if curr_cell == "0" or len(curr_cell) > 1:
    options = curr_cell
    if curr_cell == "0":
      options = "1 2 3 4 5 6 7 8 9"

    options_lst = options.split()

    possibility_found = False
    for o in options_lst:
      if not (str(r_p) + "_" + o) in row_set_copy and not (str(c_p) + "_" + o) in col_set_copy and not (str(r_p//3) + "_" + str(c_p//3) + "_" + o) in square_set_copy:
        possibility_found = True
        
        board_cells_copy[r_p*9 + c_p] = o
        row_set_copy.add(str(r_p) + "_" + o)
        col_set_copy.add(str(c_p) + "_" + o)
        square_set_copy.add(str(r_p//3) + "_" + str(c_p//3) + "_" + o)

        if r_p == 8 and c_p == 8:
          return board_cells_copy
        
        baord_cells_cp = depth_first_search_helper(copy.deepcopy(board_cells_copy), copy.deepcopy(row_set_copy), copy.deepcopy(col_set_copy), copy.deepcopy(square_set_copy), r2, c2)

        if len(baord_cells_cp) == 81:
          break
        
        board_cells_copy[r_p*9 + c_p] = options
        row_set_copy.remove(str(r_p) + "_" + o)
        col_set_copy.remove(str(c_p) + "_" + o)
        square_set_copy.remove(str(r_p//3) + "_" + str(c_p//3) + "_" + o)

    if not possibility_found:
      return []

  else:
    if r_p == 8 and c_p == 8:
      return board_cells_copy
    baord_cells_cp = depth_first_search_helper(copy.deepcopy(board_cells_copy), copy.deepcopy(row_set_copy), copy.deepcopy(col_set_copy), copy.deepcopy(square_set_copy), r2, c2)

  if len(baord_cells_cp) == 81:
    return baord_cells_cp
  return []

if __name__ == '__main__':
   main()
