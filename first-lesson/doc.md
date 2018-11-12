# First Lesson
## 内置对象
对象类型：
- 数字
- 字符串
- 列表
- 字典
- 元祖
- 文件
- 集合

python是动态类型的，它自动跟踪你的类型，而不是要求声明代码，但是它是强类型语言，你只能对一个对象进行适合该类型的有效操作，也就是不会自动转换。
## 字符串
字符串是一个文本序列，序列中的元素包含了从左到右的顺序，严格来讲，字符串是单个字符的的字符串序列。
### `string[x:y]` 字符串的分片
可以看做从字符串中提取一部分子串的方法，一般形式为`string[x,y]`，表示取出在string字符串中从偏移量x开始，直到（不包括）偏移量为y的内容。
```python
string = 'abcdefghijklmnopqrstuvwxyz'
string[1:2] # b
string[-1, -2] # error
string[-3: -2] # x
```
x和y表示区间，可以理解为坐标轴上的点，是从左到右，区间有效则返回正确的值，无效则返回空。在一个分片中，左边的边界默认为0，邮编的边界默认为序列的长度，这样可以省略左边的或右边的，一些常用的变体：
```python
string = 'abcdefghijklmnopqrstuvwxyz'
string[:2] # ab
string[-2:] # yz
```
### 字符串的运算：`+ *`
字符串可以使用加好`+`进行合并：
```python
str = 'ac' + '/'+ 'dc'
print(str) # ac/dc
```
可以使用称号`*`重复创建一个新的字符串：
```python
str = 'ac' + '/'+ 'dc'
str * 3 # 'ac/dcac/dcac/dc'
```
### `string.find(sub)` 查找子串
基本的子串查找操作，找到的话返回第一次找到的索引，没找到返回-1.
### `string.replace(old, new[, max])` 查找替换
查找子串并用新的子串替换找到的结果，max参数提供的话限定了最大替换几次：
```python
string = 'ac/dcac/dcac/dcac/dcac/dc'
string.replace('/', '-', 2) # 'ac-dcac-dcac/dcac/dcac/dc'
```
### `string.split(str[, num])` 对字符串进行切片
通过分隔符对字符串进行切片，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。

### string.title() 单词首字母大写
### string.strip() 去除变量两侧的空白符
空白符包括空格、换行、制表符等，包括两个相同的方法：
- `string.lstrip()` 去除左侧的空白符
- `string.rstrip()` 去除右侧的空白符

## 列表
列表由一系列按特定顺序排列的元素组成。用方括号`[]`表示列表。通用的方法：
- `len(list)` 返回列表的长度
- `list[x:y]` 返回列表的切片
- `list + list` 两个列表的合并

因为列表是可变的，所以大多数列表特定的方法是可以改变自己的，而不是创建一个新列表。

列表的一个优秀的特性是支持任意的嵌套。能够以任意的组合进行嵌套。

### 列表解析
处理序列的操作和列表的方法中，python还包括了一个更高级的操作，称作列表解析表达式，从而提供了一种处理像矩阵这样结构的强大工具。

先构造一个矩阵：
```python
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
我们想取出第二列：
```python
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [row[1] for row in M]
print(col2) # [2, 5, 8]
```
列表解析表达式是通过对序列中的每一项运行一个表达式来创建一个新列表的方法，每次一个，从左至右。
### `list.append(item)` 在列表尾部插入元素
### `list.insert(index)` 在列表任何位置插入元素
### `del list[index]` 从列表中删除某个元素
### `list.pop(index?)` 从列表尾部弹出某个元素
可以使用`list.pop()`删除列表中最后一项的元素，但是，可以传入位置参数，这样可以删除列表任何位置的元素。和del的区别是，这个弹出会返回弹出的元素，可以访问到，而del语句是直接删除。
### `list.remove(item)` 根据元素删除list的项
当不知道元素在list中的索引的时候，就可以使用remove来根据列表元素来删除。
### `list.sort()` 永久排序 `list.sorted()` 临时排序
默认按照字母顺序排序，可以传入`reserve=True`来反转顺序。两者的差别是排序的作用对象：
- `list.sort()` 是永久排序，列表本身被替换为排序后的列表。
- `list.sorted()` 是临时排序，返回排序后的列表。列表本身不受影响。

### `list.reverse()` 倒序排列列表
倒序排列列表，作用于本身，不做排序，只是顺序的反向。
### `len(list)` 获得列表的长度
### `for ... in` 遍历列表
`for ... in`循环建立临时变量，从列表中拿取当前的值放入临时变量中，以冒号开始循环体，以缩进结束循环体：
```python
bicycles = ['trek', 'redBic', 'canNodale']

