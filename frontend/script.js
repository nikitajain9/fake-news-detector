async function predict() {
    const text = document.getElementById("newsText").value;
    const resultElement = document.getElementById("result");

    if (!text.trim()) {
        resultElement.innerText = "⚠️ Please enter some text";
        return;
    }

    resultElement.innerText = "⏳ Checking...";

    try {
        const response = await fetch("http://127.0.0.1:9000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        if (data.prediction === 1) {
            resultElement.innerText = "✅ Real News";
            resultElement.style.color = "green";
        } else {
            resultElement.innerText = "❌ Fake News";
            resultElement.style.color = "red";
        }

    } catch (error) {
        resultElement.innerText = "❌ Error connecting to server";
        resultElement.style.color = "red";
    }
}
