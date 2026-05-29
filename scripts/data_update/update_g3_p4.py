import json
import os

new_data = [
  {
    "kanji": "暑",
    "reading_on": "ショ",
    "reading_kun": "あつ(い)",
    "meaning": "더울",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "해나 태양열을 뜻합니다." },
      { "char": "者", "role": "놈 자 (요소)", "desc": "많은 땔감을 모아 불을 피우는 모습이거나 발음 '자/쇼'를 나타냅니다." }
    ],
    "story": "태양(日) 빛이 강하게 내리쬐어 불을 피운 듯이 날씨가 '덥다'는 뜻입니다.",
    "example_words": [
      { "word": "暑い", "reading": "あつい", "meaning": "덥다", "description": "여름철 기온이 높은 상태입니다." },
      { "word": "残暑", "reading": "ざんしょ", "meaning": "늦더위", "description": "가을이 되어도 남아(残) 있는 더위(暑)입니다." }
    ]
  },
  {
    "kanji": "助",
    "reading_on": "ジョ",
    "reading_kun": "たす(ける)、たす(かる)",
    "meaning": "도울",
    "components": [
      { "char": "且", "role": "또 차 (요소)", "desc": "제기(제사 그릇)를 쌓아 올린 모양이거나 조상신을 의미합니다." },
      { "char": "力", "role": "힘 력 (부수)", "desc": "팔의 힘이나 노동력을 뜻합니다." }
    ],
    "story": "제사 그릇(且)을 나를 때 힘(力)을 보태서 옆에서 '돕다' 혹은 거든다는 의미입니다.",
    "example_words": [
      { "word": "助ける", "reading": "たすける", "meaning": "돕다, 살리다", "description": "위험에 처한 사람이나 곤란한 일을 거들어 주는 것입니다." },
      { "word": "助手", "reading": "じょしゅ", "meaning": "조수", "description": "곁에서 돕는(助) 손(手), 즉 일을 거드는 사람입니다." }
    ]
  },
  {
    "kanji": "昭",
    "reading_on": "ショウ",
    "reading_kun": "",
    "meaning": "밝을",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "해나 햇빛을 뜻합니다." },
      { "char": "召", "role": "부를 소 (요소)", "desc": "부르다는 뜻과 발음 '소/쇼우'를 담당합니다." }
    ],
    "story": "해(日)가 떠올라 사람들을 부르듯(召) 세상을 널리 환하고 '밝게' 비춘다는 뜻입니다.",
    "example_words": [
      { "word": "昭和", "reading": "しょうわ", "meaning": "쇼와 (연호)", "description": "밝고(昭) 화평한(和) 시대라는 뜻의 일본 연호입니다." },
      { "word": "昭昭", "reading": "しょうしょう", "meaning": "소소, 매우 밝음", "description": "매우 밝고 환한 모양입니다." }
    ]
  },
  {
    "kanji": "消",
    "reading_on": "ショウ",
    "reading_kun": "き(える)、け(す)",
    "meaning": "사라질 / 끄다",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 액체를 뜻합니다." },
      { "char": "肖", "role": "닮을 초 (요소)", "desc": "고기가 점점 작아지는 모습에서 작아진다는 뜻과 발음 '초/쇼우'를 줍니다." }
    ],
    "story": "물이 점점 작아져서 마르거나, 불에 물(氵)을 끼얹어 불길을 작게(肖) 하여 '끄다' 혹은 '사라지다'는 뜻입니다.",
    "example_words": [
      { "word": "消える", "reading": "きえる", "meaning": "사라지다, 꺼지다", "description": "불이나 흔적이 눈에 보이지 않게 되는 것입니다." },
      { "word": "消防", "reading": "しょうぼう", "meaning": "소방", "description": "불을 끄고(消) 화재를 막는(防) 일입니다." }
    ]
  },
  {
    "kanji": "商",
    "reading_on": "ショウ",
    "reading_kun": "あきな(う)",
    "meaning": "장사 / 상인",
    "components": [
      { "char": "亠", "role": "돼지해머리 (요소)", "desc": "장식이나 관을 뜻합니다." },
      { "char": "言", "role": "말씀 언 (요소)", "desc": "말을 하거나 의논하는 모습입니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "입을 뜻합니다." }
    ],
    "story": "고대 상(商)나라 사람들이 여기저기 돌아다니며 물건을 놓고 값을 의논(言)하여 '장사'를 했다는 데서 유래했습니다.",
    "example_words": [
      { "word": "商売", "reading": "しょうばい", "meaning": "장사", "description": "장사(商)하여 물건을 파는(売) 일입니다." },
      { "word": "商店", "reading": "しょうてん", "meaning": "상점", "description": "장사(商)를 하는 가게(店)입니다." }
    ]
  },
  {
    "kanji": "章",
    "reading_on": "ショウ",
    "reading_kun": "",
    "meaning": "글 / 표장",
    "components": [
      { "char": "音", "role": "소리 음 (요소)", "desc": "악기 소리나 운율이 있는 소리를 뜻합니다." },
      { "char": "十", "role": "열 십 (부수)", "desc": "모인다는 뜻이나 완전함을 나타냅니다." }
    ],
    "story": "음악(音)의 한 곡조가 마무리되어(十) 완성된 단락이나, 완결된 '글(문장)'의 한 단락인 '장'을 뜻합니다.",
    "example_words": [
      { "word": "文章", "reading": "ぶんしょう", "meaning": "문장", "description": "글(文)이 모여 이루어진 단락(章)입니다." },
      { "word": "腕章", "reading": "わんしょう", "meaning": "완장", "description": "팔(腕)에 차는 표장(章)이나 기호입니다." }
    ]
  },
  {
    "kanji": "勝",
    "reading_on": "ショウ",
    "reading_kun": "か(つ)、まさ(る)",
    "meaning": "이길",
    "components": [
      { "char": "月", "role": "육달월 (요소)", "desc": "원래 배주(舟)가 변형된 것으로, 무거운 물건을 들어 올리는 도구를 뜻합니다." },
      { "char": "券", "role": "문서 권 (요소)", "desc": "손으로 무언가를 강하게 쥔다는 뜻의 변형입니다." },
      { "char": "力", "role": "힘 력 (부수)", "desc": "힘이나 노력을 의미합니다." }
    ],
    "story": "온 힘(力)을 다해 무거운 짐을 들어 올리듯이, 남과 겨루어 힘으로 제압하여 '이기다'는 뜻입니다.",
    "example_words": [
      { "word": "勝つ", "reading": "かつ", "meaning": "이기다", "description": "승부나 경쟁에서 상대방을 물리치는 것입니다." },
      { "word": "優勝", "reading": "ゆうしょう", "meaning": "우승", "description": "가장 뛰어나게(優) 이기는(勝) 것입니다." }
    ]
  },
  {
    "kanji": "乗",
    "reading_on": "ジョウ",
    "reading_kun": "の(る)、の(せる)",
    "meaning": "탈",
    "components": [
      { "char": "丿", "role": "삐침 (부수)", "desc": "동작을 나타냅니다." },
      { "char": "木", "role": "나무 목 (요소)", "desc": "나무 수레나 탈것을 뜻합니다." }
    ],
    "story": "사람(丿의 변형)이 나무(木)로 만든 높은 수레나 탈것 위에 두 발을 벌리고 올라가 '타다'는 뜻을 나타냅니다.",
    "example_words": [
      { "word": "乗る", "reading": "のる", "meaning": "타다", "description": "차나 배, 비행기 등의 탈것에 올라가는 것입니다." },
      { "word": "乗客", "reading": "じょうきゃく", "meaning": "승객", "description": "차나 배에 타고(乗) 있는 손님(客)입니다." }
    ]
  },
  {
    "kanji": "植",
    "reading_on": "ショク",
    "reading_kun": "う(える)、う(わる)",
    "meaning": "심을",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무나 식물을 뜻합니다." },
      { "char": "直", "role": "곧을 직 (요소)", "desc": "똑바로 세우다, 곧다는 뜻과 발음 '직/쇼쿠'를 담당합니다." }
    ],
    "story": "나무(木) 묘목을 밭에 똑바로(直) 세워 무럭무럭 자라게 '심다'라는 뜻입니다.",
    "example_words": [
      { "word": "植物", "reading": "しょくぶつ", "meaning": "식물", "description": "심어서(植) 자라는 생물체(物)입니다." },
      { "word": "植える", "reading": "うえる", "meaning": "심다", "description": "씨앗이나 모종을 땅에 묻어 자라게 하는 것입니다." }
    ]
  },
  {
    "kanji": "申",
    "reading_on": "シン",
    "reading_kun": "もう(す)",
    "meaning": "납 / 아뢸",
    "components": [
      { "char": "田", "role": "밭 전 (부수)", "desc": "여기서는 번개가 번쩍이는 모양에서 유래했습니다." }
    ],
    "story": "번개가 번쩍이며 하늘에서 땅으로 길게 늘어나는 모습에서 '펴다'라는 뜻이 되었고, 나중에 웃어른에게 자신의 뜻을 펴서 '말씀드리다(아뢰다)'로 쓰이게 되었습니다.",
    "example_words": [
      { "word": "申す", "reading": "もうす", "meaning": "말씀드리다 (겸양어)", "description": "말하다(言う)의 낮춤말로, 자기 자신을 낮춰 말할 때 씁니다." },
      { "word": "申し訳ない", "reading": "もうしわけない", "meaning": "죄송하다", "description": "변명하여(申し訳) 빠져나갈 길이 없다는 뜻입니다." }
    ]
  },
  {
    "kanji": "身",
    "reading_on": "シン",
    "reading_kun": "み",
    "meaning": "몸",
    "components": [
      { "char": "身", "role": "몸 신 (부수)", "desc": "배가 부른 임산부의 옆모습을 본뜬 상형문자입니다." }
    ],
    "story": "배 속에 아기를 임신하여 불룩해진 여성의 몸 모양에서 유래하여, 사람의 '몸'이나 '신분'을 의미하게 되었습니다.",
    "example_words": [
      { "word": "身体", "reading": "しんたい", "meaning": "신체", "description": "사람의 몸(身)과 바탕(体)입니다." },
      { "word": "中身", "reading": "なかみ", "meaning": "알맹이, 내용물", "description": "몸(身)의 안(中)에 들어있는 것입니다." }
    ]
  },
  {
    "kanji": "神",
    "reading_on": "シン、ジン",
    "reading_kun": "かみ、かん",
    "meaning": "귀신 (신)",
    "components": [
      { "char": "示", "role": "보일 시 (부수)", "desc": "제단이나 신을 모시는 곳을 뜻합니다." },
      { "char": "申", "role": "납 신 (요소)", "desc": "번개가 치는 모양으로, 하늘의 신비로운 힘이나 발음 '신'을 나타냅니다." }
    ],
    "story": "제단(示) 위에서 번개(申)처럼 하늘의 신비로운 힘을 내려주는 조물주나 만물을 주재하는 '신'을 뜻합니다.",
    "example_words": [
      { "word": "神様", "reading": "かみさま", "meaning": "신, 하느님", "description": "만물을 주재하는 신(神)을 높여 부르는 말입니다." },
      { "word": "神社", "reading": "じんじゃ", "meaning": "신사", "description": "신(神)을 모셔놓은 사당(社)입니다." }
    ]
  },
  {
    "kanji": "真",
    "reading_on": "シン",
    "reading_kun": "ま",
    "meaning": "참",
    "components": [
      { "char": "匕", "role": "비수 비 (요소)", "desc": "사람이 거꾸로 된 모양이나 변화를 뜻합니다." },
      { "char": "目", "role": "눈 목 (부수)", "desc": "눈으로 똑똑히 본다는 뜻입니다." },
      { "char": "八", "role": "여덟 팔 (요소)", "desc": "제물을 받치는 받침대입니다." }
    ],
    "story": "거짓 없이 눈(目)으로 똑똑히 보고 사실 그대로 옮긴다는 데서 거짓이 없는 '참'이나 '진짜'를 의미합니다.",
    "example_words": [
      { "word": "写真", "reading": "しゃしん", "meaning": "사진", "description": "참된(真) 모습을 그대로 베낀(写) 것입니다." },
      { "word": "真面目", "reading": "まじめ", "meaning": "성실함, 진지함", "description": "태도나 얼굴이 참되고(真) 성실한 것입니다." }
    ]
  },
  {
    "kanji": "深",
    "reading_on": "シン",
    "reading_kun": "ふか(い)、ふか(まる)",
    "meaning": "깊을",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강, 바다를 뜻합니다." },
      { "char": "罙", "role": "깊을 심 (요소)", "desc": "사람이 횃불을 들고 굴속으로 들어가는 모양으로 깊다는 뜻을 줍니다." }
    ],
    "story": "물(氵)의 바닥이 아주 밑까지 내려가 있어서 물이 '깊다'는 뜻입니다.",
    "example_words": [
      { "word": "深い", "reading": "ふかい", "meaning": "깊다", "description": "물이나 생각 따위가 깊숙한 상태입니다." },
      { "word": "深夜", "reading": "しんや", "meaning": "심야", "description": "밤(夜)이 깊어진(深) 때입니다." }
    ]
  },
  {
    "kanji": "進",
    "reading_on": "シン",
    "reading_kun": "すす(む)、すす(める)",
    "meaning": "나아갈",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 걷거나 이동함을 뜻합니다." },
      { "char": "隹", "role": "새 추 (요소)", "desc": "새를 뜻하며, 새가 앞으로만 날아간다는 뜻을 담고 있습니다." }
    ],
    "story": "새(隹)가 뒤로 물러서지 않고 앞으로만 날아가듯, 길을 따라(辶) 목적지를 향해 '나아가다'라는 뜻입니다.",
    "example_words": [
      { "word": "進む", "reading": "すすむ", "meaning": "나아가다", "description": "앞으로 전진하거나 진행되는 것입니다." },
      { "word": "進行", "reading": "しんこう", "meaning": "진행", "description": "앞으로 나아가(進) 행하는(行) 일입니다." }
    ]
  },
  {
    "kanji": "世",
    "reading_on": "セイ、セ",
    "reading_kun": "よ",
    "meaning": "인간 (세상)",
    "components": [
      { "char": "十", "role": "열 십 (요소)", "desc": "열 십(十) 자가 세 개 겹쳐진 삼십을 나타내는 글자의 변형입니다." },
      { "char": "一", "role": "한 일 (부수)", "desc": "시간의 흐름이나 세대를 묶는다는 뜻입니다." }
    ],
    "story": "숫자 30을 뜻하는 옛 글자에서 유래하여, 약 30년을 한 '세대(世)'로 묶고 사람들이 살아가는 '세상'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "世界", "reading": "せかい", "meaning": "세계", "description": "사람들이 사는 세상(世)의 경계(界)입니다." },
      { "word": "世の中", "reading": "よのなか", "meaning": "세상물정, 사회", "description": "우리가 사는 세상(世)의 안(中)입니다." }
    ]
  },
  {
    "kanji": "整",
    "reading_on": "セイ",
    "reading_kun": "ととの(える)、ととの(う)",
    "meaning": "가지런할",
    "components": [
      { "char": "束", "role": "묶을 속 (요소)", "desc": "나뭇가지를 단단히 묶은 모습입니다." },
      { "char": "攵", "role": "칠 복 (요소)", "desc": "회초리로 치거나 행동을 재촉하는 모습입니다." },
      { "char": "正", "role": "바를 정 (요소)", "desc": "바르게 한다는 뜻입니다." }
    ],
    "story": "묶은(束) 물건을 쳐서(攵) 모양을 바르게(正) 잡아 '가지런하게' 정리정돈한다는 뜻입니다.",
    "example_words": [
      { "word": "整理", "reading": "せいり", "meaning": "정리", "description": "어지러운 것을 가지런히(整) 다스리는(理) 것입니다." },
      { "word": "整える", "reading": "ととのえる", "meaning": "정돈하다, 준비하다", "description": "모양이나 상태를 바르게 갖추는 것입니다." }
    ]
  },
  {
    "kanji": "昔",
    "reading_on": "セキ、シャク",
    "reading_kun": "むかし",
    "meaning": "예",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "해나 날짜를 의미합니다." },
      { "char": "㐆", "role": "쌓일 은 (요소)", "desc": "겹겹이 쌓인 고기 조각이나 물건 모양입니다." }
    ],
    "story": "날짜(日)가 겹겹이(㐆) 쌓여서 아주 오래전에 지나간 '옛날'을 의미합니다.",
    "example_words": [
      { "word": "昔", "reading": "むかし", "meaning": "옛날", "description": "아주 지나간 과거의 시절입니다." },
      { "word": "昔話", "reading": "むかしばなし", "meaning": "옛날이야기", "description": "옛날(昔)에 있었던 이야기(話)입니다." }
    ]
  },
  {
    "kanji": "全",
    "reading_on": "ゼン",
    "reading_kun": "まった(く)",
    "meaning": "온전할",
    "components": [
      { "char": "入", "role": "들 입 (부수)", "desc": "원래 亼(삼합 집)으로 여러 개가 모여 덮인 모양입니다." },
      { "char": "王", "role": "구슬 옥 (요소)", "desc": "구슬이나 보석을 뜻합니다." }
    ],
    "story": "흠집 없이 잘 덮어둔(入) 둥근 보석(王)처럼 흠집 하나 없이 '완전하다' 혹은 '전부'를 뜻합니다.",
    "example_words": [
      { "word": "全部", "reading": "ぜんぶ", "meaning": "전부", "description": "온전한(全) 모든 부분(部)입니다." },
      { "word": "安全", "reading": "あんぜん", "meaning": "안전", "description": "위험 없이 편안하고(安) 온전한(全) 상태입니다." }
    ]
  },
  {
    "kanji": "相",
    "reading_on": "ソウ、ショウ",
    "reading_kun": "あい",
    "meaning": "서로 / 재상",
    "components": [
      { "char": "木", "role": "나무 목 (요소)", "desc": "나무를 뜻합니다." },
      { "char": "目", "role": "눈 목 (부수)", "desc": "사람의 눈입니다." }
    ],
    "story": "사람이 눈(目)으로 나무(木)의 재질과 상태를 자세히 살핀다는 뜻에서 유래하여 사물의 생김새나 관상, 혹은 마주 보며 '서로' 돕는다는 뜻을 가집니다.",
    "example_words": [
      { "word": "相手", "reading": "あいて", "meaning": "상대", "description": "나와 서로(相) 맞서는 손(手, 사람)입니다." },
      { "word": "相談", "reading": "そうだん", "meaning": "상담", "description": "서로(相) 마주 앉아 이야기(談)를 나누는 것입니다." }
    ]
  },
  {
    "kanji": "送",
    "reading_on": "ソウ",
    "reading_kun": "おく(る)",
    "meaning": "보낼",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 가거나 이동함을 뜻합니다." },
      { "char": "灷", "role": "불꽃 전 (요소)", "desc": "횃불을 들고 있는 모습으로, 길을 밝혀준다는 뜻입니다." }
    ],
    "story": "손에 횃불(灷)을 들고 밤길(辶)을 떠나는 사람을 배웅하며 멀리 '보낸다'는 뜻입니다.",
    "example_words": [
      { "word": "送る", "reading": "おくる", "meaning": "보내다", "description": "물건을 목적지로 보내거나 사람을 배웅하는 일입니다." },
      { "word": "放送", "reading": "ほうそう", "meaning": "방송", "description": "전파를 놓아(放) 멀리 보내는(送) 것입니다." }
    ]
  },
  {
    "kanji": "想",
    "reading_on": "ソウ、ソ",
    "reading_kun": "",
    "meaning": "생각할",
    "components": [
      { "char": "相", "role": "서로 상 (요소)", "desc": "모양이나 대상, 혹은 발음 '상/소우'를 나타냅니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "마음이나 생각을 뜻합니다." }
    ],
    "story": "마음(心)속에 어떤 대상의 모양(相)을 떠올리며 깊이 '생각하다' 혹은 '상상하다'는 뜻입니다.",
    "example_words": [
      { "word": "想像", "reading": "そうぞう", "meaning": "상상", "description": "마음속으로 생각하고(想) 모양(像)을 그려보는 것입니다." },
      { "word": "感想", "reading": "かんそう", "meaning": "감상", "description": "느끼고(感) 생각한(想) 바입니다." }
    ]
  },
  {
    "kanji": "奏",
    "reading_on": "ソウ",
    "reading_kun": "かな(でる)",
    "meaning": "아뢸 / 연주하다",
    "components": [
      { "char": "大", "role": "큰 대 (부수)", "desc": "원래 두 손으로 물건을 받든 모양입니다." },
      { "char": "天", "role": "하늘 천 (요소)", "desc": "물건(옥이나 악기)을 나타내는 형태의 변형입니다." }
    ],
    "story": "두 손으로 악기를 잡고 음악을 '연주하다', 혹은 신이나 임금에게 물건을 받들어 '아뢰다'는 뜻입니다.",
    "example_words": [
      { "word": "演奏", "reading": "えんそう", "meaning": "연주", "description": "악기를 다루어(演) 소리를 내어 연주하는(奏) 일입니다." },
      { "word": "奏でる", "reading": "かなでる", "meaning": "연주하다", "description": "악기를 켜거나 타서 소리를 내는 것입니다." }
    ]
  },
  {
    "kanji": "息",
    "reading_on": "ソク",
    "reading_kun": "いき",
    "meaning": "숨 (쉴)",
    "components": [
      { "char": "自", "role": "스스로 자 (요소)", "desc": "코의 모양을 본뜬 글자로, 숨을 쉬는 곳을 의미합니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "사람의 심장이나 마음입니다." }
    ],
    "story": "코(自)로 들이마신 공기가 심장(心)까지 깊숙이 들어갔다 나오는 '숨' 혹은 생명이 쉬는 호흡을 뜻합니다.",
    "example_words": [
      { "word": "息", "reading": "いき", "meaning": "숨, 호흡", "description": "사람이나 동물이 쉬는 숨결입니다." },
      { "word": "ため息", "reading": "ためいき", "meaning": "한숨", "description": "마음속에 모였다가(ため) 내쉬는 숨(息)입니다." }
    ]
  },
  {
    "kanji": "速",
    "reading_on": "ソク",
    "reading_kun": "はや(い)、はや(める)",
    "meaning": "빠를",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "이동이나 길을 가는 것을 뜻합니다." },
      { "char": "束", "role": "묶을 속 (요소)", "desc": "나뭇가지를 단단히 묶은 모습으로 발음 '속'을 줍니다." }
    ],
    "story": "짐을 단단히 묶어(束) 메고 길(辶)을 지체 없이 재빨리 걸어간다는 데서 '빠르다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "速い", "reading": "はやい", "meaning": "빠르다", "description": "속도가 늦지 않고 빠른 상태입니다." },
      { "word": "速度", "reading": "そくど", "meaning": "속도", "description": "물체가 움직이는 빠른(速) 정도(度)입니다." }
    ]
  },
  {
    "kanji": "族",
    "reading_on": "ゾク",
    "reading_kun": "",
    "meaning": "겨레",
    "components": [
      { "char": "方", "role": "모방 (부수)", "desc": "원래 㫃(깃발 언) 자의 깃발 모양이 변형된 것입니다." },
      { "char": "矢", "role": "화살 시 (요소)", "desc": "화살이나 무기를 뜻합니다." }
    ],
    "story": "같은 깃발(方의 변형) 아래에 화살(矢)을 들고 함께 모여 싸우는 혈연 집단인 '겨레'나 '일가친척'을 뜻합니다.",
    "example_words": [
      { "word": "家族", "reading": "かぞく", "meaning": "가족", "description": "한 집(家)에 모여 사는 겨레(族)입니다." },
      { "word": "民族", "reading": "みんぞく", "meaning": "민족", "description": "언어와 문화를 공유하는 백성(民)의 겨레(族)입니다." }
    ]
  },
  {
    "kanji": "他",
    "reading_on": "タ",
    "reading_kun": "ほか",
    "meaning": "다를",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람입니다." },
      { "char": "也", "role": "어조사 야 (요소)", "desc": "뱀 모양이나 다름을 뜻하며 발음 '야/타'를 나타냅니다." }
    ],
    "story": "내가 아닌 다른 사람(亻), 즉 남이나 그 '밖'의 다른 것을 뜻합니다.",
    "example_words": [
      { "word": "他", "reading": "ほか", "meaning": "다른 곳, 그 밖", "description": "나 또는 이것 이외의 다른 것입니다." },
      { "word": "他人", "reading": "たにん", "meaning": "타인, 남", "description": "나와 친척이 아닌 다른(他) 사람(人)입니다." }
    ]
  },
  {
    "kanji": "打",
    "reading_on": "ダ",
    "reading_kun": "う(つ)",
    "meaning": "칠",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 하는 동작입니다." },
      { "char": "丁", "role": "고무래 정 (요소)", "desc": "못이나 망치를 뜻하며 세게 두드린다는 의미와 발음 '정/다'를 줍니다." }
    ],
    "story": "손(扌)에 망치(丁)를 들고 못을 강하게 내리'친다'거나 두드린다는 뜻입니다.",
    "example_words": [
      { "word": "打つ", "reading": "うつ", "meaning": "치다, 때리다", "description": "물건을 세게 치거나 타격을 가하는 것입니다." },
      { "word": "打者", "reading": "だしゃ", "meaning": "타자", "description": "야구 등에서 공을 치는(打) 사람(者)입니다." }
    ]
  },
  {
    "kanji": "対",
    "reading_on": "タイ、ツイ",
    "reading_kun": "",
    "meaning": "대할 (대답할)",
    "components": [
      { "char": "文", "role": "글월 문 (요소)", "desc": "원래 丵(풀 무성할 착) 자가 간략화된 모양입니다." },
      { "char": "寸", "role": "마디 촌 (부수)", "desc": "손의 동작이나 규칙을 뜻합니다." }
    ],
    "story": "두 손(寸)으로 물건을 마주 잡고 짝을 맞추거나, 상대방을 '마주 대하다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "反対", "reading": "はんたい", "meaning": "반대", "description": "의견이나 방향이 거꾸로(反) 마주 대하는(対) 일입니다." },
      { "word": "絶対", "reading": "ぜったい", "meaning": "절대", "description": "비교하여 마주 대할(対) 것이 끊어짐(絶), 즉 무조건임입니다." }
    ]
  },
  {
    "kanji": "待",
    "reading_on": "タイ",
    "reading_kun": "ま(つ)",
    "meaning": "기다릴",
    "components": [
      { "char": "彳", "role": "두인변 (부수)", "desc": "조금씩 걷거나 길을 뜻합니다." },
      { "char": "寺", "role": "절 사 (요소)", "desc": "발길을 멈추고 관청에 머무른다는 의미를 줍니다." }
    ],
    "story": "가던 길(彳)을 멈추고 절이나 관청(寺)에 머물며 누군가를 조용히 '기다리다' 혹은 대우하다는 뜻입니다.",
    "example_words": [
      { "word": "待つ", "reading": "まつ", "meaning": "기다리다", "description": "사람이나 때가 오기를 바라고 머무르는 일입니다." },
      { "word": "招待", "reading": "しょうたい", "meaning": "초대", "description": "불러서(招) 융숭하게 대접하고 기다리는(待) 것입니다." }
    ]
  }
]

file_path = '../../radical/src/data/kanjiDecomposerData_grade3.json'
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except:
            data = []
else:
    data = []

# Update or append
existing_kanjis = {d['kanji'] for d in data}
for item in new_data:
    if item['kanji'] not in existing_kanjis:
        data.append(item)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Grade 3 Part 4 data appended successfully.")
