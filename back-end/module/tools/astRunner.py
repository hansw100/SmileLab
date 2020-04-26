import ast
from pprint import pprint


def main():
    with open("c:/Users/rdd92/Desktop/Develop/SmileLab/smileLab/back-end/source/10/Main.py", "r", encoding='UTF8') as source:
        tree = ast.parse(source.read())

    print(ast.dump(tree) + "\n")
    analyzer = Analyzer()
    analyzer.visit(tree)
    analyzer.report()

class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"input": 0, "Return": 0, "Logical": 0, "Compare": 0, "Function": 0, "While": 0, "For": 0, "If": 0, "tuple": 0,
                      "list": 0, "num": 0, "AugAssign": 0, "Assign": 0, "BinOp": 0, "Expr": 0, "Name": [], "Str": 0, "Constant": 0}

    def visit_Assign(self, node):
        "할당정의 카운터 ex) a=5"
        self.stats["Assign"] += 1
        # if isinstance(node.targets[0], ast.Tuple):
        #     for i in range(2):
        #         self.visit_Name(node.targets[0].elts[i])
        self.generic_visit(node)

    def visit_Constant(self, node):
        "constant 카운터"
        self.stats["Constant"] += 1
        self.generic_visit(node)

    def visit_Tuple(self, node):
        "튜플 카운터"
        # self.stats["Name"].append(node)
        self.generic_visit(node)

    def visit_BinOp(self, node):
        "연산자 카운터 ex) a=3*6"
        self.stats["BinOp"] += 1
        self.generic_visit(node)

    def visit_Expr(self, node):
        "표현식에 대한 방문 정의 ex)3*7+5"
        self.stats["Expr"] += 1
        # self.generic_visit(node)

    def visit_Name(self, node):
        "변수에 값을 할당하기 위한 정의. ex) a=5값 5를 보유하는 변수 a를 말함"
        if node.id in self.stats["Name"]:
            pass
        else:
            self.stats["Name"].append(node.id)

    def visit_AugAssign(self, node):
        "단항연산자 카운터"
        self.stats["AugAssign"] += 1
        self.generic_visit(node)

    def visit_If(self, node):
        "조건문 카운터"
        self.stats["If"] += 1
        self.generic_visit(node)

    def visit_For(self, node):
        "for 카운터"
        self.stats["For"] += 1
        self.generic_visit(node)

    def visit_While(self, node):
        "while 카운터"
        self.stats["While"] += 1
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        "함수정의 카운터"
        self.stats["Function"] += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        "논리연산자 카운터"
        self.stats["Logical"] += 1
        self.generic_visit(node)

    def visit_Compare(self, node):
        "비교연산자 카운터"
        self.stats["Compare"] += 1
        self.generic_visit(node)

    def visit_Return(self, node):
        "리턴 카운터"
        self.stats["Return"] += 1
        self.generic_visit(node)

    def visit_Not(self, node):
        "논리연산자 카운터"
        self.stats["Logical"] += 1
        self.generic_visit(node)

    def report(self):
        pprint(self.stats)


if __name__ == "__main__":
    main()