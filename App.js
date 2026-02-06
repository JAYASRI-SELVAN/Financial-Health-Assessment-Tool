import { useState } from "react";
import { financialTopics } from "./financialTopics";
import "./App.css";

function App() {
  const [topics, setTopics] = useState(financialTopics);

  const updateScore = (id, value) => {
    setTopics(prev =>
      prev.map(topic =>
        topic.id === id
          ? { ...topic, score: Number(value) }
          : topic
      )
    );
  };

  const averageScore = (
    topics.reduce((sum, t) => sum + t.score, 0) / topics.length
  ).toFixed(1);

  return (
    <div className="App">
      <h1>Financial Health Assessment</h1>

      {topics.map(topic => (
        <div key={topic.id} className="card">
          <h3>{topic.title}</h3>
          <p>{topic.description}</p>

          <input
            type="range"
            min="0"
            max="10"
            value={topic.score}
            onChange={e => updateScore(topic.id, e.target.value)}
          />
          <span> Score: {topic.score}</span>
        </div>
      ))}

      <h2>Overall Score: {averageScore} / 10</h2>
    </div>
  );
}

export default App;
