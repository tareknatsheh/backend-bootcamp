# we want to return all prime number up to n using an algorithm called (sieve of eratosthenes)
# The algorithm:
# 1) loop over all the items in the main list
# 2) check if the item is dividable by any of the items in the prime nums list
# 3) if yes --> remove it from the main list and insert it into the prime list

def return_prime_numbers_up_to(n):
    # The range() returns a range obj not a list, so we have to convert it
    # if we want to use functions list .append or .remove
    main_nums_list = list(range(4, n + 1))
    prime_nums_list = [2, 3]

    # first let's remove all of the 2 and 3 prime numbers multiplications:
    main_nums_list = [i for i in main_nums_list if i % 2 != 0]
    main_nums_list = [i for i in main_nums_list if i % 3 != 0]

    # loop over a copy (important not to loop over the origianl bcoz of .remove()) of the original main_nums_list
    for num in main_nums_list[:]:
        for prime in prime_nums_list:
            if num % prime == 0:
                break

        # If it is not dividable by any of the nums in the prime_nums_list,
        # then, it's a prime number!
        # Add it to the prime_nums_list:
        else: # Note that this "else" won't get executed if we hit a "break"
            prime_nums_list.append(num)
            main_nums_list = [i for i in main_nums_list if i % num != 0]

    return prime_nums_list



user_input = int(input("Get all prime number up to: "))

prime_up_to_n = return_prime_numbers_up_to(user_input)
print(f"There are {len(prime_up_to_n)} prime numbers:")
print(prime_up_to_n)