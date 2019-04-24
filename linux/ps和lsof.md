在介绍`ps`命令（ 全称：*process status*） 之前，简单说明linux系统的进程状态，linux上进程有5种状态: 

1. 运行(正在运行或在运行队列中等待)   
   R 运行 runnable (on run queue) 

2. 中断(休眠中, 受阻, 在等待某个条件的形成或接受到信号)  
   S 中断 sleeping 

3. 不可中断(收到信号不唤醒和不可运行, 进程必须等待直到有中断发生)  
   D 不可中断 uninterruptible sleep (usually IO)  

4. 僵死(进程已终止, 但进程描述符存在, 直到父进程调用wait4()系统调用后释放)  
   Z 僵死 a defunct (”zombie”) process 

5. 停止(进程收到SIGSTOP, SIGSTP, SIGTIN, SIGTOU信号后停止运行运行)  
    T 停止 traced or stopped 

`ps -ef` 和 `ps aux` 

 这里简单介绍下linux支持三种不同的风格  
 1. UNIX风格 选项可以组合在一起，选项前需有 "`-`"连字符
 2. BSD风格，选项可以组合在一起使用，但是选项不能有"`-`"连字符
 3. GNU风格，需要有两个"`-`"连字符

需要注意 `ps -aux` 和 `ps aux`是不一样的。但是为什么输出的结果大部分情况下是一致的呢？  
其实 `ps -aux` 会去打印用户名为**x**的用户所有进程，如果找不到，才会给你默认转为 `ps aux`。因此，应该使用 `ps aux`


解释：  
`-a` 显示所有进程  
`-x` 显示没有控制终端的进程  
`-u` 显示所属用户  
`-e` 显示所有进程
`-f` 显示UID，PPID，C和STIME 栏位


另外有时候需要以树形结构显示进程，可以使用如下命令：  
`ps -axjf`或者`pstree`

解释：  
`-j` 采用工作控制的格式显示进程状态


cpu、内存使用量排序  (前4,mac上不可)  
`ps aux --sort -pcpu,+pmem |head -n 5`


lsof




