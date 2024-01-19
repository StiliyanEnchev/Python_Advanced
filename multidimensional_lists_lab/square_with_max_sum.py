row, col = [int(x) for x in input().split(', ')]
matrix = []
max_sum = float("-inf")
sub_matrix = []
for row_num in range(row):
    matrix.append([(int(x)) for x in input().split(', ')])

for row_num in range(row - 1):
    for col_num in range(col - 1):
        cur_el = matrix[row_num][col_num]
        next_el = matrix[row_num][col_num+1]
        el_under = matrix[row_num+1][col_num]
        el_diagonal = matrix[row_num+1][col_num+1]

        total_sum = cur_el + next_el + el_diagonal + el_under
        
        if total_sum >= max_sum:
            max_sum = total_sum
            sub_matrix = [[cur_el, next_el], [el_under, el_diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)