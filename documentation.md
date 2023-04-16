# Shellderer
**Very basic image/video renderer in a shell using Python**
### Introduction<br>
-This renderer mostly uses x and y coordinates
-render() shows an image quickly and erases it<br>
-modify() modifies a single value from a string with x and y<br>
-modify_raw() does the same thing but without x and y<br>
-tell() tells a value using x and y<br>
-all_y() loops through all y values in a string<br>
-all_x() loops through all x values in a string<br>
### render(text,*args)<br>
  -To render just type as the first argument what to render<br>
  -For example:"render("hello_world")"<br>
  -The second argument is optional and it determines how long it will wait before cleaning the screen for example 0.1 second<br>
  -The third argument is optional too and it allows you an input requirement so the user needs to input before they continue. It returns the value from the user.<br>
  -Here is an example: "value = render("hello world",0,' prompt: ')<br>
### modify(text,new,x,y):<br>
  -To modify your string use this function. It asks for four arguments which are string, new, x and y<br>
  -The string is asking for a string to modify<br>
  -New asks for what to modify it into<br>
  -X asks for where on 1 line to modify it<br>
  -Y asks for which line to modify<br>
  -After that, it just returns the modified string as a value<br>
  -Here is an example:"value = modify(previous_value,'hello world",0,0)<br>
### raw_modify(text,new,loc):<br>
  -Used to modify the string in the raw format following this syntax string, new, loc<br>
  -String is which string to use which is the exact same as in modify<br>
  -New is the same as modify<br>
  -Loc is used instead of x and y. It searches through a list directly<br>
  -It can't pick newlines and will return an exception if you try to<br>
  -Here is an example: "value = raw_modify('abc123\na','b' , 6)" would return an exception because you are trying to pick a newline but value = raw_modify('abc123\na' , 'b' , 5) would not.<br>
### tell(text,x,y):<br>
-This command is very similar to modify<br>
-It uses all the arguments modify uses just without new<br>
-Unlike modify this command returns the value you picked instead of the modified list<br><br>
-Here is an example:"value = tell('abc123',0,0)" This would pick "a" and value would equal "a"<br>
### all_y(text):<br>
-This command is a generator which will loop through each y in text<br>
-Here is an example:"for i in all_y("something\nsomething"): print(i,end="")" This would return :"somethingsomething"<br>
### all_x(text):<br>
-all_x is similar to all_y but it returns it in a reverse way<br>
-Note that it does return half full lines but replaces empty for spaces
