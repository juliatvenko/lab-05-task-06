import random
import numpy 
keyboard_matrix=[] 
random_matrix=[] 

def create_keyboard_matrix(matrix, n):
    for i in range(n):           
        arr =[] 
        for j in range(n):
            print("arr["+str(i)+"]["+str(j)+"]=", end="")        
            arr.append(int(input())) 
        matrix.append(arr)
    return matrix 
    
def print_matrix(matrix, n):
    print("Матриця:")
    print(numpy.matrix(matrix))

def create_random_matrix(matrix, n):
    for i in range(n):           
        arr =[] 
        for j in range(n):
            a=random.randint(-20, 20)
            print("arr["+str(i)+"]["+str(j)+"]="+str(a))
            arr.append(a)       
        matrix.append(arr)    
    return matrix

def min_main_diag(matrix, n):
    min_element=matrix[0][0]
    for i in range(n):            
            if matrix[i][i]< min_element:
                min_element=matrix[i][i]
    #або min_element=numpy.min(numpy.diag(matrix))
    print("Мінімальний елемент головної діагоналі матриці:", min_element)

n=int(input("\nВведіть розмір квадратної матриці n:"))
print("\n\t\t\tМоя матриця")
create_keyboard_matrix(keyboard_matrix, n)
print_matrix(keyboard_matrix, n)
min_main_diag(keyboard_matrix, n)
print("\n\t\t\tРандомна матриця")
create_random_matrix(random_matrix, n)
print_matrix(random_matrix, n)
min_main_diag(random_matrix, n)