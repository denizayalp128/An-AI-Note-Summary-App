from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    
    notes = ""
    summary = ""

    if request.method == "POST":
        notes = request.form["notes"]
        action = request.form["action"]
        
        
        if len(notes) > 2500:
            summary = "Error: Maximum 2500 characters allowed."
        elif action == "Summarize":
            response = requests.post(
                "http://localhost:1234/api/v1/chat",
                headers={
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gemma-1.1-2b-it",
                    "input": f"Summarize these notes:{notes}\n\n",
                    "context_length": 8000
                }
            )

            answer = response.json()
            summary = answer["output"][0]["content"]
        elif action == "Generate A Question":
            response = requests.post(
                "http://localhost:1234/api/v1/chat",
                headers={
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gemma-1.1-2b-it",
                    "input": f"Generate a question and an answer based on these notes:{notes}\n\n",
                    "context_length": 8000
                }
            )

        

            answer = response.json()
            summary = answer["output"][0]["content"]

        elif action == "Simple":
            response = requests.post(
                "http://localhost:1234/api/v1/chat",
                headers={
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gemma-1.1-2b-it",
                    "input": f"Tell It like you are explaining to a five-year-old:{notes}\n\n",
                    "context_length": 8000
                }
            )

            answer = response.json()
            summary = answer["output"][0]["content"]

        elif action == "Key Concepts":
            response = requests.post(
                "http://localhost:1234/api/v1/chat",
                headers={
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gemma-1.1-2b-it",
                    "input": f"Extract the key concepts from these notes:{notes}\n\n",
                    "context_length": 8000
                }
            )

            answer = response.json()
            summary = answer["output"][0]["content"]

        elif action == "Anki":
            response = requests.post(
                "http://localhost:1234/api/v1/chat",
                headers={
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gemma-1.1-2b-it",
                    "input": f"Create Anki flashcards based on these notes:{notes}\n\n",
                    "context_length": 8000
                }
            )

            answer = response.json()
            summary = answer["output"][0]["content"]
    return render_template(
            "index.html",
            notes=notes,
            summary=summary,
            lengthofnotes=len(notes)
        )    


if __name__ == "__main__":
    app.run(debug=True)
