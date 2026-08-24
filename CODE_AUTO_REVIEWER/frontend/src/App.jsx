import { useState } from "react";
import "./App.css";

function App() {
  const [code, setCode] = useState("");

  // Review result
  const [result, setResult] = useState(null);

  // Fixed code
  const [fixedCode, setFixedCode] = useState("");

  // Loading states
  const [reviewLoading, setReviewLoading] = useState(false);
  const [fixLoading, setFixLoading] = useState(false);

  // Error message
  const [error, setError] = useState("");

  // =========================
  // REVIEW CODE
  // =========================

  const reviewCode = async () => {
    if (!code.trim()) {
      setError("Please enter Python code first.");
      return;
    }

    setReviewLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/review",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            code: code,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("Review failed");
      }

      const data = await response.json();

      setResult(data);
    } catch (err) {
      setError(
        "Could not connect to the backend. Make sure FastAPI is running."
      );
    } finally {
      setReviewLoading(false);
    }
  };

  // =========================
  // FIX CODE
  // =========================

  const fixCode = async () => {
    if (!code.trim()) {
      setError("Please enter Python code first.");
      return;
    }

    setFixLoading(true);
    setError("");
    setFixedCode("");

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/fix",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            code: code,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("Fix failed");
      }

      const data = await response.json();

      setFixedCode(data.fixed_code);
    } catch (err) {
      setError(
        "Could not connect to the backend. Make sure FastAPI is running."
      );
    } finally {
      setFixLoading(false);
    }
  };

  // =========================
  // COPY FIXED CODE
  // =========================

  const copyFixedCode = async () => {
    try {
      await navigator.clipboard.writeText(fixedCode);
      alert("✅ Fixed code copied!");
    } catch (err) {
      setError("Could not copy the fixed code.");
    }
  };

  return (
    <div className="app">

      {/* =========================
          HEADER
      ========================= */}

      <header className="header">
        <div>
          <h1>🤖 AI Code Reviewer</h1>

         <p>
  AI-powered Python code review, security analysis, and automatic fixing.
</p>
        </div>
      </header>


      <main className="container">

        {/* =========================
            CODE EDITOR
        ========================= */}

        <section className="editor-section">

          <h2>🐍 Python Code</h2>

          <textarea
            value={code}
            onChange={(e) => setCode(e.target.value)}
            placeholder="Paste your Python code here..."
          />

          {/* BUTTONS */}

          <div className="button-group">

            {/* REVIEW */}

            <button
              onClick={reviewCode}
              disabled={reviewLoading}
            >
              {reviewLoading
                ? "🔄 Reviewing..."
                : "🔍 Review Code"}
            </button>


            {/* FIX */}

            <button
              onClick={fixCode}
              disabled={fixLoading}
            >
              {fixLoading
                ? "🔄 Fixing..."
                : "🔧 Fix Code"}
            </button>

          </div>


          {/* ERROR */}

          {error && (
            <div className="error">
              ❌ {error}
            </div>
          )}

        </section>


        {/* =========================
            REVIEW RESULTS
        ========================= */}

        {result && (

          <section className="results">

            <h2>📊 Review Results</h2>


            {/* SUMMARY */}

            <div className="summary">

              <div>
                <strong>
                  {result.static_analysis.length}
                </strong>

                <span>
                  Issues Found
                </span>
              </div>


              <div>
                <strong>
                  {
                    result.static_analysis.filter(
                      (issue) =>
                        issue.severity === "HIGH"
                    ).length
                  }
                </strong>

                <span>
                  High Severity
                </span>
              </div>


              <div>
                <strong>
                  {
                    result.static_analysis.filter(
                      (issue) =>
                        issue.severity === "LOW"
                    ).length
                  }
                </strong>

                <span>
                  Low Severity
                </span>
              </div>

            </div>


            {/* DETECTED ISSUES */}

            <h3>🔍 Detected Issues</h3>


            {result.static_analysis.length === 0 ? (

              <div className="success">
                ✅ No issues detected!
              </div>

            ) : (

              result.static_analysis.map(
                (issue, index) => (

                  <div
                    className="issue"
                    key={index}
                  >

                    <div className="issue-header">

                      <span className="category">
                        {issue.category}
                      </span>

                      <span
                        className={`severity ${issue.severity.toLowerCase()}`}
                      >
                        {issue.severity}
                      </span>

                    </div>


                    <h4>
                      {issue.title}
                    </h4>


                    <p>
                      <strong>
                        Line:
                      </strong>{" "}
                      {issue.line}
                    </p>


                    <p>
                      {issue.message}
                    </p>


                    <div className="suggestion">

                      <strong>
                        💡 Suggestion:
                      </strong>

                      <p>
                        {issue.suggestion}
                      </p>

                    </div>

                  </div>

                )
              )

            )}


            {/* AI EXPLANATION */}

            <div className="ai-review">

              <h3>
                🧠 AI Explanation
              </h3>

              <pre>
                {result.ai_review}
              </pre>

            </div>

          </section>

        )}


        {/* =========================
            FIXED CODE
        ========================= */}

        {fixedCode && (

          <section className="fixed-code">

            <h2>
              🔧 Fixed Code
            </h2>


            <pre>
              {fixedCode}
            </pre>


            {/* COPY */}

            <button
              onClick={copyFixedCode}
            >
              📋 Copy Fixed Code
            </button>

          </section>

        )}

      </main>

    </div>
  );
}

export default App;