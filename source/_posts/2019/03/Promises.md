---
title: Promises/A+ 规范学习笔记
date: 2019-03-30 18:16:21
tags:
  - ES6
  - JavaScript
categories:
  - 工作
  - 前端
  - JavaScript
---

这是我的 Promises 规范学习笔记，用自己能理解的方式描述 Promises 规范的内容。

# Promises/A+

**An open standard for sound, interoperable JavaScript promises&mdash;by implementers, for implementers.**

A *promise* represents the eventual result of an asynchronous operation. The primary way of interacting with a promise is through its `then` method, which registers callbacks to receive either a promise's eventual value or the reason why the promise cannot be fulfilled.

This specification details the behavior of the `then` method, providing an interoperable base which all Promises/A+ conformant promise implementations can be depended on to provide. As such, the specification should be considered very stable. Although the Promises/A+ organization may occasionally revise this specification with minor backward-compatible changes to address newly-discovered corner cases, we will integrate large or backward-incompatible changes only after careful consideration, discussion, and testing.

Historically, Promises/A+ clarifies the behavioral clauses of the earlier [Promises/A proposal](http://wiki.commonjs.org/wiki/Promises/A), extending it to cover *de facto* behaviors and omitting parts that are underspecified or problematic.

Finally, the core Promises/A+ specification does not deal with how to create, fulfill, or reject promises, choosing instead to focus on providing an interoperable `then` method. Future work in companion specifications may touch on these subjects.

## Terminology 术语

1. “promise”是具有 `then` 方法的对象或函数，其行为符合此规范。
2. “thenable”是一个定义 `then` 方法的对象或函数。
3. “value”是任何合法的 JavaScript 值（包括 `undefined`、thenable 或 promise）。
4. “exception”是一个使用 throw 语句抛出的值。
5. “reason”是一个值，它说明了一个 promise 为什么被拒绝。

## Requirements 要求

### Promise 的状态

promise 必须是三种状态中一种：请求态（pending），完成态（fulfilled），拒绝态（rejected）

1. promise 是 pending 状态时：
    1. 可转换为 fulfilled 或  rejected 状态。 
1. promise 是 fulfilled 状态时：
    1. 不能转换为任何其他状态。
    1. 必须有个值，此值不能改变。
1. promise 是 rejected 状态时：
    1. 不能转换为任何其他状态。
    1. 必须有个值，此值不能改变。

在这里，“此值不能改变”意味着不变的身份(即===)，但并不意味着深层的不变性。

> 这句话还不能理解透是什么意思

### `then` 方法 
promise 必须提供一个 `then` 方法来访问它当前/最终的值或 reason。
promise's `then` 方法有两个参数：
```js
promise.then(onFulfilled, onRejected)
```

1. `onFulfilled` 和 `onRejected` 都是可选参数：
    1. 如果 `onFulfilled` 不是函数，必须忽略。
    1. 如果 `onFulfilled` 不是函数，必须忽略。
2. 如果 `onFulfilled` 是函数：
    1. 它必须在 `promise` 为 fulfilled 后调用，并把 `promise` 的值作为它的第一个参数。
    1. 它绝对不能在 `promise` 为 fulfilled 之前调用。
    1. 它不能被调用超过一次。
3. 如果 `onRejected` 是函数,
    1. 它必须在 `promise` 为 rejected 后调用，并把 `promise` 的 reason 作为它的第一个参数。 
    1. 它绝对不能在 `promise` 为 rejected 之前调用。
    1. 它不能被调用超过一次。
4. `onFulfilled` or `onRejected` must not be called until the [execution context](https://es5.github.io/#x10.3) stack contains only platform code. [[3.1](#notes)].
5. `onFulfilled` 和 `onRejected` 必须作为函数调用 (i.e. with no `this` value). [[3.2](#notes)]
6. `then`可以被同一个 `promise` 调用多次。
    1. 当 promise 成功执行时，所有 onFulfilled 需按照其注册顺序依次回调
    1. 当 promise 被拒绝执行时，所有的 onRejected 需按照其注册顺序依次回调
7. `then` 必须返回一个 `promise` 对象 [[3.3](#notes)]。
    ``` js
    promise2 = promise1.then(onFulfilled, onRejected);
    ```
    1. 如果 `onFulfilled` 或 `onRejected` 返回一个值 `x`，run the Promise Resolution Procedure `[[Resolve]](promise2, x)`.
    1. 如果 `onFulfilled` 或 `onRejected` 抛出异常 `e`, `promise2` 必须拒绝执行，并返回 reason `e` 
    1. 如果 `onFulfilled` 不是一个函数并且 `promise1` 是 fulfilled， `promise2` 必须为 fulfilled 并且返回与 `promise1` 相同的 value
    1. 如果 `onRejected` 不是一个函数并且 `promise1` 是 rejected， `promise2` 必须为 rejected 并返回与 `promise1` 相同的 rejected

### Promise 解决过程

**promise resolution procedure** 是一个抽象的操作，其需输入一个 promise 和一个值，我们表示为 `[[Resolve]](promise, x)`，如果 `x` 有 then 方法且看上去像一个 Promise ，解决程序即尝试使 promise 接受 `x` 的状态；否则其用 `x` 的值来执行 `promise` 。

这种 thenable 的特性使得 Promise 的实现更具有通用性：只要其暴露出一个遵循 Promise/A+ 协议的 `then` 方法即可；这同时也使遵循 Promise/A+ 规范的实现可以与那些不太规范但可用的实现能良好共存。

运行 `[[Resolve]](promise, x)`，须遵循一下步骤：

1. 如果 `promise` 和 `x` 是同一个对象，并以 `TypeError` 为 `promise` 的 reason
1. 如果 `x` 是个 promise，则 promise 接受 `x` 的状态 [[3.4](#notes)]:
   1. 如果 `x` 是 pending, `promise` 必须保持状态为 pending ，直到 `x` 为 fulfilled 或 rejected
   1. 如果 `x` 处于 fulfilled,  `promise` 的  fulfill 使用同样的 value 
   1. 如果 `x` 处于 rejected, reject `promise` 的 reject 使用相同的   reason.
1. 另外，如果 `x` 是对象或函数
   1. 把 `x.then` 赋给 `then` . [[3.5](#notes)]
   1. 如果取 `x.then` 的值时抛出错误 `e` ，则以 `e` 为 reason 拒绝 promise
   1. 如果 `then` 是个函数， 将 `x` 作为函数作用于的 `this`，第一个参数 `resolvePromise`, and 第二个参数 `rejectPromise`, where:
      1. If/when `resolvePromise` is called with a value `y`, run `[[Resolve]](promise, y)`.
      2. 如果 `resolvePromise` 以值 `y` 为参数被调用，则运行 `[[Resolve]](promise, y)`
      3. 如果 `rejectPromise` 以 reason r 为参数被调用，则以reason r 拒绝 promise
      4. 如果 `resolvePromise` 和 `rejectPromise` 均被调用，或者被同一参数调用了多次，则优先采用首次调用并忽略剩下的调用
      5. 如果调用 `then` 抛出了异常 `e`，
         1. 如果 `resolvePromise` 或 `rejectPromise` 已经被调用，则忽略它
         1. 否则，以 `e` 作为 reject `promise` 的 reason
   1. 如果 `then` 不是函数，以`x`为参数执行 `promise`
1. 如果 `x` 不是对象或函数，以`x`为参数执行 `promise`

如果一个 `promise` 被一个循环的 thenable 链中的对象解决，而 `[[Resolve]](promise, thenable)` 的递归性质又使得其被再次调用，根据上述的算法将会陷入无限递归之中。算法虽不强制要求，但也鼓励施者检测这样的递归是否存在，若检测到存在则以一个可识别的 `TypeError` 为据因来拒绝 `promise` 。 [[3.6](#notes)]

## Notes

1. Here "platform code" means engine, environment, and promise implementation code. In practice, this requirement ensures that `onFulfilled` and `onRejected` execute asynchronously, after the event loop turn in which `then` is called, and with a fresh stack. This can be implemented with either a "macro-task" mechanism such as [`setTimeout`](https://html.spec.whatwg.org/multipage/webappapis.html#timers) or [`setImmediate`](https://dvcs.w3.org/hg/webperf/raw-file/tip/specs/setImmediate/Overview.html#processingmodel), or with a "micro-task" mechanism such as [`MutationObserver`](https://dom.spec.whatwg.org/#interface-mutationobserver) or [`process.nextTick`](http://nodejs.org/api/process.html#process_process_nexttick_callback). Since the promise implementation is considered platform code, it may itself contain a task-scheduling queue or "trampoline" in which the handlers are called.

1. That is, in strict mode `this` will be `undefined` inside of them; in sloppy mode, it will be the global object.

1. Implementations may allow `promise2 === promise1`, provided the implementation meets all requirements. Each implementation should document whether it can produce `promise2 === promise1` and under what conditions.

1. Generally, it will only be known that `x` is a true promise if it comes from the current implementation. This clause allows the use of implementation-specific means to adopt the state of known-conformant promises.

1. This procedure of first storing a reference to `x.then`, then testing that reference, and then calling that reference, avoids multiple accesses to the `x.then` property. Such precautions are important for ensuring consistency in the face of an accessor property, whose value could change between retrievals.

1. Implementations should *not* set arbitrary limits on the depth of thenable chains, and assume that beyond that arbitrary limit the recursion will be infinite. Only true cycles should lead to a `TypeError`; if an infinite chain of distinct thenables is encountered, recursing forever is the correct behavior.


# 参考资料

> https://promisesaplus.com/
> http://www.ituring.com.cn/article/66566
> https://segmentfault.com/a/1190000015914967