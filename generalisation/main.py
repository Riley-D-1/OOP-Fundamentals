from fast_food import *
import time as t
maria = Cashier("Maria",12346,15,18)
b = maria.clock_in()
t.sleep(2)
maria.clock_out(b)
maria.get_pay()
maria.add_transaction()
dave = Cleaner("Dave",12345,15,18,"Kitchen")
a = dave.clock_in()
t.sleep(2)
dave.clock_out(a)
dave.get_pay()
dave.check_area()
nathan  = Cook("Nathan",12465,12,20)
max = drive_thru_Cashier("Max",1234565,20,13,"1")
c = max.clock_in()
t.sleep(2)
max.clock_out(c)
max.get_pay()
max.check_lane()