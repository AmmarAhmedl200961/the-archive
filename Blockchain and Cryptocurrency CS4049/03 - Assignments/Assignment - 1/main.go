// to run the code: go run .
package main
import "fmt" // to print output

func main() {
	//main function
	var chainHead *Block
	genesis := Block{transactions: []string{"S2E", "S2Z"}}
	chainHead = InsertBlock(genesis.transactions, chainHead)
	fmt.Println("Data on Head = ", chainHead.transactions)
	fmt.Println("Hash of current block =", chainHead.currentHash)

	secondBlock := Block{transactions: []string{"E2Alice", "E2Bob", "S2John"}}
	chainHead = InsertBlock(secondBlock.transactions, chainHead)
	fmt.Println("Head of second block = ", chainHead.transactions)
	fmt.Println("Hash of second block = ", chainHead.currentHash)
	fmt.Println("Transactions of previous block (block 1) = ", chainHead.prevPointer.transactions)
	fmt.Println("Hash of previous block (block 1) = ", chainHead.prevPointer.currentHash)

	fmt.Print("\n\nLIST OF BLOCKS\n")
	ListBlocks(chainHead)
	ChangeBlock("S2E", "S2Trudy", chainHead)
	VerifyChain(chainHead)
}