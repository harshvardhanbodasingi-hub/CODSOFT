# Task 3: Password Generator - CodSoft

import random
import string


def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    all_chars = lower + upper + digits + symbols

    if not all_chars:
        return "Error: No character sets selected!"

    # Ensure at least one of each selected type is present
    password = []

    password.append(random.choice(lower))
    if use_upper:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    # Fill the remaining length
    remaining_length = max(0, length - len(password))
    password += [random.choice(all_chars) for _ in range(remaining_length)]

    # Shuffle to make password random
    random.shuffle(password)

    return "".join(password)


def main():
    print("=" * 40)
    print("        PASSWORD GENERATOR")
    print("=" * 40)

    while True:
        try:
            length = int(input("Enter password length (min 4): "))
            if length < 4:
                print("Length should be at least 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()
