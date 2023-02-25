from manim import *

class Blockchain(Scene):
    def construct(self):
        # Add first block
       # Add first block
        block_1 = Rectangle(width=4, height=2, fill_opacity=0.4, stroke_width=2, color=PURPLE)


        divider_line_1 = always_redraw(lambda: Line(block_1.get_left(), block_1.get_right(), color=BLUE, stroke_width=2)).set_run_time(2)      
        transaction_1 = always_redraw(lambda:Text("DATA", color=WHITE).scale(0.4).next_to(divider_line_1, DOWN, buff=0.3))
        function_1 = always_redraw(lambda:MathTex("f(x)").scale(0.4).next_to(divider_line_1, UP, buff=0.3))

        # Add second block
        block_2 = Rectangle(width=4, height=2, fill_opacity=0.4, stroke_width=2, color=PURPLE).next_to(block_1, DOWN, buff=1.4)


        divider_line_2 = Line(block_2.get_left(), block_2.get_right(), color=BLUE, stroke_width=2)    
        transaction_2 = always_redraw(lambda:Text("DATA 2", color=WHITE).scale(0.4).next_to(divider_line_2, DOWN, buff=0.3))
        function_2 = always_redraw(lambda:MathTex("g(x)").scale(0.4).next_to(divider_line_2, UP, buff=0.3))

        # Add connecting line
        line = Line(block_1.get_bottom(), block_2.get_top(), color=WHITE, stroke_width=2)

        # Add many blocks
        blocks = VGroup(*[Rectangle(width=0.5, height=0.5, fill_opacity=1, fill_color=WHITE, stroke_width=1, color=BLUE) for _ in range(10)])
        blocks.arrange_in_grid(5, 2, buff=0.3)
        blocks.shift(3*DOWN)

        # Add text to screen
        title = Text("Blockchain", color=BLUE).scale(1.2)
        subtitle = Text("A super secure digital notebook", color=BLUE).scale(0.7).next_to(title, DOWN, buff=0.3)
        thanks = Text("Thanks for watching!", color=BLUE).scale(0.7)

        # Add camera movements
        self.play(FadeIn(title))
        self.wait(0.5)
        self.play(FadeIn(subtitle))
        self.wait(0.5)
        self.play(FadeOut(subtitle))
        self.play(FadeOut(title))

        firstEle = VGroup(block_1, function_1, divider_line_1, transaction_1)
        self.play(Create(firstEle))

        self.wait(4)
        self.play(firstEle.animate.shift(2*UP))
        self.wait(4)
        secondEle = VGroup(block_2, function_2, divider_line_2, transaction_2)
        self.play(Create(secondEle))
        self.play(secondEle.animate.shift(2*UP))


        # self.play(Create(block_2))
        # self.wait(3)
        # self.play(Create(function_2))
        # self.play(Create(divider_line_2))
        # self.play(Create(transaction_2))

        # self.wait(0.5)
        # self.play(Create(line))
        # self.wait(0.5)
        # self.play(
        #     block_2.animate.shift(2*DOWN),
        #     function_2.animate.shift(2*DOWN),
        #     transaction_2.animate.shift(2*DOWN),
        #     line.animate.put_start_and_end_on(block_1.get_bottom(), block_2.get_top() - 2*DOWN)
        # )
        # self.wait(0.5)
        # self.play(Create(blocks))
        # self.wait(0.5)
        # self.play(
        #     *[block.animate.shift(3*LEFT) for block in blocks[::2]],
        #     *[block.animate.shift(3*RIGHT) for block in blocks[1::2]],
        #     run_time=1
        # )
        # self.wait(0.5)
        # self.play(FadeOut(title))
        # self.play(FadeOut(thanks))
        # self.wait(0.5)
