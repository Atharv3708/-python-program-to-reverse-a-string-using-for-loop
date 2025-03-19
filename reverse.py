def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Prepend each character
    return reversed_str

# Example usage
string = input("Enter a string: ")
print("Reversed string:", reverse_string(string))
