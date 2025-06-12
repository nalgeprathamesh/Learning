# Finally literally runs everytime with no exception.
# It is useful in function where if we use return then print() statement is not printed
# But finally overrides even in function and runs with no exception

def main():
    try:
        a = int(input("Enter a number: "))
        print(f"The number is {a}")
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I am finally, I always run")

    print("I am print, but i can't run because the value in function has been returned")


main()