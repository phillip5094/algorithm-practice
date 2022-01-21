//
//  main.swift
//  baekjoon
//
//  Created by Philip on 2022/01/20.
//

import Foundation

let t = Int(readLine()!)!
var fibonacci = Array(repeatElement(0, count: 42))
var fibonacciZero = Array(repeatElement(0, count: 42))
var fibonacciOne = Array(repeatElement(0, count: 42))

fibonacci[0] = 0
fibonacci[1] = 1

fibonacciZero[0] = 1
fibonacciZero[1] = 0

fibonacciOne[0] = 0
fibonacciOne[1] = 1

for i in 2...40 {
    fibonacciZero[i] = fibonacciZero[i - 1] + fibonacciZero[i - 2]
    fibonacciOne[i] = fibonacciOne[i - 1] + fibonacciOne[i - 2]
}

for _ in 0..<t {
    let n = Int(readLine()!)!
    print("\(fibonacciZero[n]) \(fibonacciOne[n])")
}
