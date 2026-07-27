const display = document.getElementById("display");
const keys = document.querySelector(".keys");

let firstOperand = null;
let operator = null;
let awaitingSecondOperand = false;

function updateDisplay(value) {
  display.value = value;
}

function inputNumber(number) {
  if (awaitingSecondOperand) {
    updateDisplay(number);
    awaitingSecondOperand = false;
    return;
  }

  const currentValue = display.value;
  updateDisplay(currentValue === "0" ? number : currentValue + number);
}

function inputDot() {
  if (awaitingSecondOperand) {
    updateDisplay("0.");
    awaitingSecondOperand = false;
    return;
  }

  if (!display.value.includes(".")) {
    updateDisplay(display.value + ".");
  }
}

function calculate(first, second, op) {
  if (op === "+") return first + second;
  if (op === "-") return first - second;
  if (op === "*") return first * second;
  if (op === "/") return second === 0 ? "Error" : first / second;
  return second;
}

function handleOperator(nextOperator) {
  const inputValue = parseFloat(display.value);

  if (operator && awaitingSecondOperand) {
    operator = nextOperator;
    return;
  }

  if (firstOperand === null) {
    firstOperand = inputValue;
  } else if (operator) {
    const result = calculate(firstOperand, inputValue, operator);

    if (result === "Error") {
      updateDisplay("Error");
      firstOperand = null;
      operator = null;
      awaitingSecondOperand = false;
      return;
    }

    const rounded = Number.isInteger(result)
      ? result.toString()
      : parseFloat(result.toFixed(8)).toString();

    updateDisplay(rounded);
    firstOperand = parseFloat(rounded);
  }

  awaitingSecondOperand = true;
  operator = nextOperator;
}

function clearCalculator() {
  firstOperand = null;
  operator = null;
  awaitingSecondOperand = false;
  updateDisplay("0");
}

keys.addEventListener("click", (event) => {
  const target = event.target;
  if (!target.matches("button")) return;

  const action = target.dataset.action;
  const value = target.dataset.value;

  if (action === "number") {
    inputNumber(value);
    return;
  }

  if (action === "dot") {
    inputDot();
    return;
  }

  if (action === "operator") {
    handleOperator(value);
    return;
  }

  if (action === "equals") {
    if (operator === null || awaitingSecondOperand) return;
    handleOperator(operator);
    operator = null;
    awaitingSecondOperand = false;
    return;
  }

  if (action === "clear") {
    clearCalculator();
  }
});

clearCalculator();
