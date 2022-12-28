```
def switch(choice, num1, num2):
    if choice == 1:
        result = num1 + num2;
        print(str(num1), "+",str(num2),  "= " + str(result));

    elif choice == 2:
        if num1 < num2:
           prompt = input("Number 1 is less than number 2. Do you wish to continue? Y/N: ");
           if prompt == 'Y': # 0x59
                result = num1 / num2;
                print(str(num1), "/",str(num2),  "= " + str(result));
           elif prompt == 'N': # 0x4E
                print("Very well exiting...");

    elif choice == 3:
        result = num1 * num2;
        print(str(num1), "*",str(num2),  "= " + str(result));
    
    elif choice == 4:
        if num1 < num2:
           prompt = input("Number 1 is less than number 2. Do you wish to continue? Y/N: ");
           if prompt == 'Y': # 0x59
                result = num1 / num2;
                print(str(num1), "/",str(num2),  "= " + str(result));
           elif prompt == 'N': # 0x4E
                print("Very well exiting...");

print("\t\tI got money and it's easy(calculator)");
print("--------------------------------------------------------------------------------------------");
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division");
choice = input("Option: ");
num1 =  input("Number1: ");
num2 = input("Number2: ");
switch(int(choice), int(num1), int(num2));
```
