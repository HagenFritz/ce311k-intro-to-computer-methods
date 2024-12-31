# Representing Information

### What is Binary?
- **Binary** is a numerical system with only two symbols: **0** and **1**, known as binary digits or **bits**.
- Binary is the foundation of all modern digital systems.

#### Relation to Computer Hardware
- Binary directly corresponds to the physical components of computers, such as **transistors**.
  - High voltage (on) = `1`
  - Low voltage (off) = `0`
- This simple two-state system makes binary **reliable and efficient** for electronic systems.

#### Advantages of Binary
- **Simplicity**: Easy to represent with physical states.
- **Scalability**: Scales well with increasing complexity.
- **Efficiency**: Fewer rules and operations compared to multi-symbol systems.

---

### Binary vs. Decimal

#### Base-10 (Decimal)
- Uses **10 symbols**: `0` through `9`.
- Each digit’s position represents a power of 10.
  - Example: `374 = 3×10² + 7×10¹ + 4×10⁰`

#### Base-2 (Binary)
- Uses **2 symbols**: `0` and `1`.
- Each digit’s position represents a power of 2.
  - Example: `1101 = 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 13`

#### Conversion Between Binary and Decimal
- To convert binary to decimal: Sum the products of each binary digit and its corresponding power of 2.
- To convert decimal to binary: Divide the number by 2 repeatedly, recording remainders.

---

### Mapping Everything to Binary
**Why Binary Matters**: Computers map all data (numbers, letters, images, instructions) to binary for processing and storage.

#### Bits and Bytes
- **Bits** are the smallest unit of binary information.
- **Bytes** consist of 8 bits.
- With 1 byte, you can represent numbers from **0 to 255** (2⁸ combinations).

#### Applications
- Numeric representation
- Text encoding
- Image and color representation

---

### Representing Letters

#### ASCII Encoding
- **ASCII (American Standard Code for Information Interchange)** maps binary values to characters.
  - Example: `A = 65`, `a = 97`.
  - Sufficient for English alphabet, digits, and symbols.

#### Unicode and UTF
- **Unicode Transformation Format (UTF)** extends ASCII to include characters from other languages, symbols, emojis, etc.
- Uses multiple bytes to represent diverse characters.

---

### Representing Colors

#### RGB Model
- **RGB (Red, Green, Blue)** uses three bytes to define color intensities.
  - Each color channel (R, G, B) has 256 possible values (0–255).
  - Example:
    - Red = `11111111 00000000 00000000`
    - Green = `00000000 11111111 00000000`
    - White = `11111111 11111111 11111111`

#### Hexadecimal Colors
**Hexadecimal (base-16)** provides shorthand for RGB values.
- Example: White = `#FFFFFF`, Red = `#FF0000`.
- Combining the RGB channels allows for **16,777,216 unique colors** (256³).
