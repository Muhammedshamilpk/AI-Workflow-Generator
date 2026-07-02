function WorkflowResult({ result }) {
  if (!result) return null;

  return (
    <div>
      <h2>Trigger</h2>

      <p>{result.trigger}</p>

      <h2>Actions</h2>

      <ul>
        {result.actions.map((action, index) => (
          <li key={index}>{action}</li>
        ))}
      </ul>
    </div>
  );
}

export default WorkflowResult;