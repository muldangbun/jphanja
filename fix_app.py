import sys

with open('radical/src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

target = """                      {activeRadicalDetail.reading_kun && (
                        <span 

                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  {kanjiDecomposerData[selectedDecomposerIndex].example_words.map((wordObj, wIdx) => ("""

replacement = """                      {activeRadicalDetail.reading_kun && (
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
                  {selectedDecomposerData.example_words.map((wordObj, wIdx) => ("""

if target in content:
    content = content.replace(target, replacement)
    with open('radical/src/App.jsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed App.jsx")
else:
    print("Target not found. Let's dump part of the file to see why.")
    print(repr(content[content.find('{activeRadicalDetail.reading_kun && ('):content.find('{activeRadicalDetail.reading_kun && (') + 200]))
