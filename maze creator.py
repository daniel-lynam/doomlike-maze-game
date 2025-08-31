import random
#r - read
#a - append
#w - write
#x - create
ysize = 20
xsize = 20
#read - error if file doesnt exist
with open("maze.txt", "w") as f:
    f.write("")

f.close()
with open("maze.txt", "a") as f:
    for i in range(ysize):
        f.write("1"*(xsize*2+1)+"\n")
        stri = ""
        for i in range(xsize*2+1):

            stri += str((i+1)%2)
        f.write(stri+"\n")
    f.write("1" * (xsize * 2 + 1) + "\n")
f.close()#template done

#print(f.read())
#print(f.read(5))

#print(f.readline())
#lines[0][1]
#for line in f:
#    print(line,end="")


#line = lines[y].rstrip('\n')

def change_digit_in_file(y, x, new_digit):
    filename = "maze.txt"
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    if y < 0 or y > len(lines):
        raise IndexError(f"Line number y={y} is out of range. File has {len(lines)} lines.")
    line = lines[y].rstrip('\n')
    if x < 0 or x >= len(line):
        raise IndexError(f"Digit position x={x} is out of range for line {y}.")
    modified_line = line[:x] + new_digit + line[x+1:]

    # Put back the newline character removed earlier
    modified_line += '\n'

    # Replace the line in the list
    lines[y] = modified_line

    # Write all lines back to the file
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)
    file.close()

def check_surrounding(y,x):

    with open("maze.txt") as mazefile:
        lines = mazefile.readlines()

    posloc = []

    if y-2 > 0 and lines[y-2][x] != "v":
        posloc.append("up")
    if y+2 < (ysize*2+1) and lines[y+2][x] != "v":
        posloc.append("down")
    if x-2 > 0 and lines[y][x-2] != "v":
        posloc.append("left")
    if x+2 < (xsize*2+1) and lines[y][x+2] != "v":
        posloc.append("right")

    return posloc

recentmoves = []
playerY = random.randint(0,ysize-1)*2+1
playerX = random.randint(0,xsize-1)*2+1
change_digit_in_file(playerY,playerX,"v")
invmove = {"up":"down","down":"up","left":"right","right":"left"}
while True:

    choices = check_surrounding(playerY,playerX)
    if choices == []:
        if recentmoves == []:
            break
        else:
            choice = invmove[recentmoves[-1]]
            recentmoves.pop()
            match choice:
                case "up":
                    playerY -= 2

                case "down":
                    playerY += 2

                case "left":
                    playerX -= 2

                case "right":
                    playerX += 2
            change_digit_in_file(playerY, playerX, "v")


    else:
        choice = random.choice(choices)
        match choice:
            case "up":
                playerY -= 2
                change_digit_in_file(playerY + 1, playerX, "0")
            case "down":
                playerY += 2
                change_digit_in_file(playerY - 1, playerX, "0")
            case "left":
                playerX -= 2
                change_digit_in_file(playerY, playerX + 1, "0")
            case "right":
                playerX += 2
                change_digit_in_file(playerY, playerX - 1, "0")
        recentmoves.append(choice)
        change_digit_in_file(playerY, playerX, "v")

#change_digit_in_file(1,1,"0")