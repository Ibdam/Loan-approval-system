document.getElementById("loanForm").addEventListener("submit", function(e) {
  e.preventDefault();

  // Collect input values
  const data = {
    no_of_dependents: document.getElementById("no_of_dependents").value,
    education: document.getElementById("education").value,
    self_employed: document.getElementById("self_employed").value,
    income_annum: document.getElementById("income_annum").value,
    loan_amount: document.getElementById("loan_amount").value,
    loan_term: document.getElementById("loan_term").value,
    Assets_value: document.getElementById("Assets_value").value
  };

  // Temporary mock prediction (to be replaced with API call)
  const resultCard = document.getElementById("result-card");
  const resultText = document.getElementById("prediction-result");
  const random = Math.random();
  resultText.textContent = random > 0.5 ? "Approved ✅" : "Rejected ❌";
  resultCard.classList.remove("hidden");
});
