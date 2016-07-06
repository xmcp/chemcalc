#coding=utf-8
from chemparser import *
from ply import lex, yacc
from chem_weight import weight
def proc(mat: Materials):
    return sum(map((lambda tok_cnt: weight[tok_cnt[0]]*tok_cnt[1]), mat.mats.items()))

#tokens+=['NUMBER']
literals+=['+','-','*','/','[',']']

precedence+=[
    ('left','calc_lazy'),
    ('left','calc_rapid'),
]

def p_math_fromexpr(p):
    """math : '[' expr ']'"""
    p[0]=proc(p[2])

def p_math_fromnumber(p):
    """math : CNT"""
    p[0]=p[1]

def p_math_primary_school(p):
    """math : math '+' math %prec calc_lazy
            | math '-' math %prec calc_lazy
            | math '*' math %prec calc_rapid
            | math '/' math %prec calc_rapid """
    p[0]={
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b,
        '*': lambda a,b: a*b,
        '/': lambda a,b: a/b,
    }[p[2]](p[1],p[3])

def p_math_braces(p):
    """math : '(' math ')'"""
    p[0]=p[2]

lexer=lex.lex()
parser=yacc.yacc(start='math')

if __name__=='__main__':
    print(parser.parse('304 * [Fe] / [FeSO4]',lexer=lexer))