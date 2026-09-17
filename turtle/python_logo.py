import turtle  # 画一个python

turtle.setup(400,400) 
  
turtle.speed(0)
turtle.penup()  

turtle.goto(-80,-70)#起点
turtle.color("blue","blue")
turtle.begin_fill()
turtle.left(90)
turtle.pendown()
turtle.forward(50)#竖直
turtle.circle(-20,90)
turtle.forward(100)#水平
turtle.circle(20,90)
turtle.forward(80)#竖直
turtle.circle(20,60)
turtle.circle(120,60)
turtle.circle(10,60)
turtle.forward(40)#竖直
turtle.left(90)
turtle.forward(80)#水平
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(130)#水平
turtle.circle(40,60)
turtle.circle(100,60)#大弧
turtle.circle(20,60)
turtle.forward(62)
turtle.end_fill()
turtle.penup()

turtle.goto(80,70)#起点
turtle.begin_fill()
turtle.color("yellow","yellow")
turtle.right(90)
turtle.pendown()
turtle.forward(50)#竖直
turtle.circle(-20,90)
turtle.forward(100)#水平
turtle.circle(20,90)
turtle.forward(80)#竖直
turtle.circle(20,60)
turtle.circle(120,60)
turtle.circle(10,60)
turtle.forward(40)#竖直
turtle.left(90)
turtle.forward(80)#水平
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(130)#水平
turtle.circle(40,60)
turtle.circle(100,60)#大弧
turtle.circle(20,60)
turtle.forward(62)
turtle.end_fill()
turtle.penup()

turtle.goto(-50,90)
turtle.color("white")
turtle.pendown()
turtle.dot(30)
turtle.penup()

turtle.goto(50,-90)
turtle.pendown()
turtle.dot(30)
turtle.hideturtle()

turtle.done()  # 保持绘图窗口打开，直到手动关闭
