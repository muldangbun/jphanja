import { useState, useEffect } from 'react'
import './App.css'
import vocabData from './data/n3_vocab.json'

function App() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [words, setWords] = useState([]);
  const [showMeaning, setShowMeaning] = useState(false);

  useEffect(() => {
    // Shuffle or just use directly
    setWords(vocabData);
  }, []);

  const handleNext = () => {
    setCurrentIndex((prev) => (prev + 1) % words.length);
    setShowMeaning(false);
  };

  const handlePrev = () => {
    setCurrentIndex((prev) => (prev - 1 + words.length) % words.length);
    setShowMeaning(false);
  };

  const toggleMeaning = () => {
    setShowMeaning(!showMeaning);
  };

  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'ArrowRight') handleNext();
      if (e.key === 'ArrowLeft') handlePrev();
      if (e.key === ' ' || e.key === 'Enter') toggleMeaning();
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [words.length, showMeaning]);

  if (words.length === 0) {
    return <div className="loading">Loading...</div>;
  }

  const currentWord = words[currentIndex];

  return (
    <div className="app-container">
      <div className="background-shapes">
        <div className="shape shape-1"></div>
        <div className="shape shape-2"></div>
        <div className="shape shape-3"></div>
      </div>
      
      <header className="header">
        <h1>JLPT N3 Vocabulary</h1>
        <div className="progress">
          {currentIndex + 1} / {words.length}
        </div>
      </header>

      <main className="main-content">
        <div className="flashcard glass-panel" onClick={toggleMeaning}>
          <div className="card-content">
            <h2 className="reading">{currentWord.reading}</h2>
            <h1 className="word">{currentWord.word}</h1>
            
            <div className={`meaning-container ${showMeaning ? 'visible' : 'hidden'}`}>
              <p className="meaning">{currentWord.meaning}</p>
              <span className="type-badge">{currentWord.type}</span>
            </div>
          </div>
          <div className="card-instruction">
            {showMeaning ? 'Click to hide meaning' : 'Click to show meaning'}
          </div>
        </div>

        <div className="kanji-breakdown">
          {currentWord.kanji_breakdown.map((kanjiInfo, idx) => (
            <div key={idx} className="kanji-card glass-panel fade-in" style={{ animationDelay: `${idx * 0.1}s` }}>
              <div className="kanji-char">{kanjiInfo.kanji}</div>
              <div className="kanji-detail">
                <span className="kanji-kor-meaning">{kanjiInfo.kor_meaning}</span>
                <span className="kanji-kor-sound">{kanjiInfo.kor_sound}</span>
              </div>
            </div>
          ))}
        </div>

        <div className="controls">
          <button className="control-btn glass-btn" onClick={handlePrev}>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
          </button>
          <button className="control-btn glass-btn" onClick={handleNext}>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>
        </div>
      </main>
      
      <footer className="footer">
        Use Arrow Keys ← → to navigate, Space to toggle meaning
      </footer>
    </div>
  )
}

export default App
