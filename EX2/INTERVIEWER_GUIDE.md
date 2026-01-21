# 🔐 INTERVIEWER GUIDE (DO NOT SHARE WITH CANDIDATE)

## Why This Problem Works

- **No starter code** = tests their ability to structure a solution from scratch
- **Clear requirements** = they know what to build
- **Open design** = multiple valid approaches, shows their thinking
- **Shopify-relevant** = gift cards are a real e-commerce feature

---

## Reference Implementation

Here's ONE way to do it. Many valid approaches exist!

```python
import uuid
from datetime import datetime
from enum import Enum


class CardStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class GiftCard:
    def __init__(self, initial_balance: float, code: str = None):
        self.code = code or self._generate_code()
        self.balance = initial_balance
        self.status = CardStatus.ACTIVE
        self.created_at = datetime.now()
    
    def _generate_code(self) -> str:
        return f"GIFT-{uuid.uuid4().hex[:8].upper()}"
    
    def is_active(self) -> bool:
        return self.status == CardStatus.ACTIVE
    
    def deactivate(self) -> None:
        self.status = CardStatus.INACTIVE
    
    def redeem(self, amount: float) -> dict:
        """
        Attempt to redeem the gift card for a purchase.
        Returns dict with amount_applied, remaining_balance, amount_owed.
        """
        if not self.is_active():
            raise ValueError("Gift card is inactive")
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        amount_applied = min(self.balance, amount)
        self.balance -= amount_applied
        amount_owed = amount - amount_applied
        
        return {
            "amount_applied": amount_applied,
            "remaining_balance": self.balance,
            "amount_owed": amount_owed
        }


class GiftCardSystem:
    def __init__(self):
        self._cards: dict[str, GiftCard] = {}
    
    def create_card(self, initial_balance: float, code: str = None) -> GiftCard:
        if initial_balance <= 0:
            raise ValueError("Initial balance must be positive")
        
        card = GiftCard(initial_balance, code)
        
        if card.code in self._cards:
            raise ValueError(f"Card code {card.code} already exists")
        
        self._cards[card.code] = card
        return card
    
    def get_card(self, code: str) -> GiftCard:
        card = self._cards.get(code)
        if card is None:
            raise ValueError(f"Gift card {code} not found")
        return card
    
    def check_balance(self, code: str) -> float:
        return self.get_card(code).balance
    
    def redeem(self, code: str, amount: float) -> dict:
        card = self.get_card(code)
        return card.redeem(amount)
    
    def deactivate(self, code: str) -> None:
        self.get_card(code).deactivate()


# Test it
if __name__ == "__main__":
    system = GiftCardSystem()
    
    # Create a card
    card = system.create_card(50.00)
    print(f"Created card: {card.code} with balance ${card.balance}")
    
    # Check balance
    print(f"Balance: ${system.check_balance(card.code)}")
    
    # Partial redemption
    result = system.redeem(card.code, 30.00)
    print(f"Redeemed $30: Applied ${result['amount_applied']}, "
          f"Remaining ${result['remaining_balance']}, Owed ${result['amount_owed']}")
    
    # Over-balance redemption
    result = system.redeem(card.code, 50.00)
    print(f"Redeemed $50: Applied ${result['amount_applied']}, "
          f"Remaining ${result['remaining_balance']}, Owed ${result['amount_owed']}")
    
    # Deactivate and try to use
    card2 = system.create_card(25.00)
    system.deactivate(card2.code)
    try:
        system.redeem(card2.code, 10.00)
    except ValueError as e:
        print(f"Expected error: {e}")
```

---

## Design Variations to Accept

**Single class approach:**
```python
class GiftCard:
    # All logic in one class, no separate "system"
    _all_cards = {}  # Class variable to track all cards
```
This is fine for the scope of this problem!

