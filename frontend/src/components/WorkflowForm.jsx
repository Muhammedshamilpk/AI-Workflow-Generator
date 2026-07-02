import { useState } from "react";

function WorkflowForm({ onGenerate }) {
  const [text, setText] = useState("");

  const handleSubmit = () => {
    if (!text.trim()) return;
    onGenerate(text);
  };

  return (
    <div>
      <textarea
        rows="6"
        cols="60"
        placeholder="Describe your workflow..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <br />
      <br />

      <button onClick={handleSubmit}>
        Generate Workflow
      </button>
    </div>
  );
}

export default WorkflowForm;