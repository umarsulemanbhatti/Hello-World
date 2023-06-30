from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())

def unique_koala_facts(facts):
    new_list = []
    iteration = 0
    while len(new_list) < facts and iteration < 1000:
        fact = random_koala_fact()
        if fact not in new_list:
            new_list.append(fact)
        iteration += 1
    return new_list

def num_joey_facts():
    unique_facts = []
    count = 0
    target_fact = None
    repetitions = 0

    while repetitions < 10:
        fact = random_koala_fact()
        if "joey" in fact.lower():
            if fact not in unique_facts:
                unique_facts.append(fact)
                count += 1
            if fact == target_fact:
                repetitions += 1
            elif target_fact is None:
                target_fact = fact
                repetitions = 1

    return count

def koala_weight():
    while True:
        fact = random_koala_fact()
        if "kg" in fact:
            index_of_kg = fact.find("kg")
            spl_fact = fact[:index_of_kg]
            number = spl_fact.split()[-1]
            if number.isdigit():
                int_num = int(number)
                return int_num

print(unique_koala_facts)
print(num_joey_facts)
print(koala_weight)