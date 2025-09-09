from js import document, alert

def calculate(event):
    try:
        s1 = float(document.getElementById("score1").value)
        s2 = float(document.getElementById("score2").value)
        avg = (s1 + s2) / 2

        if avg >= 75:
            result = "Yes ✅"
        else:
            result = "No ❌"

        # popup
        alert(f"Average: {avg:.2f}\nPassed?: {result}")

    except:
        alert("Invalid input. Please enter numbers only.")

document.getElementById("calcBtn").addEventListener("click", calculate)
