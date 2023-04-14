import main
value = '..............................\n..............................\n..............................\n..............................\n..............................\n..............................\n..............................\n..............................\n'
place = -1
completed = True
while True:
    current_value= value
    if place < 29 and completed:
        place += 1
    elif place > -1 and not completed:
        place -= 1
    if place == 29:
        completed = False
    if place == 0:
        completed = True
    for i in main.all_y(value):
        current_value = main.modify(current_value,' ',place,i[0])
    main.render('location:'+str(place)+'\n'+current_value,0.01)