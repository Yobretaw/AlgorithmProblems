module PrimitiveTypes
    (*
        5.1 Computing Parity
    *)
    let computeParity (num: uint64) =
        let rec helper num accu =
            match num with
            | 0UL -> accu
            | _ -> helper (num >>> 1) (accu + int (num &&& 1UL))
        (helper num 0) % 2

    let printHelper (num: uint64) (parity: int) =
        "Parity of " + num.ToString() + " is " + parity.ToString()
    do
        let num1 = 1UL 
        printfn "%A" (printHelper num1 (computeParity num1))
        let num2 = 2UL 
        printfn "%A" (printHelper num2 (computeParity num2))
        let num3 = 3UL 
        printfn "%A" (printHelper num3 (computeParity num3))

    (*
        5.2 Swap Bits
    *)
    let getIthBit num i = (num >>> i) &&& 1

    let convertToBitString(num: int) = System.Convert.ToString(num, 2)

    let swapBits num i j =
        let bitI = getIthBit num i
        let bitJ = getIthBit num j

        match bitI with
        | 0 -> match bitJ with
            | 0 -> num
            | 1 -> (num ||| (1 <<< j)) - (1 <<< i)
        | 1 -> match bitJ with
            | 0 -> (num ||| (1 <<< i)) - (1 <<< j)
            | 1 -> num

    do
        let num = 5
        printfn "%A" (convertToBitString num)
        printfn "%A" (convertToBitString (swapBits num 0 1))


    (*
        5.3 Bit Reversal
    *)
    let _reverseBit num =
        let rec helper num accu =
            match num with
            | 0 -> accu
            | _ -> helper (num >>> 1) ((accu <<< 1) + (num &&& 1))
        helper num 0

    type BitReverseTable() =
        member private this.tbl = Map(seq{ for i = 0 to 255 do yield (i, (_reverseBit i)) })
        member this.GetReversed num =
            (this.tbl.[num >>> 24] <<< 24) +
            (this.tbl.[(num >>> 16) &&& ((1 <<< 8) - 1)] <<< 16) +
            (this.tbl.[(num >>> 8) &&& ((1 <<< 8) - 1)] <<< 8) +
            this.tbl.[num &&& ((1 <<< 8) - 1)]

    do
        let t = BitReverseTable()
        for i = 0 to 10000 do
            printfn "%A : %A" i (t.GetReversed(i))