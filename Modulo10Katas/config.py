def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except PermissionError:
        print("you do not have the permissions to enter that directory")
    except (BlockingIOError, TimeoutError):
       print("Filesystem under heavy load, can't complete reading configuration file")


if __name__ == '__main__':
    main()