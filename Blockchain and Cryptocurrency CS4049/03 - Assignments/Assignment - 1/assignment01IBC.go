package main

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
)

// Block
type Block struct {
	transactions []string
	prevPointer  *Block
	prevHash     string
	currentHash  string
}

//
func CalculateHash(inputBlock *Block) string {
	//Calculate Hash of a Block
	tran := ""
	for i := 0; i < len(inputBlock.transactions); i++ {
		tran += inputBlock.transactions[i]
	}
	hash := sha256.Sum256([]byte(tran))
	hashhex := hex.EncodeToString(hash[:])
	return hashhex
}

//
func InsertBlock(transactionsToInsert []string, chainHead *Block) *Block {

	//insert new block and return head pointer
	if chainHead == nil {
		var newBlock Block
		chainHead = &newBlock
		chainHead.prevPointer = nil
		chainHead.transactions = transactionsToInsert
		chainHead.currentHash = CalculateHash(chainHead)
		chainHead.prevHash = ""
	} else {
		var newBlock Block
		newBlock.prevPointer = chainHead
		newBlock.prevHash = chainHead.currentHash
		newBlock.transactions = transactionsToInsert
		newBlock.currentHash = CalculateHash(&newBlock)
		chainHead = &newBlock
	}
	return chainHead
}

//
func ChangeBlock(oldTrans string, newTrans string, chainHead *Block) {
	curr := chainHead
	// Find and modify the block 
	for curr != nil {
		for i := 0; i < len(curr.transactions); i++ {
			if curr.transactions[i] == oldTrans {
				curr.transactions[i] = newTrans
				curr.currentHash = CalculateHash(curr)
			}
		}
		curr = curr.prevPointer
	}
	// Recalculate the hash of all blocks starting from modified block
	curr = chainHead
	for curr != nil {
		if curr.prevPointer != nil {
			curr.prevHash = curr.prevPointer.currentHash
		}
		curr.currentHash = CalculateHash(curr)	
		curr = curr.prevPointer
	} 
}

//
func ListBlocks(chainHead *Block) {

	//dispaly the data(transaction) inside all blocks 
	newHead := chainHead
	i := 1
	for newHead != nil {
		fmt.Println("Block Number = ", i)
		fmt.Print("Transactions = ")
		fmt.Println(newHead.transactions)
		fmt.Print("Hash = ")
		fmt.Println(newHead.currentHash)
		fmt.Print("Hash of Block ", i-1, " = ")
		fmt.Printf("%s", newHead.prevHash)
		i++
		fmt.Print("\n\n")
		newHead = newHead.prevPointer
	}
}

//
func VerifyChain(chainHead *Block) {

	//check whether "Block chain is compromised" or "Block chain is unchanged"
	for c := chainHead; c != nil; c = c.prevPointer {
		hashc := CalculateHash(c)
		if c.prevPointer != nil {
			hashp := CalculateHash(c.prevPointer)
			if hashp != c.prevHash || hashc != c.currentHash {
				fmt.Println("Blockchain is compromised")
				return
			}
		}
		if hashc != c.currentHash {
			fmt.Println("Blockchain is compromised")
			return
		}
	}
	fmt.Println("Blockchain Verified")
	return
}