**Dictionary-only approach:**
```python
# No classes, just functions operating on dicts
cards = {}

def create_card(balance):
    code = generate_code()
    cards[code] = {"balance": balance, "active": True}
    return code
```
Acceptable if they acknowledge tradeoffs and it works.

**Dataclass approach:**
```python
from dataclasses import dataclass

@dataclass
class GiftCard:
    code: str
    balance: float
    active: bool = True
```
Great if they know dataclasses!

---

## Interview Flow

### Opening Discussion (5 min)

Let them ask questions. Good questions include:
- "How should I generate the gift card codes?"
- "What happens if you try to redeem an invalid code?"
- "Can a card balance ever be negative?"
- "Should I handle concurrent redemptions?"

**Your answers:**
- Code generation: "Up to you - could be random, UUID, whatever"
- Invalid code: "Raise an error or return None, your choice"
- Negative balance: "No, cards can't go negative"
- Concurrency: "Don't worry about that for now"

### Implementation Checkpoints

**~5 min:** Should have basic GiftCard class/structure sketched out

**~15 min:** Should have create + check balance working

**~25 min:** Should have redeem logic working

**~30 min:** Should have deactivate + basic testing

---

## Probing Questions

**On design:**
- "Why did you separate GiftCard and GiftCardSystem?" (or "Why keep it in one class?")
- "How would this scale if we had millions of gift cards?"
- "What if we needed to persist this to a database?"

**On redeem logic:**
- "Walk me through what happens when someone tries to redeem $100 on a $50 card"
- "What if amount is negative?"
- "What if someone calls redeem on a zero-balance card?"

**On error handling:**
- "How are you handling invalid card codes?"
- "Should redeem raise an exception or return an error code?"

**On code generation:**
- "How unique is your code generation? What's the collision risk?"
- "What if someone guesses a valid code?"

---

## Edge Cases to Explore

Ask about these if they don't address them:

1. **Zero or negative initial balance** - Should reject
2. **Zero redemption amount** - Should reject or no-op?
3. **Redeeming from zero-balance card** - Works but applies $0
4. **Duplicate card codes** - Should reject
5. **Case sensitivity of codes** - "GIFT-ABC" vs "gift-abc"
6. **Float precision** - $0.10 + $0.20 weirdness

---

## Stretch Goal Hints

If they finish early and pick a stretch goal:

**Expiration:**
> "Add a `created_at` timestamp and check against current time in `redeem`"

**Transaction history:**
> "Add a list to track each redemption with amount and timestamp"

**Bulk creation:**
> "Add a method that creates N cards and returns a list of codes"

**Merge cards:**
> "Deactivate both source cards, create new card with combined balance"

---

## Evaluation Rubric

### Strong ✅
- Clean class design with clear responsibilities
- Handles core requirements correctly
- Thinks about edge cases proactively
- Good error handling
- Tests their code as they build
- Clear communication throughout

### Average 😐
- Gets it working with some guidance
- Basic structure but some rough edges
- Handles happy path, misses some edge cases
- Needs prompting to test

### Needs Work ⚠️
- Struggles to get started without structure
- Confused about OOP basics
- Doesn't handle errors
- Can't explain their design choices
- Doesn't test until the end (and it breaks)

---

## Common Stumbling Points

**"I don't know where to start"**
> "What's the main thing we're modeling here? Let's start with that class."

**Overcomplicating code generation**
> "For now, even a simple random string is fine. We can make it fancier later."

**Forgetting to store cards somewhere**
> "How will you look up a card by its code later?"

**Redeem logic confusion**
> "Let's trace through an example: $50 card, $30 purchase. What changes?"

**Not returning useful info from redeem**
> "As a customer, what would I want to know after using my gift card?"

---

## AI Usage Notes

**Good signs:**
- "Let me look up how to generate a UUID in Python"
- "What's the syntax for a dataclass again?"
- Uses AI for specific questions, drives design themselves

**Red flags:**
- "Write me a gift card system in Python"
- Pastes entire AI output without reading
- Can't explain why they used certain patterns
