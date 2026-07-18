# Python Operators and Sum of Digits

This README covers some basic Python operators and a program to calculate the sum of digits of a three-digit number.

## 1. Arithmetic Operator

```python
print(2 + 3)
```

Output:

```text
5
```

The `+` operator is used to add two numbers.

---

## 2. Floor Division Operator

```python
print(5 // 8)
```

Output:

```text
0
```

The `//` operator performs floor division. It returns the whole-number part of the division and removes the decimal portion.

For example:

```python
print(17 // 5)
```

Output:

```text
3
```

---

## 3. Comparison Operator

```python
print(6 > 3)
```

Output:

```text
True
```

The `>` operator checks whether the value on the left is greater than the value on the right.

Comparison operators return either `True` or `False`.

---

## 4. Logical `or` Operator

```python
print(8 or 9)
```

Output:

```text
8
```

The `or` operator returns the first truthy value.

Since `8` is a non-zero number, Python considers it truthy and returns it without checking the second value.

Example:

```python
print(0 or 9)
```

Output:

```text
9
```

Here, `0` is falsy, so Python returns `9`.

---

## 5. Assignment Operator

```python
a = 4
a += 4

print(a)
```

Output:

```text
8
```

The statement:

```python
a += 4
```

is a shorter way of writing:

```python
a = a + 4
```

---

## 6. Membership Operator

```python
print("M" in "Palak")
```

Output:

```text
False
```

The `in` operator checks whether a value exists inside a string, list, tuple, or another collection.

Python is case-sensitive, which means uppercase and lowercase letters are treated differently.

Example:

```python
print("P" in "Palak")
```

Output:

```text
True
```

---

# Program to Find the Sum of Digits

The following program calculates the sum of the digits of a three-digit number entered by the user.

```python
n = int(input("Enter a three-digit number: "))

a = n % 10
n = n // 10

b = n % 10
n = n // 10

c = n % 10

print("The sum of digits is:", a + b + c)
```

## Example

```text
Enter a three-digit number: 456
The sum of digits is: 15
```

## How the Program Works

Suppose the user enters:

```text
456
```

### Step 1: Extract the last digit

```python
a = n % 10
```

The modulus operator `%` returns the remainder.

```text
456 % 10 = 6
```

Therefore:

```python
a = 6
```

### Step 2: Remove the last digit

```python
n = n // 10
```

Floor division by `10` removes the last digit.

```text
456 // 10 = 45
```

### Step 3: Extract the second digit

```python
b = n % 10
```

```text
45 % 10 = 5
```

Therefore:

```python
b = 5
```

### Step 4: Remove the second digit

```python
n = n // 10
```

```text
45 // 10 = 4
```

### Step 5: Extract the first digit

```python
c = n % 10
```

```text
4 % 10 = 4
```

Therefore:

```python
c = 4
```

### Step 6: Add all digits

```python
a + b + c
```

```text
6 + 5 + 4 = 15
```

## Important Note

This version of the program is designed specifically for a three-digit number. A loop can be used when the number of digits is unknown.
