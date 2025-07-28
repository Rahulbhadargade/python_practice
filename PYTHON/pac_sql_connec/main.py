from inputs import demo, sample
from functions import add,sub
from database import db
n1,n2 = demo.user_inp()
num1 = sample.A 
num2 = sample.B
res = add.add(n1,n2)
diff =sub.sub(num1,num2)
db.create_table()
db.insert(res,diff)
db.display()


# codeshare.io/mini_pro