#coding=utf-8
from ply import lex, yacc
from collections import namedtuple

class Materials:
    def __init__(self,item=None):
        self.mats={item:1} if item is not None else {}

    @classmethod
    def from_mats(cls,mats):
        obj=Materials()
        obj.mats=mats
        return obj

    def __add__(self, other):
        new_mats=self.mats.copy()
        for item,cnt in other.mats.items():
            if item in new_mats:
                new_mats[item]+=cnt
            else:
                new_mats[item]=cnt
        return Materials.from_mats(new_mats)
    def __mul__(self, times):
        return Materials.from_mats({k:v*times for k,v in self.mats.items()})

    def __str__(self):
        return ', '.join(('%r * %d'%(k,v) for k,v in self.mats.items()))

class ExprSyntaxError(Exception):
    def __init__(self,typ,obj):
        self.typ=typ
        self.pos=obj.lexpos
        self.value=obj.value

    def __str__(self):
        return 'Invalid %s %r at position %d'%(self.typ,self.value,self.pos)

FakePattern=namedtuple('Pattern', ['lexpos', 'value'])

tokens=['TOK','CNT']
literals= ['(', ')']
precedence= [
    ('left', 'plus'),
    ('nonassoc', 'multiply'),
]

t_ignore=' '
t_TOK='[A-Z][a-z]?'
def t_CNT(t):
    r"""\d+"""
    t.value=int(t.value)
    return t

def p_material_fromtoken(p):
    """material : TOK
                | TOK CNT """
    p[0]=Materials(p[1])*(1 if len(p)==2 else p[2])
def p_material_fromsub(p):
    """material : '(' material ')'
                | '(' material ')' CNT %prec multiply """
    p[0]=p[2]*(1 if len(p)==4 else p[4])
def p_material_recursion(p):
    """material : material material %prec plus"""
    p[0]=p[1]+p[2]

def p_expr_initial(p):
    """expr : material"""
    p[0]=p[1]
def p_expr_withcount(p):
    """expr : CNT material"""
    p[0]=p[2]*p[1]

def t_error(t):
    raise ExprSyntaxError('token',t)
def p_error(p):
    raise ExprSyntaxError('pattern', p or FakePattern(lexpos=-1,value='(EOF)'))

class NullLogger:
    def info(*___):
        return lambda *__,**_:None
    debug=info
    warning=info
    error=info
    
lexer=lex.lex()
parser=yacc.yacc(start='expr',debuglog=NullLogger,errorlog=NullLogger)

if __name__=='__main__':
    print(parser.parse('5 Fe2(SO4)3',lexer=lexer))