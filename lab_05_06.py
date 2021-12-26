import numpy
import random
keyboard_matrix=[] 
random_matrix=[]

def create_keyboard_matrix(matrix, n, m):
    for i in range(n):           
        arr =[] 
        for j in range(m):
            print("arr["+str(i)+"]["+str(j)+"]=", end="")        
            arr.append(int(input())) 
        matrix.append(arr)
    return matrix 
    
def print_matrix(matrix):
    print("Матриця:")
    print(numpy.matrix(matrix))

def create_random_matrix(matrix, n, m):
    for i in range(n):           
        arr =[] 
        for j in range(m):
            a=random.randint(-5, 5)
            print("arr["+str(i)+"]["+str(j)+"]="+str(a))
            arr.append(a)       
        matrix.append(arr)    
    return matrix

def find_saddle_points(matrix, n, m):
    k=0
    arr_min_row=numpy.min(matrix, axis=1) #функція створює список з мінімальних елементів кожного рядка матриці
    arr_max_col=numpy.max(matrix, axis=0) #функція створює список з максимальних елементів кожного стовпця матриці
    for i in range(n):
        for j in range(m):
            if((matrix[i][j] == arr_min_row[i]) and (matrix[i][j] == arr_max_col[j])):
                k=k+1
                print("\nСідлова точка:", matrix[i][j]) 
                print("Номер рядка: "+str(i+1)+", номер стовпчика:", j+1, "\n")
    if(k==0):
        print("\nСідлових точок не знайдено", "\n") 

def find_negative(matrix, n):
    k=0
    m=0
    for i in range(n):
        row = matrix[i][:] #створюємо зріз рядка
        k = numpy.sum(numpy.array(row)<0) #функція рахує кількість від'ємних чисел у рядку
        m = row.count(0) #функція рахує кількість нулів у рядку
        if (k!=0 and m!=0):
            print("У рядку", i+1, "є нуль, кількість від'ємних", k)
        elif(k==0 and m!=0):
            print("У рядку", i+1, "нема від'ємних")
        elif(k!=0 and m==0):
            print("У рядку", i+1, "нема нулів")
        else:
            print("У рядку", i+1, "нема від'ємних і нема нулів")

n=int(input("\nВведіть кількість рядків матриці n:"))
m=int(input("\nВведіть кількість стовпців матриці m:"))
print("\n\tМоя матриця")
create_keyboard_matrix(keyboard_matrix, n, m)
print_matrix(keyboard_matrix)
find_saddle_points(keyboard_matrix, n, m)
find_negative(keyboard_matrix, n)
print("\n\tРандомна матриця")
create_random_matrix(random_matrix, n, m)
print_matrix(random_matrix)
find_saddle_points(random_matrix, n, m)
find_negative(random_matrix, n)