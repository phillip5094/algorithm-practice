//
//  main.swift
//  baekjoon
//
//  Created by Philip on 2022/01/19.
//

import Foundation

let t = Int(readLine()!)!

for _ in 0..<t {
    let data = readLine()!
    let dataArr = data.components(separatedBy: " ")
    
    let x1 = Int(dataArr[0])!
    let y1 = Int(dataArr[1])!
    let r1 = Int(dataArr[2])!
    
    let x2 = Int(dataArr[3])!
    let y2 = Int(dataArr[4])!
    let r2 = Int(dataArr[5])!
    
    let distance: Double = calculateDistance(x1, y1, x2, y2)
    
    if distance == 0 && r1 == r2 {
        print("-1")
    } else if distance == Double(r1 + r2) || distance == abs(Double(r1 - r2)) {
        print("1")
    } else if distance > abs(Double(r1 - r2)) && distance < Double(r1 + r2) {
        print("2")
    } else {
        print("0")
    }
}

func calculateDistance(_ x1: Int, _ y1: Int, _ x2: Int, _ y2: Int) -> Double {
    return sqrt(pow(Double(x1 - x2), 2) + pow(Double(y1 - y2), 2))
}
