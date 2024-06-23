import threading
import random
import time

random_numbers = []
list_filled = threading.Event()

# Funkce pro vytvo�en� seznamu s n�hodn�mi ��sly
def fill_list():
    global random_numbers
    random_numbers = [random.randint(1,100) for _ in range(10)]
    print(f"List filled with random numbers: {random_numbers}")
    list_filled.set() # toto je sign�l, �e byl vytvo�en seznam

# Funkce, kter� spo��t� sou�et prvk� v seznamu
def calculate_sum():
    list_filled.wait() # �ek�, dokud nebude vytvo�en seznam
    total_sum = sum(random_numbers)
    print(f"Sum of list elements: {total_sum}")

# Funkce pro v�po�et pr�m�ru z prvk� v seznamu
def calculate_average():
    list_filled.wait()
    average = sum(random_numbers) / len(random_numbers)
    print(f"Average fo list elements: {average}")

# Vytvo�en� thread�
fill_thread = threading.Thread(target=fill_list)
sum_thread = threading.Thread(target=calculate_sum)
average_thread = threading.Thread(target=calculate_average)

# SPu�t�n� thread�
fill_thread.start()
sum_thread.start()
average_thread.start()

fill_thread.join()
sum_thread.join()
average_thread.join()
