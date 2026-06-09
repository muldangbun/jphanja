import React, { useState } from "react";
import { 
  Home, 
  BookOpen, 
  Grid, 
  Layers, 
  Trophy, 
  CheckCircle, 
  XCircle, 
  RefreshCw, 
  ChevronRight,
  Info,
  Search
} from "lucide-react";
import { positionsData, coreRadicalsData } from "./data/radicalsData";
import kanjiDecomposerDataGrade1 from "./data/kanjiDecomposerData.json";
import kanjiDecomposerDataGrade2 from "./data/kanjiDecomposerData_grade2.json";
import kanjiDecomposerDataGrade3 from "./data/kanjiDecomposerData_grade3.json";
import kanjiDecomposerDataGrade4 from "./data/kanjiDecomposerData_grade4.json";
import kanjiDecomposerDataGrade5 from "./data/kanjiDecomposerData_grade5.json";
import kanjiDecomposerDataGrade6 from "./data/kanjiDecomposerData_grade6.json";

const decomposerDataMap = {
  "전체": [
    ...kanjiDecomposerDataGrade1, ...kanjiDecomposerDataGrade2, ...kanjiDecomposerDataGrade3,
    ...kanjiDecomposerDataGrade4, ...kanjiDecomposerDataGrade5, ...kanjiDecomposerDataGrade6
  ],
  "1학년": kanjiDecomposerDataGrade1,
  "2학년": kanjiDecomposerDataGrade2,
  "3학년": kanjiDecomposerDataGrade3,
  "4학년": kanjiDecomposerDataGrade4,
  "5학년": kanjiDecomposerDataGrade5,
  "6학년": kanjiDecomposerDataGrade6
};

// 부수 위치 가이드 SVG 컴포넌트
const PositionSvg = ({ pattern, className = "w-24 h-24 mx-auto" }) => {
  const getHighlightClass = (area) => {
    const active = "fill-emerald-400 stroke-emerald-600 stroke-2 opacity-90";
    const inactive = "fill-slate-200 stroke-slate-400 opacity-40";
    
    switch (pattern) {
      case "left":
        return area === "left" ? active : inactive;
      case "right":
        return area === "right" ? active : inactive;
      case "top":
        return area === "top" ? active : inactive;
      case "bottom":
        return area === "bottom" ? active : inactive;
      case "top-left":
        return area === "top" || area === "left" ? active : inactive;
      case "bottom-left":
        return area === "bottom" || area === "left" ? active : inactive;
      case "border":
        return area === "border" ? active : inactive;
      default:
        return inactive;
    }
  };

  return (
    <svg viewBox="0 0 100 100" className={`${className} transition-all duration-300`}>
      {/* 기본 테두리 */}
      <rect x="5" y="5" width="90" height="90" rx="8" fill="none" stroke="#94a3b8" strokeWidth="2" strokeDasharray="3 3" />
      
      {/* 1. 변(Left) */}
      <rect x="10" y="10" width="35" height="80" rx="4" className={getHighlightClass("left")} />
      
      {/* 2. 방(Right) */}
      <rect x="55" y="10" width="35" height="80" rx="4" className={getHighlightClass("right")} />
      
      {/* 3. 머리(Top) */}
      <rect x="10" y="10" width="80" height="25" rx="4" className={getHighlightClass("top")} />
      
      {/* 4. 발(Bottom) */}
      <rect x="10" y="65" width="80" height="25" rx="4" className={getHighlightClass("bottom")} />
      
      {/* 테두리 감싸는 몸(Border) 강조용 */}
      {pattern === "border" && (
        <rect x="8" y="8" width="84" height="84" rx="6" fill="none" strokeWidth="6" className="stroke-emerald-500 fill-emerald-100 opacity-60" />
      )}
      
      {/* 가상의 한자 코어 부분 표시 */}
      <circle cx="50" cy="50" r="4" fill="#94a3b8" />
    </svg>
  );
};

