import { useState, useEffect, useRef } from 'react'
import './App.css'
import vocabData from './data/n3_vocab.json'

function App() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [words, setWords] = useState([]);
  const [showMeaning, setShowMeaning] = useState(true);
  const audioRef = useRef(null);

  useEffect(() => {
    // Shuffle or just use directly
    setWords(vocabData);
    audioRef.current = new Audio();
  }, []);

  const playAudio = (e) => {
    if (e) e.stopPropagation();
    if (!audioRef.current) return;
    audioRef.current.src = `./audio/n3_vocab/${currentIndex}.mp3`;
    audioRef.current.play().catch(err => console.log('Autoplay prevented:', err));
  };

  useEffect(() => {
    if (words.length > 0) {
      playAudio();
    }
  }, [currentIndex, words]);

  const handleNext = () => {
    setCurrentIndex((prev) => (prev + 1) % words.length);
  };

  const handlePrev = () => {
    setCurrentIndex((prev) => (prev - 1 + words.length) % words.length);
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
        <div className="header-top">
          <button className="home-btn glass-btn" onClick={() => window.location.href = '../../index.html'} title="Go Home">
            <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round" strokeLinejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
          </button>
          <h1>JLPT N3 Vocabulary</h1>
          <div className="progress">
            {currentIndex + 1} / {words.length}
          </div>
        </div>
        <div className="slider-container">
          <input 
            type="range" 
            min="0" 
            max={words.length > 0 ? words.length - 1 : 0} 
            value={currentIndex} 
            onChange={(e) => setCurrentIndex(Number(e.target.value))}
            className="progress-slider"
          />
        </div>
      </header>

      <main className="main-content">
        <div className="flashcard glass-panel" onClick={toggleMeaning}>
          <div className="card-content">
            <div className="reading-wrapper">
              <h2 className="reading">{currentWord.reading}</h2>
              <button className="audio-btn glass-btn" onClick={playAudio} title="Play Audio">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path><path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path></svg>
              </button>
            </div>
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
