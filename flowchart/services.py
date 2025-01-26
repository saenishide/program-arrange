from graphviz import Digraph

def generate_flowchart():
    dot = Digraph(comment = 'ソースコードのフローチャート')

    dot.node('A', '開始', shape='ellipse', style='filled', color='lightgrey', fontname='Noto Sans JP')
    dot.node('B', '変数"a"を入力する', shape='box', style='filled', color='lightblue', fontname='Noto Sans JP')
    dot.node('C', '変数"b"を入力する', shape='box', style='filled', color='lightblue', fontname='Noto Sans JP')
    dot.node('D', 'a > b', shape='diamond', style='filled', color='lightgreen', fontname='Noto Sans JP')
    dot.node('E', '変数"a"の値を出力する', shape='box', style='filled', color='lightyellow', fontname='Noto Sans JP')
    dot.node('F', '変数"b"の値を出力する', shape='box', style='filled', color='lightyellow', fontname='Noto Sans JP')
    dot.node('G', '終了', shape='ellipse', style='filled', color='lightgrey', fontname='Noto Sans JP')

    dot.edges(['AB', 'BC', 'CD'])
    dot.edge('D', 'E', label='True', color='green', style='dashed')
    dot.edge('D', 'F', label='False', color='red', style='dotted')
    dot.edge('E', 'G', color='blue')
    dot.edge('F', 'G', color='blue')

    dot.render('./tmp/flowchart', format='pdf', view=True, cleanup=True)