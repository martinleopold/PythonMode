# template.py
# to get you started

from processing.core import PApplet

class pytest(PApplet):
  s = 200
  def setup(self):
    self.size(300, 300)
  
  def draw(self):
    self.background(0)
    self.fill(self.s)
    self.ellipse(self.width/2, self.height/2, self.s, self.s)
    if self.s == 0:
      self.s=200
    else:
      self.s-=1

pytest().runSketch()
