# # list with strings 
# # names = ["Bob", "Alex", "Kevin "]
# # # names.append("joseph")

# # # for name in sorted (names):
# # #     print(f"{name}")
# # #     list with floats
# # #     measuments = [-2.5,1.1,7.5,14.61,21.05,3.14]
# # #     mean = sum(measuments) / len(measuments)
# # #     print(f"Mean: {mean}")

# # # list within list
# # super_list = [[5,2,3],[4,1][2,2,5,1]]   
# # print (super_list[1][0])
# # grades =[["Shakira",8,"D"],["Bad Bunny",0,"F"],["Gabriel",10,"C"]]
# # for student in grades:
# # 	name = student[0]
# # 	grade = student[1]
# # 	letter = student[2]
# # 	print(f"{name} has a grade of {grade} which in group {letter}")
 

# matrices 
matrix = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
# Print columns instead of rows
# le pide el numero de columnas y le dice a la maquina que es igual a la matrix 
num_cols = len(matrix[0])
num_rows = len(matrix)
# explica que para col in un rango ponga num la variable numero de columnas 
for col in range(num_cols):
	column = [matrix[row][col] for row in range(num_rows)]
	# le pide a la maquibna que imprima la columna
	print(column)
# imprime las columnas  en vez de los rows    
# imprime lo que pide el profe    

