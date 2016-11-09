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
    let reverseBit num =
        let rec helper num accu =
            match num with
            | 0 -> accu
            | _ -> helper (num >>> 1) ((accu <<< 1) + (num &&& 1))
        helper num 0

    type BitReverseTable() =
        member private this.Table = Map(seq{ for i = 0 to 255 do yield (i, (reverseBit i)) })
        member this.GetReversed num =
            (this.Table.[num >>> 24] <<< 24) +
            (this.Table.[(num >>> 16) &&& ((1 <<< 8) - 1)] <<< 16) +
            (this.Table.[(num >>> 8) &&& ((1 <<< 8) - 1)] <<< 8) +
            this.Table.[num &&& ((1 <<< 8) - 1)]

    do
        let t = BitReverseTable()
        for i = 0 to 10000 do
            printfn "%A : %A" i (t.GetReversed(i))

    (*
        5.4 Closest Integers with the Same Weight
    *)
    let ConvertToBinary (num: uint64) =
        let rec helper (num: uint64) accu =
            match num with
            | 0UL -> accu
            | _ -> helper (num >>> 1) ((num &&& 1UL).ToString() + accu)
        helper num ""

    let countOneBit (num: uint64) =
        ConvertToBinary num |> String.filter (fun c -> c = '1') |> String.length
        
    let closestIntWIthSameWeight (num: uint64) =
        let rec helper (v: uint64) i =
            match v with
            | 0UL
            | 1UL when i = 63 -> failwith "All bits are 0 or 1"
            | _ when (v &&& 1UL) <> ((v >>> 1) &&& 1UL) ->
                ((v ^^^ 3UL) <<< i) + (num &&& ((1UL <<< i) - 1UL))
            | _ -> helper (v >>> 1) (i + 1)
        helper num 0

    do
        for i = 1 to 10000 do
            printfn "%s" "--------------------------------"
            printfn "%d" i
            let res = closestIntWIthSameWeight (uint64 i)
            printfn "%d" res
            printfn "%A" (ConvertToBinary (uint64 i))
            printfn "%A" (ConvertToBinary res)
            printfn "%A" ((countOneBit (uint64 i)) = (countOneBit res))
            printfn "%d" (if (uint64 i) > res then (uint64 i) - res else res - (uint64 i))