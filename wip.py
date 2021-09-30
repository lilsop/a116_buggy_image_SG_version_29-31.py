#   a116_buggy_image.py
import turtle as trtl
# creating a spider body (spider is my painter name)
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
# configuring the spider legs
leg_num = 4
leg_length = 70
leg_heading = 180 / leg_num
print("leg_heading=", leg_heading)
spider.pensize(5)
count = 0
# drawing legs
while (count < leg_num):
  spider.goto(0,20)
  spider.setheading(leg_heading*(count + 45))
  spider.forward(leg_length)
  count = count + 1
while (count < leg_num)
  spider.goto(0,20)
  spider.setheading(leg_heading*(count - 45))
  spider.forward(leg_length)
  count = count + 1
  print("leg_heading*count=", leg_heading*count)
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
