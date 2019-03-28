# Data Structures

## Stack

A stack (sometimes called a “push-down stack”) is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end. This end is commonly referred to as the “top.” The end opposite the top is known as the “base.”

Methods:

- isEmpty -> True if empty
- push    -> push item to the top
- pop     -> get item at the top and remove it
- peek    -> get item under the top
- size    -> get size

## Queue

A queue is an ordered collection of items where the addition of new items happens at one end, called the “rear,” and the removal of existing items occurs at the other end, commonly called the “front.” As an element enters the queue it starts at the rear and makes its way toward the front, waiting until that time when it is the next element to be removed.

Methods:

- isEmpty -> True if empty
- enqueue -> add item to the end
- dequeue -> get item from the front and remove it
- size    -> get size