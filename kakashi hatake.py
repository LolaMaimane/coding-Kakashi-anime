Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Lola Maimane\AppData\Local\Programs\Python\Python312\kakashi hatake.py
Traceback (most recent call last):
  File "C:\Users\Lola Maimane\AppData\Local\Programs\Python\Python312\kakashi hatake.py", line 338, in <module>
    kakashi_obj.draw()
  File "C:\Users\Lola Maimane\AppData\Local\Programs\Python\Python312\kakashi hatake.py", line 318, in draw
    self.draw_fn(self.right_eye)
  File "C:\Users\Lola Maimane\AppData\Local\Programs\Python\Python312\kakashi hatake.py", line 299, in draw_fn
    self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)
  File "C:\Users\Lola Maimane\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 1775, in goto
    self._goto(Vec2D(x, y))
  File "C:\Users\Lola Maimane\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 3230, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Users\Lola Maimane\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 745, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Users\Lola Maimane\AppData\Local\Programs\Python\Python312\Lib\tkinter\__init__.py", line 2851, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
