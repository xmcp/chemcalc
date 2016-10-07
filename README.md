# ChemParser
计算原子量的有力工具 *（非清真）*

## 使用方法
安装依赖：`py -3 -m pip install -r requirements.txt`

用 chemparser 解释化学式：
```python
>>> import chemparser
>>> chemparser.parser.parse('Fe2(SO4)3')
<chemparser.Materials object at 0x02BC70D0>
>>> _.mats
{'S': 3, 'O': 12, 'Fe': 2}
```

用 chemcalc 进行关于分子量的计算（支持四则运算、括号、负号、化学式和科学计数法）
```python
>>> import chemcalc
>>> chemcalc.parser.parse('304 * Fe / FeSO4')
Fraction(112, 1)
>>> chemcalc.parser.parse('- 1e3 / CH4')
Fraction(-125, 2)
```

## 附赠：良心™计算器
`LXcalc.pyw`

![image](https://cloud.githubusercontent.com/assets/6646473/19179969/d8c7b762-8c94-11e6-9f81-fc1eef4bc937.png)
