from enum import Enum

class State(Enum):
    unknown = 0
    light = -1
    heavy = 1

def getInput(left, right):
    print(f"|{','.join([str(x) for x in left])}| \t |{','.join([str(x) for x in right])}|")
    print(f"|{'-'*(len(left)*2-1)}| \t |{'-'*(len(right)*2-1)}|")
    dir = -1
    while dir < 1 or dir > 3:
        print("Where does the scale lean:")
        print("1. Left")
        print("2. Right")
        print("3. Neither")
        try:
            dir = int(input(':'))
        except(ValueError):
            pass

    dir = int(dir)
    if dir == 1:
        dir = 'left'
    elif dir == 2:
        dir = 'right'
    elif dir == 3:
        dir = 'none'
    return dir

def resolve3(balls, state):
    left = [balls[0]]
    right = [balls[1]]
    dir = getInput(left, right)

    if dir == 'left':
        if state == State.heavy:
            print(f"The fake ball is the ball {left[0]} and it's heavier than the rest")
        else:
            print(f"The fake ball is the ball {right[0]} and it's lighter than the rest")
    elif dir == 'right':
        if state == State.heavy:
            print(f"The fake ball is the ball {right[0]} and it's heavier than the rest")
        else:
            print(f"The fake ball is the ball {left[0]} and it's lighter than the rest")
    else:
        if state == State.heavy:
            print(f"The fake ball is the ball {balls[2]} and it's heavier than the rest")
        else:
            print(f"The fake ball is the ball {balls[2]} and it's lighter than the rest")


def resolve1(ball, real_ball):
    left = [ball]
    right = [real_ball]
    dir = getInput(left, right)
    if dir == 'left':
        print(f"The fake ball is the ball {ball} and it's heavier than the rest")
    else:
        print(f"The fake ball is the ball {ball} and it's lighter than the rest")

def resolve8(light, heavy, real):
    left = light[:3]
    left.extend(heavy[:2])
    right = [light[3]] + real[:4]
    dir = getInput(left, right)
    if dir == 'left':
        new_left = [left[-2]]
        new_right = [left[-1]]
        dir = getInput(new_left, new_right)
        if dir == 'left':
            print(f"The fake ball is ball {new_left[0]} and it's heavier than the rest")
        elif dir == 'right':
            print(f"The fake ball is ball {new_right[0]} and it's heavier than the rest")
        else:
            print(f"The fake ball is ball {right[0]} and it's lighter than the rest")
    elif dir == 'right':
        resolve3(light[:3], State.light)
    else:
        new_left = [heavy[2]]
        new_right = [heavy[3]]
        dir = getInput(new_left, new_right)
        if dir == 'left':
            print(f"The fake ball is ball {new_left[0]} and it's heavier than the rest")
        else:
            print(f"The fake ball is ball {new_right[0]} and it's heavier than the rest")

def welcome():
    print('########################################################')
    print('12 Balls')
    print('########################################################')
    print('''Let's say we have twelve numbered balls on the table ''')
    print(' '.join(['o'for num in range(1,13)]))
    print(' '.join([str(num) for num in range(1,13)]))
    print('''Choose one of them and decide if it will weigh heavier or lighter than the rest.
The rest will weight the same. Now my task is to guess which ball you picked and whether it
weighs more or less than the other balls using my handy scale only three times.
    ''')
    print('########################################################')
    print()

def main():
    welcome()
    resolve12()

def resolve12():
    left = [1,2,3,4]
    right = [5,6,7,8]
    real = []
    light = []
    heavy = []
    skip = False
    dir = getInput(left, right)
    if dir == 'left':
        real = [9,10,11,12]
        heavy = left[:]
        light = right[:]
    elif dir == 'right':
        real = [9,10,11,12]
        heavy = right[:]
        light = left[:]
    else:
        real = left + right
        left = [9,10,11]
        right = real[:3]
        dir = getInput(left, right)
        if dir == 'left':
            resolve3(left, State.heavy)
        elif dir == 'right':
            resolve3(left, State.light)
        else:
            resolve1(12, real[0])
        return

    resolve8(light, heavy, real)

if __name__ == '__main__':
    main()