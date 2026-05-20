const scanBtn = document.getElementById(
  "scanBtn"
);

const resultDiv = document.getElementById(
  "result"
);


scanBtn.addEventListener("click", async () => {

  const tabs = await chrome.tabs.query({
    active: true,
    currentWindow: true
  });

  const currentURL = tabs[0].url;

  resultDiv.innerHTML =
    "Scanning...";


  try {

    const response = await fetch(
      "http://localhost:8000/scan/",
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json",

          "Authorization":
            `Bearer ${localStorage.getItem("token")}`
        },

        body: JSON.stringify({
          url: currentURL
        })
      }
    );

    const data = await response.json();

    let riskClass = "low";

    if (data.risk_score === "HIGH") {
      riskClass = "high";
    }

    else if (
      data.risk_score === "MEDIUM"
    ) {
      riskClass = "medium";
    }


    resultDiv.className = riskClass;

    resultDiv.innerHTML = `

      <h2>${data.risk_score} RISK</h2>

      <p>
        Prediction:
        ${data.prediction}
      </p>

      <p>
        Confidence:
        ${data.confidence}%
      </p>

    `;

  } catch (error) {

    console.error(error);

    resultDiv.innerHTML =
      "Error scanning website";
  }
});
