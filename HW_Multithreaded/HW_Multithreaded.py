import threading
import random
import time

random_numbers = []
list_filled = threading.Event()

# Funkce pro vytvoøení seznamu s náhodnými èísly
def fill_list():
    global random_numbers
    random_numbers = [random.randint(1,100) for _ in range(10)]
    print(f"List filled with random numbers: {random_numbers}")
    list_filled.set() # toto je signál, že byl vytvoøen seznam

# Funkce, která spoèítá souèet prvkù v seznamu
def calculate_sum():
    list_filled.wait() # èeká, dokud nebude vytvoøen seznam
    total_sum = sum(random_numbers)
    print(f"Sum of list elements: {total_sum}")

# Funkce pro výpoèet prùmìru z prvkù v seznamu
def calculate_average():
    list_filled.wait()
    average = sum(random_numbers) / len(random_numbers)
    print(f"Average fo list elements: {average}")

# Vytvoøení threadù
fill_thread = threading.Thread(target=fill_list)
sum_thread = threading.Thread(target=calculate_sum)
average_thread = threading.Thread(target=calculate_average)

# SPuštìní threadù
fill_thread.start()
sum_thread.start()
average_thread.start()

fill_thread.join()
sum_thread.join()
average_thread.join()
