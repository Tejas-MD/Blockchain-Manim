from manim import *

# class Updaters(Scene):
#         def construct(self):
#                 num = MathTex("f(x)")
#                 box = always_redraw(lambda: SurroundingRectangle(num, color=BLUE, fill_opacity =0.4, fill_color=RED, buff = 2))
#                 name= always_redraw(lambda:Text("Tejas", color = BLUE).next_to(box, DOWN))

#                 self.play(Create(VGroup(num, box, name)), run_time = 7)
#                 self.play(num.animate.shift(RIGHT*4), run_time = 4)


                
class Testing (Scene):
    def construct(self):
        rect = Rectangle(color = WHITE, height= 3, width = 3)

        circ = Circle().to_edge(DL)

        arrow = always_redraw(lambda : Line(start= rect.get_edge_center(LEFT), end = circ.get_center(), color = RED).add_tip())

        self.play(Create(VGroup(rect, circ, arrow)), run_time = 6)
        self.play(rect.animate.to_edge(DR),circ.animate.to_edge(UL),run_time = 6)
    


