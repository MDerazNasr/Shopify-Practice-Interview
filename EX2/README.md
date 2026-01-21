# Shopify Pair Programming Practice Interview

## The Scenario

You're building a **Gift Card System** for an e-commerce platform. Customers can purchase gift cards, redeem them at checkout, and check their balance.

This is a blank slate - design and implement the system from scratch.

---

## Core Requirements

Your system needs to support these operations:

### 1. Create a Gift Card
- Each gift card has a **unique code** (e.g., "GIFT-ABC123")
- Each gift card has an **initial balance** (e.g., $50.00)
- Gift cards start as **active**

### 2. Check Balance
- Given a gift card code, return the current balance
- Handle invalid/non-existent codes gracefully

### 3. Redeem Gift Card
- Apply a gift card to a purchase amount
- Deduct the appropriate amount from the card's balance
- A gift card can be used for **partial payment** (e.g., $50 card on a $30 purchase leaves $20 remaining)
- A gift card **cannot go negative** (e.g., $50 card on a $80 purchase covers $50, customer owes $30)
- Return how much was actually applied and any remaining amount due

### 4. Deactivate a Gift Card
- Mark a gift card as inactive (e.g., for fraud prevention)
- Inactive cards cannot be redeemed

---

## Example Usage

Your implementation should support something like this (exact API is up to you):

```python
# Create some gift cards
# ... your code here ...

# Check balance
# >>> check balance for "GIFT-ABC123"
# 50.00

# Redeem partial amount
# >>> redeem "GIFT-ABC123" for a $30 purchase
# Applied: $30.00, Remaining balance: $20.00, Amount still owed: $0.00

# Redeem more than balance
# >>> redeem "GIFT-ABC123" for a $50 purchase  
# Applied: $20.00, Remaining balance: $0.00, Amount still owed: $30.00

# Try to use inactive card
# >>> deactivate "GIFT-ABC123"
# >>> redeem "GIFT-ABC123" for a $10 purchase
# Error: Card is inactive
```

---

## What You're Building

Design this however makes sense to you. Consider:

- What classes do you need?
- What data structures will you use?
- How will you generate/validate gift card codes?
- How will you handle errors?

There's no single "right" answer - we want to see how you approach the design.

---

## Stretch Goals (if time permits)

Pick one if you finish early:

1. **Expiration dates** - Gift cards expire after 1 year
2. **Transaction history** - Track all redemptions on a card
3. **Bulk creation** - Generate multiple gift cards at once with the same initial value
4. **Merge cards** - Combine two gift cards into one

---

## Time Budget

| Phase | Time |
|-------|------|
| Clarifying questions & design discussion | 5 min |
| Implementation | 20-25 min |
| Testing & edge cases | 5 min |
| Q&A | 10 min |

---

## Tips

- **Think out loud** - explain your reasoning as you go
- **Start simple** - get the basics working before adding complexity
- **Ask questions** - clarify requirements before diving in
- **Test as you go** - don't wait until the end to run your code

---

## Getting Started

Create a new file called `giftcard.py` and build your solution from scratch.

```bash
touch giftcard.py
python giftcard.py
```

Good luck! 🎁
