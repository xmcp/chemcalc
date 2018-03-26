#coding=utf-8
from chemparser import *
from ply import lex, yacc
from chem_weight import weight
from fractions import Fraction

def proc(mat: Materials): # calc weight
    return Fraction(sum(
        map((lambda tok_cnt: weight[tok_cnt[0]]*tok_cnt[1]), mat.mats.items())
    ))

global_last=0
    
tokens+=['ADD','SUB','MUL','DIV','EXP','LAST']
t_ADD=r'\+'
t_SUB=r'-'
t_MUL=r'\*'
t_DIV=r'/'
t_EXP=r'[eE]'
t_LAST=r'_'

precedence+=[
    ('left','ADD','SUB'),
    ('left','MUL','DIV'),
    ('nonassoc','calc_eval','EXP'),
]

def p_math_fromexpr(p):
    """math : expr %prec calc_eval"""
    p[0]=proc(p[1])

def p_math_legacyexpr(p):
    """math : '[' expr ']'"""
    p[0]=proc(p[2])

def p_math_fromnumber(p):
    """math : CNT """
    p[0]=p[1]
def p_math_fromlast(p):
    """math : LAST """
    p[0]=global_last
def p_math_fromexp(p):
    """math : CNT EXP math"""
    p[0]=p[1]*(10**p[3])
    
def p_math_add(p):
    """math : math ADD math"""
    p[0]=p[1]+p[3]
def p_math_sub(p):
    """math : math SUB math"""
    p[0]=p[1]-p[3]
def p_math_mul(p):
    """math : math MUL math"""
    p[0]=p[1]*p[3]
def p_math_div(p):
    """math : math DIV math"""
    p[0]=p[1]/p[3]

def p_math_neg(p):
    """math : SUB math %prec calc_eval """
    p[0]=-p[2]

def p_math_braces(p):
    """math : '(' math ')'"""
    p[0]=p[2]
    
lexer=lex.lex()
parser=yacc.yacc(start='math',debuglog=NullLogger,errorlog=NullLogger)

if __name__=='__main__':
    while True:
        try:
            print()
            result=parser.parse(input('calc > '),lexer=lexer)
        except Exception as e:
            print(' [ERROR] %s %s'%(type(e),e))
        else:
            print(' = %s (%.5f)'%(result,result))
            global_last=result