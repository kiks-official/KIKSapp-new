import streamlit as st

# -----------------------------------------------------------------------------
# 1. ページ基本設定 & カスタムCSS
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="未来ルートナビ | 高校の系列・コース診断",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    /* 全体デザイン調整 */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-weight: 700;
        padding: 0.6rem 1rem;
        transition: all 0.2s ease-in-out;
    }
    .main-header {
        font-size: 1.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #FF6B9B, #8B5CF6, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .speech-box {
        background-color: #F3E8FF;
        border-radius: 16px;
        padding: 1.2rem;
        border: 2px solid #DDD6FE;
        margin-bottom: 1.5rem;
    }
    .badge {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        margin-right: 0.3rem;
        margin-bottom: 0.3rem;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. データ定義 (8系列・コース情報 & 質問)
# -----------------------------------------------------------------------------
TRACKS = {
    'SPACE_WEATHER': {
        'id': 'SPACE_WEATHER',
        'name': '宇宙・気象系列',
        'badge_bg': '#E0F2FE',
        'badge_color': '#0369A1',
        'mascotComment': 'データや自然の神秘、宇宙のスケールにワクワクするキミ！空や宇宙の謎を解き明かす理数アドベンチャーへ飛び出そう！',
        'traits': [
            'データやグラフの変化・法則を読むのが好き',
            '天気や宇宙・自然現象への探究心がある',
            '数学的な計算や公式を使って解くのが得意'
        ],
        'faculties': ['理学部', '気象大学校', '地球惑星科学科', '宇宙航空学科'],
        'careers': ['気象予報士', '宇宙開発エンジニア', 'データアナリスト', '環境研究員']
    },
    'DX': {
        'id': 'DX',
        'name': 'DX系列',
        'badge_bg': '#F3E8FF',
        'badge_color': '#6B21A8',
        'mascotComment': 'デジタルテクノロジーと新アイデアの創出が得意なキミ！Web・アプリ・ゲームなど、デジタルで世界を変革しよう！',
        'traits': [
            'PCやスマホの操作・活用が得意',
            '「こんなサービス欲しい！」と妄想するのが好き',
            'デジタル技術で新しい価値を作ることに興味がある'
        ],
        'faculties': ['情報工学部', 'データサイエンス学部', 'デジタルコンテンツ学部'],
        'careers': ['Webエンジニア', 'アプリ開発者', 'ゲームデザイナー', 'DXコンサルタント']
    },
    'HYOGO_STARTUP': {
        'id': 'HYOGO_STARTUP',
        'name': 'ひょうごからスタートアップ系列',
        'badge_bg': '#FCE7F3',
        'badge_color': '#9D174D',
        'mascotComment': '地域の魅力発信や新しい挑戦・起業に燃えるキミ！企画力と情熱で兵庫から世界へ新しい風を起こそう！',
        'traits': [
            '地元の魅力を多くの人に伝えるのが好き',
            'イベントや新しい企画を立ち上げるのが好き',
            '将来自分で事業やサービスを起こす（起業）に興味がある'
        ],
        'faculties': ['経営学部', '経済学部', '地域創生学部', 'アントレプレナーシップ学科'],
        'careers': ['起業家', '新規事業プロデューサー', '地域活性化コーディネーター', 'イベントプロデューサー']
    },
    'OUTDOOR_DISASTER': {
        'id': 'OUTDOOR_DISASTER',
        'name': 'スポーツ・アウトドアと防災系列',
        'badge_bg': '#D1FAE5',
        'badge_color': '#065F46',
        'mascotComment': '体を動かす情熱と、災害から命を守る優しさを兼ね備えたキミ！仲間と協力して安心・安全な社会を作ろう！',
        'traits': [
            '体を動かすことやアクティビティが好き',
            '防災や緊急時に人を助けることに強い興味がある',
            'チームで協力して課題に取り組み達成するのが好き'
        ],
        'faculties': ['防災学部', 'スポーツ健康科学部', '社会安全学部', '救急救命学科'],
        'careers': ['消防士・救急救命士', '防災コーディネーター', 'スポーツインストラクター', 'アウトドアガイド']
    },
    'DIVERSITY': {
        'id': 'DIVERSITY',
        'name': 'ダイバーシティ&インクルージョン系列',
        'badge_bg': '#FFE4E6',
        'badge_color': '#9F1239',
        'mascotComment': '多様な価値観を理解し、「誰もが過ごしやすい社会」を追求できる優しい視点を持ったキミにピッタリ！',
        'traits': [
            '「当たり前」に疑問を持ち、多様な意見に耳を傾けられる',
            '自分と異なる考え方や立場の人を尊重できる',
            'いろんな人の視点から社会課題を考えられる'
        ],
        'faculties': ['看護学部', '外国語学部', '総合人間科学部', '社会学部', '国際共生学部', '福祉学部'],
        'careers': ['看護師・医療従事者', '語学を活かした職種', 'ダイバーシティ推進担当', '社会福祉士', '国際協力スタッフ']
    },
    'LIBERAL_SCIENCE': {
        'id': 'LIBERAL_SCIENCE',
        'name': 'リベラルアーツ理系系列',
        'badge_bg': '#E0E7FF',
        'badge_color': '#3730A3',
        'mascotComment': '「なぜ？」をロジカルに掘り下げる探究派！特定の分野に縛られず、幅広い理系知性を身につけよう！',
        'traits': [
            '理由や仕組みから本質を理解するのが好き',
            '理系進学希望だが、まだ一つの分野に絞っていない',
            '仮説を立てて試行錯誤しながら答えを探すのが好き'
        ],
        'faculties': ['理学部（学科横断コース）', '総合科学部', '教養学部（理系）'],
        'careers': ['サイエンスコミュニケーション', '開発研究員', 'システム分析官', '進学・大学院研究']
    },
    'LIBERAL_ARTS': {
        'id': 'LIBERAL_ARTS',
        'name': 'リベラルアーツ文系系列',
        'badge_bg': '#FEF3C7',
        'badge_color': '#92400E',
        'mascotComment': '思考を言語化し、人間や社会の文脈を深く味わうキミ！幅広い文系知性で物事を多角的に捉えよう！',
        'traits': [
            '自分の考えを文章や言葉で表現するのが好き',
            '文系進学希望だが、まだ学科を一つに絞っていない',
            '言語学・心理学・社会学など人間社会の探究が好き'
        ],
        'faculties': ['文学部', '教養学部（文系）', '総合人間学科', '人文社会学科'],
        'careers': ['ライター・編集者', '企画マーケター', '広報担当', '国際交流ディレクター']
    },
    'CREATIVE_ARTS': {
        'id': 'CREATIVE_ARTS',
        'name': 'クリエイティブ・表現系列',
        'badge_bg': '#FFEDD5',
        'badge_color': '#9A3412',
        'mascotComment': '自らの感性やアイデアを発信し、アートやデザインで人の心を動かすことが大好きなクリエイタータイプ！',
        'traits': [
          'イラスト・音楽・映像など表現することが好き',
          '自分ならではの世界観やアイデアを持っている',
          '作品づくりを通して思いを他人に伝えたい'
        ],
        'faculties': ['芸術学部', '美術学部', 'デザイン学部', '音楽学部'],
        'careers': ['イラストレーター', 'グラフィックデザイナー', '映像クリエイター', '音楽制作者']
    }
}

DIAGNOSIS_QUESTIONS = [
    {"question": "Q1. グラフ・表などのデータから傾向や変化を読み取ることが好きだ", "track": "SPACE_WEATHER"},
    {"question": "Q2. 天気・宇宙などに興味がある", "track": "SPACE_WEATHER"},
    {"question": "Q3. 数学の計算や公式を使って、問題を解くことに抵抗がない", "track": "SPACE_WEATHER"},
    {"question": "Q4. パソコン・スマートフォン操作が得意だ", "track": "DX"},
    {"question": "Q5. 将来Web・アプリ・ゲームに関係する職に就きたいと思う", "track": "DX"},
    {"question": "Q6. 「こんなサービスがあったらいいのに」など新しいものを考えるのが好きだ", "track": "DX"},
    {"question": "Q7. 地元の魅力をみんなに知ってもらいたい！", "track": "HYOGO_STARTUP"},
    {"question": "Q8. イベントやサービスの企画がとても好きだ", "track": "HYOGO_STARTUP"},
    {"question": "Q9. 将来起業することに興味がある", "track": "HYOGO_STARTUP"},
    {"question": "Q10. 体を動かすことがとても好きだ", "track": "OUTDOOR_DISASTER"},
    {"question": "Q11. 地震や豪雨などの自然災害時に人を助けたりすることに興味がある", "track": "OUTDOOR_DISASTER"},
    {"question": "Q12. グループで協力して課題や活動に取り組むことが好きだ", "track": "OUTDOOR_DISASTER"},
    {"question": "Q13. 当たり前のことになぜ？と疑問を持てる", "track": "DIVERSITY"},
    {"question": "Q14. 自分と違う考え方の人の意見に興味がある", "track": "DIVERSITY"},
    {"question": "Q15. 一つの問題に様々な立場の人の意見を考えることができる", "track": "DIVERSITY"},
    {"question": "Q16. 「なぜそうなるか」を、理由や仕組みから理解することが好き", "track": "LIBERAL_SCIENCE"},
    {"question": "Q17. 将来理系の大学に進みたいが分野が決まっていない", "track": "LIBERAL_SCIENCE"},
    {"question": "Q18. 仮説をたてて試行錯誤しながら答えを導くのが好きだ", "track": "LIBERAL_SCIENCE"},
    {"question": "Q19. 自分の考えを文章で表すことが好きだ", "track": "LIBERAL_ARTS"},
    {"question": "Q20. 将来文系の大学に進みたいが分野が決まっていない", "track": "LIBERAL_ARTS"},
    {"question": "Q21. 言語学や社会学に興味がある", "track": "LIBERAL_ARTS"}
]

DECIDED_OPTIONS = [
    {"text": "宇宙・理学・気象・データ解析系", "track": "SPACE_WEATHER"},
    {"text": "IT・情報・Web・ゲームアプリ系", "track": "DX"},
    {"text": "経営・経済・地域創生・ビジネス企画系", "track": "HYOGO_STARTUP"},
    {"text": "スポーツ・健康・防災・社会安全系", "track": "OUTDOOR_DISASTER"},
    {"text": "社会学・国際共生・福祉・人権系", "track": "DIVERSITY"},
    {"text": "理系全般（まだ具体的な学科を絞りたくない）", "track": "LIBERAL_SCIENCE"},
    {"text": "文系全般（まだ具体的な学科を絞りたくない）", "track": "LIBERAL_ARTS"}
]

FOUR_CHOICES = [
    {"text": "とても当てはまる", "score": 4},
    {"text": "やや当てはまる", "score": 3},
    {"text": "あまり当てはまらない", "score": 2},
    {"text": "全く当てはまらない", "score": 1}
]

# -----------------------------------------------------------------------------
# 3. セッション状態の初期化
# -----------------------------------------------------------------------------
if 'screen' not in st.session_state:
    st.session_state.screen = 'start'
if 'q_idx' not in st.session_state:
    st.session_state.q_idx = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {k: 0 for k in TRACKS.keys()}
if 'is_decided' not in st.session_state:
    st.session_state.is_decided = False

# -----------------------------------------------------------------------------
# 4. ヘッダー & サイドバー情報
# -----------------------------------------------------------------------------
st.markdown('<div class="main-header">✦ 未来ルートナビ ✦</div>', unsafe_allow_html=True)
st.caption("高校生のための進路・系列コース診断アプリ")

with st.expander("ℹ️ KIKS・各系列について / SNSリンク"):
    tab1, tab2, tab3 = st.tabs(["KIKSについて", "各系列一覧", "公式SNS"])
    
    with tab1:
        st.subheader("KIKSについて")
        st.write("KIKSでは、一人ひとりの個性や将来の夢に合わせた多角的なカリキュラムを展開しています。文系・理系の枠にとらわれず、最新のテクノロジー、地域創生、防災、ダイバーシティなど、自分の「好き」を突き詰めることができる環境が整っています。")
        st.markdown("- **01. 特長豊かな系列群:** 自分の適性に合わせて主体的に深掘り")
        st.markdown("- **02. 地域・社会連携:** 探究型プロジェクト学習")
        st.markdown("- **03. 一人ひとりの進路実現:** 個別の手厚いサポート")

    with tab2:
        st.subheader("全系列・コース一覧")
        for key, t in TRACKS.items():
            st.markdown(f"**{t['name']}**")
            st.caption(t['mascotComment'])
            st.markdown("---")

    with tab3:
        st.subheader("公式 Instagram")
        st.markdown("- [学校公式 Instagram (@kiks_official)](https://instagram.com)")
        st.markdown("- [運動部公式アカウント](https://instagram.com)")
        st.markdown("- [文化部・生徒会](https://instagram.com)")

st.divider()

# -----------------------------------------------------------------------------
# 5. メイン画面遷移
# -----------------------------------------------------------------------------

# --- A. スタート画面 ---
if st.session_state.screen == 'start':
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <h2 style="font-weight: 800;">キミにピッタリの<br><span style="color: #8B5CF6;">高校の系列・コース</span>を探そう！</h2>
        <p style="color: #64748B; font-size: 0.95rem;">
            ナビゲーターの「ナビィ」だよ！直感的な質問に答えるだけで、あなたの得意や興味に合ったコースを分析するよ✨
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("診断をはじめる 🚀", type="primary", use_container_width=True):
        st.session_state.screen = 'branch'
        st.rerun()

# --- B. 進路分岐選択画面 ---
elif st.session_state.screen == 'branch':
    st.markdown("""
    <div class="speech-box">
        <strong>ナビィ:</strong><br>
        教えて！進学したい大学や学びたい分野は、もう具体的に決まっているかな？
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("はい！決まっている ✨\n(目的の分野からピンポイント案内)", use_container_width=True):
            st.session_state.is_decided = True
            st.session_state.screen = 'decided_select'
            st.rerun()
    with col2:
        if st.button("まだ探している！ 🤔\n(質問に答えて適性診断)", use_container_width=True):
            st.session_state.is_decided = False
            st.session_state.q_idx = 0
            st.session_state.scores = {k: 0 for k in TRACKS.keys()}
            st.session_state.screen = 'quiz'
            st.rerun()

# --- C-1. 大学決定ルート直接選択 ---
elif st.session_state.screen == 'decided_select':
    st.markdown("""
    <div class="speech-box">
        <strong>ナビィ:</strong><br>
        進学したい大学の学部や学びたい分野の方向性はどれに近い？
    </div>
    """, unsafe_allow_html=True)

    for opt in DECIDED_OPTIONS:
        if st.button(opt["text"], use_container_width=True):
            st.session_state.scores[opt["track"]] = 12
            st.session_state.screen = 'result'
            st.rerun()

# --- C-2. クイズ進行画面 (21問) ---
elif st.session_state.screen == 'quiz':
    total_q = len(DIAGNOSIS_QUESTIONS)
    curr_q = st.session_state.q_idx + 1
    
    # プログレスバー
    st.progress(curr_q / total_q)
    st.caption(f"QUESTION {curr_q} / {total_q}")
    
    q_data = DIAGNOSIS_QUESTIONS[st.session_state.q_idx]
    
    st.markdown(f"""
    <div class="speech-box">
        <strong>ナビィ:</strong><br>
        <span style="font-size: 1.1rem; font-weight: 700;">{q_data['question']}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 選択肢ボタン
    for choice in FOUR_CHOICES:
        if st.button(f"{choice['text']} (+{choice['score']}pt)", use_container_width=True):
            st.session_state.scores[q_data['track']] += choice['score']
            if st.session_state.q_idx + 1 < total_q:
                st.session_state.q_idx += 1
                st.rerun()
            else:
                st.session_state.screen = 'result'
                st.rerun()

# --- D. 診断結果画面 ---
elif st.session_state.screen == 'result':
    # 最高スコアの判定
    top_track_key = max(st.session_state.scores, key=st.session_state.scores.get)
    res = TRACKS[top_track_key]
    
    max_score = st.session_state.scores[top_track_key]
    match_score = 99 if st.session_state.is_decided else min(99, int((max_score / 12) * 100))
    
    st.balloons()
    
    st.markdown(f"""
    <div style="text-align: center; padding: 1.5rem; background: #FFF; border-radius: 20px; border: 2px solid #8B5CF6; box-shadow: 0 10px 25px rgba(0,0,0,0.05); margin-bottom: 1.5rem;">
        <span style="background: #8B5CF6; color: white; font-size: 0.8rem; font-weight: 800; padding: 0.2rem 0.8rem; border-radius: 999px;">✦ 診断結果 ✦</span>
        <p style="color: #64748B; font-size: 0.85rem; margin-top: 0.8rem;">あなたと最も相性が良い高校のコースは...</p>
        <h1 style="font-weight: 900; color: #0F172A; margin: 0.5rem 0;">{res['name']}</h1>
        <p style="font-weight: 800; color: #8B5CF6;">適性マッチ度: {match_score}%</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="speech-box">
        <strong>ナビィからのメッセージ:</strong><br>
        {res['mascotComment']}
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✨ あなたの強み・特徴")
        for trait in res['traits']:
            st.markdown(f"- {trait}")
            
    with col2:
        st.subheader("🧭 目指せる進路")
        st.markdown("**【おすすめ学部】**")
        badges_fac = "".join([f'<span class="badge" style="background-color:{res["badge_bg"]}; color:{res["badge_color"]};">{f}</span>' for f in res['faculties']])
        st.markdown(badges_fac, unsafe_allow_html=True)
        
        st.markdown("**【向いている職種】**")
        badges_car = "".join([f'<span class="badge" style="background-color:#F1F5F9; color:#475569;">{c}</span>' for c in res['careers']])
        st.markdown(badges_car, unsafe_allow_html=True)
        
    st.divider()
    
    if st.button("もう一度診断する 🔄", type="primary", use_container_width=True):
        st.session_state.screen = 'start'
        st.session_state.q_idx = 0
        st.session_state.scores = {k: 0 for k in TRACKS.keys()}
        st.rerun()
