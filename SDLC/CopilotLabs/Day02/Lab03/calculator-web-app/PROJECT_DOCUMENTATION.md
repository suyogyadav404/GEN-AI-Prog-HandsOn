# Project Documentation: Calculator Web App

## 1. Purpose

The Calculator Web App is a lightweight browser-based tool for performing basic arithmetic operations with a modern, responsive interface.

Primary goals:

- Provide a clean and intuitive calculator experience
- Keep implementation simple and framework-free
- Demonstrate front-end fundamentals in HTML, CSS, and JavaScript

## 2. Functional Requirements Covered

- Number buttons 0 through 9
- Addition, subtraction, multiplication, and division
- Clear operation
- Equals evaluation
- Responsive UI behavior
- Modern visual styling

## 3. Application Architecture

The application follows a simple three-file front-end structure:

- index.html: Defines UI skeleton and semantic structure
- style.css: Defines design system, component styles, and responsive behavior
- script.js: Handles state and calculator logic

There is no backend and no external JavaScript dependency.

## 4. UI Structure

Main UI sections in index.html:

- Header section:
  - Eyebrow text and title
- Display area:
  - Read-only input field showing current value or result
- Keypad grid:
  - Clear key
  - Operator keys
  - Number keys
  - Decimal key
  - Equals key (spans two rows)
- Footer note

## 5. Styling And Responsiveness

The CSS design includes:

- Layered gradient background
- Frosted glass style calculator card
- Elevated button design with hover and active feedback
- Distinct color coding for number, operator, clear, and equals actions
- Adaptive spacing and typography using clamp
- Mobile optimizations using media queries at 480px and 340px

Result:

- Better readability across screen sizes
- Comfortable touch targets on smaller devices
- Visual hierarchy that separates actions clearly

## 6. JavaScript Logic Design

Core state variables:

- firstOperand: stores the first numeric operand
- operator: stores the selected operator
- awaitingSecondOperand: tracks when input should begin a new second operand

Key functions:

- updateDisplay(value): writes value to display
- inputNumber(number): appends or replaces display based on state
- inputDot(): safely inserts decimal point once per number
- calculate(first, second, op): computes result for selected operator
- handleOperator(nextOperator): manages operator transitions and intermediate results
- clearCalculator(): resets state and display

Event handling:

- A single delegated click listener on keypad container
- Actions are identified via data attributes
- Each button dispatches to the proper handler

## 7. Error Handling

- Division by zero returns Error
- After Error, calculator state is reset so the next input starts fresh

## 8. Accessibility Considerations

- Display has a hidden text label for assistive technologies
- Focus-visible styles improve keyboard focus visibility
- Button text labels are concise and meaningful

## 9. Manual Test Scenarios

Recommended manual checks:

1. Basic operations:
   - 12 + 7 = 19
   - 20 - 8 = 12
   - 9 * 6 = 54
   - 21 / 3 = 7

2. Decimal operations:
   - 3.5 + 2.25 = 5.75

3. Sequential operator behavior:
   - 5 + - 2 should use the latest selected operator

4. Clear behavior:
   - Enter values, press C, display returns to 0

5. Division by zero:
   - 7 / 0 displays Error

6. Responsive layout:
   - Validate visual quality at desktop width and mobile width

## 10. Limitations

- No keyboard input support yet
- No expression history
- No backspace key
- No advanced operations (percent, square root, etc.)

## 11. Suggested Roadmap

Short-term:

- Add keyboard input mapping
- Add Backspace key

Mid-term:

- Add history panel with last N calculations
- Add dark/light theme toggle

Long-term:

- Add scientific mode as optional expanded panel

## 12. Maintenance Notes

When updating the app:

- Keep UI and logic changes separated by file responsibility
- Preserve data-action and data-value attributes for button behavior
- Re-test division by zero and decimal input paths after logic changes
- Re-check mobile layout after spacing or button size adjustments
