#!/usr/bin/env python3
"""
Chapter 3: Digital Signals
Demonstrates digital signal representation and bit/byte concepts
"""

def char_to_binary(char):
    """Convert a character to its 8-bit binary representation"""
    ascii_val = ord(char)
    return format(ascii_val, '08b')

def binary_to_char(binary_str):
    """Convert 8-bit binary to character"""
    decimal = int(binary_str, 2)
    return chr(decimal)

def string_to_binary(text):
    """Convert string to binary representation"""
    return ' '.join(char_to_binary(c) for c in text)

def digital_signal_visualization(binary_str):
    """Visualize digital signal as high/low levels"""
    print("\nDigital Signal Visualization:")
    print("Bit:     ", ' '.join(binary_str))
    print("Signal:  ", end='')
    
    for bit in binary_str:
        if bit == '1':
            print("█████ ", end='')
        else:
            print("_____ ", end='')
    print()
    
    print("Voltage: ", end='')
    for bit in binary_str:
        print(" 5V  " if bit == '1' else " 0V  ", end='')
    print()

def main():
    print("=" * 60)
    print("CHAPTER 3: Digital Signals")
    print("=" * 60)
    
    # Example 1: Character to Binary
    print("\n--- Example 1: Character Encoding ---")
    char = 'A'
    binary = char_to_binary(char)
    print(f"Character: {char}")
    print(f"ASCII value: {ord(char)}")
    print(f"Binary (8 bits): {binary}")
    print(f"This is 1 byte (8 bits)")
    
    # Example 2: Binary to Character
    print("\n--- Example 2: Binary Decoding ---")
    binary = "01000001"
    char = binary_to_char(binary)
    print(f"Binary: {binary}")
    print(f"Character: {char}")
    
    # Example 3: String to Binary
    print("\n--- Example 3: Digital Data Representation ---")
    text = "HELLO"
    binary_text = string_to_binary(text)
    print(f"Text: {text}")
    print(f"Binary representation:")
    for i, char in enumerate(text):
        print(f"  {char}: {char_to_binary(char)}")
    
    # Example 4: Digital Signal Visualization
    print("\n--- Example 4: Digital Signal Levels ---")
    sample_binary = "10110100"
    digital_signal_visualization(sample_binary)
    
    # Example 5: Bit and Byte counting
    print("\n--- Example 5: Bit and Byte Calculations ---")
    text = "Computer"
    bits = len(text) * 8
    bytes_count = len(text)
    print(f"Text: '{text}'")
    print(f"Characters: {len(text)}")
    print(f"Bytes: {bytes_count} (1 byte per character)")
    print(f"Bits: {bits} (8 bits per byte)")
    
    print("\n" + "=" * 60)
    print("Key Concepts:")
    print("- Digital signals have only discrete values (0 and 1)")
    print("- 1 bit = smallest unit (0 or 1)")
    print("- 1 byte = 8 bits")
    print("- Voltage levels represent binary: 0V=0, 5V=1 (typical)")
    print("- Digital signals are robust against noise")
    print("=" * 60)

if __name__ == "__main__":
    main()
