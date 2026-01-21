# Shopify Pair Programming Practice Interview

## 🎯 Overview

This is a practice interview simulating Shopify's 45-minute pair programming session. You'll build an **inventory management system** for an e-commerce store using object-oriented programming in Python.

---

## ⏱️ Time Breakdown

| Phase | Duration | Description |
|-------|----------|-------------|
| Problem Introduction | 2-3 min | Read through the problem, ask clarifying questions |
| Implementation | 25-30 min | Write code, think aloud, collaborate |
| Testing & Refinement | 5-7 min | Test your solution, handle edge cases |
| Q&A | ~10 min | Ask your interviewer questions |

---

## 📋 The Problem

Build an inventory management system with three main classes:

### 1. `Product` 
- Stores name, price, and stock quantity
- Can check if a requested quantity is available

### 2. `Inventory`
- Manages a collection of products
- Can add products, look them up, and update stock levels

### 3. `Order`
- Represents a customer's shopping cart
- Can add items, calculate totals, and process the order (deducting from inventory)

### Stretch Goal (if time permits)
- Add tiered discounts: 10% off orders over $100, 15% off orders over $200

---

## 🚀 Getting Started

```bash
# Clone the repo (you'll receive an invite)
git clone <repo-url>
cd shopify-practice-interview

# Open in your preferred IDE
code .  # or your editor of choice

# Run the file to test
python inventory.py
```

---

## 💡 What We're Looking For

1. **Problem-Solving Approach** - How do you break down the problem?
2. **Code Quality** - Clean, readable, well-structured code
3. **Communication** - Think out loud! Explain your decisions
4. **Collaboration** - Ask questions, receive feedback gracefully
5. **Testing Mindset** - Consider edge cases and validate your work

---

## 🤖 AI Usage Guidelines

**AI tools ARE encouraged** - Shopify explicitly wants to see how you leverage AI. However, use them strategically:

### ✅ Good Uses of AI
- **Syntax help** - "What's the Python syntax for dictionary comprehension?"
- **Quick lookups** - "How do I type hint a method that returns None?"
- **Boilerplate generation** - Getting basic class structure set up quickly
- **Edge case brainstorming** - "What edge cases should I consider for inventory updates?"
- **Debugging specific errors** - When you hit a traceback you don't understand

### ⚠️ Use With Caution
- **Generating entire solutions** - You should drive the design decisions
- **Copy-pasting without understanding** - Always read and understand AI-generated code
- **Over-relying during discussion** - The interviewer wants to see YOUR thought process

### 🎯 The Golden Rule
**Use AI like a helpful colleague, not a crutch.** 

The interviewer is evaluating:
- Can you explain WHY you made certain design choices?
- Do you understand the code you're writing?
- Can you think critically about the AI's suggestions?

A good rule of thumb: If you couldn't have written the code yourself given more time, don't use it.

---

## 🧪 Sample Test Cases

Once implemented, your code should handle scenarios like:

```python
# Basic flow
inv = Inventory()
inv.add_product(Product("Laptop", 999.99, 5))
inv.add_product(Product("Mouse", 29.99, 50))

order = Order(inv)
order.add_item("Laptop", 2)  # Should return True
order.add_item("Mouse", 3)   # Should return True
order.add_item("Keyboard", 1)  # Should return False (doesn't exist)

print(order.calculate_total())  # Should be 2089.95

order.place_order()
print(inv.get_product("Laptop").quantity)  # Should be 3

# Edge cases to consider:
# - Ordering more than available stock
# - Ordering from empty inventory
# - Negative quantities?
# - Products with same name?
```

---

## 📝 Notes for the Practice Interviewer

When running this mock interview:

1. **Let them struggle a bit** - Don't jump in too quickly with hints
2. **Ask probing questions**:
   - "Why did you choose a dictionary here instead of a list?"
   - "What happens if someone tries to order -5 items?"
   - "How would you extend this if products had variants (size, color)?"
3. **Observe AI usage** - Are they using it effectively or as a crutch?
4. **Give incremental feedback** - Just like a real pairing session

---

## 🔗 Files

- `inventory.py` - Starter code with TODOs to implement
- `README.md` - This file

Good luck! 🍀
