it = 10

while it>1:     #colon only in loops
    if it == 9:
        it = it - 1
        continue        #continue keyword will skip the current iteration, and go to next iteration
    if it == 3:
        break           #break will halt or stop the execution, it'll break the entirev while loop
    print(it)

    it = it - 1

print('while loop execution is done')

print("*********************************")

it = 5
while it > 1:
    if it == 3:
        break
    print(it)
    it = it - 1

