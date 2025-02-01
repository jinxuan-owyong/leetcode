// 211. Design Add and Search Words Data Structure

package main

import "fmt"

type WordDictionary struct {
	children map[rune]*WordDictionary
	isWord   bool
}

func Constructor() WordDictionary {
	return WordDictionary{children: make(map[rune]*WordDictionary)}
}

func (dict *WordDictionary) AddWord(word string) {
	curr := dict
	for _, ch := range word {
		if _, exists := curr.children[ch]; !exists {
			temp := Constructor()
			curr.children[ch] = &temp
		}
		curr = curr.children[ch]
	}
	curr.isWord = true
}

func (dict *WordDictionary) Search(word string) bool {
	curr := dict
	for i, ch := range word {
		if _, exists := curr.children[rune(word[i])]; !exists {
			if ch == '.' {
				// search all children of the current node if there is a wildcard
				for _, next := range curr.children {
					if next.Search(word[i+1:]) {
						return true
					}
				}
			}
			// similar to a normal trie in #208
			return false

		}
		curr = curr.children[rune(word[i])]
	}
	return curr.isWord
}

func main() {
	obj := Constructor()
	obj.AddWord("bad")
	obj.AddWord("dad")
	obj.AddWord("mad")
	fmt.Println(obj.Search("pad")) // return False
	fmt.Println(obj.Search("bad")) // return True
	fmt.Println(obj.Search(".ad")) // return True
	fmt.Println(obj.Search("b..")) // return True
	fmt.Println(obj.Search("b.d")) // return True

	// obj := Constructor()
	// obj.AddWord("a")
	// obj.AddWord("a")
	// fmt.Println(obj.Search("."))
	// fmt.Println(obj.Search("a"))
	// fmt.Println(obj.Search("aa"))
	// fmt.Println(obj.Search("a"))
	// fmt.Println(obj.Search(".a"))
	// fmt.Println(obj.Search("a."))
}
