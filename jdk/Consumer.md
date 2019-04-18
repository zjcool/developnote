函数式编程 Consumer 源码解读


``` 
package java.util.function;

import java.util.Objects;


@FunctionalInterface
public interface Consumer<T> {

   //接受 一个函数
    void accept(T t);

 
    //接受一个Consumer，返回一个新的Consumer，该Consumer执行自己的accepct()后，会执行传入进来的Consumer的accepct()
    default Consumer<T> andThen(Consumer<? super T> after) {
        Objects.requireNonNull(after);
        return (T t) -> { accept(t); after.accept(t); };
    }
}
```

**default** 关键词作用: 接口默认实现方法，为实现该接口的每一个类实现一个默认方法
**好处**：无需将接口转变为抽象类或为每一个实现类实现一个同样的方法。

##### Example:
```
Consumer c = (x) -> {
    System.out.println("x is:" + x);
};
c.accpect(10);

```
