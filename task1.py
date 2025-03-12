def total_salary(path):
    try:
        total = 0                                        
        workers = 0 
        with open(path, "r", encoding="utf-8") as file:
     
            for line in file:
                try:
                    salary = int(line.strip().split(",")[1])
                    total += salary
                    workers += 1

                except ValueError:
                    print(f"Can't count because value should be integer: {line.strip().split(",")[1]}")

                average_salary = int(total / workers) 
            
    except FileNotFoundError:
        print("File not found")   
    except Exception as e:
        print(f"Unexpected error: {e}")
     
    return (total, average_salary)


total, average = total_salary("./salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
