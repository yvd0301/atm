# ATM Controller Implementation
- Insert Card
- PIN number validation
- Select Account
- See Balance
- Deposit
- Withdraw

# Assumption
- The card number and bank account number are not string but integer for simplifying the implementation.
- The pin number has an initial number and will be updated later.

# Classes
1. CardInterface : Abstract class for Card
2. Card : Card object implementation
3. Account : Account object implentation
4. AtmInterface : Abstract class for Atm
5. Atm : API implementation

# Instruction
1. clone this repository
```
https://github.com/yvd0301/atm
```
2. Run Tests using pytest
install pytest and run tests
```
pip install pytest==7.2.0
```
```
pytest -vs
```
![스크린샷 2023-01-01 오전 7 06 45](https://user-images.githubusercontent.com/120325179/210156464-38cd9e08-2e57-4558-93d8-c8e24be3f561.png)
