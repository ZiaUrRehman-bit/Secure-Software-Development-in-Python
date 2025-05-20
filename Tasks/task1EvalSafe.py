import ast
import operator

def safe_eval(expr):
    allowed_ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv
    }

    def eval_node(node):
        if isinstance(node, ast.BinOp):
            return allowed_ops[type(node.op)](eval_node(node.left), eval_node(node.right))
        elif isinstance(node, ast.Num):
            return node.n
        else:
            raise ValueError("Unsupported operation")

    tree = ast.parse(expr, mode='eval')
    return eval_node(tree.body)

expr = input("Enter a simple math expression (e.g., 2+3*4): ")
print("Result:", safe_eval(expr))
