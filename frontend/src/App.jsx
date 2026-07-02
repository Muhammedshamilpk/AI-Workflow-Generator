import { useState } from "react";
import api from "./api/api";
import WorkflowForm from "./components/WorkflowForm";
import WorkflowResult from "./components/WorkflowResult";

function App() {
  const [result, setResult] = useState(null);

  async function generateWorkflow(text) {
    try {
      const response = await api.post("/predict", {
        text: text,
      });

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Prediction failed.");
    }
  }

  return (
    <div>
      <h1>AI Workflow Generator</h1>

      <WorkflowForm onGenerate={generateWorkflow} />

      <WorkflowResult result={result} />
    </div>
  );
}

export default App;