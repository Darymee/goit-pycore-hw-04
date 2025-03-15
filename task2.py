def get_cats_info(path):
    cat_list = []
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    age = int(age)
                    cat_list.append({"id": cat_id, "name": name, "age": age})
            

                except ValueError as e:
                    print(f"Can't read line: {line.strip()} ({e})")

    except FileNotFoundError:
        print("File not found")  
    except Exception as e:
        print(f"Unexpected error: {e}")

    
    return cat_list   


cats_info = get_cats_info("./cats.txt")
print(cats_info)