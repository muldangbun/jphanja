
        let KANJI_DATA = [];

        // 전역 로마자-가나 변환 맵 (백스페이스 처리에서도 참조)
        const ROMAJI_MAP = {
            'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
            'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
            'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
            'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
            'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
            'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
            'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
            'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
            'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
            'wa': 'わ', 'wo': 'を', 'nn': 'ん',
            'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
            'za': 'ざ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
            'da': 'だ', 'di': 'ぢ', 'du': 'づ', 'de': 'で', 'do': 'ど',
            'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
            'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
            'sha': 'しゃ', 'shu': 'しゅ', 'sho': 'しょ',
            'cha': 'ちゃ', 'chu': 'ちゅ', 'cho': 'ちょ',
            'kya': 'きゃ', 'kyu': 'きゅ', 'kyo': 'きょ',
            'nya': 'にゃ', 'nyu': 'にゅ', 'nyo': 'にょ',
            'hya': 'ひゃ', 'hyu': 'ひゅ', 'hyo': 'ひょ',
            'mya': 'みゃ', 'myu': 'みゅ', 'myo': 'みょ',
            'rya': 'りゃ', 'ryu': 'りゅ', 'ryo': 'りょ',
            'gya': 'ぎゃ', 'gyu': 'ぎゅ', 'gyo': 'ぎょ',
            'bya': 'びゃ', 'byu': 'びゅ', 'byo': 'びょ',
            'pya': 'ぴゃ', 'pyu': 'ぴゅ', 'pyo': 'ぴょ',
            'ja': 'じゃ', 'ju': 'じゅ', 'jo': 'じょ',
            'si': 'し', 'ti': 'ち', 'tu': 'つ', 'zi': 'じ', 'hu': 'ふ'
        };

        const romajiToKana = (text) => {
            let res = ""; let i = 0;
            while (i < text.length) {
                let found = false;
                if (i + 2 < text.length) {
                    let sub = text.substring(i, i + 3);
                    if (ROMAJI_MAP[sub]) { res += ROMAJI_MAP[sub]; i += 3; found = true; }
                }
                if (!found && i + 1 < text.length) {
                    let sub = text.substring(i, i + 2);
                    if (ROMAJI_MAP[sub]) {
                        res += ROMAJI_MAP[sub]; i += 2; found = true;
                    }
                    else if (sub[0] === sub[1] && !'aeiou'.includes(sub[0]) && sub[0] !== 'n') {
                        res += 'っ'; i += 1; found = true;
                    }
                }
                if (!found) {
                    let sub = text.substring(i, i + 1);
                    if (ROMAJI_MAP[sub]) { res += ROMAJI_MAP[sub]; i += 1; found = true; }
                    else if (sub === 'n' && i + 1 < text.length && !'aeiouy'.includes(text[i + 1])) {
                        res += 'ん'; i += 1; found = true;
                    }
                    else { res += sub; i += 1; }
                }
            }
            return res;
        };

        const hiraganaToKatakana = (text) => text.replace(/[ぁ-ん]/g, (s) => String.fromCharCode(s.charCodeAt(0) + 0x60));

        const normalizeText = (str) => {
            if (!str) return "";
            return str
                .replace(/[^\u3040-\u309F\u30A0-\u30FF]/g, '') // 히라가나, 가타카나만 남김
                .replace(/は/g, 'わ').replace(/を/g, 'お').replace(/へ/g, 'え') // 입으로 소리나는 대로 (조사 처리)
                .replace(/っ/g, 'つ') // 작은 つ 처리
                .replace(/ゃ/g, 'や').replace(/ゅ/g, 'ゆ').replace(/ょ/g, 'よ'); // 요음 처리
        };

        const state = {
            currentIndex: 0,
            phase: 'ONYOMI',
            currentKanji: null,
            currentExample: null,
            currentExampleIndex: 0,
            currentSentence: null,
            rawInput: "",
            isStoryMode: false,
            learningMode: 'KANJI',
            showFurigana: true,
            isAudiobookMode: false,
            isComplete: false,
            isFinish: false,
            isLocked: false,
            currentStoryName: ""
        };

        // Audio & State Management
        let audioCtx = null;
        let audioBufferCache = {};
        let currentAudio = null;
        let currentSource = null;
        let audiobookTimeout = null;
        let audiobookSessionId = 0;
        function initAudioContext() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
        }

        async function loadAudioBuffer(index) {
            // Already in cache?
            if (audioBufferCache[index]) return audioBufferCache[index];

            // If loading a new story, we might want to clear old cache if it gets too large,
            // but for a single story it's usually fine.
            const storyFolder = state.currentStoryName || 'story';
            const audioPath = `audio/${storyFolder}/${index}.mp3`;
            try {
                const response = await fetch(audioPath);
                if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
                const arrayBuffer = await response.arrayBuffer();
                
                // Use the newer promise-based decodeAudioData
                const audioBuffer = await new Promise((resolve, reject) => {
                    audioCtx.decodeAudioData(arrayBuffer, resolve, reject);
                });
                
                audioBufferCache[index] = audioBuffer;
                return audioBuffer;
            } catch (e) {
                console.warn(`Failed to load/decode audio buffer for ${index}:`, e);
                return null;
            }
        }

        function playClickSound() {
            try {
                initAudioContext();

                // Haptic feedback (Vibration)
                if (navigator.vibrate) {
                    navigator.vibrate(10);
                }

                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(800, audioCtx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(100, audioCtx.currentTime + 0.1);
                gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
                osc.connect(gain); gain.connect(audioCtx.destination);
                osc.start(); osc.stop(audioCtx.currentTime + 0.1);
            } catch (e) {
                console.warn("Audio/Haptic failed:", e);
            }
        }

        // Global unlock for Web Audio (Mobile Policy)
        const unlockAudio = () => {
            initAudioContext();
            document.removeEventListener('click', unlockAudio);
            document.removeEventListener('touchstart', unlockAudio);
        };
        document.addEventListener('click', unlockAudio);
        document.addEventListener('touchstart', unlockAudio);

        const els = {
            container: document.getElementById('game-container'),
            kanjiMain: document.getElementById('kanji-main'),
            meaningHint: document.getElementById('meaning-hint'),
            phaseTag: document.getElementById('phase-tag'),
            input: document.getElementById('typing-input'),
            kanaHint: document.getElementById('kana-hint'),
            currentIndexDisplay: document.getElementById('current-index'),
            totalCountDisplay: document.getElementById('total-count'),
            kanjiView: document.getElementById('kanji-view'),
            wordView: document.getElementById('word-view'),
            sentenceView: document.getElementById('sentence-view'),
            sentenceDisplay: document.getElementById('sentence-display'),
            sentenceMeaning: document.getElementById('sentence-meaning'),
            okBadge: document.getElementById('ok-badge'),
            wordDisplay: document.getElementById('word-display'),
            wordKana: document.getElementById('word-kana'),
            wordMeaning: document.getElementById('word-meaning'),
            kanjiSentencesView: document.getElementById('kanji-sentences-view'),
            sentencesContainer: document.getElementById('sentences-container'),
            inputSection: document.querySelector('.input-section'),
            romajiGuide: document.getElementById('romaji-guide'),
            card: document.getElementById('card'),
            btnKanji: document.getElementById('play-kanji'),
            btnWord: document.getElementById('play-word'),
            btnSentence: document.getElementById('play-sentence'),
            slider: document.getElementById('progress-slider'),
            furiganaControls: document.getElementById('furigana-controls'),
            furiganaSwitch: document.getElementById('furigana-switch'),
            audiobookSwitch: document.getElementById('audiobook-switch'),
            finishDialog: document.getElementById('finish-dialog'),
            grammarBtn: document.getElementById('grammar-btn'),
            grammarModalOverlay: document.getElementById('grammar-modal-overlay'),
            grammarModal: document.getElementById('grammar-modal'),
            grammarContent: document.getElementById('grammar-content'),
            keyboard: document.getElementById('virtual-keyboard'),
            examplesModalOverlay: document.getElementById('examples-modal-overlay'),
            examplesModal: document.getElementById('examples-modal'),
            examplesContent: document.getElementById('examples-content'),
            showExamplesBtn: document.getElementById('show-examples-btn')
        };



        const speakText = async (text) => {
            return new Promise(async (resolve) => {
                // Stop existing audio/TTS
                stopAudio();
                initAudioContext();

                // 1. Story Mode: Use Web Audio API Buffer (Best for mobile gapless)
                if (state.phase === 'STORY') {
                    const indexToPlay = state.currentIndex;
                    const buffer = await loadAudioBuffer(indexToPlay);
                    
                    // Safety check: has the user moved to another sentence while we were loading?
                    if (indexToPlay !== state.currentIndex || state.phase !== 'STORY') {
                        resolve();
                        return;
                    }

                    if (buffer) {
                        try {
                            const source = audioCtx.createBufferSource();
                            source.buffer = buffer;
                            source.connect(audioCtx.destination);
                            currentSource = source;
                            source.onended = () => {
                                if (currentSource === source) currentSource = null;
                                resolve();
                            };
                            source.start(0);
                        } catch (err) {
                            console.warn("Buffer playback failed:", err);
                            playTTS(text, resolve);
                        }
                    } else {
                        // Fallback to TTS if buffer loading fails
                        playTTS(text, resolve);
                    }
                } else {
                    // 2. Other Modes: Use browser TTS
                    playTTS(text, resolve);
                }
            });
        };

        const playTTS = (text, resolve) => {
            if (!window.speechSynthesis) {
                resolve();
                return;
            }
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'ja-JP';
            utterance.rate = 1.0;

            const voices = window.speechSynthesis.getVoices();
            const googleVoice = voices.find(v => v.name.includes('Google') && v.lang.startsWith('ja'));
            const jaVoice = googleVoice || voices.find(v => v.lang.startsWith('ja'));

            if (jaVoice) utterance.voice = jaVoice;

            utterance.onend = () => resolve();
            utterance.onerror = () => resolve();

            window.speechSynthesis.speak(utterance);

            // TTS가 가끔 onend를 호출하지 않는 경우를 대비한 안전 장치
            setTimeout(() => resolve(), text.length * 500 + 2000);
        };

        function getRomajiHint(index = 0) {
            const current = state.currentKanji;
            if (!current) return "hint";
            if (state.phase === 'ONYOMI' && current.romaji_on) return current.romaji_on[index] || current.romaji_on[0];
            if (state.phase === 'KUNYOMI' && current.romaji_kun) return current.romaji_kun[index] || current.romaji_kun[0];
            if (state.phase === 'EXAMPLE' && state.currentExample && state.currentExample.romaji) return state.currentExample.romaji;
            return "hint";
        }

        async function selectMode(grade, mode) {
            playClickSound();
            if (grade > 4) {
                alert(`${grade}학년 데이터는 서비스 준비 중입니다!`);
                return;
            }
            state.isStoryMode = false;
            state.isAudiobookMode = false;
            if (els.audiobookSwitch) els.audiobookSwitch.checked = false;
            els.card.classList.remove('audiobook-active');
            if (currentAudio) {
                currentAudio.pause();
                currentAudio = null;
            }
            if (currentSource) {
                try { currentSource.stop(); } catch (e) { }
                currentSource = null;
            }
            window.speechSynthesis.cancel();
            audiobookSessionId++; // Increment to stop any active loop
            if (audiobookTimeout) clearTimeout(audiobookTimeout);

            state.learningMode = mode;
            els.container.classList.remove('story-mode');
            els.furiganaControls.classList.add('hidden');
            state.currentIndex = 0;

            try {
                const response = await fetch(`data/kanji/kanji_grade${grade}.json`);
                KANJI_DATA = await response.json();

                document.title = `Zen Kanji Master - Grade ${grade}`;
                document.getElementById('start-screen').classList.add('hidden');
                document.getElementById('game-container').classList.remove('hidden');

                els.totalCountDisplay.innerText = KANJI_DATA.length;
                els.slider.max = KANJI_DATA.length - 1;
                loadKanji();
                els.input.focus();
            } catch (err) {
                console.error("Data load failed:", err);
                alert("한자 데이터를 불러오지 못했습니다. 서버 환경에서 실행해 주세요.");
            }
        }

        async function openSceneModal(fileName) {
            playClickSound();
            try {
                const response = await fetch(fileName);
                const data = await response.json();
                
                const listContainer = document.getElementById('scenario-list');
                listContainer.innerHTML = '';
                
                data.scenarios.forEach(scene => {
                    const btn = document.createElement('button');
                    btn.className = 'grade-btn';
                    btn.style.textAlign = 'left';
                    btn.style.height = 'auto';
                    btn.style.padding = '15px';
                    btn.innerHTML = `
                        <div style="font-weight:600; margin-bottom:5px; color:white;">${scene.title}</div>
                        <div style="font-size:0.9rem; color:#aaa; white-space:normal;">${scene.description}</div>
                    `;
                    btn.onclick = () => selectScene(scene, fileName);
                    listContainer.appendChild(btn);
                });
                
                document.getElementById('scenario-modal').classList.remove('hidden');
            } catch (err) {
                console.error("Failed to load scenes:", err);
                alert("데이터를 불러오지 못했습니다.");
            }
        }

        function selectScene(scene, fileName) {
            playClickSound();
            document.getElementById('scenario-modal').classList.add('hidden');
            initAudioContext();
            state.isStoryMode = true;
            state.learningMode = 'SCENE';
            state.currentStoryName = scene.id;
            els.container.classList.add('story-mode');
            els.furiganaControls.classList.remove('hidden');
            state.currentIndex = 0;
            
            audioBufferCache = {};

            // Convert dialogue into KANJI_DATA format
            KANJI_DATA = scene.dialogue.map((d, index) => ({
                ...d,
                grammar: d.grammar
            }));

            document.getElementById('start-screen').classList.add('hidden');
            document.getElementById('game-container').classList.remove('hidden');

            els.totalCountDisplay.innerText = KANJI_DATA.length;
            els.slider.max = KANJI_DATA.length - 1;
            loadKanji();
            els.input.focus();

            KANJI_DATA.forEach((_, idx) => loadAudioBuffer(idx));
        }

        async function selectStory(fileName) {
            playClickSound();
            initAudioContext();
            state.isStoryMode = true;
            state.learningMode = 'STORY';
            // Extract story name from file name (e.g. 'kaninotokoya.JSON' -> 'kaninotokoya')
            state.currentStoryName = fileName.split('/').pop().replace(/\.[^/.]+$/, "");
            els.container.classList.add('story-mode');
            els.furiganaControls.classList.remove('hidden');
            state.currentIndex = 0;
            
            // Clear buffer cache when starting a new story
            audioBufferCache = {};

            try {
                const response = await fetch(fileName);
                KANJI_DATA = await response.json();

                document.getElementById('start-screen').classList.add('hidden');
                document.getElementById('game-container').classList.remove('hidden');

                els.totalCountDisplay.innerText = KANJI_DATA.length;
                els.slider.max = KANJI_DATA.length - 1;
                loadKanji();
                els.input.focus();

                // Background preload audio files
                KANJI_DATA.forEach((_, idx) => loadAudioBuffer(idx));
            } catch (err) {
                console.error("Story load failed:", err);
                alert("동화 데이터를 불러오지 못했습니다.");
            }
        }

        function jumpToIndex(index, shouldSpeak = true) {
            playClickSound();
            if (index < 0 || index >= KANJI_DATA.length) return;
            state.currentIndex = index;
            loadKanji(shouldSpeak);
        }

        function nextKanji() {
            playClickSound();
            state.currentIndex = (state.currentIndex + 1) % KANJI_DATA.length;
            loadKanji();
        }

        function prevKanji() {
            playClickSound();
            state.currentIndex = (state.currentIndex - 1 + KANJI_DATA.length) % KANJI_DATA.length;
            loadKanji();
        }

        function manualJump() {
            const num = prompt(`이동할 번호를 입력하세요 (1-${KANJI_DATA.length}):`, state.currentIndex + 1);
            if (num) {
                const idx = parseInt(num) - 1;
                if (idx >= 0 && idx < KANJI_DATA.length) jumpToIndex(idx);
            }
        }

        function goHome() {
            playClickSound();
            state.isFinish = false;
            state.isAudiobookMode = false;
            if (els.audiobookSwitch) els.audiobookSwitch.checked = false;
            els.card.classList.remove('audiobook-active');
            if (els.finishDialog) els.finishDialog.classList.add('hidden');
            window.speechSynthesis.cancel();
            audiobookSessionId++; // Increment to stop any active loop
            document.getElementById('game-container').classList.add('hidden');
            document.getElementById('start-screen').classList.remove('hidden');
            // Reset state
            state.currentIndex = 0;
            state.isComplete = false;
        }

        async function init() {
            // Initial view is start screen
            initVirtualKeyboard();
        }

        function loadKanji(shouldSpeak = true) {
            state.isComplete = false;
            if (els.okBadge) els.okBadge.classList.add('hidden');
            if (state.isStoryMode) {
                state.currentSentence = KANJI_DATA[state.currentIndex];
                els.currentIndexDisplay.innerText = state.currentIndex + 1;
                els.slider.value = state.currentIndex;
                setPhase('STORY', shouldSpeak);
            } else {
                state.currentKanji = KANJI_DATA[state.currentIndex];
                els.kanjiMain.innerText = state.currentKanji.kanji;

                let hintText = state.currentKanji.meanings.join(', ');
                if (state.currentKanji.kor_meaning && state.currentKanji.kor_sound) {
                    hintText += ` <span class="kor-huneum">(${state.currentKanji.kor_meaning} ${state.currentKanji.kor_sound})</span>`;
                }
                els.meaningHint.innerHTML = hintText;

                els.currentIndexDisplay.innerText = state.currentIndex + 1;
                els.slider.value = state.currentIndex;

                if (state.learningMode === 'WORD') {
                    state.currentExampleIndex = 0;
                    setPhase('EXAMPLE', shouldSpeak);
                } else if (state.learningMode === 'SENTENCE') {
                    setPhase('KANJI_SENTENCES', shouldSpeak);
                } else {
                    // KANJI 모드 진입 시 예시 버튼 노출 여부 사전 세팅
                    if (state.currentKanji.examples && state.currentKanji.examples.length > 0) {
                        els.showExamplesBtn.classList.remove('hidden');
                    } else {
                        els.showExamplesBtn.classList.add('hidden');
                    }
                    setPhase('ONYOMI', shouldSpeak);
                }
            }
        }

        function alignFurigana(kanjiStr, kanaStr) {
            let result = [];
            const isKanji = (c) => /[\u4E00-\u9FAF\u3005]/.test(c);
            let blocks = [];
            let currentBlock = "";
            if (kanjiStr.length === 0) return [];
            let currentIsKanji = isKanji(kanjiStr[0]);

            for (let c of kanjiStr) {
                if (isKanji(c) === currentIsKanji) {
                    currentBlock += c;
                } else {
                    blocks.push({ text: currentBlock, isKanji: currentIsKanji });
                    currentIsKanji = isKanji(c);
                    currentBlock = c;
                }
            }
            if (currentBlock) blocks.push({ text: currentBlock, isKanji: currentIsKanji });

            let kStrIdx = 0;
            const clean = (s) => s.replace(/[ \f\n\r\t\v\u2028\u2029、。,.!?？！]/g, '');

            for (let i = 0; i < blocks.length; i++) {
                let block = blocks[i];
                if (!block.isKanji) {
                    // 비한자 블록(히라가나 등)이 가나 문자열의 어디에 있는지 찾음
                    // 공백이나 문장부호 차이를 무시하기 위해 검색 로직 강화
                    let target = clean(block.text);
                    let foundIdx = -1;

                    if (target.length === 0) {
                        // 문장 부호만 있는 블록인 경우, 가장 가까운 문장 부호 위치를 찾음
                        foundIdx = kanaStr.split('').findIndex((c, idx) => idx >= kStrIdx && !isKanji(c) && clean(c) === "");
                    } else {
                        // 가나 문자가 포함된 경우, 해당 가나가 나타나는 위치를 찾음
                        for (let j = kStrIdx; j <= kanaStr.length - target.length; j++) {
                            if (clean(kanaStr.substring(j, j + block.text.length + 5)).startsWith(target)) {
                                foundIdx = j;
                                break;
                            }
                        }
                    }

                    if (foundIdx >= kStrIdx) {
                        if (result.length > 0 && result[result.length - 1].isKanji) {
                            result[result.length - 1].kana = kanaStr.substring(kStrIdx, foundIdx);
                        }
                        result.push({ text: block.text });
                        kStrIdx = foundIdx + block.text.length;
                        // 실제 kanaStr에서 해당 블록이 끝나는 지점을 정확히 맞추기 위해 보정
                        while (kStrIdx < kanaStr.length && clean(kanaStr[kStrIdx - 1]) === "" && clean(block.text).length > 0 && clean(kanaStr[kStrIdx]) === "") {
                            // 기호 처리 로직 보강 가능
                        }
                    } else {
                        // 매핑 실패 시 안전 장치
                        result.push({ text: block.text });
                    }
                } else {
                    result.push({ text: block.text, isKanji: true });
                    if (i === blocks.length - 1) {
                        result[result.length - 1].kana = kanaStr.substring(kStrIdx);
                    }
                }
            }
            return result;
        }

        function renderSentence() {
            if (!state.currentSentence) return;
            const kanji = state.currentSentence.kanji;
            const kana = state.currentSentence.kana;
            const romaji = state.currentSentence.romaji;
            const typed = els.input.value;

            const targetClean = normalizeText(kana);
            const typedClean = normalizeText(typed);

            let validCount = 0;
            while (validCount < typedClean.length && validCount < targetClean.length && typedClean[validCount] === targetClean[validCount]) {
                validCount++;
            }

            let storyHtml = "";
            const segments = alignFurigana(kanji, kana);

            // 1. 각 글자별로 요구되는 가나(타자) 수를 계산하여 배열에 저장
            const charKanaMapping = [];
            for (let seg of segments) {
                if (!seg.isKanji) {
                    for (let i = 0; i < seg.text.length; i++) {
                        const char = seg.text[i];
                        // normalizeText 결과가 없더라도 최소한 0으로 기록하여 인덱스 유지
                        const nLen = normalizeText(char).length;
                        charKanaMapping.push(nLen);
                    }
                } else {
                    const kanjiLen = seg.text.length;
                    const normalizedKana = normalizeText(seg.kana || "");
                    const kanaLen = normalizedKana.length;

                    if (kanaLen === 0 && kanjiLen > 0) {
                        // 가나 매핑에 실패한 경우(데이터 오류 등), 최소 1타는 치도록 방어 로직 추가
                        for (let i = 0; i < kanjiLen; i++) charKanaMapping.push(1);
                    } else {
                        let base = Math.floor(kanaLen / kanjiLen);
                        let remainder = kanaLen % kanjiLen;
                        for (let i = 0; i < kanjiLen; i++) {
                            charKanaMapping.push(base + (i < remainder ? 1 : 0));
                        }
                    }
                }
            }

            let charIndex = 0;
            let requiredKanaForNextChar = 0;

            for (let seg of segments) {
                let segHtml = "";
                for (let i = 0; i < seg.text.length; i++) {
                    // 현재 글자까지 도달하기 위해 필요한 누적 타자 수
                    requiredKanaForNextChar += charKanaMapping[charIndex];

                    // 내가 친 타자(validCount)가 누적 요구 타수보다 같거나 커야 글자가 밝혀짐
                    const isRevealed = validCount >= requiredKanaForNextChar;
                    const charClass = isRevealed ? "progress-highlight" : "char-remaining";
                    segHtml += `<span class="${charClass}">${seg.text[i]}</span>`;
                    charIndex++;
                }

                if (seg.isKanji && state.showFurigana && seg.kana) {
                    storyHtml += `<ruby>${segHtml}<rt class="ruby-text">${seg.kana}</rt></ruby>`;
                } else {
                    storyHtml += segHtml;
                }
            }

            let speakerHtml = "";
            if (state.currentSentence.speaker) {
                speakerHtml = `<div style="font-size:0.9rem; color:#aaa; margin-bottom:8px; font-weight:bold; display:flex; align-items:center; gap:5px;"><svg viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>${state.currentSentence.speaker}</div>`;
            }
            els.sentenceDisplay.innerHTML = speakerHtml + storyHtml;

            // 2. 로마자 가이드 하이라이트 계산
            // 기존: 가나 단위로 뭉쳐서 하이라이트 (so가 다 입력되어야 そ가 되면서 하이라이트)
            // 변경: 사용자가 입력한 raw 알파벳 단위로 즉시 하이라이트
            let romajiRevealCount = 0;
            const targetRomaji = romaji.toLowerCase();
            const currentRaw = (state.rawInput || "").toLowerCase();

            // 2-1. 가나 매핑 기반의 최소 하이라이트 범위 계산 (기존 로직 유지하여 완성된 부분 보장)
            let kanaBaseCount = 0;
            for (let i = 0; i <= romaji.length; i++) {
                const prefix = romaji.substring(0, i).replace(/[ \f\n\r\t\v\u2028\u2029]+/g, '');
                const generatedKana = romajiToKana(prefix);
                if (normalizeText(generatedKana).length >= validCount) {
                    kanaBaseCount = i;
                    while (kanaBaseCount < romaji.length && romaji[kanaBaseCount] === ' ') {
                        kanaBaseCount++;
                    }
                    break;
                }
            }

            // 2-2. 실제 입력한 알파벳(rawInput)과 비교하여 낱자 단위 하이라이트 범위 계산
            let rawMatchCount = 0;
            let rIdx = 0; // targetRomaji index
            let iIdx = 0; // currentRaw index

            while (rIdx < targetRomaji.length && iIdx < currentRaw.length) {
                if (targetRomaji[rIdx] === currentRaw[iIdx]) {
                    rIdx++;
                    iIdx++;
                    rawMatchCount = rIdx;
                } else if (targetRomaji[rIdx] === ' ') {
                    // 목표 로마자에 공백이 있는데 입력에는 없다면 공백을 건너뛰고 비교
                    rIdx++;
                    rawMatchCount = rIdx;
                } else {
                    break;
                }
            }

            // 두 방식 중 더 많이 진행된 쪽을 선택 (가나 스타일 차이 등으로 인한 누락 방지)
            romajiRevealCount = Math.max(kanaBaseCount, rawMatchCount);

            if (validCount === targetClean.length) {
                romajiRevealCount = romaji.length;
            }

            const rRevealed = romaji.substring(0, romajiRevealCount);
            const rRemaining = romaji.substring(romajiRevealCount);

            const romajiDisplay = `<span style="color: var(--accent-color); opacity: 1; font-weight: 800; border-bottom: 2px solid var(--accent-color);">${rRevealed}</span><span style="opacity: 0.4;">${rRemaining}</span>`;
            els.kanaHint.innerHTML = `<div style="font-size: 1.1rem; font-family: 'Outfit'; color: var(--text-dim); text-align: center;">${romajiDisplay}</div>`;
        }

        function isModalOpen() {
            return !els.grammarModal.classList.contains('hidden') || 
                   (els.examplesModal && !els.examplesModal.classList.contains('hidden'));
        }

        function openGrammarModal() {
            playClickSound();
            if (!state.currentSentence || !state.currentSentence.grammar) return;
            
            // 모바일 키보드 내림 최적화
            if (els.input) els.input.blur();

            const data = state.currentSentence.grammar;
            let html = '';

            if (data.points) {
                data.points.forEach(p => {
                    html += `
                        <div class="grammar-point">
                            <div class="grammar-point-title">${p.title}</div>
                            <ul class="grammar-point-desc">
                                ${p.desc.map(d => `<li>${d}</li>`).join('')}
                            </ul>
                        </div>
                    `;
                });
            }
            if (data.summary) {
                html += `<div class="grammar-summary">${data.summary}</div>`;
            }

            els.grammarContent.innerHTML = html;
            els.grammarModalOverlay.classList.remove('hidden');
            els.grammarModal.classList.remove('hidden');
        }

        function closeGrammarModal() {
            playClickSound();
            els.grammarModalOverlay.classList.add('hidden');
            els.grammarModal.classList.add('hidden');
            
            // 모바일 포커스 복원 최적화
            if (els.input) els.input.focus();
        }

        function openExamplesModal() {
            playClickSound();
            const current = state.currentKanji;
            if (!current || !current.examples || current.examples.length === 0) {
                alert("이 한자에는 예시 단어가 없습니다.");
                return;
            }

            // 모바일 키보드 내림 최적화
            if (els.input) els.input.blur();

            let html = '';
            current.examples.forEach(ex => {
                const word = ex.word;
                const match = word.match(/^(.*?)\s*\((.*?)\)$/);
                let wordText = word;
                let kanaText = '';
                if (match) {
                    wordText = match[1];
                    kanaText = match[2];
                }
                
                html += `
                    <div class="grammar-point">
                        <div class="grammar-point-title" style="display: flex; justify-content: space-between; align-items: center; gap: 10px;">
                            <span style="word-break: break-all;">${wordText} <span style="font-size: 0.95rem; color: var(--text-secondary); font-weight: normal; margin-left: 6px;">(${kanaText || word})</span></span>
                            <button class="audio-btn" onclick="event.stopPropagation(); speakText('${kanaText || wordText}')" title="발음 듣기" style="flex-shrink: 0;">🔊</button>
                        </div>
                        <ul class="grammar-point-desc" style="margin-top: 8px;">
                            <li>뜻: ${ex.meaning}</li>
                            <li>읽기: ${ex.romaji}</li>
                        </ul>
                    </div>
                `;
            });

            els.examplesContent.innerHTML = html;
            els.examplesModalOverlay.classList.remove('hidden');
            els.examplesModal.classList.remove('hidden');
        }

        function closeExamplesModal() {
            playClickSound();
            els.examplesModalOverlay.classList.add('hidden');
            els.examplesModal.classList.add('hidden');
            
            // 모바일 포커스 복원 최적화
            if (els.input) els.input.focus();
        }

        function setPhase(phase, shouldSpeak = true) {
            state.phase = phase; state.rawInput = ""; els.input.value = ""; els.kanaHint.innerText = "";
            const current = state.currentKanji;

            if (phase === 'STORY') {
                els.showExamplesBtn.classList.add('hidden');
                els.phaseTag.innerText = "Reading Practice (동화 읽기)";
                els.kanjiView.classList.add('hidden');
                els.wordView.classList.add('hidden');
                els.kanjiSentencesView.classList.add('hidden');
                els.sentenceView.classList.remove('hidden');
                els.sentenceMeaning.innerHTML = state.currentSentence.meaning;
                els.romajiGuide.innerText = "";
                if (state.currentSentence.grammar) {
                    els.grammarBtn.classList.remove('hidden');
                } else {
                    els.grammarBtn.classList.add('hidden');
                }
                renderSentence();
                if (state.isAudiobookMode) {
                    if (shouldSpeak) startAudiobookLoop();
                } else if (shouldSpeak) {
                    speakText(state.currentSentence.kana);
                }
            } else if (phase === 'ONYOMI') {
                els.sentenceView.classList.add('hidden');
                if (current && current.examples && current.examples.length > 0) {
                    els.showExamplesBtn.classList.remove('hidden');
                } else {
                    els.showExamplesBtn.classList.add('hidden');
                }
                els.phaseTag.innerText = "음독 (Onyomi)"; els.wordView.classList.add('hidden'); els.kanjiSentencesView.classList.add('hidden'); els.kanjiView.classList.remove('hidden'); if (els.inputSection) els.inputSection.classList.remove('hidden');
                els.romajiGuide.innerText = `(${getRomajiHint()})`;
                if (shouldSpeak) speakText(current.readings_on[0]);
            } else if (phase === 'KUNYOMI') {
                els.sentenceView.classList.add('hidden');
                if (current && current.examples && current.examples.length > 0) {
                    els.showExamplesBtn.classList.remove('hidden');
                } else {
                    els.showExamplesBtn.classList.add('hidden');
                }
                if (!current.readings_kun || current.readings_kun.length === 0) {
                    state.currentIndex++; if (state.currentIndex >= KANJI_DATA.length) { alert("모든 한자를 완료했습니다!"); state.currentIndex = 0; }
                    loadKanji(shouldSpeak);
                    return;
                }
                els.phaseTag.innerText = "훈독 (Kunyomi)"; els.wordView.classList.add('hidden'); els.kanjiSentencesView.classList.add('hidden'); els.kanjiView.classList.remove('hidden'); if (els.inputSection) els.inputSection.classList.remove('hidden');
                els.romajiGuide.innerText = `(${getRomajiHint()})`;
                if (shouldSpeak) speakText(current.readings_kun[0].replace(/\./g, ''));
            } else if (phase === 'KANJI_SENTENCES') {
                els.showExamplesBtn.classList.add('hidden');
                els.sentenceView.classList.add('hidden');
                els.wordView.classList.add('hidden');
                els.kanjiView.classList.add('hidden');
                if (els.inputSection) els.inputSection.classList.add('hidden');
                
                if (!current.sentences || current.sentences.length === 0) {
                    state.currentIndex++; if (state.currentIndex >= KANJI_DATA.length) { alert("모든 예문을 완료했습니다!"); state.currentIndex = 0; }
                    loadKanji(shouldSpeak);
                    return;
                }
                els.phaseTag.innerText = `예문 (Sentences)`;
                els.kanjiSentencesView.classList.remove('hidden');
                els.romajiGuide.innerText = "";
                renderKanjiSentences();
            } else if (phase === 'EXAMPLE') {
                els.showExamplesBtn.classList.add('hidden');
                els.sentenceView.classList.add('hidden');
                if (!current.examples || current.examples.length === 0) {
                    state.currentIndex++; if (state.currentIndex >= KANJI_DATA.length) { alert("모든 단어를 완료했습니다!"); state.currentIndex = 0; }
                    loadKanji(shouldSpeak);
                    return;
                }
                els.phaseTag.innerText = `예시 (Example ${state.currentExampleIndex + 1}/${current.examples.length})`; els.kanjiSentencesView.classList.add('hidden'); if (els.inputSection) els.inputSection.classList.remove('hidden');
                state.currentExample = current.examples[state.currentExampleIndex];
                
                const word = state.currentExample.word;
                const match = word.match(/^(.*?)\s*\((.*?)\)$/);
                if (match) {
                    els.wordDisplay.innerText = match[1];
                    els.wordKana.innerText = match[2];
                    els.wordKana.classList.remove('hidden');
                } else {
                    els.wordDisplay.innerText = word;
                    els.wordKana.innerText = '';
                    els.wordKana.classList.add('hidden');
                }
                
                els.wordMeaning.innerHTML = state.currentExample.meaning;
                els.kanjiView.classList.add('hidden'); els.wordView.classList.remove('hidden');
                els.romajiGuide.innerText = `(${getRomajiHint()})`;
                if (shouldSpeak) {
                    const match = state.currentExample.word.match(/\((.*?)\)/);
                    speakText(match ? match[1] : state.currentExample.word);
                }
            }
        }

        function playCurrent() {
            playClickSound();
            if (state.phase === 'STORY') {
                speakText(state.currentSentence.kana);
            } else if (state.phase === 'EXAMPLE') {
                const match = state.currentExample.word.match(/\((.*?)\)/);
                speakText(match ? match[1] : state.currentExample.word);
            } else {
                const text = state.phase === 'ONYOMI' ? state.currentKanji.readings_on[0] : state.currentKanji.readings_kun[0].replace(/\./g, '');
                speakText(text);
            }
        }

        function checkAnswer() {
            const typed = els.input.value;

            if (state.isStoryMode || state.learningMode === 'STORY') {
                const targetClean = normalizeText(state.currentSentence.kana);
                const typedClean = normalizeText(typed);

                // Debug logging to help identify mismatches
                console.log(`[Story Mode] Target: ${targetClean} | Typed: ${typedClean}`);

                renderSentence();

                if (typedClean === targetClean && targetClean.length > 0) {
                    state.isComplete = true;
                    els.okBadge.classList.remove('hidden');
                    console.log("[Story Mode] Complete! Waiting for Enter...");
                }
                return;
            }

            let targets = [];
            if (state.phase === 'ONYOMI') targets = state.currentKanji.readings_on;
            else if (state.phase === 'KUNYOMI') targets = state.currentKanji.readings_kun;
            else {
                const match = state.currentExample.word.match(/\((.*?)\)/);
                targets = match ? [match[1]] : [state.currentExample.word];
            }
            const cleanTargets = targets.map(t => t.replace(/\./g, ''));

            if (cleanTargets.some(t => t === typed)) { handleSuccess(); return; }

            if (state.rawInput.endsWith('n')) {
                let altKana = romajiToKana(state.rawInput.slice(0, -1)) + 'ん';
                if (state.phase === 'ONYOMI') altKana = hiraganaToKatakana(altKana);
                if (cleanTargets.some(t => t === altKana)) { handleSuccess(); return; }
            }

            const isAnyPrefix = cleanTargets.some(t => t.startsWith(typed));
            if (!isAnyPrefix && typed.length > 0) {
                const lastChar = state.rawInput[state.rawInput.length - 1];
                if (lastChar && !/[a-z]/.test(lastChar)) handleError();
            }
        }

        function handleSuccess() {
            if (state.isLocked) return;
            state.isLocked = true;

            els.card.classList.add('success-flash');
            els.input.classList.add('success-flash');
            setTimeout(() => {
                els.card.classList.remove('success-flash');
                els.input.classList.remove('success-flash');
            }, 400);

            setTimeout(() => {
                state.isLocked = false;
                if (state.isStoryMode || state.learningMode === 'STORY') {
                    state.currentIndex++;
                    if (state.currentIndex >= KANJI_DATA.length) {
                        state.isFinish = true;
                        els.finishDialog.classList.remove('hidden');
                        if (currentAudio) {
                            currentAudio.pause();
                            currentAudio = null;
                        }
                        window.speechSynthesis.cancel();
                    } else {
                        loadKanji();
                    }
                } else if (state.learningMode === 'KANJI') {
                    if (state.phase === 'ONYOMI') {
                        setPhase('KUNYOMI');
                    } else if (state.phase === 'KUNYOMI') {
                        state.currentIndex++; if (state.currentIndex >= KANJI_DATA.length) { alert("모든 한자를 완료했습니다!"); state.currentIndex = 0; }
                        loadKanji();
                    }
                } else if (state.learningMode === 'WORD') {
                    state.currentExampleIndex++;
                    if (state.currentKanji.examples && state.currentExampleIndex < state.currentKanji.examples.length) {
                        setPhase('EXAMPLE');
                    } else {
                        state.currentIndex++; if (state.currentIndex >= KANJI_DATA.length) { alert("모든 단어를 완료했습니다!"); state.currentIndex = 0; }
                        loadKanji();
                    }
                } else {
                    state.currentIndex++; if (state.currentIndex >= KANJI_DATA.length) { alert("모든 항목을 완료했습니다!"); state.currentIndex = 0; }
                    loadKanji();
                }

                // Clear input and keep focus
                state.rawInput = "";
                els.input.value = "";
                els.input.focus();
            }, 500);
        }
        function restartStory() {
            playClickSound();
            state.isFinish = false;
            els.finishDialog.classList.add('hidden');
            state.currentIndex = 0;
            loadKanji();
        }

        function handleError() {
            state.rawInput = "";
            els.card.classList.add('error-shake');
            els.input.classList.add('error-shake');
            setTimeout(() => {
                els.card.classList.remove('error-shake');
                els.input.classList.remove('error-shake');
            }, 400);
            els.input.value = ""; els.kanaHint.innerText = "";
        }

        function handleKey(e) {
            if (isModalOpen()) {
                if (e.key === 'Escape') {
                    e.preventDefault();
                    closeGrammarModal();
                    closeExamplesModal();
                } else {
                    e.preventDefault();
                }
                return;
            }

            if (e.key === 'Escape') {
                goHome();
                return;
            }
            if (state.isFinish) {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    restartStory();
                }
                return;
            }
            if (e.key === 'Backspace') return;
            if (state.isLocked) return;
            if (e.key === 'Enter') {
                e.preventDefault();
                if (state.isComplete) { handleSuccess(); return; }
                // In non-story mode, we might not need Enter, but we'll leave it for now
            }
            if (e.key === ' ' && state.isComplete) {
                e.preventDefault();
                state.rawInput = "";
                loadKanji();
                return;
            }
            if (e.key.length === 1 && /[a-zA-Z\s]/.test(e.key)) {
                if (state.isComplete) return; // Prevent typing more once complete
                e.preventDefault();
                state.rawInput += e.key.toLowerCase();
                const kana = romajiToKana(state.rawInput);
                let displayKana = kana; if (state.phase === 'ONYOMI') displayKana = hiraganaToKatakana(kana);
                els.input.value = displayKana; els.kanaHint.innerText = ""; // Guide is already there
                checkAnswer();
            }
        }

        function handleBackspace() {
            const raw = state.rawInput;
            if (raw.length === 0) return;
            if (raw.length >= 3 && ROMAJI_MAP[raw.slice(-3)]) {
                state.rawInput = raw.slice(0, -3);
            } else if (raw.length >= 2 && (ROMAJI_MAP[raw.slice(-2)] || raw.slice(-2) === 'nn')) {
                state.rawInput = raw.slice(0, -2);
            } else {
                state.rawInput = raw.slice(0, -1);
            }
            const kana = romajiToKana(state.rawInput);
            let disp = kana; if (state.phase === 'ONYOMI') disp = hiraganaToKatakana(kana);
            els.input.value = disp;
            if (state.isStoryMode) {
                renderSentence();
            } else {
                els.kanaHint.innerText = "";
            }
        }

        function initVirtualKeyboard() {
            const keyboard = document.getElementById('virtual-keyboard');
            if (!keyboard) return;

            // Use lowercase internally for letters
            const rows = [
                ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'back'],
                ['space', 'enter']
            ];

            keyboard.innerHTML = rows.map(row => `
                <div class="keyboard-row">
                    ${row.map(key => {
                let className = 'key';
                let label = key;
                if (key === 'back' || key === 'enter') {
                    className += ' wide';
                    label = key.toUpperCase();
                }
                if (key === 'space') {
                    className += ' space';
                    label = key.toUpperCase();
                }
                return `<button class="${className}" data-key="${key}">${label}</button>`;
            }).join('')}
                </div>
            `).join('');

            const handleInteraction = (e, key) => {
                e.preventDefault();
                handleVirtualInput(key);
            };

            keyboard.addEventListener('touchstart', (e) => {
                const btn = e.target.closest('.key');
                if (btn) handleInteraction(e, btn.dataset.key);
            }, { passive: false });

            keyboard.addEventListener('mousedown', (e) => {
                const btn = e.target.closest('.key');
                if (btn) {
                    if (!('ontouchstart' in window)) {
                        handleInteraction(e, btn.dataset.key);
                    } else {
                        e.preventDefault(); // Prevent focus theft on touch devices
                    }
                }
            });
        }

        function handleVirtualInput(key) {
            if (isModalOpen()) return; // 모달이 열려있다면 가상 키 입력 차단
            playClickSound(); // Play haptic/click sound immediately on touch
            if (state.isLocked) return;

            if (key === 'back') {
                handleBackspace();
            } else if (key === 'enter') {
                if (state.isComplete) {
                    handleSuccess();
                } else if (!state.isStoryMode) {
                    checkAnswer();
                }
            } else if (key === 'space') {
                if (state.isComplete) {
                    handleSuccess();
                } else {
                    state.rawInput += ' ';
                    if (state.isStoryMode) renderSentence();
                    checkAnswer();
                }
            } else {
                if (state.isComplete) return;
                state.rawInput += key;
                const kana = romajiToKana(state.rawInput);
                let displayKana = kana;
                if (state.phase === 'ONYOMI') displayKana = hiraganaToKatakana(kana);
                els.input.value = displayKana;

                if (state.isStoryMode) renderSentence();
                checkAnswer();
            }
        }

        els.input.addEventListener('keydown', (e) => {
            if (e.key === 'Backspace') {
                e.preventDefault();
                handleBackspace();
                return;
            }
            handleKey(e);
        });

        els.phaseTag.addEventListener('click', (e) => {
            e.stopPropagation();
            playClickSound();
            if (state.learningMode === 'KANJI') {
                if (state.phase === 'ONYOMI') {
                    if (state.currentKanji && state.currentKanji.readings_kun && state.currentKanji.readings_kun.length > 0) {
                        setPhase('KUNYOMI');
                    } else {
                        els.phaseTag.classList.remove('error-shake');
                        void els.phaseTag.offsetWidth; // trigger reflow
                        els.phaseTag.classList.add('error-shake');
                    }
                } else if (state.phase === 'KUNYOMI') {
                    if (state.currentKanji && state.currentKanji.readings_on && state.currentKanji.readings_on.length > 0) {
                        setPhase('ONYOMI');
                    } else {
                        els.phaseTag.classList.remove('error-shake');
                        void els.phaseTag.offsetWidth; // trigger reflow
                        els.phaseTag.classList.add('error-shake');
                    }
                }
            }
        });

        els.btnKanji.addEventListener('click', (e) => { e.stopPropagation(); playCurrent(); });
        els.btnWord.addEventListener('click', (e) => { e.stopPropagation(); playCurrent(); });
        els.btnSentence.addEventListener('click', (e) => { e.stopPropagation(); playCurrent(); });

        els.slider.addEventListener('input', (e) => {
            stopAudio();
            audiobookSessionId++;
            jumpToIndex(parseInt(e.target.value), false);
        });

        els.slider.addEventListener('change', (e) => {
            if (state.isStoryMode && state.currentSentence) {
                if (state.isAudiobookMode) {
                    startAudiobookLoop();
                } else {
                    speakText(state.currentSentence.kana);
                }
            }
        });

        els.furiganaSwitch.addEventListener('change', (e) => {
            playClickSound();
            state.showFurigana = e.target.checked;
            if (state.isStoryMode) renderSentence();
        });

        els.audiobookSwitch.addEventListener('change', (e) => {
            playClickSound();
            state.isAudiobookMode = e.target.checked;
            if (state.isAudiobookMode) {
                els.card.classList.add('audiobook-active');
                if (state.isStoryMode) startAudiobookLoop();
            } else {
                els.card.classList.remove('audiobook-active');
                audiobookSessionId++; // Stop the active loop
                stopAudio();
            }
        });


        async function startAudiobookLoop() {
            // If already finishing or not in audiobook mode, exit
            if (!state.isAudiobookMode || !state.isStoryMode || state.isFinish) return;

            const sessionId = ++audiobookSessionId;

            // Clear any existing timeout to avoid multiple loops
            if (audiobookTimeout) {
                clearTimeout(audiobookTimeout);
                audiobookTimeout = null;
            }

            // 1. Read current sentence
            // This await waits for the audio to actually finish
            await speakText(state.currentSentence.kana);

            // Check if we should still continue (user might have toggled off during playback)
            if (sessionId !== audiobookSessionId || !state.isAudiobookMode || !state.isStoryMode || state.isFinish) return;

            // 2. Wait for 2 seconds before moving to next
            audiobookTimeout = setTimeout(() => {
                // Safety check before moving
                if (sessionId !== audiobookSessionId || !state.isAudiobookMode || !state.isStoryMode || state.isFinish) return;

                // 3. Move to next sentence
                state.currentIndex++;
                if (state.currentIndex >= KANJI_DATA.length) {
                    state.isFinish = true;
                    els.finishDialog.classList.remove('hidden');
                    stopAudio();
                } else {
                    loadKanji();
                    // loadKanji -> setPhase -> startAudiobookLoop is called again
                    // But we should ensure it doesn't double-call.
                    // Actually, setPhase('STORY') already calls startAudiobookLoop().
                }
            }, 2000);
        }

        function stopAudio() {
            if (currentAudio) {
                try { currentAudio.pause(); } catch (e) { }
                currentAudio.onended = null;
                currentAudio = null;
            }
            if (currentSource) {
                try { currentSource.stop(); } catch (e) { }
                currentSource = null;
            }
            if (window.speechSynthesis) {
                window.speechSynthesis.cancel();
            }
            if (audiobookTimeout) {
                clearTimeout(audiobookTimeout);
                audiobookTimeout = null;
            }
        }

        window.addEventListener('load', () => { init(); });
        document.addEventListener('click', () => {
            els.input.focus();
            if (window.speechSynthesis.getVoices().length === 0) window.speechSynthesis.getVoices();
        });
    
        function renderKanjiSentences() {
            els.sentencesContainer.innerHTML = '';
            const sentences = state.currentKanji.sentences;
            sentences.forEach((sentence, idx) => {
                const sDiv = document.createElement('div');
                sDiv.className = 'kanji-sentence-item';
                
                const rubySegments = alignFurigana(sentence.kanji, sentence.kana);
                let rubyHtml = '';
                rubySegments.forEach(seg => {
                    if (seg.isKanji && seg.kana) {
                        rubyHtml += `<ruby>${seg.text}<rt>${seg.kana}</rt></ruby>`;
                    } else {
                        rubyHtml += seg.text;
                    }
                });

                sDiv.innerHTML = `
                    <div class="sentence-text-row">
                        <span class="sentence-ruby-text">${rubyHtml}</span>
                        <button class="audio-btn small-audio-btn" onclick="playTTS('${sentence.kanji.replace(/'/g, "\'")}')" title="발음 듣기">
                            <svg viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path><path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path></svg>
                        </button>
                    </div>
                    <div class="sentence-meaning-row">
                        <button class="meaning-toggle-btn" onclick="this.nextElementSibling.classList.toggle('hidden'); this.innerText = this.nextElementSibling.classList.contains('hidden') ? '뜻 보기' : '뜻 숨기기'">뜻 보기</button>
                        <span class="sentence-meaning hidden">${sentence.meaning}</span>
                    </div>
                `;
                els.sentencesContainer.appendChild(sDiv);
            });
        }

        function playTTS(text) {
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'ja-JP';
            window.speechSynthesis.speak(utterance);
        }

    