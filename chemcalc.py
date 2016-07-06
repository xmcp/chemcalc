#coding=utf-8
from chemparser import *
from ply import lex, yacc
from chem_weight import weight
from fractions import Fraction

def proc(mat: Materials):
    return Fraction(sum(
        map((lambda tok_cnt: weight[tok_cnt[0]]*tok_cnt[1]), mat.mats.items())
    ))

literals+=['+','-','*','/','[',']']

tokens+=['DECIMAL']
t_DECIMAL=r"""\d*\.\d*"""

precedence+=[
    ('left','calc_lazy'),
    ('left','calc_rapid'),
]

def p_math_fromexpr(p):
    """math : '[' expr ']'"""
    p[0]=proc(p[2])

def p_math_fromnumber(p):
    """math : CNT
            | DECIMAL """
    p[0]=Fraction(p[1])

def p_math_lazy(p):
    """math : math '+' math
            | math '-' math %prec calc_lazy """
    p[0]={
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b,
    }[p[2]](p[1],p[3])

def p_math_rapid(p):
    """math : math '*' math
            | math '/' math %prec calc_rapid """
    p[0]={
        '*': lambda a,b: a*b,
        '/': lambda a,b: a/b,
    }[p[2]](p[1],p[3])

    
def p_math_braces(p):
    """math : '(' math ')'"""
    p[0]=p[2]

class NullLogger:
    def info(*___):
        return lambda *__,**_:None
    debug=info
    warning=info
    error=info
    
lexer=lex.lex()
parser=yacc.yacc(start='math',debuglog=NullLogger,errorlog=NullLogger)

if __name__=='__main__':
    while True:
        try:
            result=parser.parse(input('calc > '),lexer=lexer)
        except Exception as e:
            print(' [ERROR] %s'%e)
        else:
            print(' = %s (%.5f)'%(result,result))
        finally:
            print()