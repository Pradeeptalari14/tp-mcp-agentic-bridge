from manim import *

class MCPGatewayAnimation(Scene):
    def construct(self):
        title = Text("Model Context Protocol (MCP) Gateway", font_size=36, color=PURPLE)
        title.to_edge(UP)
        self.play(Write(title))

        agent = Rectangle(width=3, height=1.5, color=GREEN).shift(LEFT * 4)
        agent_txt = Text("AI Agent\n(Claude / Cursor)", font_size=16).move_to(agent)

        gateway = Rectangle(width=3.5, height=2, color=PURPLE).move_to(ORIGIN)
        gw_txt = Text("MCP Gateway\n(RBAC + SSE)", font_size=18).move_to(gateway)

        tool = Rectangle(width=3, height=1.5, color=BLUE).shift(RIGHT * 4)
        tool_txt = Text("Backend Tools\n(DB / Git / K8s)", font_size=16).move_to(tool)

        arr1 = Arrow(agent.get_right(), gateway.get_left(), color=YELLOW)
        arr2 = Arrow(gateway.get_right(), tool.get_left(), color=YELLOW)

        self.play(Create(agent), Write(agent_txt))
        self.play(GrowArrow(arr1), Create(gateway), Write(gw_txt))
        self.play(GrowArrow(arr2), Create(tool), Write(tool_txt))
        self.wait(1)
