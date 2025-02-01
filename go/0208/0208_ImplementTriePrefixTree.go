// 208. Implement Trie (Prefix Tree)

package main

import (
	"fmt"
)

type Trie struct {
	children map[rune]*Trie
	isWord   bool
}

func Constructor() Trie {
	return Trie{children: make(map[rune]*Trie)}
}

func (t *Trie) Insert(word string) {
	curr := t
	for _, ch := range word {
		if _, exists := curr.children[ch]; !exists {
			curr.children[ch] = &Trie{children: make(map[rune]*Trie)}
		}
		curr = curr.children[ch]
	}
	curr.isWord = true
}

func (t *Trie) Search(word string) bool {
	curr := t
	for _, ch := range word {
		if _, exists := curr.children[ch]; !exists {
			return false
		}
		curr = curr.children[ch]
	}
	return curr.isWord
}

func (t *Trie) StartsWith(prefix string) bool {
	curr := t
	for _, ch := range prefix {
		if _, exists := curr.children[ch]; !exists {
			return false
		}
		curr = curr.children[ch]
	}
	return true
}

func main() {
	obj := Constructor()
	obj.Insert("apple")
	fmt.Println(obj.Search("apple"))   // true
	fmt.Println(obj.Search("app"))     // false
	fmt.Println(obj.StartsWith("app")) // true
	obj.Insert("app")
	fmt.Println(obj.Search("app")) // true
}
