import streamlit as st
import time

# --- ページ基本設定 ---
st.set_page_config(
    page_title="未来ルートナビ | 系列・コース診断",
    page_icon="✦",
    layout="centered"
)

# --- カスタムCSS（デザインの調整） ---
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #FFF1F5 0%, #E0E7FF 50%, #E0F2FE 100%);
    }
    .main-title {
        font-size: 1.8rem;
        font-weight: 800;
        text-align: center;
        background: -webkit-linear-gradient(45deg, #FF6B9B, #8B5CF6, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    .mascot-box {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        padding: 15px;
        border: 2px solid white;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
    }
    .badge {
        display: inline-block;
        background-color: #8B5CF6;
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: bold;
        margin-right: 5px;
        margin-bottom: 5px;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. データ定義 (8系列) ---
TRACKS = {
    'SPACE_WEATHER': {
        'name': '宇宙・気象系列',
        'comment': 'データや自然の神秘、宇宙のスケールにワクワクするキミ！空や宇宙の謎を解き明かす理数アドベンチャーへ飛び出そう！',
        'traits': ['データやグラフの変化・法則を読むのが好き', '天気や宇宙・自然現象への探究心がある', '数学的な計算や公式を使って解くのが得意'],
        'faculties': ['理学部', '気象大学校', '地球惑星科学科', '宇宙航空学科'],
        'careers': ['気象予報士', '宇宙開発エンジニア', 'データアナリスト', '環境研究員']
    },
    'DX': {
        'name': 'DX系列',
        'comment': 'デジタルテクノロジーと新アイデアの創出が得意なキミ！Web・アプリ・ゲームなど、デジタルで世界を変革しよう！',
        'traits': ['PCやスマホの操作・活用が得意', '「こんなサービス欲しい！」と妄想するのが好き', 'デジタル技術で新しい価値を作ることに興味がある'],
        'faculties': ['情報工学部', 'データサイエンス学部', 'デジタルコンテンツ学部'],
        'careers': ['Webエンジニア', 'アプリ開発者', 'ゲームデザイナー', 'DXコンサルタント']
    },
    'HYOGO_STARTUP': {
        'name': 'ひょうごからスタートアップ系列',
        'comment': '地域の魅力発信や新しい挑戦・起業に燃えるキミ！企画力と情熱で兵庫から世界へ新しい風を起こそう！',
        'traits': ['地元の魅力を多くの人に伝えるのが好き', 'イベントや新しい企画を立ち上げるのが好き', '将来自分で事業やサービスを起こす（起業）に興味がある'],
        'faculties': ['経営学部', '経済学部', '地域創生学部', 'アントレプレナーシップ学科'],
        'careers': ['起業家', '新規事業プロデューサー', '地域活性化コーディネーター', 'イベントプロデューサー']
    },
    'OUTDOOR_DISASTER': {
        'name': 'スポーツ・アウトドアと防災系列',
        'comment': '体を動かす情熱と、災害から命を守る優しさを兼ね備えたキミ！仲間と協力して安心・安全な社会を作ろう！',
        'traits': ['体を動かすことやアクティビティが好き', '防災や緊急時に人を助けることに強い興味がある', 'チームで協力して課題に取り組み達成するのが好き'],
        'faculties': ['防災学部', 'スポーツ健康科学部', '社会安全学部', '救急救命学科'],
        'careers': ['消防士・救急救命士', '防災コーディネーター', 'スポーツインストラクター', 'アウトドアガイド']
    },
    'DIVERSITY': {
        'name': 'ダイバーシティ&インクルージョン系列',
        'comment': '多様な価値観を理解し、「誰もが過ごしやすい社会」を追求できる優しい視点を持ったキミにピッタリ！',
        'traits': ['「当たり前」に疑問を持ち、多様な意見に耳を傾けられる', '自分と異なる考え方や立場の人を尊重できる', 'いろんな人の視点から社会課題を考えられる'],
        'faculties': ['看護学部', '外国語学部', '総合人間科学部', '社会学部', '福祉学部'],
        'careers': ['看護師・医療従事者', '語学を活かした職種', 'ダイバーシティ推進担当', '社会福祉士']
    },
    'LIBERAL_SCIENCE': {
        'name': 'リベラルアーツ理系系列',
        'comment': '「なぜ？」をロジカルに掘り下げる探究派！特定の分野に縛られず、幅広い理系知性を身につけよう！',
        'traits': ['理由や仕組みから本質を理解するのが好き', '理系進学希望だが、まだ一つの分野に絞っていない', '仮説を立てて試行錯誤しながら答えを探すのが好き'],
        'faculties': ['理学部（学科横断コース）', '総合科学部', '教養学部（理系）'],
        'careers': ['サイエンスコミュニケーション', '開発研究員', 'システム分析官']
    },
    'LIBERAL_ARTS': {
        'name': 'リベラルアーツ文系系列',
        'comment': '思考を言語化し、人間や社会の文脈を深く味わうキミ！幅広い文系知性で物事を多角的に捉えよう！',
        'traits': ['自分の考えを文章や言葉で表現するのが好き', '文系進学希望だが、まだ学科を一つに絞っていない', '言語学・心理学・社会学など人間社会の探究が好き'],
        'faculties': ['文学部', '教養学部（文系）', '総合人間学科', '人文社会学科'],
        'careers': ['ライター・編集者', '企画マーケター', '広報担当', '国際交流ディレクター']
    },
    'CREATIVE_ARTS': {
        'name': 'クリエイティブ・表現系列',
        'comment': '自らの感性やアイデアを発信し、アートやデザインで人の心を動かすことが大好きなクリエイタータイプ！',
        'traits': ['イラスト・音楽・映像など表現することが好き', '自分ならではの世界観やアイデアを持っている', '作品づくりを通して思いを他人に伝えたい'],
        'faculties': ['芸術学部', '美術学部', 'デザイン学部', '音楽学部'],
        'careers': ['イラストレーター', 'グラフィックデザイナー', '映像クリエイター', '音楽制作者']
    }
}

DIAGNOSIS_QUESTIONS = [
    {"q": "Q1. グラフ・表などのデータから傾向や変化を読み取ることが好きだ", "track": "SPACE_WEATHER"},
    {"q": "Q2. 天気・宇宙などに興味がある", "track": "SPACE_WEATHER"},
    {"q": "Q3. 数学の計算や公式を使って、問題を解くことに抵抗がない", "track": "SPACE_WEATHER"},
    {"q": "Q4. パソコン・スマートフォン操作が得意だ", "track": "DX"},
    {"q": "Q5. 将来Web・アプリ・ゲームに関係する職に就きたいと思う", "track": "DX"},
    {"q": "Q6. 「こんなサービスがあったらいいのに」など新しいものを考えるのが好きだ", "track": "DX"},
    {"q": "Q7. 地元の魅力をみんなに知ってもらいたい！", "track": "HYOGO_STARTUP"},
    {"q": "Q8. イベントやサービスの企画がとても好きだ", "track": "HYOGO_STARTUP"},
    {"q": "Q9. 将来起業することに興味がある", "track": "HYOGO_STARTUP"},
    {"q": "Q10. 体を動かすことがとても好きだ", "track": "OUTDOOR_DISASTER"},
    {"q": "Q11. 自然災害時に人を助けたりすることに興味がある", "track": "OUTDOOR_DISASTER"},
    {"q": "Q12. グループで協力して課題や活動に取り組むことが好きだ", "track": "OUTDOOR_DISASTER"},
    {"q": "Q13. 当たり前のことになぜ？と疑問を持てる", "track": "DIVERSITY"},
    {"q": "Q14. 自分と違う考え方の人の意見に興味がある", "track": "DIVERSITY"},
    {"q": "Q15. 一つの問題に様々な立場の人の意見を考えることができる", "track": "DIVERSITY"},
    {"q": "Q16. 「なぜそうなるか」を、理由や仕組みから理解することが好き", "track": "LIBERAL_SCIENCE"},
    {"q": "Q17. 将来理系の大学に進みたいが分野が決まっていない", "track": "LIBERAL_SCIENCE"},
    {"q": "Q18. 仮説をたてて試行錯誤しながら答えを導くのが好きだ", "track": "LIBERAL_SCIENCE"},
    {"q": "Q19. 自分の考えを文章で表すことが好きだ", "track": "LIBERAL_ARTS"},
    {"q": "Q20. 将来文系の大学に進みたいが分野が決まっていない", "track": "LIBERAL_ARTS"},
    {"q": "Q21. 言語学や社会学に興味がある", "track": "LIBERAL_ARTS"}
]

# --- ステート初期化 ---
if 'step' not in st.session_state:
    st.session_state.step = 'start'
if 'scores' not in st.session_state:
    st.session_state.scores = {k: 0 for k in TRACKS.keys()}
if 'q_idx' not in st.session_state:
    st.session_state.q_idx = 0

# --- 画面制御 ---

# 1. スタート画面
if st.session_state.step == 'start':
    st.markdown("<h1 class='main-title'>未来ルートナビ</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #475569;'>キミにピッタリの高校の系列・コースを探そう！</p>", unsafe_allow_html=True)

    with st.container():
        st.markdown("""
        <div class="mascot-box" style="text-align: center;">
            <p>🤖 <b>ナビィ</b>: 直感的な質問に答えるだけで、あなたの得意や興味に合ったコースを分析するよ✨</p>
        </div>
        """, unsafe_allow_html=True)

    if st.button("🚀 診断をはじめる", use_container_width=True, type="primary"):
        st.session_state.step = 'quiz'
        st.session_state.q_idx = 0
        st.session_state.scores = {k: 0 for k in TRACKS.keys()}
        st.rerun()

# 2. クイズ画面
elif st.session_state.step == 'quiz':
    total_q = len(DIAGNOSIS_QUESTIONS)
    curr_q = st.session_state.q_idx
    q_data = DIAGNOSIS_QUESTIONS[curr_q]

    # 進捗バー
    st.progress((curr_q + 1) / total_q)
    st.caption(f"QUESTION {curr_q + 1} / {total_q}")

    st.markdown(f"""
    <div class="mascot-box">
        <p style="font-size: 1.1rem; font-weight: bold; color: #1E293B;">{q_data['q']}</p>
    </div>
    """, unsafe_allow_html=True)

    choices = [
        ("とても当てはまる", 4),
        ("やや当てはまる", 3),
        ("あまり当てはまらない", 2),
        ("全く当てはまらない", 1)
    ]

    for label, score in choices:
        if st.button(label, key=f"btn_{curr_q}_{score}", use_container_width=True):
            st.session_state.scores[q_data['track']] += score
            if st.session_state.q_idx + 1 < total_q:
                st.session_state.q_idx += 1
                st.rerun()
            else:
                st.session_state.step = 'result'
                st.rerun()

# 3. 診断結果画面
elif st.session_state.step == 'result':
    # スコア集計
    top_track_key = max(st.session_state.scores, key=st.session_state.scores.get)
    result = TRACKS[top_track_key]

    st.balloons()
    st.markdown("<h2 style='text-align: center; color: #64748B;'>✦ 診断結果 ✦</h2>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='main-title'>{result['name']}</h1>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="mascot-box">
        <p>🤖 <b>ナビィのコメント:</b><br>{result['comment']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("💡 あなたの強み・特徴")
    for trait in result['traits']:
        st.markdown(f"- {trait}")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎓 目指せる大学学部")
        for f in result['faculties']:
            st.markdown(f"<span class='badge'>{f}</span>", unsafe_allow_html=True)
    with col2:
        st.subheader("💼 向いている職種")
        for c in result['careers']:
            st.markdown(f"<span class='badge' style='background-color:#06B6D4;'>{c}</span>", unsafe_allow_html=True)

    st.divider()
    if st.button("🔄 もう一度診断する", use_container_width=True):
        st.session_state.step = 'start'
        st.rerun()