print('start')

for item in bicycles:
    print('item:' + str(item) + '\n')

print('end')
```
## 字典
字典是一种映射，映射是一个其他对象的集合，字典里面的元素通过键而不是相对位置来存储的。字典编写在大括号中，并包含一系列的"键:值"。
``` python
D = {
    'food': 'Spam',
    'quantity': 4,
    'color': 'pink',
}
print(D['food'])
# 控制台输出：Spam

D['quantity'] += 1
print(D)
# 控制台输出：{'food': 'Spam', 'color': 'pink', 'quantity': 5}
```
当然，我们可以创建一个空字典，并动态的往字典中添加内容：
``` python
D = {}
D['name'] = 'tony'
D['age'] = 18
D['age'] += 1
print(D)
# 控制台输出：{'age': 19, 'name': 'tony'}
```
### 嵌套使用字典
``` python
person = {
    'name': {'first': 'Tony', 'last': 'Yang'},
    'job': ['dev', 'managor'],
    'age': 18.5,
}
print(person['job'][1])
# 控制台输出：managor
```
### 键的排序
因为字典不是序列，它并不包含任何可靠的从左到右的顺序。意味着我们建立一个字典，并将它打印出来并不是按照我们输入的顺序出现的：
``` python
D = {'a': 1, 'b': 2, 'c': 3}
print(Ks)
# 控制台输出：
# ['a', 'c', 'b']
```
如何让字典按照某种顺序输出？一个常用的解决办法是通过字典的key方法收集到字典的键的列表，然后用列表的sort方法给字典的键进行排序，然后使用for循环挨个输出：
``` python
Ks = list(D.keys())
print(Ks)
for key in Ks:
    print(key, '=>', D[key])
# 控制台依次输出：
# ['a', 'b', 'c']
# ('a', '=>', 1)
# ('b', '=>', 2)
# ('c', '=>', 3)
```
### 断键是否存在
我们可以通过字典的键获取对应的值，但是当键不存在字典中时会发生一个错误，我们需要避免这种情况。`in`关系表达式允许我们查询字典中一个键是否存在。然后结合`if`判断来进行分支处理：
``` python
D = {'a': 1, 'b': 2, 'c': 3}
if 'd' in D:
    print('yes')
else:
    print('no')
```
## 元组
元组对象，基本上就像一个不可以改变的列表。元组是序列，但是具有不可变性，和字符串类似。编写在圆括号中，支持任意类型、任意前台哦以及常见的序列操作。
``` python
T = (1, 2, 3, 'test')
print(len(T)) # 元组的长度
print(T.index(3)) # 元组项3的位置索引
print(T[2]) # 元组的第二个元素
# 控制台依次输出：4，2，3
```
如果在程序中以列表的形式传递一个对象的集合，它可能在任何地方改变；如果使用元组，则无法改变。也就是说，元组提供了一种完整性约束。
## 文件
没有特定的常亮语法创建文件。需要创建一个文件对象，需要调用内置的`open`函数以字符串的形式传递它一个**外部的文件名**以及一个**处理模式的字符串**。
例如，创建文件，并写入对应的内容，然后关闭文件：
``` python 
f = open('data.txt', 'w')
f.write('hello \n')
f.write('world \n')
f.close()
```
这样，在当前文件夹下创建了一个文件（文件名可以是完整的路径）。

为了读取刚写入的内容，重新以`r`处理模式打开文件，读取输入。对脚本而言文件的内容总是字符串，无论文件包含的数据是什么类型。
例如，读取刚刚创建的文件：
``` python
f = open('data.txt', 'r')
text = f.read()
print(text.split())
# 控制台输出：['hello', 'world']
```
## 用户自定义的类
可以使用关键字`class`来自定义类，类定义了新的对象类型，扩展了核心类型。例如：
``` python
class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
bob = Worker('Bob Smith', 5000)
print(bob.lastName())
# 控制台输出：Smith
```