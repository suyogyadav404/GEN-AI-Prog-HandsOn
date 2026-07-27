# Calculator Web App

A responsive calculator web application built with plain HTML, CSS, and JavaScript.
It provides a clean interface for quick arithmetic operations and is designed to work well on desktop and mobile screens.

## Overview

This project demonstrates a complete front-end mini application without any frameworks.
The app focuses on:

- Simple and fast user interaction
- Clear, readable display output
- Modern visual design with responsive behavior
- Maintainable JavaScript logic for calculator operations

## Features

- Numeric input buttons from 0 to 9
- Decimal input support
- Arithmetic operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
- Clear button (C) to reset the calculator
- Equals button (=) to evaluate the current expression
- Error handling for division by zero
- Responsive layout for small and large screens
- Modern UI styling with gradients, depth, and interaction feedback

## Tech Stack

- HTML5
- CSS3
- Vanilla JavaScript (ES6)

## Project Structure

- index.html: UI structure, display, and key layout
- style.css: Theme, spacing, responsive layout, and component styles
- script.js: Calculator state management and button event handling
- PROJECT_DOCUMENTATION.md: Detailed implementation and maintenance documentation

## Setup And Run

1. Open the project folder.
2. Open index.html in any modern browser.
3. Start calculating using on-screen buttons.

No build step or package installation is required.

## Calculator Behavior

- The app stores the first operand and operator after an operator button is clicked.
- When the second operand is entered and equals is pressed, the calculation is performed.
- Repeated operator presses before the second operand update the selected operator.
- Decimal values are allowed once per number segment.
- Division by zero displays Error and resets the operation state.

## Responsive Design Notes

- Container width uses fluid sizing with max constraints.
- Button sizes use scalable values for better touch targets.
- Media queries adapt spacing and control density for narrow devices.

## Accessibility Notes

- The display has an associated hidden label for screen readers.
- Buttons use clear text labels and visible focus styles.

## Manual Testing Checklist

- Enter multi-digit numbers
- Use each operator (+, -, *, /)
- Evaluate with equals
- Clear state using C
- Enter decimal numbers (for example 3.14 + 2.5)
- Verify division by zero shows Error
- Verify layout on desktop and mobile widths

## Future Enhancements

- Keyboard support (numbers, operators, Enter, Backspace)
- Backspace button for single-character deletion
- Calculation history panel
- Theme toggle (light and dark)

## License

This project is intended for learning and lab usage.