export default function App() {
  const [activeTab, setActiveTab] = useState("positions");

  // 일본어 TTS 재생 헬퍼 함수
  const speakJapanese = (text) => {
    if (!text) return;
    if (!window.speechSynthesis) {
      alert("이 브라우저는 음성 재생(TTS)을 지원하지 않습니다.");
      return;
    }
    window.speechSynthesis.cancel();
    
    // 괄호 및 특수문자 정제
    let cleanText = text
      .replace(/[a-zA-Z가-힣]/g, "") // 한글, 영문 제거
      .replace(/\((.*?)\)/g, "$1")   // 괄호 내용 복원: (く) -> く
      .replace(/\s*\/\s*/g, "、")     // 슬래시 -> 쉼표
      .trim();

    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.lang = "ja-JP";
    utterance.rate = 0.85;
    window.speechSynthesis.speak(utterance);
  };
  
  // 1. Positions State
  const [selectedPosition, setSelectedPosition] = useState(positionsData[0]);

  // 2. Core 50 State
  const [filter, setFilter] = useState("all");
  const [activeRadicalDetail, setActiveRadicalDetail] = useState(null);

  // 3. Decomposer State
  const [decomposerGradeFilter, setDecomposerGradeFilter] = useState("1학년");
  const [decomposerSearchQuery, setDecomposerSearchQuery] = useState("");
  const [selectedDecomposerData, setSelectedDecomposerData] = useState(kanjiDecomposerDataGrade1[0] || null);
  const [activeComponentDetail, setActiveComponentDetail] = useState(null);

  // Decomposer 렌더링을 위한 필터링 데이터 계산
  const filteredDecomposerData = React.useMemo(() => {
    let data = decomposerDataMap[decomposerGradeFilter] || [];
    if (decomposerSearchQuery.trim()) {
      const q = decomposerSearchQuery.trim().toLowerCase();
      data = data.filter(d => 
        d.kanji.includes(q) || 
        d.meaning.includes(q) || 
        (d.reading_on && d.reading_on.includes(q)) || 
        (d.reading_kun && d.reading_kun.includes(q))
      );
    }
    return data;
  }, [decomposerGradeFilter, decomposerSearchQuery]);
  
  // 학년이나 검색어가 변경될 때 첫 번째 한자로 자동 선택
  React.useEffect(() => {
    if (activeTab === "decomposer" && filteredDecomposerData.length > 0) {
      if (!filteredDecomposerData.find(d => d.kanji === selectedDecomposerData?.kanji)) {
        setSelectedDecomposerData(filteredDecomposerData[0]);
        setActiveComponentDetail(null);
      }
    } else if (filteredDecomposerData.length === 0) {
      setSelectedDecomposerData(null);
    }
  }, [filteredDecomposerData, activeTab]);

  // 4. Quiz State
  const [quizStarted, setQuizStarted] = useState(false);
  const [quizQuestions, setQuizQuestions] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [score, setScore] = useState(0);
  const [showScore, setShowScore] = useState(false);

  // Decomposer 한자가 바뀔 때 선택된 컴포넌트 디테일 초기화 (이벤트 핸들러에서 직접 처리하여 useEffect 제거)

  // 퀴즈 제너레이터
  const generateQuiz = () => {
    // 50개 부수 중 무작위 5개 선정
    const shuffled = [...coreRadicalsData].sort(() => 0.5 - Math.random());
    const selected = shuffled.slice(0, 5);

    const questions = selected.map((rad, idx) => {
      // 오답 보기 3개 구성
      const otherAnswers = coreRadicalsData
        .filter(r => r.meaning !== rad.meaning)
        .sort(() => 0.5 - Math.random())
        .slice(0, 3)
        .map(r => r.meaning);

      // 문제 유형 결정 (0: 부수 기호 -> 한국어 뜻 맞추기, 1: 한국어 뜻 -> 부수 기호 맞추기)
      const type = Math.random() > 0.5 ? 0 : 1;

      let questionText;
      let correctAnswer;
      let choices;

      if (type === 0) {
        questionText = `부수 "${rad.variant !== rad.original ? `${rad.original} (${rad.variant})` : rad.original}"의 올바른 뜻은 무엇인가요?`;
        correctAnswer = rad.meaning;
        choices = [rad.meaning, ...otherAnswers].sort(() => 0.5 - Math.random());
      } else {
        questionText = `다음 중 "${rad.meaning}"의 뜻을 가진 한자 부수는 무엇인가요?`;
        correctAnswer = rad.variant !== rad.original ? `${rad.original} (${rad.variant})` : rad.original;
        
        const otherChoices = coreRadicalsData
          .filter(r => r.meaning !== rad.meaning)
          .sort(() => 0.5 - Math.random())
          .slice(0, 3)
          .map(r => r.variant !== r.original ? `${r.original} (${r.variant})` : r.original);
          
        choices = [correctAnswer, ...otherChoices].sort(() => 0.5 - Math.random());
      }

      return {
        id: idx,
        question: questionText,
        choices: choices,
        answer: correctAnswer,
        rawRadical: rad
      };
    });

    setQuizQuestions(questions);
    setCurrentQuestionIndex(0);
    setSelectedAnswer(null);
    setIsAnswered(false);
    setScore(0);
    setShowScore(false);
    setQuizStarted(true);
  };

  const handleAnswerClick = (choice) => {
    if (isAnswered) return;
    setSelectedAnswer(choice);
    setIsAnswered(true);
    if (choice === quizQuestions[currentQuestionIndex].answer) {
      setScore(prev => prev + 1);
    }
  };

  const handleNextQuestion = () => {
    setSelectedAnswer(null);
    setIsAnswered(false);
    if (currentQuestionIndex + 1 < quizQuestions.length) {
      setCurrentQuestionIndex(prev => prev + 1);
    } else {
      setShowScore(true);
    }
  };

  // 50선 필터링
  const filteredRadicals = coreRadicalsData.filter(rad => {
    if (filter === "all") return true;
    return rad.category === filter;
  });

  return (
    <div className="min-h-screen bg-[#f4f3ef] text-slate-800 transition-all duration-300">
      {/* Top Banner & Header */}
      <header className="glass sticky top-0 z-40 border-b border-stone-200 py-4 px-6 md:px-12 flex flex-col md:flex-row justify-between items-center gap-4">
        <div className="flex items-center gap-3">
          <div className="bg-emerald-600 text-white p-2 rounded-xl shadow-md">
            <Layers className="w-6 h-6 animate-pulse" />
          </div>
          <div>
            <h1 className="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">
              일본어 한자 부수 마스터
            </h1>
            <p className="text-xs text-slate-500 font-medium font-sans">Kanji Radical Learner</p>
          </div>
        </div>

        {/* Navigation Buttons */}
        <div className="flex flex-wrap items-center gap-2">
          <button 
            onClick={() => setActiveTab("positions")}
            className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all duration-300 flex items-center gap-2 ${
              activeTab === "positions" 
                ? "bg-slate-900 text-white shadow-md scale-105" 
                : "bg-white/60 hover:bg-white text-slate-600 border border-slate-200"
            }`}
          >
            <BookOpen className="w-4 h-4" />
            부수 위치 7가지
          </button>
          <button 
            onClick={() => setActiveTab("core50")}
            className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all duration-300 flex items-center gap-2 ${
              activeTab === "core50" 
                ? "bg-slate-900 text-white shadow-md scale-105" 
                : "bg-white/60 hover:bg-white text-slate-600 border border-slate-200"
            }`}
          >
            <Grid className="w-4 h-4" />
            필수 부수 50선
          </button>
          <button 
            onClick={() => setActiveTab("decomposer")}
            className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all duration-300 flex items-center gap-2 ${
              activeTab === "decomposer" 
                ? "bg-slate-900 text-white shadow-md scale-105" 
                : "bg-white/60 hover:bg-white text-slate-600 border border-slate-200"
            }`}
          >
            <Layers className="w-4 h-4" />
            한자 조립 분해
          </button>
          <button 
            onClick={() => {
              setActiveTab("quiz");
              setQuizStarted(false);
            }}
            className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all duration-300 flex items-center gap-2 ${
              activeTab === "quiz" 
                ? "bg-slate-900 text-white shadow-md scale-105" 
                : "bg-white/60 hover:bg-white text-slate-600 border border-slate-200"
            }`}
          >
            <Trophy className="w-4 h-4" />
            미니 퀴즈
          </button>

          {/* 메인 화면으로 가기 */}
          <a 
            href="../../index.html" 
            className="ml-2 md:ml-4 bg-emerald-50 hover:bg-emerald-100 text-emerald-700 px-4 py-2 rounded-xl text-sm font-bold border border-emerald-200 transition-all duration-300 flex items-center gap-1.5 shadow-sm"
          >
            <Home className="w-4 h-4" />
            홈으로
          </a>
        </div>
      </header>

      {/* Main Container */}
      <main className="max-w-6xl mx-auto px-4 py-8 md:py-12">
        
        {/* ==================== PAGE 1: 부수 위치 7가지 ==================== */}
        {activeTab === "positions" && (
          <div className="space-y-8 animate-fadeIn">
            {/* Info Introduction */}
            <div className="glass rounded-3xl p-6 md:p-8 hidden md:flex flex-col md:flex-row items-center gap-6 shadow-sm border border-stone-200">
              <div className="bg-emerald-100 p-4 rounded-2xl text-emerald-800">
                <Info className="w-8 h-8" />
              </div>
              <div className="space-y-2 text-center md:text-left">
                <h2 className="text-xl font-bold text-slate-900">부수(部首)와 7가지 결합 위치</h2>
                <p className="text-slate-600 leading-relaxed max-w-3xl">
                  한자는 단독으로 쓰이기도 하지만 여러 글자가 조립되어 만들어집니다. 이때 한자의 핵심 뜻을 담당하며, 결합하는 위치에 따라 크게 <strong>7가지 위치(변, 방, 머리, 발, 엄, 받침, 몸)</strong>로 구분됩니다.
                </p>
              </div>
            </div>

            {/* Content Layout */}
            {/* 1. Desktop Layout (lg screens) */}
            <div className="hidden lg:grid grid-cols-3 gap-8">
              {/* Left Side: 7 Positions List Cards */}
              <div className="col-span-2 grid grid-cols-2 gap-4">
                {positionsData.map((pos) => (
                  <div
                    key={pos.id}
                    onClick={() => setSelectedPosition(pos)}
                    onMouseEnter={() => setSelectedPosition(pos)}
                    className={`glass p-5 rounded-2xl border cursor-pointer transition-all duration-300 flex items-center justify-between group ${
                      selectedPosition.id === pos.id 
                        ? "border-emerald-500 ring-2 ring-emerald-500/20 bg-emerald-50/30 translate-x-1" 
                        : "border-slate-200 hover:border-slate-400 hover:shadow-md"
                    }`}
                  >
                    <div className="space-y-2">
                      <div className="flex items-baseline gap-2">
                        <h3 className="text-3xl font-black text-slate-950 tracking-tighter">{pos.name}</h3>
                        <span className={`text-xl font-black font-sans transition-colors ${
                          selectedPosition.id === pos.id ? "text-emerald-600" : "text-slate-400"
                        }`}>
                          {pos.japanese}
                        </span>
                      </div>
                      <p className="text-sm text-slate-500 line-clamp-1 group-hover:text-slate-700">
                        대표: {pos.exampleChar} ({pos.exampleKanji})
                      </p>
                    </div>
                    <div className="w-10 h-10 rounded-xl bg-slate-100 flex items-center justify-center text-slate-600 font-serif text-lg font-black group-hover:bg-emerald-600 group-hover:text-white transition-colors duration-300">
                      {pos.exampleChar}
                    </div>
                  </div>
                ))}
              </div>

              {/* Right Side: Visual Simulator Panel */}
              <div className="glass rounded-3xl p-6 border border-stone-200 flex flex-col justify-between shadow-sm sticky top-28 h-fit min-h-[420px] bg-white">
                <div className="space-y-6">
                  <div className="text-center">
                    <span className="text-xs font-bold uppercase tracking-widest text-emerald-600 bg-emerald-50 px-3 py-1 rounded-full">
                      위치 시각화 가이드
                    </span>
                    <h3 className="text-2xl font-black mt-2 text-slate-900">{selectedPosition.name}</h3>
                  </div>

                  {/* SVG Hanger */}
                  <div className="py-4">
                    <PositionSvg pattern={selectedPosition.guidePattern} />
                  </div>

                  {/* Description Info */}
                  <div className="space-y-4">
                    <div className="bg-slate-50 p-4 rounded-xl border border-slate-100">
                      <h4 className="text-xs font-extrabold text-slate-400 mb-1">위치 설명</h4>
                      <p className="text-sm text-slate-700 leading-relaxed font-medium">
                        {selectedPosition.description}
                      </p>
                    </div>

                    <div className="bg-emerald-50/50 p-4 rounded-xl border border-emerald-100">
                      <h4 className="text-xs font-extrabold text-emerald-700 mb-1">구조 예시 ({selectedPosition.exampleKanji})</h4>
                      <p className="text-lg font-serif font-black text-slate-800 text-center py-1">
                        {selectedPosition.exampleKanjiDisplay}
                      </p>
                    </div>
                  </div>
                </div>

                <div className="text-center text-xs text-slate-400 mt-6 font-sans">
                  카드를 호버하거나 클릭하여 다른 위치도 구경해보세요.
                </div>
              </div>
            </div>

            {/* 2. Mobile Layout (lg 미만 화면) */}
            <div className="lg:hidden space-y-4">
              {/* Compact 7 Buttons Grid */}
              <div className="grid grid-cols-2 gap-2 bg-white/60 p-2 rounded-2xl border border-slate-200">
                {positionsData.map((pos) => {
                  const isSelected = selectedPosition.id === pos.id;
                  return (
                    <button
                      key={pos.id}
                      onClick={() => setSelectedPosition(pos)}
                      className={`py-4 px-3 text-center rounded-xl border transition-all ${
                        isSelected
                          ? "bg-emerald-600 text-white border-emerald-600 shadow-md scale-105"
                          : "bg-white hover:bg-slate-50 text-slate-700 border-slate-200"
                      }`}
                    >
                      <span className="text-3xl font-black font-sans tracking-tighter">
                        {pos.name}
                      </span>
                      <span className={`text-xl font-black font-sans ml-2 transition-colors ${
                        isSelected ? "text-emerald-100/90" : "text-slate-400"
                      }`}>
                        {pos.japanese}
                      </span>
                    </button>
                  );
                })}
              </div>

              {/* Compact Detail Panel */}
              <div className="glass rounded-2xl p-4 border border-stone-200 bg-white shadow-sm space-y-3">
                <div className="flex flex-col items-center justify-center text-center border-b border-slate-100 pb-3 space-y-2">
                  <span className="text-base font-bold uppercase tracking-widest text-emerald-600 bg-emerald-50 px-3.5 py-1 rounded-full font-sans">
                    {selectedPosition.japanese}
                  </span>
                  <h3 className="text-3xl font-black text-slate-900 mt-1">{selectedPosition.name}</h3>
                  <div className="text-lg font-extrabold text-slate-600 font-sans">
                    대표 부수: <span className="text-2xl font-serif font-black text-emerald-600">{selectedPosition.exampleChar}</span> ({selectedPosition.exampleKanji})
                  </div>
                </div>

                {/* 2. 시각화 그래픽 (단독으로 중앙 배치) */}
                <div className="flex flex-col items-center justify-center py-2">
                  <div className="w-24 h-24 bg-slate-50 rounded-2xl border border-slate-200 flex items-center justify-center p-2 shadow-inner">
                    <PositionSvg pattern={selectedPosition.guidePattern} className="w-full h-full" />
                  </div>
                </div>

                {/* 3. 구조예시 (시각화 그래픽 아래에 위치하며, 중앙 정렬 & 크기 2배) */}
                <div className="bg-slate-50 p-4 rounded-xl border border-slate-100 flex flex-col items-center justify-center text-center space-y-1">
                  <h4 className="text-base font-extrabold text-slate-400">구조 예시 ({selectedPosition.exampleKanji})</h4>
                  <p className="text-xl font-serif font-black text-slate-800 py-1">
                    {selectedPosition.exampleKanjiDisplay}
                  </p>
                </div>

                {/* 4. 위치설명 (중앙 정렬 & 크기 2배) */}
                <div className="bg-emerald-50/30 p-4 rounded-xl border border-emerald-100/50 flex flex-col items-center justify-center text-center space-y-1">
                  <h4 className="text-base font-extrabold text-emerald-700">위치 설명</h4>
                  <p className="text-sm md:text-base text-slate-700 leading-relaxed font-semibold">
                    {selectedPosition.description}
                  </p>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* ==================== PAGE 2: 필수 핵심 부수 50선 ==================== */}
        {activeTab === "core50" && (
          <div className="space-y-8 animate-fadeIn">
            {/* Filtering Navigation */}
            <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 bg-white/60 p-3 rounded-2xl border border-slate-200">
              <div className="flex flex-wrap items-center gap-1.5 w-full md:w-auto">
                <button
                  onClick={() => setFilter("all")}
                  className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all duration-300 ${
                    filter === "all" ? "bg-slate-900 text-white shadow-sm" : "hover:bg-slate-200 text-slate-600"
                  }`}
                >
                  전체 ({coreRadicalsData.length})
                </button>
                <button
                  onClick={() => setFilter("human")}
                  className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all duration-300 ${
                    filter === "human" ? "bg-amber-600 text-white shadow-sm" : "hover:bg-slate-200 text-slate-600"
                  }`}
                >
                  인간 / 신체
                </button>
                <button
                  onClick={() => setFilter("nature")}
                  className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all duration-300 ${
                    filter === "nature" ? "bg-blue-600 text-white shadow-sm" : "hover:bg-slate-200 text-slate-600"
                  }`}
                >
                  자연 / 환경
                </button>
                <button
                  onClick={() => setFilter("tool")}
                  className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all duration-300 ${
                    filter === "tool" ? "bg-indigo-600 text-white shadow-sm" : "hover:bg-slate-200 text-slate-600"
                  }`}
                >
                  도구 / 행동
                </button>
              </div>

              <div className="text-xs text-slate-500 font-semibold px-2 font-sans">
                각 부수를 클릭하면 상세 자원 설명을 확인하실 수 있습니다.
              </div>
            </div>

            {/* Radicals Grid */}
            <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
              {filteredRadicals.map((rad) => {
                const isSelected = activeRadicalDetail?.original === rad.original;
                return (
                  <div
                    key={rad.original}
                    onClick={() => setActiveRadicalDetail(isSelected ? null : rad)}
                    className={`glass p-4 rounded-2xl border text-center cursor-pointer transition-all duration-300 hover:shadow-md hover:-translate-y-0.5 ${
                      isSelected 
                        ? "border-emerald-600 bg-emerald-50/20 ring-2 ring-emerald-500/20" 
                        : "border-slate-200"
                    }`}
                  >
                    <div className="flex justify-between items-start mb-2">
                      <span className={`text-[10px] px-1.5 py-0.5 rounded font-bold uppercase tracking-wider font-sans ${
                        rad.category === "human" ? "bg-amber-100 text-amber-800" :
                        rad.category === "nature" ? "bg-blue-100 text-blue-800" : "bg-indigo-100 text-indigo-800"
                      }`}>
                        {rad.category === "human" ? "신체" : rad.category === "nature" ? "자연" : "도구"}
                      </span>
                      {rad.variant !== rad.original && (
                        <span className="text-xs font-bold text-slate-400 font-sans">변형 있음</span>
                      )}
                    </div>
                    
                    {/* Big Radical Char */}
                    <div className="text-4xl md:text-5xl font-serif font-black text-slate-900 my-2">
                      {rad.original}
                      {rad.variant !== rad.original && (
                        <span className="text-lg md:text-xl text-emerald-600 ml-1.5 font-bold font-serif">
                          ({rad.variant})
                        </span>
                      )}
                    </div>
                    
                    <div className="font-extrabold text-base md:text-lg text-slate-800 truncate mb-1">
                      {rad.name}
                    </div>
                    <div className="text-xs md:text-sm text-emerald-700 font-extrabold font-sans truncate mb-1 flex items-center justify-center gap-1.5 flex-wrap">
                      {rad.reading_on && (
                        <span 
                          onClick={(e) => {
                            e.stopPropagation();
                            speakJapanese(rad.reading_on.split(",")[0]);
                          }}
                          className="cursor-pointer hover:underline hover:text-emerald-950 inline-flex items-center"
                          title="음독 듣기"
                        >
                          음: {rad.reading_on.split(",")[0]}
                        </span>
                      )}
                      {rad.reading_on && rad.reading_kun && <span className="opacity-40">|</span>}
                      {rad.reading_kun && (
                        <span 
                          onClick={(e) => {
                            e.stopPropagation();
                            speakJapanese(rad.reading_kun.split(",")[0]);
                          }}
                          className="cursor-pointer hover:underline hover:text-emerald-950 inline-flex items-center"
                          title="훈독 듣기"
                        >
                          훈: {rad.reading_kun.split(",")[0]}
                        </span>
                      )}
                    </div>
                    <div className="text-sm text-slate-500 font-medium truncate">
                      {rad.meaning}
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Active Radical Detail Drawer/Modal */}
            {activeRadicalDetail && (
              <div className="glass bg-white border-2 border-emerald-500 rounded-3xl p-6 md:p-8 shadow-lg animate-fadeIn flex flex-col md:flex-row items-center md:items-start justify-between gap-6">
                <div className="flex flex-col md:flex-row items-center md:items-start gap-6 w-full">
                  {/* Big view */}
                  <div className="w-32 h-32 flex-shrink-0 rounded-2xl bg-emerald-50 border border-emerald-200 flex items-center justify-center text-7xl font-serif font-black text-emerald-700 shadow-sm">
                    {activeRadicalDetail.original}
                  </div>
                  
                  <div className="space-y-3 text-center md:text-left flex-1">
                    <div className="flex flex-wrap items-center justify-center md:justify-start gap-3">
                      <h3 className="text-3xl md:text-4xl font-black text-slate-900">{activeRadicalDetail.name}</h3>
                      <span className="text-sm font-bold bg-slate-100 text-slate-600 px-3 py-1 rounded-lg uppercase tracking-wider font-sans">
                        {activeRadicalDetail.category === "human" ? "인간 / 신체" :
                         activeRadicalDetail.category === "nature" ? "자연 / 환경" : "도구 / 행동"}
                      </span>
                    </div>
                    <p className="text-slate-800 font-extrabold text-xl md:text-2xl">
                      대표 뜻: <span className="text-emerald-600">{activeRadicalDetail.meaning}</span>
                    </p>
                    <div className="flex flex-wrap gap-4 text-sm md:text-lg font-bold text-slate-600 font-sans my-2 justify-center md:justify-start">
                      {activeRadicalDetail.reading_on && (
                        <span 
                          onClick={() => speakJapanese(activeRadicalDetail.reading_on)}
                          className="cursor-pointer hover:underline group inline-flex items-center gap-1"
                          title="음독 듣기"
                        >
                          일본어 음독:{" "}
                          <span className="bg-slate-100 group-hover:bg-emerald-50 px-2.5 py-1 rounded-xl text-slate-800 group-hover:text-emerald-700 font-black font-sans inline-flex items-center transition-colors">
                            {activeRadicalDetail.reading_on}
                          </span>
                        </span>
                      )}
                      {activeRadicalDetail.reading_kun && (
                        <span 
                          onClick={() => speakJapanese(activeRadicalDetail.reading_kun)}
                          className="cursor-pointer hover:underline group inline-flex items-center gap-1"
                          title="훈독 듣기"
                        >
                          일본어 훈독:{" "}
                          <span className="bg-slate-100 group-hover:bg-emerald-50 px-2.5 py-1 rounded-xl text-slate-800 group-hover:text-emerald-700 font-black font-sans inline-flex items-center transition-colors">
                            {activeRadicalDetail.reading_kun}
                          </span>
                        </span>
                      )}
                    </div>
                    <div className="text-base md:text-lg text-slate-600 space-y-2 leading-relaxed">
                      {activeRadicalDetail.variant !== activeRadicalDetail.original && (
                        <p>• 변형 꼴: <span className="font-bold text-slate-800 font-serif text-lg md:text-xl">{activeRadicalDetail.variant}</span> (한자가 다른 글자와 결합할 때 변형되는 모양)</p>
                      )}
                      <p>• 주요 특징: 이 부수가 들어가면 대체적으로 "{activeRadicalDetail.meaning}" 관련 개념을 묘사하는 한자가 됩니다.</p>
                    </div>
                  </div>
                </div>
                
                <button
                  onClick={() => setActiveRadicalDetail(null)}
                  className="bg-slate-100 hover:bg-slate-200 text-slate-700 px-6 py-3 rounded-2xl text-base font-black border border-slate-200 transition-colors w-full md:w-auto self-center md:self-start flex-shrink-0"
                >
                  닫기
                </button>
              </div>
            )}
          </div>
        )}

        {/* ==================== PAGE 3: 한자 조립/분해 ==================== */}
        {activeTab === "decomposer" && (
          <div className="space-y-8 animate-fadeIn">
            {/* Top Description */}
            <div className="glass rounded-3xl p-6 shadow-sm border border-stone-200">
              <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                <div>
                  <h2 className="text-xl font-bold text-slate-900 mb-1">한자 조립/분해 시각화 디렉토리</h2>
                  <p className="text-slate-600 text-sm md:text-base leading-relaxed">
                    한자는 부수와 다양한 뼈대 조각들이 수학 수식처럼 조립되어 하나의 글자를 이룹니다. 한자가 분해된 모습을 클릭해 보면서 그 조각들의 조립 스토리와 한자의 진짜 의미를 재미있게 학습해 보세요.
                  </p>
                </div>
                {/* Search Bar */}
                <div className="relative w-full md:w-64 flex-shrink-0">
                  <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <Search className="h-5 w-5 text-slate-400" />
                  </div>
                  <input
                    type="text"
                    placeholder="한자, 뜻, 음독 검색..."
                    value={decomposerSearchQuery}
                    onChange={(e) => setDecomposerSearchQuery(e.target.value)}
                    className="block w-full pl-10 pr-3 py-2 border border-slate-300 rounded-xl leading-5 bg-white/80 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm transition-all"
                  />
                </div>
              </div>
            </div>

            {/* Grade Filter Bar */}
            <div className="flex flex-wrap items-center gap-2 bg-white/60 p-2 rounded-2xl border border-slate-200">
              {["전체", "1학년", "2학년", "3학년", "4학년", "5학년", "6학년"].map(grade => (
                <button
                  key={grade}
                  onClick={() => setDecomposerGradeFilter(grade)}
                  className={`px-4 py-2 rounded-xl text-sm font-bold transition-all duration-300 ${
                    decomposerGradeFilter === grade
                      ? "bg-emerald-600 text-white shadow-sm"
                      : "hover:bg-slate-200 text-slate-600"
                  }`}
                >
                  {grade}
                </button>
              ))}
            </div>

            {/* Selector Grid (Scrollable) */}
            <div className="bg-white/60 p-4 rounded-2xl border border-slate-200 max-h-56 overflow-y-auto">
              {filteredDecomposerData.length > 0 ? (
                <div className="flex flex-wrap gap-2">
                  {filteredDecomposerData.map((data) => (
                    <button
                      key={data.kanji}
                      onClick={() => {
                        setSelectedDecomposerData(data);
                        setActiveComponentDetail(null);
                      }}
                      className={`w-14 h-14 rounded-2xl text-xl font-serif font-black transition-all duration-200 ${
                        selectedDecomposerData?.kanji === data.kanji 
                          ? "bg-slate-900 text-white shadow-lg scale-105" 
                          : "bg-white hover:bg-emerald-50 text-slate-700 border border-slate-200 hover:border-emerald-300"
                      }`}
                    >
                      {data.kanji}
                    </button>
                  ))}
                </div>
              ) : (
                <div className="text-center py-8 text-slate-500 font-medium">
                  조건에 맞는 한자가 없습니다.
                </div>
              )}
            </div>

            {/* Split Screen Layout */}
            {selectedDecomposerData && (
              <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
                {/* Left Panel: Completed Kanji Display */}
                <div className="lg:col-span-5 glass rounded-3xl p-8 border border-stone-200 bg-white flex flex-col justify-center items-center text-center shadow-sm relative overflow-hidden min-h-[300px]">
                  <div className="absolute top-4 left-4 bg-slate-100 text-slate-700 px-3 py-1 rounded-xl text-xs font-bold font-sans">
                    완성형
                  </div>
                  
                  {/* Kanji representation */}
                  <div className="text-9xl font-serif font-black text-slate-900 my-6 drop-shadow-sm select-none transition-transform duration-500 hover:scale-105">
                    {selectedDecomposerData.kanji}
                  </div>
                  
                  <div className="space-y-1">
                    <h3 className="text-2xl font-extrabold text-slate-900">
                      {selectedDecomposerData.meaning}
                    </h3>
                    <div className="text-sm font-semibold text-slate-500 font-sans flex items-center justify-center gap-1.5 flex-wrap">
                      {selectedDecomposerData.reading_on && (
                        <span 
                          onClick={() => speakJapanese(selectedDecomposerData.reading_on)}
                          className="cursor-pointer hover:underline hover:text-emerald-800 inline-flex items-center"
                          title="음독 듣기"
                        >
                          음: {selectedDecomposerData.reading_on}
                        </span>
                      )}
                      {selectedDecomposerData.reading_on && selectedDecomposerData.reading_kun && <span className="opacity-40">|</span>}
                      {selectedDecomposerData.reading_kun && (
                        <span 
                          onClick={() => speakJapanese(selectedDecomposerData.reading_kun)}
                          className="cursor-pointer hover:underline hover:text-emerald-800 inline-flex items-center"
                          title="훈독 듣기"
                        >
                          훈: {selectedDecomposerData.reading_kun}
                        </span>
                      )}
                    </div>
                  </div>
                </div>

                {/* Middle / Right Panel: Formula Assembly */}
                <div className="lg:col-span-7 flex flex-col justify-between gap-6">
                  
                  {/* Formula Section */}
                  <div className="glass rounded-3xl p-6 border border-stone-200 flex flex-col items-center justify-center gap-4 bg-white/40 min-h-[140px] shadow-sm">
                    <span className="text-xs font-bold uppercase tracking-widest text-slate-400">
                      조각 조립 수식
                    </span>
                    
                    <div className="flex flex-wrap items-center justify-center gap-3">
                      {/* 완성형 복기 */}
                      <div className="text-3xl font-serif font-black text-slate-800 bg-white shadow-sm border border-slate-200 w-14 h-14 rounded-2xl flex items-center justify-center">
                        {selectedDecomposerData.kanji}
                      </div>

                      <div className="text-2xl font-bold text-slate-400 font-sans">=</div>

                      {/* 분해 자소 버튼들 */}
                      {selectedDecomposerData.components && selectedDecomposerData.components.map((comp, idx) => (
                        <React.Fragment key={idx}>
                          {idx > 0 && <div className="text-2xl font-bold text-slate-400 font-sans">+</div>}
                          <button
                            onClick={() => setActiveComponentDetail(comp)}
                            className={`w-14 h-14 rounded-2xl text-2xl font-serif font-black transition-all duration-300 flex flex-col items-center justify-center shadow-sm relative group ${
                              activeComponentDetail?.char === comp.char
                                ? "bg-emerald-600 text-white scale-110 ring-4 ring-emerald-500/20"
                                : "bg-white hover:bg-emerald-50 text-slate-800 border border-slate-200"
                            }`}
                          >
                            {comp.char}
                            <span className="text-[9px] font-sans font-medium text-slate-400 group-hover:text-emerald-700 absolute bottom-1 truncate w-12 text-center pointer-events-none">
                              {activeComponentDetail?.char === comp.char ? "" : "클릭"}
                            </span>
                          </button>
                        </React.Fragment>
                      ))}
                    </div>
                  </div>

                  {/* Story / Resource Explanation Panel */}
                  <div className="glass rounded-3xl p-6 border border-stone-200 bg-white flex-1 flex flex-col justify-between shadow-sm min-h-[180px]">
                    <div>
                      <h4 className="text-sm font-bold text-slate-400 mb-2 flex items-center gap-1.5">
                        <span className="w-2 h-2 rounded-full bg-emerald-500"></span>
                        이야기가 있는 한자 해설
                      </h4>
                      <p className="text-slate-700 leading-relaxed font-semibold text-base">
                        {selectedDecomposerData.story}
                      </p>
                    </div>

                    {/* Component Detail Callout */}
                    {activeComponentDetail ? (
                      <div className="mt-4 p-4 bg-emerald-50 border border-emerald-100 rounded-2xl animate-fadeIn">
                        <div className="flex items-center gap-2 mb-1">
                          <span className="text-xl font-serif font-black text-emerald-800">{activeComponentDetail.char}</span>
                          <span className="text-xs font-bold bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded font-sans">
                            {activeComponentDetail.role}
                          </span>
                        </div>
                        <p className="text-sm text-slate-600 font-medium">
                          {activeComponentDetail.desc}
                        </p>
                      </div>
                    ) : (
                      <div className="mt-4 p-4 bg-slate-50 border border-slate-100 rounded-2xl flex items-center justify-center text-xs text-slate-400 font-medium font-sans">
                        수식에서 분해 조각을 클릭하면 각 조각의 핵심 자원 정보를 학습할 수 있습니다.
                      </div>
                    )}
                  </div>
                </div>
              </div>
            )}

            {/* Example Words Section (실전 활용 어휘) */}
            {selectedDecomposerData?.example_words && selectedDecomposerData.example_words.length > 0 && (
              <div className="glass rounded-3xl p-6 md:p-8 border border-stone-200 bg-white shadow-sm mt-8 space-y-6 animate-fadeIn">
                <div>
                  <h4 className="text-lg font-black text-slate-900 mb-1 flex items-center gap-2">
                    <span className="w-2.5 h-2.5 rounded-full bg-emerald-600 animate-pulse"></span>
                    실전 활용 어휘 ({selectedDecomposerData.kanji})
                  </h4>
                  <p className="text-slate-500 text-sm font-medium font-sans">
                    해당 한자가 포함된 실전 어휘들의 쓰임새와 단어 구성 한자의 개별 자원을 학습해 보세요.
                  </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  {selectedDecomposerData.example_words.map((wordObj, wIdx) => (
                    <div key={wIdx} className="bg-slate-50 hover:bg-emerald-50/20 border border-slate-200/80 hover:border-emerald-500/30 p-5 rounded-2xl transition-all duration-300 flex flex-col justify-between space-y-4 shadow-sm group">
                      <div className="space-y-3">
                        <div className="flex justify-between items-baseline">
                          <span className="text-2xl font-serif font-black text-slate-950 group-hover:text-emerald-700 transition-colors duration-300">
                            {wordObj.word}
                          </span>
                          <span 
                            onClick={(e) => {
                              e.stopPropagation();
                              speakJapanese(wordObj.reading);
                            }}
                            className="text-sm font-bold text-emerald-700 bg-emerald-50 hover:bg-emerald-100 cursor-pointer px-2 py-0.5 rounded-lg font-sans transition-colors"
                            title="발음 듣기"
                          >
                            {wordObj.reading}
                          </span>
                        </div>
                        <div className="text-base font-black text-slate-800">
                          뜻: <span className="text-emerald-700 font-extrabold">{wordObj.meaning}</span>
                        </div>
                        <p className="text-xs text-slate-500 font-semibold leading-relaxed font-sans">
                          {wordObj.description}
                        </p>
                      </div>

                      {/* 단어 구성 한자 개별 해설 */}
                      {wordObj.kanji_explanations && (
                        <div className="border-t border-slate-200/60 pt-3 space-y-2">
                          <div className="text-[10px] font-bold text-slate-400 font-sans uppercase tracking-wider">
                            글자별 낱자 구성 분석
                          </div>
                          <div className="space-y-1.5">
                            {wordObj.kanji_explanations.map((ex, exIdx) => (
                              <div key={exIdx} className="text-xs text-slate-600 bg-white/80 p-2 rounded-xl border border-slate-100 flex gap-3 items-center">
                                <span className="font-serif font-black text-slate-900 bg-slate-100 w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0 text-center text-xl shadow-sm">
                                  {ex.kanji}
                                </span>
                                <span className="font-semibold leading-relaxed">
                                  {ex.explanation}
                                </span>
                              </div>
                            ))}
                          </div>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        {/* ==================== PAGE 4: 퀴즈 미니 게임 ==================== */}
        {activeTab === "quiz" && (
          <div className="space-y-8 animate-fadeIn max-w-2xl mx-auto">
            {!quizStarted ? (
              /* 시작 화면 */
              <div className="glass rounded-3xl p-8 border border-stone-200 bg-white text-center space-y-6 shadow-sm">
                <div className="w-20 h-20 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto shadow-inner">
                  <Trophy className="w-10 h-10 animate-bounce" />
                </div>
                <div className="space-y-2">
                  <h2 className="text-2xl md:text-3xl font-black text-slate-900">부수 매칭 퀴즈 미니 게임</h2>
                  <p className="text-slate-500 max-w-md mx-auto text-sm md:text-base leading-relaxed">
                    오늘 배운 부수 지식을 점검해보세요! 필수 핵심 부수 50선 리스트에서 랜덤하게 5문제의 4지선다 퀴즈가 만들어집니다.
                  </p>
                </div>
                <button
                  onClick={generateQuiz}
                  className="bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold px-8 py-3 rounded-2xl shadow-md transition-all duration-300 scale-105 hover:scale-110 flex items-center gap-2 mx-auto"
                >
                  퀴즈 시작하기
                  <ChevronRight className="w-5 h-5" />
                </button>
              </div>
            ) : showScore ? (
              /* 결과 화면 */
              <div className="glass rounded-3xl p-8 border border-stone-200 bg-white text-center space-y-6 shadow-sm">
                <div className="w-20 h-20 bg-amber-100 text-amber-600 rounded-full flex items-center justify-center mx-auto shadow-inner">
                  <Trophy className="w-10 h-10" />
                </div>
                <div className="space-y-2">
                  <h3 className="text-3xl font-black text-slate-900">퀴즈 결과</h3>
                  <p className="text-slate-500 text-sm md:text-base">
                    5문제 중 총 <strong className="text-2xl text-emerald-600 font-sans">{score}</strong>문제를 맞추셨습니다!
                  </p>
                </div>
                
                {/* 점수별 격려 문구 */}
                <div className="bg-slate-50 p-4 rounded-xl border border-slate-100 max-w-sm mx-auto text-sm text-slate-600 font-medium">
                  {score === 5 && "🥇 완벽해요! 부수 마스터이십니다!"}
                  {score === 4 && "🥈 훌륭한 실력이에요! 한 문제만 더 맞췄으면 만점이네요!"}
                  {score >= 2 && score <= 3 && "🥉 준수해요! 틀린 부수를 복습하면 더 잘할 수 있어요!"}
                  {score <= 1 && "💡 부수 50선 카드를 천천히 읽어보고 다시 도전해 보세요!"}
                </div>

                <div className="flex justify-center gap-3">
                  <button
                    onClick={generateQuiz}
                    className="bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold px-6 py-2.5 rounded-xl transition-all flex items-center gap-2"
                  >
                    <RefreshCw className="w-4 h-4" />
                    다시 풀기
                  </button>
                  <button
                    onClick={() => setQuizStarted(false)}
                    className="bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200 font-extrabold px-6 py-2.5 rounded-xl transition-all"
                  >
                    퀴즈 홈으로
                  </button>
                </div>
              </div>
            ) : (
              /* 진행 화면 */
              <div className="space-y-6">
                {/* Progress bar */}
                <div className="flex justify-between items-center text-xs font-bold text-slate-400">
                  <span className="font-sans">QUESTION {currentQuestionIndex + 1} / {quizQuestions.length}</span>
                  <span className="font-sans">SCORE: {score}</span>
                </div>
                <div className="w-full bg-slate-200 h-2 rounded-full overflow-hidden">
                  <div 
                    className="bg-emerald-500 h-2 transition-all duration-300"
                    style={{ width: `${((currentQuestionIndex + 1) / quizQuestions.length) * 100}%` }}
                  ></div>
                </div>

                {/* Question Card */}
                <div className="glass rounded-3xl p-6 md:p-8 border border-stone-200 bg-white space-y-6 shadow-sm">
                  <h3 className="text-xl md:text-2xl font-black text-slate-900 leading-snug">
                    {quizQuestions[currentQuestionIndex].question}
                  </h3>

                  {/* Choice Grid */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    {quizQuestions[currentQuestionIndex].choices.map((choice) => {
                      const isSelected = selectedAnswer === choice;
                      const isCorrect = choice === quizQuestions[currentQuestionIndex].answer;
                      
                      let buttonClass = "bg-white hover:bg-slate-50 border-slate-200 text-slate-800";
                      
                      if (isAnswered) {
                        if (isCorrect) {
                          buttonClass = "bg-emerald-50 border-emerald-500 text-emerald-800 ring-2 ring-emerald-500/20";
                        } else if (isSelected) {
                          buttonClass = "bg-red-50 border-red-500 text-red-800 ring-2 ring-red-500/20";
                        } else {
                          buttonClass = "bg-white border-slate-100 text-slate-400 opacity-60";
                        }
                      } else {
                        if (isSelected) {
                          buttonClass = "bg-slate-100 border-slate-600 text-slate-900";
                        }
                      }

                      return (
                        <button
                          key={choice}
                          onClick={() => handleAnswerClick(choice)}
                          disabled={isAnswered}
                          className={`w-full text-left p-4 rounded-xl border-2 font-semibold transition-all duration-300 flex items-center justify-between text-sm md:text-base ${buttonClass}`}
                        >
                          <span>{choice}</span>
                          {isAnswered && isCorrect && <CheckCircle className="w-5 h-5 text-emerald-600 flex-shrink-0" />}
                          {isAnswered && isSelected && !isCorrect && <XCircle className="w-5 h-5 text-red-600 flex-shrink-0" />}
                        </button>
                      );
                    })}
                  </div>

                  {/* Next Step / Explanation */}
                  {isAnswered && (
                    <div className="space-y-4 animate-fadeIn">
                      <div className="bg-slate-50 border border-slate-100 p-4 rounded-2xl flex items-start gap-3">
                        <Info className="w-5 h-5 text-emerald-600 mt-0.5 flex-shrink-0" />
                        <div className="text-xs text-slate-500 space-y-1">
                          <p className="font-extrabold text-slate-700 text-sm">부수 도우미 팁</p>
                          <p>
                            이 문제의 정답은 <strong className="text-slate-800 font-serif font-black">"{quizQuestions[currentQuestionIndex].rawRadical.original}"</strong> 부수이며, 명칭은 <strong className="text-slate-800 font-extrabold">"{quizQuestions[currentQuestionIndex].rawRadical.name}"</strong>입니다.
                          </p>
                          <p>
                            이 부수는 대개 <strong className="text-slate-800 font-extrabold">"{quizQuestions[currentQuestionIndex].rawRadical.meaning}"</strong>(와)과 깊은 조립 연관성을 지닙니다.
                          </p>
                        </div>
                      </div>

                      <button
                        onClick={handleNextQuestion}
                        className="w-full bg-slate-900 hover:bg-slate-800 text-white font-extrabold py-3 rounded-xl shadow-sm transition-colors text-sm md:text-base"
                      >
                        {currentQuestionIndex + 1 < quizQuestions.length ? "다음 문제로" : "결과 확인하기"}
                      </button>
                    </div>
                  )}
                </div>
              </div>
            )}
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="text-center py-8 text-xs text-slate-400 font-sans border-t border-slate-200 mt-12 bg-white/40">
        © 2026 Zen Kanji Master. Built with React & Tailwind CSS. All rights reserved.
      </footer>
    </div>
  );
}
