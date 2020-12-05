## 类属性、 实例属性

- 类属性，在内存中只保存一份（所有实例对象，共用一份类属性）
- 实例属性在每个实例对象中保存一份

## 实例方法、静态方法、类方法

- 实例方法： self，（类，不能调用实例方法）

- 类方法： @classmethod， cls（只在类属性的内存中有一份代码）

- 静态方法： @staticmethod， 不需要参数（）


## property属性： 把方法作为属性使用，一般返回值
```python3
class Goods(object):
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    @property
    def price(self):
        return self.original_price * self.discount

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price

obj = Goods()
obj.price
obj.price = 200
obj.pirce
del obj.price

```
