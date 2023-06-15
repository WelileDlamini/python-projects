while True:

    try:
        age = int(input('What is your age'))
        print(age)
        raise ValueError('Hey cut it out!!!!') #identifying an error and stopping
    except (ValueError, NameError):
        print('please enter a number')
        continue

    except ZeroDivisionError:
        print('please enter a number greater than zero')
        break
    else: # however if the is no error do this
        print('thank you')
        break
    finally: # runs regardless at the end of everything
        print('ok I am done now thank you')
