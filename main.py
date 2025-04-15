from random import random, randint
import time

# addition game
def addition(n):
    correct = 0

    start = time.time()
    for i in range(n):
        print(f"Round {i+1}")
        n1 = randint(1,100)
        n2 = randint(1,100)
        
        answer = n1 + n2
        guess = int(input(f"{n1} + {n2}\n"))
        
        if guess == answer:
            correct += 1
    end = time.time()
            
    print(f"Correct: {correct}, in {end-start} seconds.")

def multiplication(n):
    correct = 0
    
    start = time.time()
    for i in range(n):
        print(f"Round {i+1}")
        n1 = randint(2,15)
        n2 = randint(2,15)
        
        answer = n1 * n2
        guess = int(input(f"{n1} * {n2}\n"))
        
        if guess == answer:
            correct += 1
    end = time.time()

    print(f"Correct: {correct}, in {end-start} seconds.")
    
        

def main():
    addition(10)
    multiplication(10)


if __name__ == "__main__":
    main()
